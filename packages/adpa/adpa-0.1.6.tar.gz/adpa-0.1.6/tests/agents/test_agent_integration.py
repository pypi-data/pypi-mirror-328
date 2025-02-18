"""Integration tests for agent functionality."""

import pytest
import pytest_asyncio
from unittest.mock import Mock, AsyncMock, patch
from typing import Dict, Any, List

from adpa.agents.base import BaseAgent
from adpa.agents.researcher import ResearchAgent
from adpa.agents.config import AgentConfig
from adpa.llm.models import RESEARCHER_RAG
from adpa.research.search import ResearchEngine

# Test data
TEST_TASKS = [
    "Research quantum computing advances",
    "Analyze the impact of AI on healthcare",
    "Review latest developments in renewable energy"
]

@pytest.fixture
def mock_research_engine():
    """Create a mock research engine."""
    engine = Mock(spec=ResearchEngine)
    engine.tavily_search.return_value = "Mock search results"
    return engine

@pytest.fixture
def test_agent_config():
    """Create a test agent configuration."""
    return AgentConfig(
        name="test_agent",
        description="Test agent for integration tests",
        capabilities=["research", "analysis"],
        model_name="gpt-4-1106-preview",
        temperature=0.7,
        max_tokens=2000
    )

class TestAgent(BaseAgent):
    """Test agent implementation."""
    
    def __init__(self, config: AgentConfig):
        super().__init__(config)
        self.processed_tasks = []

    async def process(self, task: str) -> str:
        self.processed_tasks.append(task)
        return f"Processed: {task}"

@pytest.mark.asyncio
async def test_base_agent_initialization(test_agent_config):
    """Test base agent initialization."""
    agent = TestAgent(test_agent_config)
    assert agent.config == test_agent_config
    assert agent.get_capabilities() == test_agent_config.capabilities
    assert agent.is_ready()

@pytest.mark.asyncio
async def test_agent_task_processing(test_agent_config):
    """Test agent task processing."""
    agent = TestAgent(test_agent_config)
    
    for task in TEST_TASKS:
        response = await agent.process(task)
        assert response == f"Processed: {task}"
        assert task in agent.processed_tasks

@pytest.mark.asyncio
async def test_research_agent_initialization():
    """Test research agent initialization."""
    agent = ResearchAgent()
    assert isinstance(agent.research_engine, ResearchEngine)
    assert agent.rag_llm is not None
    assert agent.analysis_llm is not None

@pytest.mark.asyncio
async def test_research_agent_news_search(mock_research_engine):
    """Test research agent news search."""
    with patch('adpa.agents.researcher.ResearchEngine', return_value=mock_research_engine):
        agent = ResearchAgent()
        response = await agent.process("Latest news about OpenAI")
        assert response == "Mock search results"
        mock_research_engine.tavily_search.assert_called_once()

@pytest.mark.asyncio
async def test_research_agent_analysis(mock_chat_model):
    """Test research agent analysis."""
    agent = ResearchAgent()
    agent.analysis_llm = mock_chat_model
    
    response = await agent.process("Analyze quantum computing")
    assert isinstance(response, str)
    assert len(response) > 0

@pytest.mark.asyncio
async def test_agent_error_handling(mock_chat_model_with_errors):
    """Test agent error handling."""
    agent = ResearchAgent()
    agent.analysis_llm = mock_chat_model_with_errors
    
    with pytest.raises(Exception):
        await agent.process("This should fail")

@pytest.mark.asyncio
async def test_agent_with_tools(test_agent_config):
    """Test agent with tools."""
    agent = TestAgent(test_agent_config)
    
    # Mock tool
    tool = Mock()
    tool.name = "test_tool"
    tool.description = "Test tool"
    tool.func = AsyncMock(return_value="Tool result")
    
    # Add tool and test
    agent.add_tool(tool)
    assert tool in agent.tools
    
    # Remove tool and test
    agent.remove_tool(tool)
    assert tool not in agent.tools

@pytest.mark.asyncio
async def test_agent_context_handling(test_agent_config):
    """Test agent context handling."""
    agent = TestAgent(test_agent_config)
    
    # Test context updates
    context = {"key": "value"}
    agent._context.update(context)
    
    response = await agent.process("Task with context")
    assert "Task with context" in agent.processed_tasks

@pytest.mark.asyncio
async def test_agent_capabilities(test_agent_config):
    """Test agent capabilities."""
    agent = TestAgent(test_agent_config)
    
    # Test capability checks
    capabilities = agent.get_capabilities()
    assert isinstance(capabilities, list)
    assert "research" in capabilities
    assert "analysis" in capabilities

@pytest.mark.asyncio
async def test_agent_concurrent_tasks(test_agent_config):
    """Test handling multiple concurrent tasks."""
    import asyncio
    
    agent = TestAgent(test_agent_config)
    
    async def process_task(task: str):
        return await agent.process(task)
    
    tasks = [process_task(task) for task in TEST_TASKS]
    responses = await asyncio.gather(*tasks)
    
    assert len(responses) == len(TEST_TASKS)
    for task, response in zip(TEST_TASKS, responses):
        assert response == f"Processed: {task}"
        assert task in agent.processed_tasks
