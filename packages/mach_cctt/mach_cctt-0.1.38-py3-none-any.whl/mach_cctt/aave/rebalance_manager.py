from __future__ import annotations
import abc
from abc import ABC
import dataclasses
from decimal import Decimal
import typing

from mach_client.asset import EthereumToken

from .. import config
from ..log import LogContextAdapter, Logger


@dataclasses.dataclass(kw_only=True, slots=True)
class RebalanceAnalysis:
    rebalance: bool
    token_rates: dict[EthereumToken, Decimal]
    portfolio_interest_rate: Decimal
    portfolio: dict[EthereumToken, Decimal]
    portfolio_value: Decimal


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class RebalanceManager(ABC):
    logger: Logger

    @abc.abstractmethod
    def __call__(
        self,
        token_rates: dict[EthereumToken, Decimal],
        uninvested_balances: dict[EthereumToken, Decimal],
        invested_balances: dict[EthereumToken, Decimal],
    ) -> RebalanceAnalysis:
        self.logger.info("Checking for rebalance")

        # Warning: this assumes that all tokens are USD stablecoins
        portfolio_balance = Decimal(
            sum(uninvested_balances.values()) + sum(invested_balances.values())
        )

        portfolio_interest_rate = (
            sum(
                balance * token_rates[token] / portfolio_balance
                for token, balance in invested_balances.items()
            )
            if portfolio_balance > 0
            else 0
        )

        self.logger.info(f"Portfolio interest rate: {portfolio_interest_rate}")

        return RebalanceAnalysis(
            rebalance=False,
            token_rates=token_rates,
            portfolio_interest_rate=Decimal(portfolio_interest_rate),
            portfolio=invested_balances,
            portfolio_value=portfolio_balance,
        )


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class ProfitableRebalanceManager(RebalanceManager):
    @classmethod
    def create(cls, logger: Logger) -> ProfitableRebalanceManager:
        return cls(logger=LogContextAdapter(logger, "Profitable Rebalance Manager"))

    @typing.override
    def __call__(
        self,
        token_rates: dict[EthereumToken, Decimal],
        uninvested_balances: dict[EthereumToken, Decimal],
        invested_balances: dict[EthereumToken, Decimal],
    ) -> RebalanceAnalysis:
        rebalance_analysis = super(ProfitableRebalanceManager, self).__call__(
            token_rates, uninvested_balances, invested_balances
        )

        highest_rate = next(iter(token_rates.values()))

        rebalance_analysis.rebalance = (
            highest_rate - rebalance_analysis.portfolio_interest_rate
            > config.config.aave.rebalance_threshold
        )

        return rebalance_analysis


# Used for testing; always rebalances even if not profitable
@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class FrequentRebalanceManager(RebalanceManager):
    @classmethod
    def create(cls, logger: Logger) -> FrequentRebalanceManager:
        return cls(logger=LogContextAdapter(logger, "Frequent Rebalance Manager"))

    @typing.override
    def __call__(
        self,
        token_rates: dict[EthereumToken, Decimal],
        uninvested_balances: dict[EthereumToken, Decimal],
        invested_balances: dict[EthereumToken, Decimal],
    ) -> RebalanceAnalysis:
        rebalance_analysis = super(FrequentRebalanceManager, self).__call__(
            token_rates, uninvested_balances, invested_balances
        )
        rebalance_analysis.rebalance = True
        return rebalance_analysis
