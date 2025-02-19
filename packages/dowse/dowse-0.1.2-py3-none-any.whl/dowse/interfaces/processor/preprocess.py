import logging
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from dowse.exceptions import PreprocessorError
from dowse.models.message import AgentMessage

from ..example_loader import ExampleLoader
from ..prompt_loader import PromptLoader
from .base import Processor

T = TypeVar("T")
U = TypeVar("U", bound=BaseModel)

logger = logging.getLogger("dowse")


class PreProcess(ExampleLoader, PromptLoader, Generic[T, U]):
    preprocessors: list[Processor] = Field(default_factory=list)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.load_examples()
        cls.load_prompt()

    async def run_preprocessors(self, input_: T) -> AgentMessage[U]:
        processed_data = input_
        if not self.preprocessors:
            return AgentMessage(content=processed_data, error_message=None)  # type: ignore[arg-type]

        for preprocessor in self.preprocessors:
            logger.debug("Running preprocessor: %s", processed_data)
            processed_data: AgentMessage = await preprocessor.format(processed_data)  # type: ignore[no-redef]
            logger.debug("Preprocessor result: %s", processed_data)
            if processed_data.error_message is not None:  # type: ignore[attr-defined]
                raise PreprocessorError(processed_data.error_message)  # type: ignore[attr-defined]
        return processed_data  # type: ignore
