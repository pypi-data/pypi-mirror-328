"""Tests for the Research Agent."""

import os
import pytest
from pathlib import Path
from unittest.mock import Mock, patch
from dotenv import load_dotenv, find_dotenv
from adpa.agents.research_agent import ResearchAgent

# Load environment variables from .env file
env_path = Path("c:/Users/achim/github/ADPA/.env")
if not env_path.exists():
    pytest.skip(f".env file not found at {env_path}")

# Force reload of environment variables
os.environ.clear()
load_dotenv(env_path, override=True)

@pytest.fixture
def mock_research_agent():
    """Create a mocked research agent instance."""
    with patch.dict('os.environ', {
        'OPENAI_API_KEY': 'test-key',
        'TAVILY_API_KEY': 'test-key'
    }):
        agent = ResearchAgent(openai_api_key='test-key', tavily_api_key='test-key')
        # Mock the agent executor
        mock_executor = Mock()
        agent.agent_executor = mock_executor
        return agent

@pytest.mark.parametrize("query,expected_status", [
    ("What is Python?", True),
    ("", False),
    (None, False),
])
def test_research_agent_process(mock_research_agent, query, expected_status):
    """Test research agent process with different queries."""
    # Mock the agent executor's invoke method
    mock_result = {"output": "Test research result"}
    mock_research_agent.agent_executor.invoke.return_value = mock_result
    
    if query is None or query == "":
        with pytest.raises(ValueError):
            mock_research_agent.process(query)
    else:
        result = mock_research_agent.process(query)
        assert result['success'] == expected_status
        if expected_status:
            assert result['task']['content'] == mock_result['output']

@patch('tavily.TavilyClient')
def test_research_agent_integration(mock_tavily, mock_research_agent):
    """Test research agent integration with Tavily."""
    # Mock Tavily search results
    mock_tavily_result = {
        'results': [
            {
                'title': 'Test Title',
                'content': 'Test Content',
                'url': 'https://test.com',
                'score': 0.9
            }
        ]
    }
    mock_tavily.return_value.search.return_value = mock_tavily_result
    
    # Mock agent executor response
    mock_result = {"output": "Test research result"}
    mock_research_agent.agent_executor.invoke.return_value = mock_result
    
    # Test query
    query = "What are OpenAI Assistants?"
    result = mock_research_agent.process(query)
    
    # Verify success
    assert result['success']
    assert result['task']['content'] == mock_result['output']

def test_research_agent_error_handling(mock_research_agent):
    """Test research agent error handling."""
    # Mock agent executor to raise an exception
    mock_research_agent.agent_executor.invoke.side_effect = Exception("Test error")
    result = mock_research_agent.process("Test query")
    assert not result['success']
    assert result['error'] == "Test error"
    assert result['task'] is None

@pytest.mark.integration
def test_research_agent_real_call():
    """Test research agent with real API calls."""
    # Skip test if API keys are not set
    openai_key = os.getenv('OPENAI_API_KEY')
    tavily_key = os.getenv('TAVILY_API_KEY')
    
    # Print debugging information without revealing full keys
    print(f"Looking for .env at: {env_path}")
    print(f"File exists: {env_path.exists()}")
    
    if openai_key:
        print(f"OpenAI Key found:")
        print(f"  - Length: {len(openai_key)}")
        print(f"  - Starts with: {openai_key[:7]}...")
    else:
        print("OpenAI Key not found")
    
    if tavily_key:
        print(f"Tavily Key found:")
        print(f"  - Length: {len(tavily_key)}")
        print(f"  - Starts with: {tavily_key[:6]}..." if tavily_key else "")
    else:
        print("Tavily Key not found")
    
    # Print all environment variables (excluding their values)
    print("\nAll environment variables:")
    for key in sorted(os.environ.keys()):
        print(f"  - {key}")
    
    if not openai_key or not tavily_key:
        pytest.skip("API keys not set in environment")
    
    # Create agent with real API keys
    agent = ResearchAgent(openai_api_key=openai_key, tavily_api_key=tavily_key)
    
    # Test query about a specific Python topic
    query = "What are the key differences between Python's asyncio and threading modules? Include code examples."
    try:
        result = agent.process(query)
        
        # Verify success and content
        assert result['success'], f"Agent process failed with error: {result.get('error', 'Unknown error')}"
        assert result['task'] is not None, "Task should not be None"
        assert result['task']['content'] is not None, "Task content should not be None"
        assert len(result['task']['content']) > 100, "Task content should be substantial"
        
        # Check for code examples
        assert "```python" in result['task']['content'], "Response should include Python code examples"
        assert "import" in result['task']['content'], "Response should include import statements"
        
        # Check for references
        assert "http" in result['task']['content'], "Response should include references"
    except Exception as e:
        pytest.fail(f"Test failed with exception: {str(e)}")
