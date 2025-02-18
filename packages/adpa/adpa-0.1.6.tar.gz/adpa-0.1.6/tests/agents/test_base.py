"""Test base agent functionality."""
import pytest
from datetime import datetime
from adpa.agents.base import BaseAgent, AgentConfig

def test_should_create_agent_with_config():
    """Test agent creation with config."""
    config = AgentConfig(
        name="test_agent",
        type="test",
        capabilities=["capability1", "capability2"],
        settings={"setting1": "value1"}
    )
    
    agent = BaseAgent(config)
    
    assert agent.config == config
    assert agent.state == {}
    assert agent.history == []

def test_should_update_agent_state():
    """Test updating agent state."""
    config = AgentConfig(
        name="test_agent",
        type="test"
    )
    agent = BaseAgent(config)
    
    state_update = {"key1": "value1", "key2": "value2"}
    agent.update_state(state_update)
    
    assert agent.state == state_update
    assert len(agent.history) == 1
    assert agent.history[0]["state_update"] == state_update
    assert isinstance(agent.history[0]["timestamp"], datetime)

def test_should_maintain_state_history():
    """Test state history maintenance."""
    config = AgentConfig(
        name="test_agent",
        type="test"
    )
    agent = BaseAgent(config)
    
    update1 = {"key1": "value1"}
    update2 = {"key2": "value2"}
    
    agent.update_state(update1)
    agent.update_state(update2)
    
    assert agent.state == {"key1": "value1", "key2": "value2"}
    assert len(agent.history) == 2
    assert agent.history[0]["state_update"] == update1
    assert agent.history[1]["state_update"] == update2

def test_should_raise_not_implemented_for_process():
    """Test process method raises NotImplementedError."""
    config = AgentConfig(
        name="test_agent",
        type="test"
    )
    agent = BaseAgent(config)
    
    with pytest.raises(NotImplementedError):
        agent.process({"test": "data"})
