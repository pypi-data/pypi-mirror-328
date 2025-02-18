"""Integration tests for LLM functionality."""

import pytest
import pytest_asyncio
from unittest.mock import Mock, AsyncMock, patch
from typing import Dict, Any, List

from adpa.llm.models import (
    LLMConfig,
    RESEARCHER_RAG,
    RESEARCHER_ANALYSIS,
    SUPPORT_GENERAL
)
from adpa.llm.openai_config import get_chat_model, ChatModel
from adpa.llm.model_constants import ModelProvider

# Test data
TEST_PROMPTS = [
    "What is the capital of France?",
    "How does a quantum computer work?",
    "Write a Python function to sort a list.",
]

TEST_SYSTEM_MESSAGES = [
    "You are a helpful assistant.",
    "You are a technical expert.",
    "You are a coding tutor."
]

@pytest.mark.asyncio
async def test_chat_model_real_call(real_chat_model):
    """Test real API call to chat model."""
    response = await real_chat_model.ainvoke(TEST_PROMPTS[0])
    assert isinstance(response.content, str)
    assert len(response.content) > 0

@pytest.mark.asyncio
async def test_chat_model_mock_call(mock_chat_model):
    """Test mocked chat model call."""
    response = await mock_chat_model.ainvoke(TEST_PROMPTS[0])
    assert isinstance(response.content, str)
    assert len(response.content) > 0

@pytest.mark.asyncio
async def test_chat_model_streaming(real_chat_model):
    """Test streaming responses from chat model."""
    async for chunk in real_chat_model.astream(TEST_PROMPTS[0]):
        assert isinstance(chunk.content, str)

@pytest.mark.asyncio
async def test_chat_model_with_system_message(real_chat_model):
    """Test chat model with system message."""
    messages = [
        {"role": "system", "content": TEST_SYSTEM_MESSAGES[0]},
        {"role": "user", "content": TEST_PROMPTS[0]}
    ]
    response = await real_chat_model.ainvoke(messages)
    assert isinstance(response.content, str)
    assert len(response.content) > 0

@pytest.mark.asyncio
async def test_chat_model_error_handling(mock_chat_model_with_errors):
    """Test error handling in chat model."""
    with pytest.raises(Exception):
        await mock_chat_model_with_errors.ainvoke(TEST_PROMPTS[0])

@pytest.mark.asyncio
async def test_chat_model_retries(mock_chat_model_with_retries):
    """Test retry mechanism in chat model."""
    response = await mock_chat_model_with_retries.ainvoke(TEST_PROMPTS[0])
    assert isinstance(response.content, str)
    assert len(response.content) > 0

@pytest.mark.parametrize("provider", [
    ModelProvider.OPENAI,
    ModelProvider.GROQ
])
def test_chat_model_providers(provider):
    """Test different model providers."""
    config = LLMConfig(provider=provider)
    model = get_chat_model(config)
    assert model is not None
    assert isinstance(model, (ChatModel, Mock))

@pytest.mark.parametrize("config", [
    RESEARCHER_RAG,
    RESEARCHER_ANALYSIS,
    SUPPORT_GENERAL
])
def test_specialized_configs(config):
    """Test specialized model configurations."""
    model = get_chat_model(config)
    assert model is not None
    assert isinstance(model, (ChatModel, Mock))
    assert model.model_name == config.model_name
    assert model.temperature == config.temperature
    assert model.max_tokens == config.max_tokens

def test_chat_model_validation():
    """Test chat model parameter validation."""
    with pytest.raises(ValueError):
        LLMConfig(temperature=2.0)  # Invalid temperature
    
    with pytest.raises(ValueError):
        LLMConfig(max_tokens=0)  # Invalid max_tokens
    
    with pytest.raises(ValueError):
        LLMConfig(top_p=1.5)  # Invalid top_p

@pytest.mark.asyncio
async def test_concurrent_requests(real_chat_model):
    """Test handling multiple concurrent requests."""
    import asyncio
    
    async def make_request(prompt: str):
        return await real_chat_model.ainvoke(prompt)
    
    tasks = [make_request(prompt) for prompt in TEST_PROMPTS]
    responses = await asyncio.gather(*tasks)
    
    assert len(responses) == len(TEST_PROMPTS)
    for response in responses:
        assert isinstance(response.content, str)
        assert len(response.content) > 0
