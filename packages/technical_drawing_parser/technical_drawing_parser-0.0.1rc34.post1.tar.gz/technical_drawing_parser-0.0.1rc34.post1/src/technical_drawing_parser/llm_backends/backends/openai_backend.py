"""Concrete implementation of the LLMBackend class for the OpenAI API"""

from typing import Type
from openai import OpenAI
from pydantic import BaseModel
from technical_drawing_parser.llm_backends.llm_backend import LLMBackend


class OpenaiBackend(LLMBackend):
    """OpenAI backend class"""

    def send_request(self, messages: list, output_format: Type[BaseModel]) -> BaseModel:
        """Send a request to the OpenAI model with structured output"""
        client = OpenAI()
        completion = client.beta.chat.completions.parse(
            model=self.model_name, messages=messages, response_format=output_format, temperature=0
        )
        print(completion.usage)
        if completion.usage:
            print(
                f"cost of the page: {(completion.usage.completion_tokens * 10
                                      + completion.usage.prompt_tokens * 2.5) / 1000000}"
            )
        else:
            print("No usage information available.")

        if completion.choices[0].message.parsed is None:
            raise ValueError("Parsed message is None")
        return completion.choices[0].message.parsed
