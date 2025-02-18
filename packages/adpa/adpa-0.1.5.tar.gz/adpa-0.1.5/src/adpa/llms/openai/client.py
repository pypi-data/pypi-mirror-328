"""OpenAI LLM client module."""
import asyncio
from typing import Optional

from openai import OpenAI

from ..base import BaseLLMClient, LLMConfig, ModelResponse, TokenUsage


class OpenAIClient(BaseLLMClient):
    """OpenAI LLM client."""

    def __init__(self, config: LLMConfig) -> None:
        """Initialize OpenAI client.

        Args:
            config: LLM configuration
        """
        super().__init__(config)
        self.client = OpenAI(api_key=config.api_key)

    async def generate(self, prompt: str) -> ModelResponse:
        """Generate response using OpenAI.

        Args:
            prompt: Input prompt

        Returns:
            Model response

        Raises:
            Exception: If OpenAI API call fails
        """
        try:
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model=self.config.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
            )

            usage = TokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            )

            return ModelResponse(content=response.choices[0].message.content, usage=usage)

        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}") from e
