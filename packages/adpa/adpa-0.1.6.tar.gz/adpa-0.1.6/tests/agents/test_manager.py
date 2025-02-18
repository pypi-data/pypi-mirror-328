"""Tests for agent management functionality."""

import pytest
from datetime import datetime

from adpa.agents.types import (
    AgentConfig, AgentHealth, AgentStatus, AgentType,
    AgentPriority, ResourceLimits, RetryConfig
)
from adpa.agents.manager import AgentManager


@pytest.fixture
def agent_config():
    """Create sample agent configuration."""
    return AgentConfig(
        agent_type=AgentType.PROCESSOR,
        priority=AgentPriority.HIGH,
        resource_limits=ResourceLimits(
            max_memory="1G",
            max_cpu=1.0,
            max_tasks=5
        ),
        retry_config=RetryConfig(
            max_attempts=5,
            initial_delay=0.1
        )
    )


@pytest.fixture
def manager(agent_config):
    """Create AgentManager instance."""
    return AgentManager(agent_config)


@pytest.mark.asyncio
async def test_start_agent(manager):
    """Test starting an agent."""
    # Start new agent
    await manager.start_agent("test_agent")
    assert "test_agent" in manager._agents
    assert manager._agents["test_agent"] == AgentStatus.RUNNING

    # Try starting duplicate agent
    with pytest.raises(ValueError, match="already exists"):
        await manager.start_agent("test_agent")


@pytest.mark.asyncio
async def test_stop_agent(manager):
    """Test stopping an agent."""
    # Start and stop agent
    await manager.start_agent("test_agent")
    await manager.stop_agent("test_agent")
    assert manager._agents["test_agent"] == AgentStatus.TERMINATED

    # Try stopping non-existent agent
    with pytest.raises(ValueError, match="not found"):
        await manager.stop_agent("invalid_agent")


@pytest.mark.asyncio
async def test_check_agent_health(manager):
    """Test checking agent health."""
    # Start agent and check health
    await manager.start_agent("test_agent")
    health = await manager.check_agent_health("test_agent")
    assert isinstance(health, AgentHealth)
    assert health.is_healthy

    # Try checking non-existent agent
    with pytest.raises(ValueError, match="not found"):
        await manager.check_agent_health("invalid_agent")


@pytest.mark.asyncio
async def test_get_resource_usage(manager):
    """Test getting resource usage."""
    # Start agent and check resources
    await manager.start_agent("test_agent")
    usage = await manager.get_resource_usage("test_agent")
    assert usage.memory >= 0.0
    assert usage.cpu >= 0.0
    assert usage.disk >= 0.0
    assert usage.network >= 0.0

    # Try checking non-existent agent
    with pytest.raises(ValueError, match="not found"):
        await manager.get_resource_usage("invalid_agent")
