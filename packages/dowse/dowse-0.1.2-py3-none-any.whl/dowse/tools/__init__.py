import logging
from typing import Annotated

from eth_rpc.utils import to_checksum
from eth_typeshed.chainlink.eth_usd_feed import ChainlinkPriceOracle, ETHUSDPriceFeed
from eth_typing import ChecksumAddress
from typing_extensions import Doc

from dowse.exceptions import TokenNotFoundError

from .address import is_address
from .best_route.kyber import get_quote as get_kyber_quote
from .simulacrum import get_user_address, get_user_address_helper
from .symbol_to_address import get_token_address
from .twitter import get_user_id
from .wei import convert_token_amount_to_wei

logger = logging.getLogger("dowse")


async def get_token_address_tool(
    symbol_or_token_address: Annotated[
        str, Doc("The symbol of the token to get the address for")
    ],
) -> ChecksumAddress | str:
    """
    Get the address for a given token symbol
    """

    logger.debug("Tool Call: get_token_address (%s)", symbol_or_token_address)

    symbol_or_token_address = symbol_or_token_address.lstrip("$")

    if is_address(symbol_or_token_address):
        return to_checksum(symbol_or_token_address)
    if symbol_or_token_address.lower() == "eth":
        return to_checksum("0x4200000000000000000000000000000000000006")

    if symbol_or_token_address[0] == "@":
        user_id = await get_user_id(symbol_or_token_address)
        assert user_id is not None
        return await get_user_address(user_id)

    try:
        return to_checksum(await get_token_address(symbol_or_token_address))
    except TokenNotFoundError as e:
        return f"ERROR: {e}"


async def get_eth_price() -> float:
    """
    get the price of ETH in USD
    """

    eth_usd_feed = ETHUSDPriceFeed(address=ChainlinkPriceOracle.Ethereum.ETH)
    latest_round_data = await eth_usd_feed.latest_round_data().get()
    return latest_round_data.answer / 1e8


async def convert_dollar_amount_to_eth(
    amount: Annotated[str, Doc("The dollar amount to convert to ETH")],
) -> str:
    """
    Given a dollar amount, converts it to the corresponding amount in ETH.  For example, you could provide "$100"
    and it will strip the "$" and return an amount of ETH
    """
    eth_price = await get_eth_price()
    dollar_amount = float(amount.strip("$"))

    result = str(round(dollar_amount / eth_price, 4))

    # conver to wei
    if True:
        return str(int(float(result) * 1e18))

    logger.debug("Tool Call: convert_dollar_amount_to_eth (%s) -> %s", amount, result)
    return result


def convert_decimal_eth_to_wei(amount: str) -> str:
    """
    convert a decimal ETH amount to a string ETH amount
    """
    result = str(int(float(amount) * 1e18))
    logger.debug("Tool Call: convert_decimal_eth_to_wei (%s) -> %s", amount, result)
    return result


__all__ = [
    "get_token_address_tool",
    "convert_dollar_amount_to_eth",
    "convert_decimal_eth_to_wei",
    "get_kyber_quote",
    "is_address",
    "get_eth_price",
    "get_user_address_helper",
    "convert_token_amount_to_wei",
]
