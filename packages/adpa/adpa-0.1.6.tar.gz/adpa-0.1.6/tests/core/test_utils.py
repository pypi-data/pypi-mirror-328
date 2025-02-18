"""Tests for core utilities."""
import asyncio
import pytest
from typing import Any, List

from adpa.core.utils import AsyncBatcher, ThreadPoolManager, memoize, validate_json
from adpa.core.exceptions import ValidationError


@pytest.mark.asyncio
async def test_should_batch_items_when_using_async_batcher():
    """Test AsyncBatcher functionality."""
    processed_items: List[List[int]] = []

    async def process_batch(items: List[int]) -> None:
        processed_items.append(items)

    batcher = AsyncBatcher[int](batch_size=3, flush_interval=0.1, processor=process_batch)

    # Add items
    for i in range(5):
        await batcher.add(i)

    # Wait for automatic flush
    await asyncio.sleep(0.2)

    # Add more items and manual flush
    for i in range(5, 8):
        await batcher.add(i)
    await batcher.flush()

    assert len(processed_items) == 3
    assert processed_items[0] == [0, 1, 2]  # First batch (size limit)
    assert processed_items[1] == [3, 4]  # Second batch (time limit)
    assert processed_items[2] == [5, 6, 7]  # Third batch (manual flush)


def test_should_execute_in_thread_pool():
    """Test ThreadPoolManager functionality."""
    def cpu_bound(x: int) -> int:
        return x * x

    manager = ThreadPoolManager(max_workers=2)

    with manager.get_executor() as executor:
        futures = [executor.submit(cpu_bound, i) for i in range(5)]
        results = [f.result() for f in futures]

    assert results == [0, 1, 4, 9, 16]


@pytest.mark.asyncio
async def test_should_run_function_in_thread():
    """Test running function in thread pool."""
    def cpu_bound(x: int, y: int) -> int:
        return x * y

    manager = ThreadPoolManager(max_workers=2)
    result = await manager.run_in_thread(cpu_bound, 5, y=3)

    assert result == 15


def test_should_memoize_function_results():
    """Test memoization decorator."""
    call_count = 0

    @memoize
    def expensive_function(x: int, y: int) -> int:
        nonlocal call_count
        call_count += 1
        return x * y

    # First call
    result1 = expensive_function(2, 3)
    assert result1 == 6
    assert call_count == 1

    # Second call with same arguments
    result2 = expensive_function(2, 3)
    assert result2 == 6
    assert call_count == 1  # Should not increase

    # Call with different arguments
    result3 = expensive_function(3, 4)
    assert result3 == 12
    assert call_count == 2


def test_should_memoize_with_maxsize():
    """Test memoization with maximum cache size."""
    call_count = 0

    @memoize(maxsize=2)
    def expensive_function(x: int) -> int:
        nonlocal call_count
        call_count += 1
        return x * x

    expensive_function(1)  # Cache: {1}
    assert call_count == 1

    expensive_function(2)  # Cache: {1, 2}
    assert call_count == 2

    expensive_function(3)  # Cache: {2, 3}, 1 evicted
    assert call_count == 3

    expensive_function(2)  # Cache hit
    assert call_count == 3

    expensive_function(1)  # Cache miss, recalculate
    assert call_count == 4


def test_should_validate_json_with_valid_input():
    """Test JSON validation with valid input."""
    # Test simple types
    assert validate_json(42) == 42
    assert validate_json("test") == "test"
    assert validate_json(True) is True
    assert validate_json(None) is None

    # Test dictionary
    data = {"a": 1, "b": "test", "c": [1, 2, 3]}
    result = validate_json(data)
    assert result == data

    # Test nested structures
    nested = {
        "a": {
            "b": [1, {"c": "test"}],
            "d": None
        }
    }
    result = validate_json(nested)
    assert result == nested


def test_should_validate_json_with_custom_object():
    """Test JSON validation with custom object."""
    class CustomObject:
        def __init__(self, value: Any):
            self.value = value

        def to_json(self) -> dict[str, Any]:
            return {"value": self.value}

    obj = CustomObject(42)
    result = validate_json(obj)
    assert result == {"value": 42}


def test_should_raise_error_for_invalid_json():
    """Test JSON validation with invalid input."""
    class NonSerializable:
        pass

    with pytest.raises(ValueError):
        validate_json(NonSerializable())
