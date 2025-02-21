"""Base class for all LLM backends and a factory class to create LLM backends"""

from abc import ABC, abstractmethod
import importlib
from typing import Type
from pydantic import BaseModel


class LLMBackend(ABC):
    """Base class for all LLM backends"""

    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    def send_request(self, messages: list, output_format: Type[BaseModel]) -> BaseModel:
        """Send a request to the LLM model"""


class BackendFactory:
    """Factory class to create LLM backends"""

    @classmethod
    def create_backend(cls, backend_name: str, model_name: str) -> LLMBackend:
        """Dynamically create a backend instance based on the backend and model name

        Args:
            backend_name (str): name of the llm backend, openai, gemini, etc.
            model_name (str): name of the model for the backend, such as gpt-4o
        """
        backend_class_name = f"{backend_name.capitalize()}Backend"
        module_path = f"technical_drawing_parser.llm_backends.backends.{backend_name}_backend"

        # Dynamically import the module
        try:
            module = importlib.import_module(module_path)
        except ImportError as exc:
            raise ValueError(f"Invalid backend name: {backend_name}") from exc

        # Instantiate the backend class
        backend_class = getattr(module, backend_class_name)
        return backend_class(model_name)
