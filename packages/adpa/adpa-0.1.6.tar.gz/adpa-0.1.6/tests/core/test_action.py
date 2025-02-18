"""Test action components."""
import pytest
from datetime import datetime
from adpa.core.action.executor import ActionExecutor, Action
from adpa.core.action.validator import ActionValidator

def test_should_create_action():
    """Test action creation."""
    action = Action(
        id="test_action",
        type="database_query",
        parameters={"query": "SELECT * FROM test"},
        priority=0.8,
        timeout=30
    )
    
    assert action.id == "test_action"
    assert action.type == "database_query"
    assert action.parameters == {"query": "SELECT * FROM test"}
    assert action.priority == 0.8
    assert action.timeout == 30
    assert action.status == "pending"

def test_should_execute_action(action_executor):
    """Test action execution."""
    action = Action(
        id="test_action",
        type="log_message",
        parameters={"message": "Test message"}
    )
    
    result = action_executor.execute(action)
    assert result.success
    assert action.status == "completed"
    assert isinstance(result.completion_time, datetime)

def test_should_handle_action_failure(action_executor):
    """Test handling failed actions."""
    action = Action(
        id="test_action",
        type="invalid_type",
        parameters={}
    )
    
    result = action_executor.execute(action)
    assert not result.success
    assert action.status == "failed"
    assert result.error is not None

def test_should_validate_action(action_validator):
    """Test action validation."""
    # Valid action
    valid_action = Action(
        id="test_action",
        type="database_query",
        parameters={"query": "SELECT * FROM test"}
    )
    assert action_validator.validate(valid_action)
    
    # Invalid action (missing required parameter)
    invalid_action = Action(
        id="test_action",
        type="database_query",
        parameters={}
    )
    assert not action_validator.validate(invalid_action)

def test_should_handle_action_timeout(action_executor):
    """Test action timeout handling."""
    action = Action(
        id="test_action",
        type="long_running_task",
        parameters={},
        timeout=0.1  # Very short timeout
    )
    
    result = action_executor.execute(action)
    assert not result.success
    assert action.status == "timeout"
    assert "timeout" in result.error.lower()

def test_should_handle_parallel_actions(action_executor):
    """Test parallel action execution."""
    actions = [
        Action(id=f"action_{i}", 
               type="quick_task",
               parameters={}) 
        for i in range(3)
    ]
    
    results = action_executor.execute_parallel(actions)
    assert len(results) == 3
    assert all(r.success for r in results)
    assert all(a.status == "completed" for a in actions)

def test_should_handle_action_dependencies(action_executor):
    """Test action dependency handling."""
    action1 = Action(
        id="action1",
        type="task1",
        parameters={}
    )
    
    action2 = Action(
        id="action2",
        type="task2",
        parameters={},
        dependencies=["action1"]
    )
    
    # Execute dependent actions
    result1 = action_executor.execute(action1)
    assert result1.success
    
    result2 = action_executor.execute(action2)
    assert result2.success
    assert result2.start_time > result1.completion_time

def test_should_validate_action_sequence(action_validator):
    """Test validation of action sequences."""
    actions = [
        Action(id="action1", type="task1", parameters={}),
        Action(id="action2", type="task2", parameters={}, dependencies=["action1"]),
        Action(id="action3", type="task3", parameters={}, dependencies=["action2"])
    ]
    
    # Valid sequence
    assert action_validator.validate_sequence(actions)
    
    # Invalid sequence (circular dependency)
    actions[0].dependencies = ["action3"]
    assert not action_validator.validate_sequence(actions)
