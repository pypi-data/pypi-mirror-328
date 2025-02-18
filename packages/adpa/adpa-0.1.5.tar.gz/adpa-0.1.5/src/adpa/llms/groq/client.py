"""Groq LLM client module."""
import asyncio
from typing import Optional

import groq

from ..base import BaseLLMClient, LLMConfig, ModelResponse, TokenUsage


class GroqClient(BaseLLMClient):
    """Groq LLM client."""

    def __init__(self, config: LLMConfig) -> None:
        """Initialize Groq client.

        Args:
            config: LLM configuration
        """
        super().__init__(config)
        self.client = groq.Client(api_key=config.api_key)

    async def generate(self, prompt: str) -> ModelResponse:
        """Generate response using Groq.

        Args:
            prompt: Input prompt

        Returns:
            Model response

        Raises:
            Exception: If Groq API call fails
        """
        try:
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model=self.config.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
            )

            # Estimate token usage (Groq doesn't provide this)
            words = len(response.choices[0].message.content.split())
            estimated_tokens = words * 1.3  # Rough estimate: 1.3 tokens per word

            usage = TokenUsage(
                prompt_tokens=int(len(prompt.split()) * 1.3),
                completion_tokens=int(estimated_tokens),
                total_tokens=int(estimated_tokens + len(prompt.split()) * 1.3),
            )

            return ModelResponse(content=response.choices[0].message.content, usage=usage)

        except Exception as e:
            raise Exception(f"Groq API error: {str(e)}") from e
