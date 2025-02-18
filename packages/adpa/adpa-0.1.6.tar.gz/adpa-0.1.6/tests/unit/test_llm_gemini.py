"""Unit tests for Gemini LLM client."""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from adpa.llms.base import LLMConfig, ModelResponse
from adpa.llms.gemini.client import GeminiClient


@pytest.fixture
def gemini_config():
    """Fixture for Gemini LLM configuration."""
    return LLMConfig(
        primary_provider="Gemini",
        model="gemini-pro",
        api_key="test-key",
        temperature=0.7,
        max_tokens=1000
    )


@pytest.fixture
def mock_gemini_response():
    """Fixture for mocked Gemini response."""
    response = MagicMock()
    response.text = "Test response"
    return response


@pytest.mark.asyncio
async def test_gemini_client_initialization(gemini_config):
    """Test GeminiClient initialization."""
    with patch("google.generativeai.configure") as mock_configure:
        client = GeminiClient(gemini_config)
        mock_configure.assert_called_once_with(api_key=gemini_config.api_key)
        assert client.config == gemini_config


@pytest.mark.asyncio
async def test_gemini_client_initialization_no_api_key():
    """Test GeminiClient initialization with missing API key."""
    config = LLMConfig(
        primary_provider="Gemini",
        model="gemini-pro",
        api_key="",
        temperature=0.7,
        max_tokens=1000
    )
    with pytest.raises(ValueError) as exc_info:
        GeminiClient(config)
    assert str(exc_info.value) == "Gemini API key not provided"


@pytest.mark.asyncio
async def test_gemini_client_generate(gemini_config, mock_gemini_response):
    """Test GeminiClient generate method."""
    with patch("google.generativeai.configure"), \
         patch("google.generativeai.GenerativeModel") as MockGenerativeModel:
        mock_model = MagicMock()
        mock_model.generate_content = AsyncMock(return_value=mock_gemini_response)
        MockGenerativeModel.return_value = mock_model

        client = GeminiClient(gemini_config)
        response = await client.generate("Test prompt")

        assert isinstance(response, ModelResponse)
        assert response.content == "Test response"
        assert response.usage is not None
        assert response.usage.prompt_tokens > 0
        assert response.usage.completion_tokens > 0
        assert response.usage.total_tokens > 0

        mock_model.generate_content.assert_called_once_with(
            "Test prompt",
            temperature=gemini_config.temperature,
            max_output_tokens=gemini_config.max_tokens
        )


@pytest.mark.asyncio
async def test_gemini_client_generate_error(gemini_config):
    """Test GeminiClient generate method error handling."""
    with patch("google.generativeai.configure"), \
         patch("google.generativeai.GenerativeModel") as MockGenerativeModel:
        mock_model = MagicMock()
        mock_model.generate_content = AsyncMock(
            side_effect=Exception("API error")
        )
        MockGenerativeModel.return_value = mock_model

        client = GeminiClient(gemini_config)
        with pytest.raises(Exception) as exc_info:
            await client.generate("Test prompt")
        assert str(exc_info.value) == "Gemini API error: API error"


@pytest.mark.asyncio
async def test_gemini_client_token_estimation(gemini_config, mock_gemini_response):
    """Test GeminiClient token estimation."""
    with patch("google.generativeai.configure"), \
         patch("google.generativeai.GenerativeModel") as MockGenerativeModel:
        mock_model = MagicMock()
        mock_model.generate_content = AsyncMock(return_value=mock_gemini_response)
        MockGenerativeModel.return_value = mock_model

        client = GeminiClient(gemini_config)
        response = await client.generate("This is a test prompt")

        # Check token estimation logic
        expected_prompt_tokens = int(len("This is a test prompt".split()) * 1.3)
        expected_completion_tokens = int(len("Test response".split()) * 1.3)

        assert response.usage.prompt_tokens == expected_prompt_tokens
        assert response.usage.completion_tokens == expected_completion_tokens
        assert response.usage.total_tokens == expected_prompt_tokens + expected_completion_tokens
