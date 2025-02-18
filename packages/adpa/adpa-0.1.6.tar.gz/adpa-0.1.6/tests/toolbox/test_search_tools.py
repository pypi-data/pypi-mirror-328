"""Tests for search tools."""
import pytest
from unittest.mock import Mock, patch

from adpa.research.search import (
    TavilySearchTool,
    BraveSearchTool,
    ScrapingBeeTool,
    SerperSearchTool
)

@pytest.fixture
def mock_response():
    """Create a mock response."""
    mock = Mock()
    mock.json.return_value = {"results": [{"title": "Test", "content": "Test content"}]}
    mock.text = "<html><body>Test content</body></html>"
    mock.raise_for_status = Mock()
    return mock

@patch("requests.get")
def test_tavily_search(mock_get, mock_response):
    """Test Tavily search."""
    mock_get.return_value = mock_response
    
    tool = TavilySearchTool(api_key="test_key")
    result = tool._run(query="test query")
    
    assert "results" in result
    mock_get.assert_called_once()

@patch("requests.get")
def test_brave_search(mock_get, mock_response):
    """Test Brave search."""
    mock_get.return_value = mock_response
    
    tool = BraveSearchTool(api_key="test_key")
    result = tool._run(query="test query")
    
    assert "results" in result
    mock_get.assert_called_once()

@patch("requests.get")
def test_scrapingbee_extract(mock_get, mock_response):
    """Test ScrapingBee content extraction."""
    mock_get.return_value = mock_response
    
    tool = ScrapingBeeTool(api_key="test_key")
    result = tool._run(url="https://example.com")
    
    assert "content" in result
    mock_get.assert_called_once()

@patch("requests.post")
def test_serper_search(mock_post, mock_response):
    """Test Serper search."""
    mock_post.return_value = mock_response
    
    tool = SerperSearchTool(api_key="test_key")
    result = tool._run(query="test query")
    
    assert "results" in result
    mock_post.assert_called_once()

def test_tavily_search_no_api_key():
    """Test Tavily search without API key."""
    with pytest.raises(ValueError):
        TavilySearchTool()

def test_brave_search_no_api_key():
    """Test Brave search without API key."""
    with pytest.raises(ValueError):
        BraveSearchTool()

def test_scrapingbee_extract_no_api_key():
    """Test ScrapingBee without API key."""
    with pytest.raises(ValueError):
        ScrapingBeeTool()

def test_serper_search_no_api_key():
    """Test Serper search without API key."""
    with pytest.raises(ValueError):
        SerperSearchTool()

@patch("requests.get")
def test_tavily_search_error(mock_get):
    """Test Tavily search error handling."""
    mock_get.side_effect = Exception("Test error")
    
    tool = TavilySearchTool(api_key="test_key")
    result = tool._run(query="test query")
    
    assert "error" in result

@patch("requests.get")
def test_brave_search_error(mock_get):
    """Test Brave search error handling."""
    mock_get.side_effect = Exception("Test error")
    
    tool = BraveSearchTool(api_key="test_key")
    result = tool._run(query="test query")
    
    assert "error" in result

@patch("requests.get")
def test_scrapingbee_extract_error(mock_get):
    """Test ScrapingBee error handling."""
    mock_get.side_effect = Exception("Test error")
    
    tool = ScrapingBeeTool(api_key="test_key")
    result = tool._run(url="https://example.com")
    
    assert "error" in result

@patch("requests.post")
def test_serper_search_error(mock_post):
    """Test Serper search error handling."""
    mock_post.side_effect = Exception("Test error")
    
    tool = SerperSearchTool(api_key="test_key")
    result = tool._run(query="test query")
    
    assert "error" in result
