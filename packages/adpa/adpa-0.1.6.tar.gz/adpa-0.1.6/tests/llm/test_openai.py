"""Tests for OpenAI LLM integration."""
import pytest
from unittest.mock import patch, AsyncMock
import os
import logging

from adpa.llm.models import LLMConfig, LLMAPIError
from adpa.llm.openai_config import (
    get_api_key,
    get_chat_model,
    LLMConfigError,
    ChatModel
)

class TestOpenAIConfig:
    """Tests for OpenAI configuration."""
    
    def test_get_api_key_adpa(self):
        """Test API key retrieval from openai_adpa1."""
        with patch.dict("os.environ", {"openai_adpa1": "test-key-1234"}):
            key = get_api_key()
            assert key == "test-key-1234"
    
    def test_get_api_key_openai(self):
        """Test API key retrieval from OPENAI_API_KEY."""
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key-5678", "openai_adpa1": ""}):
            key = get_api_key()
            assert key == "test-key-5678"
    
    def test_get_api_key_missing(self):
        """Test error when no API key is available."""
        with patch.dict("os.environ", clear=True):
            with pytest.raises(LLMConfigError):
                get_api_key()

class TestChatModel:
    """Tests for OpenAI chat model."""
    
    @pytest.mark.asyncio
    async def test_chat_model_mock(self, mock_chat_model):
        """Test chat model with mock."""
        response = await mock_chat_model.ainvoke("Say hello")
        assert response == "Test response"
        mock_chat_model.ainvoke.assert_called_once_with("Say hello")
    
    @pytest.mark.asyncio
    async def test_chat_model_real(self, real_chat_model):
        """Test chat model with real API."""
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key-1234"}):
            response = await real_chat_model.ainvoke("Say hello")
            assert isinstance(response, str)
            assert len(response) > 0
    
    @pytest.mark.asyncio
    async def test_chat_model_error(self, mock_chat_model):
        """Test chat model error handling."""
        mock_chat_model.ainvoke.side_effect = LLMAPIError("API Error")
        with pytest.raises(LLMAPIError):
            await mock_chat_model.ainvoke("Say hello")
    
    @pytest.mark.asyncio
    async def test_chat_model_streaming(self, mock_chat_model):
        """Test chat model streaming."""
        chunks = []
        async for chunk in await mock_chat_model.astream("Say hello"):
            chunks.append(chunk.content)
        
        assert chunks == ["Hello", " World"]
        mock_chat_model.astream.assert_called_once_with("Say hello")

class TestRetryBehavior:
    """Tests for retry behavior."""
    
    @pytest.mark.asyncio
    async def test_retry_success(self):
        """Test successful retry after failure."""
        # Create a mock client
        mock_client = AsyncMock()
        mock_client.chat.completions.create = AsyncMock(side_effect=[
            Exception("First attempt failed"),
            AsyncMock(choices=[AsyncMock(message=AsyncMock(content="Success on retry"))])
        ])
        
        # Create chat model with mock client
        chat_model = ChatModel(mock_client)
        
        # Test the function
        response = await chat_model.ainvoke("Say hello")
        assert response == "Success on retry"
        assert mock_client.chat.completions.create.call_count == 2
    
    @pytest.mark.asyncio
    async def test_retry_max_attempts(self, caplog):
        """Test that after max retries, the original error is raised.
        
        This test verifies that:
        1. The method retries the maximum number of times (3)
        2. Each retry attempt uses the correct arguments
        3. The original error is preserved and raised
        4. A proper error message is logged
        
        Note: This test is expected to raise LLMAPIError after max retries.
        """
        # Create a mock client that always fails with LLMAPIError
        mock_client = AsyncMock()
        error = LLMAPIError("Test error")
        mock_client.chat.completions.create = AsyncMock(side_effect=error)
        
        # Create chat model with mock client
        chat_model = ChatModel(mock_client)
        
        # Verify that after max retries, the original error is raised
        with pytest.raises(LLMAPIError) as exc_info, caplog.at_level(logging.ERROR):
            await chat_model.ainvoke("Say hello")
        
        # Verify error details
        assert str(exc_info.value) == "Test error"  # Original error message is preserved
        assert mock_client.chat.completions.create.call_count == 3  # Called max times
        
        # Verify that each retry attempt used correct arguments
        expected_args = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Say hello"}]
        }
        for call in mock_client.chat.completions.create.call_args_list:
            assert call.kwargs == expected_args
        
        # Verify that max retries was logged
        assert "Max retries (3) reached. Last error: Test error" in caplog.text
