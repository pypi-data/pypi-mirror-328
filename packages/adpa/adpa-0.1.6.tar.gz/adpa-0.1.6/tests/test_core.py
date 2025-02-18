"""Test suite for ADPA Core functionality."""

import pytest
from adpa.core import CoreManager, DataProcessor, WorkflowEngine, EventSystem, StateManager
from adpa.core.types import CoreConfig, ProcessingResult, Workflow, WorkflowStep, Event

@pytest.fixture
def core_config() -> CoreConfig:
    """Create test configuration.
    
    Returns:
        Test configuration
    """
    return CoreConfig(
        max_threads=2,
        queue_size=100,
        batch_size=10
    )

@pytest.fixture
def core_manager(core_config: CoreConfig) -> CoreManager:
    """Create test core manager.
    
    Args:
        core_config: Test configuration
        
    Returns:
        Test core manager
    """
    return CoreManager(core_config)

@pytest.mark.unit
def test_should_initialize_core_manager_with_config(core_config: CoreConfig):
    """Test core manager initialization.
    
    Args:
        core_config: Test configuration
    """
    manager = CoreManager(core_config)
    assert manager.config == core_config
    assert isinstance(manager.processor, DataProcessor)
    assert isinstance(manager.workflow, WorkflowEngine)
    assert isinstance(manager.events, EventSystem)
    assert isinstance(manager.state, StateManager)

@pytest.mark.unit
async def test_should_process_valid_request(core_manager: CoreManager):
    """Test request processing.
    
    Args:
        core_manager: Test core manager
    """
    request = {
        "type": "test",
        "data": {"value": 42}
    }
    
    result = await core_manager.process_request(request)
    
    assert isinstance(result, ProcessingResult)
    assert result.success is True
    assert result.data["value"] == 42

@pytest.mark.unit
async def test_should_handle_invalid_request(core_manager: CoreManager):
    """Test invalid request handling.
    
    Args:
        core_manager: Test core manager
    """
    request = {
        "type": "invalid"
    }
    
    with pytest.raises(ValueError):
        await core_manager.process_request(request)

@pytest.mark.unit
async def test_should_emit_event_on_processing_complete(core_manager: CoreManager):
    """Test event emission.
    
    Args:
        core_manager: Test core manager
    """
    events = []
    
    async def handler(event: Event):
        events.append(event)
    
    core_manager.events.register_handler("processing_complete", handler)
    
    request = {
        "type": "test",
        "data": {"value": 42}
    }
    
    await core_manager.process_request(request)
    
    assert len(events) == 1
    assert events[0].type == "processing_complete"
    assert events[0].data["value"] == 42

@pytest.mark.integration
async def test_should_execute_workflow(core_manager: CoreManager):
    """Test workflow execution.
    
    Args:
        core_manager: Test core manager
    """
    workflow = Workflow(
        steps=[
            WorkflowStep(
                name="step1",
                action="test_action",
                dependencies=[]
            ),
            WorkflowStep(
                name="step2",
                action="test_action",
                dependencies=["step1"]
            )
        ]
    )
    
    results = await core_manager.workflow.execute_workflow(workflow)
    
    assert len(results) == 2
    assert "step1" in results
    assert "step2" in results

@pytest.mark.integration
async def test_should_maintain_state(core_manager: CoreManager):
    """Test state management.
    
    Args:
        core_manager: Test core manager
    """
    initial_state = await core_manager.state.get_state()
    
    update = {
        "counter": 1,
        "last_request": "test"
    }
    
    await core_manager.state.update_state(update)
    
    new_state = await core_manager.state.get_state()
    
    assert new_state != initial_state
    assert new_state.counter == 1
    assert new_state.last_request == "test"
