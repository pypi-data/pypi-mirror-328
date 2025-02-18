"""Integration tests for team functionality."""

import pytest
import pytest_asyncio
from unittest.mock import Mock, AsyncMock, patch
from typing import Dict, Any, List

from adpa.teams.base import BaseTeam
from adpa.teams.research_team import ResearchTeam
from adpa.teams.support import SupportTeam
from adpa.teams.technical import TechnicalTeam
from adpa.agents.base import BaseAgent
from adpa.agents.config import AgentConfig

# Test data
TEST_MESSAGES = [
    "How do I implement a neural network?",
    "What are the best practices for code review?",
    "Can you help debug this error?"
]

@pytest.fixture
def mock_agent_factory():
    """Create a mock agent factory."""
    def create_mock_agent(name: str, capabilities: List[str]):
        agent = Mock(spec=BaseAgent)
        agent.name = name
        agent.capabilities = capabilities
        agent.process = AsyncMock(return_value=f"Response from {name}")
        return agent
    return create_mock_agent

@pytest.fixture
def test_team():
    """Create a test team."""
    class TestTeam(BaseTeam):
        def __init__(self):
            super().__init__("test_team")
            self.processed_messages = []

        async def process(self, message: str) -> str:
            self.processed_messages.append(message)
            return f"Team processed: {message}"
    
    return TestTeam()

@pytest.mark.asyncio
async def test_base_team_initialization():
    """Test base team initialization."""
    team = BaseTeam("test")
    assert team.name == "test"
    assert isinstance(team.agents, list)
    assert isinstance(team.capabilities, list)
    assert isinstance(team.context, dict)

@pytest.mark.asyncio
async def test_team_agent_management(mock_agent_factory):
    """Test adding and removing agents from team."""
    team = BaseTeam("test")
    
    # Create and add agents
    agent1 = mock_agent_factory("agent1", ["capability1"])
    agent2 = mock_agent_factory("agent2", ["capability2"])
    
    team.add_agent(agent1)
    team.add_agent(agent2)
    
    assert len(team.agents) == 2
    assert "capability1" in team.capabilities
    assert "capability2" in team.capabilities
    
    # Remove agent
    team.remove_agent(agent1)
    assert len(team.agents) == 1
    assert "capability1" not in team.capabilities
    assert "capability2" in team.capabilities

@pytest.mark.asyncio
async def test_research_team_initialization():
    """Test research team initialization."""
    team = ResearchTeam()
    assert team.name == "research"
    assert team.researcher is not None
    assert len(team.capabilities) > 0

@pytest.mark.asyncio
async def test_research_team_processing():
    """Test research team message processing."""
    team = ResearchTeam()
    
    # Mock researcher
    team.researcher.process = AsyncMock(return_value="Research complete")
    
    response = await team.process("Research quantum computing")
    assert response == "Research complete"
    team.researcher.process.assert_called_once()

@pytest.mark.asyncio
async def test_support_team_initialization():
    """Test support team initialization."""
    team = SupportTeam()
    assert team.name == "support"
    assert len(team.agents) > 0
    assert len(team.capabilities) > 0

@pytest.mark.asyncio
async def test_technical_team_initialization():
    """Test technical team initialization."""
    team = TechnicalTeam()
    assert team.name == "technical"
    assert len(team.agents) > 0
    assert len(team.capabilities) > 0

@pytest.mark.asyncio
async def test_team_message_routing(test_team, mock_agent_factory):
    """Test message routing to appropriate agents."""
    team = test_team
    
    # Add agents with different capabilities
    agent1 = mock_agent_factory("agent1", ["research"])
    agent2 = mock_agent_factory("agent2", ["support"])
    
    team.add_agent(agent1)
    team.add_agent(agent2)
    
    # Process messages
    for message in TEST_MESSAGES:
        response = await team.process(message)
        assert isinstance(response, str)
        assert message in team.processed_messages

@pytest.mark.asyncio
async def test_team_context_handling(test_team):
    """Test team context handling."""
    team = test_team
    
    # Update context
    team.update_context("key", "value")
    assert team.get_context()["key"] == "value"
    
    # Process with context
    response = await team.process("Message with context")
    assert "Message with context" in team.processed_messages

@pytest.mark.asyncio
async def test_team_capabilities(mock_agent_factory):
    """Test team capabilities management."""
    team = BaseTeam("test")
    
    # Add agents with capabilities
    agent1 = mock_agent_factory("agent1", ["cap1", "cap2"])
    agent2 = mock_agent_factory("agent2", ["cap2", "cap3"])
    
    team.add_agent(agent1)
    team.add_agent(agent2)
    
    capabilities = team.get_capabilities()
    assert "cap1" in capabilities
    assert "cap2" in capabilities
    assert "cap3" in capabilities

@pytest.mark.asyncio
async def test_team_error_handling(test_team, mock_agent_factory):
    """Test team error handling."""
    team = test_team
    
    # Add agent that raises error
    error_agent = mock_agent_factory("error_agent", ["error"])
    error_agent.process = AsyncMock(side_effect=Exception("Test error"))
    
    team.add_agent(error_agent)
    
    # Should handle error and continue
    response = await team.process("Test message")
    assert isinstance(response, str)

@pytest.mark.asyncio
async def test_team_concurrent_processing(test_team):
    """Test handling multiple concurrent messages."""
    import asyncio
    
    team = test_team
    
    async def process_message(message: str):
        return await team.process(message)
    
    tasks = [process_message(msg) for msg in TEST_MESSAGES]
    responses = await asyncio.gather(*tasks)
    
    assert len(responses) == len(TEST_MESSAGES)
    for msg, response in zip(TEST_MESSAGES, responses):
        assert isinstance(response, str)
        assert msg in team.processed_messages
