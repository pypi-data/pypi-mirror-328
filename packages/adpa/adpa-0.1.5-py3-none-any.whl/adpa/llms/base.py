"""Base classes and types for LLM providers."""
from typing import Optional

from pydantic import BaseModel, Field


class TokenUsage(BaseModel):
    """Token usage information."""
    prompt_tokens: int = Field(..., description="Number of tokens in the prompt")
    completion_tokens: int = Field(..., description="Number of tokens in the completion")
    total_tokens: int = Field(..., description="Total number of tokens used")


class ModelResponse(BaseModel):
    """Model response information."""
    content: str = Field(..., description="Generated text content")
    usage: Optional[TokenUsage] = Field(None, description="Token usage statistics")


class LLMConfig(BaseModel):
    """LLM configuration."""
    primary_provider: str = Field(..., description="Primary LLM provider")
    model: str = Field(..., description="Model name")
    api_key: str = Field(..., description="API key for the provider")
    temperature: float = Field(0.7, description="Sampling temperature")
    max_tokens: int = Field(1000, description="Maximum tokens to generate")


class BaseLLMClient:
    """Base class for LLM clients."""

    def __init__(self, config: LLMConfig) -> None:
        """Initialize LLM client.

        Args:
            config: LLM configuration
        """
        self.config = config

    async def generate(self, prompt: str) -> ModelResponse:
        """Generate a response for the given prompt.

        Args:
            prompt: Input prompt

        Returns:
            Model response with generated content and usage statistics

        Raises:
            NotImplementedError: Must be implemented by subclasses
        """
        raise NotImplementedError
