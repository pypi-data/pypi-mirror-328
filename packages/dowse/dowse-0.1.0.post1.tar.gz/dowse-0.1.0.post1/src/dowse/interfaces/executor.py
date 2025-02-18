import logging
from abc import ABC
from typing import Any, Awaitable, Callable, Generic, TypeVar

from emp_agents import AgentBase, GenericTool
from emp_agents.models import Message, Provider
from emp_agents.providers import OpenAIModelType, OpenAIProvider
from pydantic import BaseModel, Field, PrivateAttr

from dowse.exceptions import PreprocessorError
from dowse.models.message import AgentMessage

from .effects import Effect
from .example_loader import ExampleLoader
from .processor import PreProcess, Processor
from .prompt_loader import PromptLoader

logger = logging.getLogger("dowse")

T = TypeVar("T", bound=BaseModel)
U = TypeVar("U", bound=BaseModel)
OutputType = TypeVar("OutputType")


class Executor(
    ABC, PreProcess[T, U], ExampleLoader, PromptLoader, Generic[T, U, OutputType]
):
    provider: Provider = Field(
        default_factory=lambda: OpenAIProvider(default_model=OpenAIModelType.gpt4o)
    )
    preprocessors: list[Processor] = Field(default_factory=list)
    tools: list[Callable | GenericTool] = Field(default_factory=list)
    effects: list[Effect[T, OutputType]] = Field(default_factory=list)
    examples: list[list[Message]] = Field(default_factory=list)

    _agent: AgentBase | None = PrivateAttr(default=None)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.load_examples()
        cls.load_prompt()

    def model_post_init(self, __context: Any) -> None:
        super().model_post_init(__context)

        if self._prompt is not None:
            self.prompt = self._prompt
        if self._examples:
            self.examples = self._examples

    async def load_tools(self, input_: AgentMessage[U]) -> list[Callable | GenericTool]:
        """This can be overriden by subclasses to provide tools dynamically"""
        return self.tools

    async def after_execution(self, input_: T, output: OutputType) -> None:
        """A function that is called after the execution completes.
        Can be overridden by subclasses to add post-execution behavior.

        Args:
            input_: The original input that was executed
            output: The output from the execution
        """
        for effect in self.effects:
            maybe_coro = effect.execute(input_, output)
            if isinstance(maybe_coro, Awaitable):
                await maybe_coro

    async def execute(
        self,
        input_: T,
    ) -> AgentMessage[OutputType]:
        response_format_type = self._extract_response_format()
        response_format = AgentMessage[response_format_type]  # type: ignore[valid-type]
        response_format.__name__ = "AgentMessage"

        if response_format_type is None:
            return response_format(
                content=None,
                error_message="",
            )

        try:
            processed_input = await self.run_preprocessors(input_)
        except PreprocessorError as e:
            return response_format(
                content=None,
                error_message=str(e),
            )

        logger.debug("Processed input: (%s)", processed_input)

        if not self.prompt:
            raise ValueError("Prompt is required")

        self._agent = AgentBase(
            prompt=self.prompt,
            provider=self.provider,
            tools=await self.load_tools(processed_input),
        )

        assert processed_input.content is not None

        for example_lst in self.examples:
            self._agent.add_messages(example_lst)

        response = await self._agent.answer(
            processed_input.content.model_dump_json(),
            response_format=response_format,
        )

        formatted_response: AgentMessage[OutputType] = (  # type: ignore[valid-type]
            response_format.model_validate_json(response)
        )
        if formatted_response.content is None:
            logger.error(
                "No content in response: (%s) -> %s", processed_input, response
            )
            raise ValueError(formatted_response.error_message)
        await self.after_execution(input_, formatted_response.content)

        return formatted_response

    def _extract_response_format(self) -> type[OutputType]:
        if type(self).__base__ is Executor:
            return type(self).__pydantic_generic_metadata__["args"][2]
        return type(self).__bases__[0].__pydantic_generic_metadata__["args"][2]  # type: ignore[attr-defined]

    def __repr__(self):
        return f"{self.__class__.__name__}[{self._extract_response_format().__name__}]"

    __str__ = __repr__

    def __init__(self, **kwargs):
        if self._extract_response_format() == Any:
            raise ValueError("Response format is not set")
        super().__init__(**kwargs)

    def __rrshift__(self, other: Processor | list[Processor]) -> "Executor":
        if isinstance(other, list):
            self.preprocessors.extend(other)
        else:
            self.preprocessors.append(other)
        return self

    def __rshift__(
        self, other: Effect[T, OutputType] | list[Effect[T, OutputType]]
    ) -> "Executor":
        if isinstance(other, list):
            self.effects.extend(other)
        else:
            self.effects.append(other)
        return self
