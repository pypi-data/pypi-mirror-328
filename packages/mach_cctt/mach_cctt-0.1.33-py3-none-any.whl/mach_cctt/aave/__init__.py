import asyncio
import dataclasses
from decimal import Decimal
import itertools
import pprint
from types import TracebackType
import typing
from typing import AsyncGenerator, Optional

from mach_client import AccountManager, RiskManager
from mach_client.account import EthereumAccount
from mach_client.client.event import Trade

from .event import (
    AaveEvent,
    ConvertError,
    LiquidityRateError,
    RebalanceEvaluation,
    Supply,
    SupplyError,
    Withdraw,
    WithdrawError,
)
from .rebalance_manager import (
    FrequentRebalanceManager,
    ProfitableRebalanceManager,
    RebalanceAnalysis,
    RebalanceManager,
)
from .. import config, mach
from ..log import Logger
from ..mach.destination_policy import TokenIteratorPolicy
from .aave import Aave


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class AaveRunner:
    aave: Aave
    accounts: AccountManager
    rebalance_manager: RebalanceManager
    filter_lower_rate_tokens: bool
    risk_manager: RiskManager
    logger: Logger

    async def __call__(self) -> AsyncGenerator[AaveEvent, None]:
        while True:
            # Inner loop determines when to rebalance portfolio
            while True:
                try:
                    token_rates = await self.aave.get_liquidity_rates(
                        self.aave.enabled_tokens
                    )
                except Exception as e:
                    self.logger.error(
                        "An exception was thrown while fetching liquidity rates from Aave:",
                        exc_info=e,
                    )
                    yield LiquidityRateError(self.aave.enabled_tokens, e)
                    continue

                self.logger.info("Liquidity rates:")
                self.logger.info(pprint.pformat(token_rates))

                token_balances_list = await asyncio.gather(
                    *[
                        self.aave.get_atoken_balance_in_coins(
                            token,
                            typing.cast(
                                EthereumAccount, self.accounts[token.chain]
                            ).downcast(),
                        )
                        for token in self.aave.enabled_tokens
                    ]
                )

                portfolio_balances = dict(
                    zip(self.aave.enabled_tokens, token_balances_list)
                )

                self.logger.info("Portfolio balances:")
                self.logger.info(pprint.pformat(portfolio_balances))

                rebalance_analysis = self.rebalance_manager(
                    token_rates, portfolio_balances
                )

                yield RebalanceEvaluation(rebalance_analysis)

                if rebalance_analysis.rebalance:
                    break

                self.logger.info("Not rebalancing portfolio")
                await asyncio.sleep(config.config.aave.supply_duration)

            self.logger.info("Rebalancing portfolio")

            self.logger.info("Withdrawing funds from Aave")

            withdrawn = []

            for token in self.aave.enabled_tokens:
                account = typing.cast(EthereumAccount, self.accounts[token.chain])
                amount, exception = await self.aave.withdraw(token, account)

                if exception:
                    self.logger.error(
                        f"An exception was thrown while withdrawing {token} from Aave:",
                        exc_info=exception,
                    )
                    yield WithdrawError(token, token.to_coins(amount), exception)
                    continue

                elif amount <= 0:
                    continue

                withdrawn.append((token, token.to_coins(amount)))

            yield Withdraw(withdrawn)

            self.logger.info("Swapping funds in wallet")

            for src_token, rate in token_rates.items():
                account = typing.cast(EthereumAccount, self.accounts[src_token.chain])

                if await src_token.get_balance(account.downcast()) <= 0:
                    continue

                if self.filter_lower_rate_tokens:
                    next_tokens = itertools.takewhile(
                        lambda item: item[1] > rate, token_rates.items()
                    )
                else:
                    next_tokens = token_rates.items()

                if not next_tokens:
                    continue

                destination_policy = TokenIteratorPolicy(
                    self.aave.asset_server,
                    map(lambda item: item[0], next_tokens),
                )

                runner = mach.run(
                    client=self.aave.client,
                    asset_server=self.aave.asset_server,
                    src_token=src_token,
                    destination_policy=destination_policy,
                    accounts=self.accounts,
                    risk_manager=self.risk_manager,
                    logger=self.logger,
                )

                try:
                    async for event in runner:
                        if isinstance(event, Trade):
                            break

                        self.logger.error(
                            f"Unexpected event while swapping out of {src_token}:"
                        )
                        self.logger.error(pprint.pformat(event))

                        yield ConvertError(src_token, event)

                except Exception as e:
                    self.logger.error(
                        f"An exception was thrown while swapping {src_token}:",
                        exc_info=e,
                    )
                    yield ConvertError(src_token, e)

            supplied = []

            for token in self.aave.enabled_tokens:
                account = typing.cast(EthereumAccount, self.accounts[token.chain])
                amount, exception = await self.aave.supply(token, account)

                if exception:
                    self.logger.error(
                        f"An exception was thrown while supplying {token} to Aave:",
                        exc_info=exception,
                    )
                    yield SupplyError(
                        token, Decimal(amount) / 10**token.decimals, exception
                    )
                    continue
                elif amount <= 0:
                    continue

                supplied.append((token, Decimal(amount) / 10**token.decimals))

            yield Supply(supplied)

            if not supplied:
                self.logger.warning("No tokens were supplied. Trying again.")
                continue

            self.logger.info("Sleeping...")
            await asyncio.sleep(config.config.aave.supply_duration)

    async def __aenter__(self) -> AsyncGenerator[AaveEvent, None]:
        return self()

    # Withdraw all tokens when the runner is done
    async def __aexit__(
        self,
        _exc_type: Optional[type[BaseException]],
        _exc_value: Optional[BaseException],
        _traceback: Optional[TracebackType],
    ) -> None:
        for token in self.aave.enabled_tokens:
            account = typing.cast(EthereumAccount, self.accounts[token.chain])
            _amount, exception = await self.aave.withdraw(token, account)

            if exception:
                self.logger.error(
                    f"Withdrawal of {token.symbol} from Aave failed with exception:",
                    exc_info=exception,
                )


__all__ = [
    "Aave",
    "AaveEvent",
    "AaveRunner",
    "FrequentRebalanceManager",
    "ProfitableRebalanceManager",
    "RebalanceAnalysis",
    "RebalanceEvaluation",
    "RebalanceManager",
]
