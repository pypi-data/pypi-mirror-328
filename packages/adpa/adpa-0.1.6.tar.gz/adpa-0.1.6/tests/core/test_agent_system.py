"""Tests for the ADPA agent system."""
import pytest
from typing import Dict, List, Optional
from unittest.mock import AsyncMock, MagicMock, patch

from adpa.core.agent import Agent, AgentConfig, AgentState
from adpa.core.types import AgentType, ProcessingState
from adpa.core.manager import AgentManager


@pytest.fixture
def agent_config():
    """Fixture for agent configuration."""
    return AgentConfig(
        name="test_agent",
        type=AgentType.PROCESSOR,
        enabled=True,
        config={
            "model": "gpt-4",
            "temperature": 0.7,
            "max_tokens": 1000,
            "timeout": 30
        }
    )


@pytest.fixture
def mock_llm_client():
    """Fixture for mock LLM client."""
    client = AsyncMock()
    client.generate.return_value = {
        "content": "Test response",
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 5,
            "total_tokens": 15
        }
    }
    return client


@pytest.fixture
def test_agent(agent_config, mock_llm_client):
    """Fixture for test agent."""
    agent = Agent(agent_config)
    agent.llm_client = mock_llm_client
    return agent


@pytest.fixture
def agent_manager():
    """Fixture for agent manager."""
    return AgentManager()


def test_agent_initialization(agent_config):
    """Test agent initialization."""
    agent = Agent(agent_config)
    assert agent.name == "test_agent"
    assert agent.type == AgentType.PROCESSOR
    assert agent.enabled is True
    assert agent.state == AgentState.IDLE
    assert agent.config["model"] == "gpt-4"


@pytest.mark.asyncio
async def test_agent_processing(test_agent):
    """Test agent processing capabilities."""
    input_data = {
        "query": "Select all employees",
        "context": {"department": "HR"}
    }
    
    result = await test_agent.process(input_data)
    assert result is not None
    assert "content" in result
    assert "usage" in result
    
    # Verify LLM client was called correctly
    test_agent.llm_client.generate.assert_called_once()


def test_agent_state_transitions(test_agent):
    """Test agent state transitions."""
    # Test initial state
    assert test_agent.state == AgentState.IDLE
    
    # Test valid state transitions
    test_agent.state = AgentState.PROCESSING
    assert test_agent.state == AgentState.PROCESSING
    
    test_agent.state = AgentState.ERROR
    assert test_agent.state == AgentState.ERROR
    
    # Test invalid state transition
    with pytest.raises(ValueError):
        test_agent.state = "INVALID_STATE"


@pytest.mark.asyncio
async def test_agent_error_handling(test_agent):
    """Test agent error handling."""
    # Setup LLM client to raise an error
    test_agent.llm_client.generate.side_effect = Exception("API Error")
    
    with pytest.raises(Exception) as exc_info:
        await test_agent.process({"query": "test"})
    
    assert str(exc_info.value) == "API Error"
    assert test_agent.state == AgentState.ERROR


def test_agent_configuration_validation(agent_config):
    """Test agent configuration validation."""
    # Test valid configuration
    agent = Agent(agent_config)
    assert agent.validate_config() is True
    
    # Test invalid configuration
    invalid_config = AgentConfig(
        name="",  # Invalid: empty name
        type=AgentType.PROCESSOR,
        enabled=True,
        config={}
    )
    with pytest.raises(ValueError):
        Agent(invalid_config)


@pytest.mark.asyncio
async def test_agent_manager_operations(agent_manager, agent_config):
    """Test agent manager operations."""
    # Test agent registration
    agent = Agent(agent_config)
    agent_manager.register_agent(agent)
    assert len(agent_manager.agents) == 1
    assert agent_manager.get_agent("test_agent") == agent
    
    # Test agent removal
    agent_manager.remove_agent("test_agent")
    assert len(agent_manager.agents) == 0
    assert agent_manager.get_agent("test_agent") is None


@pytest.mark.asyncio
async def test_agent_manager_processing(agent_manager, test_agent):
    """Test agent manager processing coordination."""
    agent_manager.register_agent(test_agent)
    
    input_data = {
        "query": "Test query",
        "context": {"type": "test"}
    }
    
    result = await agent_manager.process(input_data)
    assert result is not None
    assert "content" in result
    assert "usage" in result


def test_agent_manager_state_monitoring(agent_manager, test_agent):
    """Test agent manager state monitoring."""
    agent_manager.register_agent(test_agent)
    
    # Test state monitoring
    states = agent_manager.get_agent_states()
    assert len(states) == 1
    assert states["test_agent"] == AgentState.IDLE
    
    # Test state updates
    test_agent.state = AgentState.PROCESSING
    states = agent_manager.get_agent_states()
    assert states["test_agent"] == AgentState.PROCESSING


@pytest.mark.asyncio
async def test_agent_manager_error_handling(agent_manager, test_agent):
    """Test agent manager error handling."""
    agent_manager.register_agent(test_agent)
    
    # Setup agent to raise an error
    test_agent.process = AsyncMock(side_effect=Exception("Processing Error"))
    
    with pytest.raises(Exception) as exc_info:
        await agent_manager.process({"query": "test"})
    
    assert str(exc_info.value) == "Processing Error"
    assert test_agent.state == AgentState.ERROR


@pytest.mark.asyncio
async def test_agent_manager_concurrent_processing(agent_manager):
    """Test concurrent processing with multiple agents."""
    # Create multiple agents
    agents = [
        Agent(AgentConfig(
            name=f"agent_{i}",
            type=AgentType.PROCESSOR,
            enabled=True,
            config={"model": "gpt-4"}
        )) for i in range(3)
    ]
    
    # Register agents
    for agent in agents:
        agent_manager.register_agent(agent)
    
    # Test concurrent processing
    import asyncio
    tasks = [
        agent_manager.process({"query": f"test_{i}"})
        for i in range(3)
    ]
    
    results = await asyncio.gather(*tasks)
    assert len(results) == 3


def test_agent_metrics_collection(test_agent):
    """Test agent metrics collection."""
    metrics = test_agent.get_metrics()
    assert "processed_count" in metrics
    assert "error_count" in metrics
    assert "average_processing_time" in metrics
    
    # Test metrics after processing
    test_agent.update_metrics(
        processing_time=1.5,
        token_usage={"total_tokens": 100}
    )
    
    updated_metrics = test_agent.get_metrics()
    assert updated_metrics["processed_count"] == 1
    assert updated_metrics["total_tokens"] == 100
    assert updated_metrics["average_processing_time"] == 1.5


@pytest.mark.asyncio
async def test_agent_timeout_handling(test_agent):
    """Test agent timeout handling."""
    # Setup agent with a short timeout
    test_agent.config["timeout"] = 0.1
    test_agent.llm_client.generate = AsyncMock(side_effect=asyncio.sleep(0.2))
    
    with pytest.raises(asyncio.TimeoutError):
        await test_agent.process({"query": "test"})
    
    assert test_agent.state == AgentState.ERROR
