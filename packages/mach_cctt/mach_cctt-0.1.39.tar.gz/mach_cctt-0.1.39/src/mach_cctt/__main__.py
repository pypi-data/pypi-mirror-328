import argparse
import asyncio
from enum import Enum
import logging
import typing

from mach_client import (
    AccountManager,
    AssetServer,
    Chain,
    MachClient,
    RiskManager,
    SupportedChain,
    Token,
    config as client_config,
)
from mach_client.client.risk_manager import SlippageManager
import uvloop

from . import config, mach, utility, withdraw
from .aave import Aave, AaveRunner, FrequentRebalanceManager
from .mach.destination_policy import (
    CheapChainFixedSymbolPolicy,
    DestinationPolicy,
    RandomChainFixedSymbolPolicy,
    RandomTokenPolicy,
    SingleChainPolicy,
)


USAGE = """
First create a `config.yaml` file following the `template.config.yaml` template and fill in your private keys for each chain under the `accounts` map.

cctt balances
    Display balances of all tokens on all supported chains from accounts specified in the config.

cctt run --source Arbitrum-USDC --destination USDC
    Perform the test using the account in the account file. 
    The first trade is made by selling the token specified by the --source argument.
    In each trade, a random chain is chosen as the destination chain and the entire balance of the source token is sold for the destination token.
    The choice of destination token is controlled by the --destination argument.
    In the next trade, the destination token becomes the new source token.
    This repeats until the program is stopped.

    Note: currently does not support trading gas assets.

cctt aave
    Run the AAVE testing script. Constantly moves balances between the highest interest pool.

cctt withdraw
    Withdraw all non-gas funds from the accounts specified in the config into the accounts specified in the `mach_cctt.withdraw` section of the config.
"""

DESCRIPTION = "Cross chain trade test (CCTT) - test swaps between random chains"

DEFAULT_SOURCE_TOKEN = "Base-USDC"

DEFAULT_DESTINATION_POLICY = "USDC"

SOURCE_TOKEN_DESCRIPTION = """
The initial token to be sold in the first trade in the form of "<chain>-<symbol>". If left empty, the token with the highest value balance in your accounts will be chosen.
"""

DESTINATION_POLICY_DESCRIPTION = f"""
Controls how the destination token is chosen in each trade.
If set to "random", then a completely random chain and symbol will be chosen.
If set to "fixed:SYMBOL", then a token on a random chain with the given symbol will be chosen.
If set to "cheap:SYMBOL", then the token with the given symbol on only Arbitrum or Optimism will be chosen.
If set to "chains:CHAINS", where CHAINS is a comma-separated list of chains, it trades every token on each chain in a random order, and goes through all chains in a random order.
Defaults to `{DEFAULT_DESTINATION_POLICY}`.
"""


class Command(Enum):
    BALANCES = "balances"
    RUN = "run"
    AAVE = "aave"
    WITHDRAW = "withdraw"


async def show_balances(client: AssetServer, accounts: AccountManager) -> None:
    balances = await client.get_all_token_balances(accounts.downcast())

    print("Balances:")

    for _, chain_balances in balances.items():
        non_zero = [item for item in chain_balances.items() if item[1] > 0]

        if len(non_zero) == 0:
            continue

        print()

        for token, balance in non_zero:
            print(token.format_amount(balance))

    return


async def run() -> None:
    parser = argparse.ArgumentParser(
        prog="cctt",
        usage=USAGE,
        description=DESCRIPTION,
    )

    parser.add_argument(
        "command",
        choices=tuple(Command),
        help="Command to perform",
        nargs=1,
        type=Command,
    )

    parser.add_argument(
        "--source",
        "-s",
        default=DEFAULT_SOURCE_TOKEN,
        dest="src_token",
        help=SOURCE_TOKEN_DESCRIPTION,
        required=False,
        nargs="?",
        type=str,
    )

    parser.add_argument(
        "--destination-policy",
        "-d",
        default=DEFAULT_DESTINATION_POLICY,
        dest="destination_policy",
        help=DESTINATION_POLICY_DESCRIPTION,
        required=False,
        nargs="?",
        type=str,
    )

    arguments = parser.parse_args()

    command: Command = arguments.command[0]
    assert command, "Command required"

    asset_server = await AssetServer.create()
    logger = logging.getLogger("cctt")
    assert (accounts := client_config.accounts)

    if command == Command.BALANCES:
        await show_balances(asset_server, accounts)
        await asset_server.close()
        return

    client = await MachClient.create()

    if command == Command.WITHDRAW:
        await withdraw.withdraw(
            client=client,
            asset_server=asset_server,
            account_manager=accounts,
            recipients=config.config.withdraw,
            logger=logger,
        )
        await asset_server.close()
        return

    risk_manager: RiskManager = SlippageManager(
        asset_server,
        client_config.config.trading.slippage_tolerance,
        logger,
    )

    if command == Command.RUN:
        if arguments.src_token:
            src_token = Token.from_str(arguments.src_token)
        else:
            src_token = await utility.choose_source_token(
                asset_server,
                asset_server.tokens,
                accounts.downcast(),
            )

        logger.info(f"Source token: {src_token}")

        assert arguments.destination_policy, (
            "Destination policy must be provided to run test"
        )

        match arguments.destination_policy.split(":"):
            case ["random"]:
                logger.info("Destination token policy: randomize")
                destination_policy: DestinationPolicy = RandomTokenPolicy(asset_server)

            case ["fixed", symbol]:
                logger.info(f"Destination token policy: fixed symbol {symbol}")
                destination_policy: DestinationPolicy = RandomChainFixedSymbolPolicy(
                    asset_server, symbol
                )

            case ["cheap", symbol]:
                logger.info(f"Destination token policy: cheap chain {symbol}")
                destination_policy: DestinationPolicy = CheapChainFixedSymbolPolicy(
                    asset_server, symbol
                )

            case ["chains", chain_names]:
                logger.info(
                    f"Destination token policy: single chain across {chain_names}"
                )
                chains = {Chain.from_str(chain) for chain in chain_names.split(",")}
                destination_policy: DestinationPolicy = SingleChainPolicy(
                    asset_server, chains
                )

            case _ as arg:
                raise ValueError(f"Invalid destination policy: {arg}")

        runner = mach.run(
            client=client,
            asset_server=asset_server,
            src_token=src_token,
            destination_policy=destination_policy,
            accounts=accounts,
            risk_manager=risk_manager,
            logger=logger,
        )

        async for _ in runner:
            pass

    elif command == Command.AAVE:
        rebalance_manager = FrequentRebalanceManager.create(logger)

        chains = frozenset(
            (
                SupportedChain.ARBITRUM.value,
                SupportedChain.BASE.value,
                SupportedChain.OPTIMISM.value,
            )
        )

        aave = await Aave.create(
            client=client, asset_server=asset_server, chains=chains, logger=logger
        )

        runner = AaveRunner(
            aave=aave,
            accounts=accounts,
            rebalance_manager=rebalance_manager,
            filter_lower_rate_tokens=False,
            risk_manager=risk_manager,
            logger=logger,
        )

        async with runner as events:
            async for _event in events:
                pass

    else:
        typing.assert_never(command)

    await asyncio.gather(client.close(), asset_server.close())


def main() -> None:
    logging.getLogger().setLevel(logging.DEBUG)

    # Silence annoying aiohttp warning about unclosed client session originating from web3's code
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)

    uvloop.run(run())


if __name__ == "__main__":
    main()
