"""Tests for core ADPA components."""
import pytest
from typing import Dict, List, Optional

from adpa.core.base import BaseComponent, ComponentConfig
from adpa.core.types import ComponentType, ProcessingState
from adpa.core.utils import validate_config


class TestComponent(BaseComponent):
    """Test component for unit tests."""

    def __init__(self, config: ComponentConfig):
        super().__init__(config)
        self.processed_data: List[Dict] = []

    async def process(self, data: Dict) -> Optional[Dict]:
        """Process test data."""
        self.processed_data.append(data)
        return {"processed": True, **data}


@pytest.fixture
def component_config():
    """Fixture for component configuration."""
    return ComponentConfig(
        name="test_component",
        type=ComponentType.PROCESSOR,
        enabled=True,
        config={
            "timeout": 30,
            "max_retries": 3
        }
    )


@pytest.fixture
def test_component(component_config):
    """Fixture for test component."""
    return TestComponent(component_config)


def test_component_initialization(component_config):
    """Test component initialization."""
    component = TestComponent(component_config)
    assert component.name == "test_component"
    assert component.type == ComponentType.PROCESSOR
    assert component.enabled is True
    assert component.config["timeout"] == 30
    assert component.config["max_retries"] == 3


@pytest.mark.asyncio
async def test_component_processing(test_component):
    """Test component data processing."""
    test_data = {"input": "test"}
    result = await test_component.process(test_data)
    
    assert result is not None
    assert result["processed"] is True
    assert result["input"] == "test"
    assert len(test_component.processed_data) == 1
    assert test_component.processed_data[0] == test_data


def test_component_config_validation(component_config):
    """Test component configuration validation."""
    # Test valid config
    assert validate_config(component_config) is True

    # Test invalid config
    invalid_config = ComponentConfig(
        name="",  # Invalid: empty name
        type=ComponentType.PROCESSOR,
        enabled=True,
        config={}
    )
    with pytest.raises(ValueError):
        validate_config(invalid_config)


@pytest.mark.asyncio
async def test_component_error_handling(test_component):
    """Test component error handling."""
    # Test with invalid input
    with pytest.raises(ValueError):
        await test_component.process(None)

    # Test with empty input
    with pytest.raises(ValueError):
        await test_component.process({})


def test_component_state_management(test_component):
    """Test component state management."""
    # Test initial state
    assert test_component.state == ProcessingState.IDLE

    # Test state transitions
    test_component.state = ProcessingState.PROCESSING
    assert test_component.state == ProcessingState.PROCESSING

    test_component.state = ProcessingState.ERROR
    assert test_component.state == ProcessingState.ERROR

    # Test invalid state transition
    with pytest.raises(ValueError):
        test_component.state = "INVALID_STATE"


@pytest.mark.asyncio
async def test_component_concurrent_processing(test_component):
    """Test concurrent processing capabilities."""
    import asyncio

    # Create multiple processing tasks
    test_data = [{"input": f"test_{i}"} for i in range(5)]
    tasks = [test_component.process(data) for data in test_data]

    # Run tasks concurrently
    results = await asyncio.gather(*tasks)

    # Verify results
    assert len(results) == 5
    assert all(r["processed"] for r in results)
    assert len(test_component.processed_data) == 5


def test_component_configuration_updates(test_component):
    """Test dynamic configuration updates."""
    # Test updating timeout
    test_component.config["timeout"] = 60
    assert test_component.config["timeout"] == 60

    # Test adding new config option
    test_component.config["new_option"] = "value"
    assert test_component.config["new_option"] == "value"

    # Test removing config option
    del test_component.config["new_option"]
    assert "new_option" not in test_component.config


@pytest.mark.parametrize("test_input,expected", [
    ({"input": "test1"}, True),
    ({"input": "test2", "extra": "data"}, True),
    ({"input": ""}, False),
])
async def test_component_input_validation(test_component, test_input, expected):
    """Test input validation with different scenarios."""
    if expected:
        result = await test_component.process(test_input)
        assert result["processed"] is True
    else:
        with pytest.raises(ValueError):
            await test_component.process(test_input)
