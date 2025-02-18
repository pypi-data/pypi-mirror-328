"""Unit tests for base LLM components."""
import pytest
from pydantic import ValidationError

from adpa.llms.base import BaseLLMClient, LLMConfig, ModelResponse, TokenUsage


def test_token_usage_creation():
    """Test TokenUsage model creation and validation."""
    # Test valid creation
    usage = TokenUsage(
        prompt_tokens=10,
        completion_tokens=20,
        total_tokens=30
    )
    assert usage.prompt_tokens == 10
    assert usage.completion_tokens == 20
    assert usage.total_tokens == 30

    # Test invalid values
    with pytest.raises(ValidationError):
        TokenUsage(
            prompt_tokens=-1,
            completion_tokens=20,
            total_tokens=30
        )

    with pytest.raises(ValidationError):
        TokenUsage(
            prompt_tokens="invalid",
            completion_tokens=20,
            total_tokens=30
        )


def test_model_response_creation():
    """Test ModelResponse model creation and validation."""
    # Test without usage
    response = ModelResponse(content="Test response")
    assert response.content == "Test response"
    assert response.usage is None

    # Test with usage
    usage = TokenUsage(
        prompt_tokens=10,
        completion_tokens=20,
        total_tokens=30
    )
    response = ModelResponse(
        content="Test response",
        usage=usage
    )
    assert response.content == "Test response"
    assert response.usage == usage

    # Test invalid content
    with pytest.raises(ValidationError):
        ModelResponse(content=None)

    with pytest.raises(ValidationError):
        ModelResponse(content="")


def test_llm_config_creation():
    """Test LLMConfig model creation and validation."""
    # Test valid creation
    config = LLMConfig(
        primary_provider="OpenAI",
        model="gpt-4",
        api_key="test-key",
        temperature=0.7,
        max_tokens=1000
    )
    assert config.primary_provider == "OpenAI"
    assert config.model == "gpt-4"
    assert config.api_key == "test-key"
    assert config.temperature == 0.7
    assert config.max_tokens == 1000

    # Test default values
    config = LLMConfig(
        primary_provider="OpenAI",
        model="gpt-4",
        api_key="test-key"
    )
    assert config.temperature == 0.7  # Default value
    assert config.max_tokens == 1000  # Default value

    # Test invalid values
    with pytest.raises(ValidationError):
        LLMConfig(
            primary_provider="",
            model="gpt-4",
            api_key="test-key"
        )

    with pytest.raises(ValidationError):
        LLMConfig(
            primary_provider="OpenAI",
            model="gpt-4",
            api_key="test-key",
            temperature=2.0  # Invalid temperature
        )


def test_base_llm_client():
    """Test BaseLLMClient functionality."""
    config = LLMConfig(
        primary_provider="OpenAI",
        model="gpt-4",
        api_key="test-key"
    )
    client = BaseLLMClient(config)
    assert client.config == config

    # Test generate method raises NotImplementedError
    with pytest.raises(NotImplementedError):
        pytest.mark.asyncio
        async def test_generate():
            await client.generate("Test prompt")
        pytest.mark.asyncio(test_generate())
