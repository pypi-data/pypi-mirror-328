"""Unit tests for Agent functionality."""
import pytest

from adpa.agents import Agent
from adpa.agents.models import AgentConfig, Task


def test_agent_initialization():
    """Test Agent class initialization."""
    config = AgentConfig(
        name="test_agent",
        type="research",
        team="Research Team",
        description="Test agent",
        tools=["web_search", "summarization"],
        llm_config={"primary_provider": "OpenAI", "model": "gpt-4"},
    )
    agent = Agent(config)
    assert agent.name == "test_agent"
    assert agent.type == "research"
    assert len(agent.tools) == 2


def test_agent_task_execution():
    """Test task execution by agent."""
    agent = Agent(
        AgentConfig(
            name="test_agent",
            type="research",
            team="Research Team",
            description="Test agent",
            tools=["web_search"],
        )
    )

    task = Task(id="task_1", type="research", description="Search for Python tutorials", priority=1)

    result = agent.execute_task(task)
    assert result.status == "completed"
    assert result.output is not None


def test_agent_tool_access():
    """Test agent tool access and restrictions."""
    agent = Agent(
        AgentConfig(
            name="test_agent",
            type="research",
            team="Research Team",
            description="Test agent",
            tools=["web_search"],
        )
    )

    # Test allowed tool
    assert agent.can_use_tool("web_search")

    # Test restricted tool
    assert not agent.can_use_tool("code_generation")


def test_concurrent_task_limit():
    """Test maximum concurrent task limit."""
    agent = Agent(
        AgentConfig(
            name="test_agent",
            type="research",
            team="Research Team",
            description="Test agent",
            tools=["web_search"],
            max_concurrent_tasks=2,
        )
    )

    task1 = Task(id="task_1", type="research", description="Task 1")
    task2 = Task(id="task_2", type="research", description="Task 2")
    task3 = Task(id="task_3", type="research", description="Task 3")

    agent.execute_task(task1)
    agent.execute_task(task2)

    with pytest.raises(ValueError):
        agent.execute_task(task3)


def test_task_timeout():
    """Test task timeout functionality."""
    agent = Agent(
        AgentConfig(
            name="test_agent",
            type="research",
            team="Research Team",
            description="Test agent",
            tools=["web_search"],
            timeout=1,
        )
    )

    task = Task(id="long_task", type="research", description="This task should timeout", priority=1)

    with pytest.raises(TimeoutError):
        agent.execute_task(task)


def test_agent_state_management():
    """Test agent state management."""
    agent = Agent(
        AgentConfig(
            name="test_agent",
            type="research",
            team="Research Team",
            description="Test agent",
            tools=["web_search"],
        )
    )

    # Test state transitions
    assert agent.status == "idle"

    task = Task(id="task_1", type="research", description="Test task")
    agent.execute_task(task)

    assert agent.status == "busy"
    assert len(agent.task_history) == 1


def test_error_handling():
    """Test error handling in agent operations."""
    agent = Agent(
        AgentConfig(
            name="test_agent",
            type="research",
            team="Research Team",
            description="Test agent",
            tools=["web_search"],
        )
    )

    # Test invalid task
    with pytest.raises(ValueError):
        agent.execute_task(None)

    # Test unsupported task type
    task = Task(id="task_1", type="unsupported", description="Test task")
    with pytest.raises(ValueError):
        agent.execute_task(task)
