"""Test configuration for agent tests."""
import os
import pytest
from unittest.mock import Mock, patch

# Test API Keys
TEST_OPENAI_KEY = "test-key-1234"
TEST_TAVILY_KEY = "test-tavily-key-5678"

@pytest.fixture(autouse=True)
def setup_test_env(monkeypatch):
    """Set up test environment variables."""
    monkeypatch.setenv("OPENAI_API_KEY", TEST_OPENAI_KEY)
    monkeypatch.setenv("TAVILY_API_KEY", TEST_TAVILY_KEY)

@pytest.fixture
def mock_openai():
    """Create a mock OpenAI client."""
    with patch("openai.ChatCompletion.create") as mock:
        mock.return_value = {
            "choices": [{
                "message": {
                    "content": "Test response"
                }
            }]
        }
        yield mock

@pytest.fixture
def mock_tavily():
    """Create a mock Tavily client."""
    with patch("tavily.TavilyClient") as mock:
        mock.return_value.search.return_value = {
            "results": [{
                "title": "Test Title",
                "content": "Test Content",
                "url": "https://test.com",
                "score": 0.9
            }]
        }
        yield mock
