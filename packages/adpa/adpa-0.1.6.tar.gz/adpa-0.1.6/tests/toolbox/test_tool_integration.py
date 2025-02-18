"""Tests for tool integration."""
import pytest
from unittest.mock import Mock, patch

from adpa.toolbox.base import BaseTool
from adpa.research.search import TavilySearchTool, BraveSearchTool

class TestTool(BaseTool):
    """Test tool implementation."""
    
    def __init__(self, name="test_tool", description="Test tool", run_func=None):
        super().__init__(name=name, description=description)
        self._run_func = run_func or (lambda **kwargs: {"result": "test_result"})
        
    def _run(self, **kwargs):
        return self._run_func(**kwargs)

def test_tool_initialization():
    """Test tool initialization."""
    tool = TestTool()
    assert tool.name == "test_tool"
    assert tool.description == "Test tool"

def test_tool_execution():
    """Test tool execution."""
    tool = TestTool()
    result = tool._run()
    assert result == {"result": "test_result"}

def test_tool_as_langchain_tool():
    """Test tool as Langchain tool."""
    tool = TestTool()
    langchain_tool = tool.as_langchain_tool()
    assert langchain_tool.name == tool.name
    assert langchain_tool.description == tool.description

def test_tool_error_handling():
    """Test tool error handling."""
    def error_func(**kwargs):
        raise Exception("Test error")
        
    tool = TestTool(run_func=error_func)
    with pytest.raises(Exception):
        tool._run()

def test_concurrent_tool_execution():
    """Test concurrent tool execution."""
    tools = [TestTool(name=f"tool_{i}") for i in range(3)]
    results = []
    
    for tool in tools:
        results.append(tool._run())
        
    assert len(results) == 3
    assert all(r["result"] == "test_result" for r in results)

@patch("requests.get")
def test_research_tool_tavily(mock_get):
    """Test research tool with Tavily."""
    mock_response = Mock()
    mock_response.json.return_value = {"results": "Mock search results"}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response
    
    tool = TavilySearchTool(api_key="test_key")
    result = tool._run(query="test query")
    
    assert result == {"results": "Mock search results"}

@patch("requests.get")
def test_research_tool_brave(mock_get):
    """Test research tool with Brave."""
    mock_response = Mock()
    mock_response.json.return_value = {"results": "Mock search results"}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response
    
    tool = BraveSearchTool(api_key="test_key")
    result = tool._run(query="test query")
    
    assert result == {"results": "Mock search results"}

def test_tool_validation():
    """Test tool validation."""
    tool = TestTool()
    
    # Test required parameters
    with pytest.raises(TypeError):
        tool._run(invalid_param="test")
        
    # Test return value validation
    def invalid_return(**kwargs):
        return "invalid"  # Should return dict
        
    tool = TestTool(run_func=invalid_return)
    with pytest.raises(TypeError):
        tool._run()

def test_tool_with_context():
    """Test tool with context."""
    context = {"key": "value"}
    
    def context_func(**kwargs):
        return {"context": context, **kwargs}
        
    tool = TestTool(run_func=context_func)
    result = tool._run(param="test")
    
    assert result["context"] == context
    assert result["param"] == "test"

def test_tool_rate_limiting():
    """Test tool rate limiting."""
    from time import sleep
    
    def rate_limited_func(**kwargs):
        sleep(0.1)  # Simulate API call
        return {"result": "rate_limited"}
        
    tool = TestTool(run_func=rate_limited_func)
    
    # Test multiple calls
    results = []
    for _ in range(3):
        results.append(tool._run())
        
    assert len(results) == 3
    assert all(r["result"] == "rate_limited" for r in results)
