"""Test position components."""
import pytest
from datetime import datetime
from adpa.core.position.state import StateManager, StateSnapshot
from adpa.core.position.context import ContextManager

def test_should_create_state_snapshot():
    """Test creating state snapshot."""
    snapshot = StateSnapshot(
        timestamp=datetime.utcnow(),
        variables={"var1": 1, "var2": "test"},
        resources={"cpu": 0.5, "memory": 0.7},
        status="running"
    )
    
    assert isinstance(snapshot.timestamp, datetime)
    assert snapshot.variables == {"var1": 1, "var2": "test"}
    assert snapshot.resources == {"cpu": 0.5, "memory": 0.7}
    assert snapshot.status == "running"

def test_should_manage_state_history(state_manager):
    """Test state history management."""
    # Create initial state
    state_manager.update_state({"var1": 1})
    assert len(state_manager.history) == 1
    assert state_manager.current_state["var1"] == 1
    
    # Update state
    state_manager.update_state({"var2": "test"})
    assert len(state_manager.history) == 2
    assert state_manager.current_state["var1"] == 1
    assert state_manager.current_state["var2"] == "test"
    
    # Get state at specific time
    timestamp = state_manager.history[0].timestamp
    historical_state = state_manager.get_state_at(timestamp)
    assert historical_state["var1"] == 1
    assert "var2" not in historical_state

def test_should_handle_resource_updates(state_manager):
    """Test resource state updates."""
    resources = {
        "cpu": 0.5,
        "memory": 0.7,
        "disk": 0.3
    }
    
    state_manager.update_resources(resources)
    assert state_manager.current_resources == resources
    
    # Update single resource
    state_manager.update_resources({"cpu": 0.8})
    assert state_manager.current_resources["cpu"] == 0.8
    assert state_manager.current_resources["memory"] == 0.7

def test_should_manage_context(context_manager):
    """Test context management."""
    # Add context variables
    context_manager.set_context("user", "test_user")
    context_manager.set_context("env", "test")
    
    assert context_manager.get_context("user") == "test_user"
    assert context_manager.get_context("env") == "test"
    
    # Update context
    context_manager.set_context("user", "new_user")
    assert context_manager.get_context("user") == "new_user"
    
    # Remove context
    context_manager.remove_context("env")
    assert context_manager.get_context("env") is None

def test_should_handle_nested_context(context_manager):
    """Test nested context handling."""
    context = {
        "user": {
            "id": "user1",
            "role": "admin",
            "settings": {
                "theme": "dark",
                "notifications": True
            }
        }
    }
    
    context_manager.set_context("user", context["user"])
    assert context_manager.get_context("user.id") == "user1"
    assert context_manager.get_context("user.settings.theme") == "dark"
    
    # Update nested context
    context_manager.set_context("user.settings.theme", "light")
    assert context_manager.get_context("user.settings.theme") == "light"

def test_should_handle_context_snapshots(context_manager):
    """Test context snapshot functionality."""
    # Set initial context
    context_manager.set_context("var1", "value1")
    context_manager.set_context("var2", "value2")
    
    # Create snapshot
    snapshot = context_manager.create_snapshot()
    
    # Modify context
    context_manager.set_context("var1", "new_value")
    context_manager.set_context("var3", "value3")
    
    # Restore snapshot
    context_manager.restore_snapshot(snapshot)
    assert context_manager.get_context("var1") == "value1"
    assert context_manager.get_context("var2") == "value2"
    assert context_manager.get_context("var3") is None
