"""Test configuration for research tests."""
import pytest
import os
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in os.environ.get("PYTHONPATH", ""):
    os.environ["PYTHONPATH"] = project_root + os.pathsep + os.environ.get("PYTHONPATH", "")

def pytest_configure():
    """Configure pytest."""
    pytest.register_assert_rewrite("tests.research.test_search")
    pytest.register_assert_rewrite("tests.research.test_analyzer")

@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    """Mock environment variables for all tests."""
    monkeypatch.setenv("TAVILY_API_KEY", "mock-tavily-key")
    monkeypatch.setenv("BRAVE_API_KEY", "mock-brave-key")
    monkeypatch.setenv("GOOGLE_SERPER_API_KEY", "mock-serper-key")
    monkeypatch.setenv("SERPAPI_API_KEY", "mock-serpapi-key")
    monkeypatch.setenv("SCRAPINGBEE_API_KEY", "mock-scrapingbee-key")

@pytest.fixture
def sample_search_results():
    """Create sample search results for testing."""
    return {
        "tavily": [
            {
                "title": "Machine Learning Advances",
                "content": "Significant advances in AI research. Important findings show improvements.",
                "published": "2024-01-15T10:00:00Z"
            }
        ],
        "serper": [
            {
                "title": "Data Science Trends",
                "snippet": "Research indicates new trends in data science. Key developments in 2024.",
                "published": "2024-01-20T15:30:00Z"
            }
        ],
        "google_scholar": [
            {
                "title": "Neural Networks Study",
                "summary": "Study reveals breakthrough in neural network architecture.",
                "publish_date": "2024-01-10T08:00:00Z"
            }
        ]
    }
