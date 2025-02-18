"""Gemini LLM client module."""
import asyncio
from typing import Optional

import google.generativeai as genai

from ..base import BaseLLMClient, LLMConfig, ModelResponse, TokenUsage


class GeminiClient(BaseLLMClient):
    """Gemini LLM client."""

    def __init__(self, config: LLMConfig) -> None:
        """Initialize Gemini client.

        Args:
            config: LLM configuration

        Raises:
            ValueError: If API key is not provided
        """
        super().__init__(config)
        if not config.api_key:
            raise ValueError("Gemini API key not provided")
        genai.configure(api_key=config.api_key)
        self.client = genai.GenerativeModel(model_name=config.model)

    async def generate(self, prompt: str) -> ModelResponse:
        """Generate response using Gemini.

        Args:
            prompt: Input prompt

        Returns:
            Model response with generated content and usage statistics

        Raises:
            Exception: If Gemini API call fails
        """
        try:
            response = await asyncio.to_thread(
                self.client.generate_content,
                prompt,
                temperature=self.config.temperature,
                max_output_tokens=self.config.max_tokens,
            )

            # Estimate token usage (Gemini doesn't provide this)
            words = len(response.text.split())
            estimated_tokens = words * 1.3  # Rough estimate: 1.3 tokens per word

            usage = TokenUsage(
                prompt_tokens=int(len(prompt.split()) * 1.3),
                completion_tokens=int(estimated_tokens),
                total_tokens=int(estimated_tokens + len(prompt.split()) * 1.3),
            )

            return ModelResponse(
                content=response.text,
                usage=usage
            )

        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}") from e
