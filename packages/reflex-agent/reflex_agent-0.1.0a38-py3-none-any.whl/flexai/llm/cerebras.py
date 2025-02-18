from __future__ import annotations
import json
import os
import time
from dataclasses import dataclass
from typing import Any, AsyncGenerator, Sequence, Type

# Try to import the openai library.
try:
    from openai import AsyncOpenAI  # type: ignore
    from pydantic import BaseModel  # type: ignore
except ImportError:
    raise ImportError(
        "The openai library is required for the OpenAIClient. "
        "Please install it using `pip install openai`."
    )
from flexai.llm.client import Client
from flexai.message import (
    AIMessage,
    Message,
    ToolCall,
    ToolResult,
    MessageContent,
    SystemMessage,
    TextBlock,
    Usage,
)
from flexai.tool import Tool, TYPE_MAP


def get_tool_call(tool_use) -> ToolCall:
    """Get the tool call from a tool use block.

    Args:
        tool_use: The tool use block to get the call from.

    Returns:
        The tool call from the tool use block.
    """
    return ToolCall(
        id=tool_use.id,
        name=tool_use.function.name,
        input=json.loads(tool_use.function.arguments),
    )


@dataclass(frozen=True)
class CerebrasClient(Client):
    """Client for interacting with the Cerebras language model."""

    # The client to use for interacting with the model.
    client: AsyncOpenAI = AsyncOpenAI(
        base_url="https://api.cerebras.ai/v1",
        api_key=os.environ.get("CEREBRAS_API_KEY"),
    )

    # The model to use for generating responses.
    model: str = os.getenv("OPENAI_MODEL", "llama3.3-70b")

    async def get_chat_response(
        self,
        messages: list[Message],
        system: str | SystemMessage = "",
        tools: list[Tool] | None = None,
    ) -> AIMessage:
        # Send the messages to the model and get the response.
        start = time.time()
        params = self._get_params(messages, system, tools)
        response = await self.client.chat.completions.create(**params)
        generation_time = time.time() - start

        # Parse out the tool uses from the response.
        message = response.choices[0].message
        tool_uses = [get_tool_call(message) for message in message.tool_calls]

        # Get the content to return.
        content_to_return = tool_uses or message.content
        return AIMessage(
            content=content_to_return,
            usage=Usage(
                input_tokens=response.usage.prompt_tokens,
                output_tokens=response.usage.completion_tokens,
                generation_time=generation_time,
            ),
        )

    async def stream_chat_response(  # type: ignore
        self,
        messages: list[Message],
        system: str | SystemMessage = "",
        tools: list[Tool] | None = None,
    ) -> AsyncGenerator[str | AIMessage, None]:
        stream = await self.client.chat.completions.create(
            **self._get_params(messages, system, tools), stream=True
        )
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                yield content

    def _get_params(
        self,
        messages: list[Message],
        system: str | SystemMessage,
        tools: list[Tool] | None,
    ) -> dict:
        """Get the common params to send to the model.

        Args:
            messages: The messages to send to the model.
            system: The system message to send to the model.
            tools: The tools to send to the model.

        Returns:
            The common params to send to the model.
        """
        if isinstance(system, str):
            system = SystemMessage(system)
        messages = self.format_content([system, *messages])
        kwargs = {
            "model": self.model,
            "messages": messages,
        }

        # If tools are provided, force the model to use them (for now).
        if tools:
            kwargs["tools"] = [self.format_tool(tool) for tool in tools]
            kwargs["tool_choice"] = "required"

        return kwargs

    async def get_structured_response(
        self,
        messages: list[Message],
        model: Type[BaseModel],
        system: str | SystemMessage = "",
    ) -> BaseModel:
        """Get the structured response from the chat model.

        Args:
            messages: The messages to send to the model.
            model: The model to use for the response.
            system: Optional system message to set the behavior of the AI.

        Returns:
            The structured response from the model.

        Raises:
            ValueError: If the response cannot be parsed.
        """
        # Send the messages to the model and get the response.
        response = await self.client.beta.chat.completions.parse(  # type: ignore
            **self._get_params(messages, system, []),
            response_format=model,
        )
        result = response.choices[0].message.parsed
        if result is None:
            raise ValueError("Failed to parse the response.")
        return result

    @staticmethod
    def format_tool(tool: Tool) -> dict:
        """Convert the tool to a description.

        Args:
            tool: The tool to format.

        Returns:
            A dictionary describing the tool.
        """
        input_schema = {
            "type": "object",
            "properties": {},
        }
        for param_name, param_type in tool.params:
            param_type = TYPE_MAP.get(str(param_type), param_type)
            input_schema["properties"][param_name] = {
                "type": param_type,
            }

        description = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": input_schema,
            },
        }
        return description

    @classmethod
    def format_content(
        cls,
        value: str
        | Message
        | MessageContent
        | Sequence[MessageContent]
        | Sequence[Message],
    ) -> Any:
        """Format the message content for the Anthropic model.

        Args:
            value: The value to format.

        Returns:
            The formatted message content.

        Raises:
            ValueError: If the message content type is unknown.
        """
        # Base types.
        if isinstance(value, str):
            return value
        if isinstance(value, list):
            output = [cls.format_content(v) for v in value]
            # Flatten output messages
            print("output")
            print(output)
            import itertools

            return list(
                itertools.chain.from_iterable(
                    item if isinstance(item, list) else [item] for item in output
                )
            )
            # return list(itertools.chain(*output))

        # Anthropic message format.
        if isinstance(value, Message):
            # Tool calls use a "tool" role.
            if isinstance(value.content, list):
                if value.role == "user":
                    if isinstance(value.content[0], ToolResult):
                        return [cls.format_content(v) for v in value.content]
                    return {
                        "role": value.role,
                        "content": [cls.format_content(v) for v in value.content],
                    }
                return {
                    "role": value.role,
                    "tool_calls": [cls.format_content(v) for v in value.content],
                }
            else:
                return {
                    "role": value.role,
                    "content": cls.format_content(value.content),
                }

        # Message content types.
        if isinstance(value, TextBlock):
            return {"type": "text", "text": value.text}
        if isinstance(value, ToolCall):
            return {
                "type": "function",
                "id": value.id,
                "function": {
                    "name": value.name,
                    "arguments": json.dumps(value.input),
                },
            }
        if isinstance(value, ToolResult):
            return {
                "role": "tool",
                "tool_call_id": value.tool_call_id,
                "content": json.dumps(value.result),
            }
        raise ValueError(f"Unknown message content type: {type(value)}")

    @classmethod
    def load_content(
        cls, content: str | list[dict[str, Any]]
    ) -> str | list[MessageContent]:
        """Load the message content from the Anthropic model to dataclasses.

        Args:
            content: The content to load.

        Returns:
            The loaded message content
        """
        # If it's a string, return it.
        if isinstance(content, str):
            return content

        # If it's a list of dictionaries, parse them.
        assert isinstance(content, list)
        parsed_content: list[MessageContent] = []

        for entry in content:
            match entry.pop("type"):
                case "text":
                    parsed_content.append(TextBlock(**entry))
                case "function":
                    parsed_content.append(
                        ToolCall(
                            id=entry["id"],
                            name=entry["function"]["name"],
                            input=json.loads(entry["function"]["arguments"]),
                        )
                    )
                case "tool":
                    parsed_content.append(
                        ToolResult(
                            tool_call_id=entry.pop("tool_call_id"),
                            result=json.loads(entry.pop("content")),
                            **entry,
                        )
                    )

        return parsed_content
