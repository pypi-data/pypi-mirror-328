from typing import Callable

from pydantic import BaseModel, Field

from dowse.interfaces.processor.base import Processor
from dowse.models import Tweet
from dowse.tools import (
    convert_dollar_amount_to_eth,
    convert_token_amount_to_wei,
    get_token_address_tool,
)


class FormattedCommand(BaseModel):
    content: str
    caller: str = Field(description="The Twitter handle of the caller")


class ProcessTokens(Processor[Tweet, FormattedCommand]):
    tools: list[Callable] = [
        get_token_address_tool,
        convert_dollar_amount_to_eth,
        convert_token_amount_to_wei,
    ]
