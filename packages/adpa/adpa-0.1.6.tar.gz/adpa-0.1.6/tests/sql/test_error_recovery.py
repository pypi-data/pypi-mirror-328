"""Tests for SQL error recovery scenarios."""
import pytest
import asyncio
from typing import Optional
from sqlalchemy import create_engine
from adpa.sql.generator import SQLGenerator, SQLGenerationConfig
from adpa.sql.validation import SQLValidator
from adpa.sql.middleware import SQLMiddleware


class ErrorSimulator:
    """Simulates various error conditions."""

    def __init__(self):
        """Initialize error simulator."""
        self.next_error: Optional[Exception] = None
        self.error_count: int = 0
        self.recovery_attempts: int = 0

    def set_next_error(self, error: Exception):
        """Set next error to be raised."""
        self.next_error = error

    def maybe_raise(self):
        """Raise error if one is set."""
        if self.next_error:
            error = self.next_error
            self.next_error = None
            self.error_count += 1
            raise error

    def record_recovery(self):
        """Record recovery attempt."""
        self.recovery_attempts += 1


@pytest.fixture
def error_simulator():
    """Create error simulator."""
    return ErrorSimulator()


@pytest.fixture
def mock_db(mocker):
    """Create mock database with error simulation."""
    db = mocker.Mock()
    db.connect.return_value.__enter__.return_value = mocker.Mock()
    return db


@pytest.fixture
def generator(mock_db, error_simulator):
    """Create SQL generator with error simulation."""
    config = SQLGenerationConfig()
    generator = SQLGenerator(config, mock_db)
    
    original_generate = generator.generate_query
    
    def generate_with_errors(*args, **kwargs):
        error_simulator.maybe_raise()
        try:
            return original_generate(*args, **kwargs)
        except Exception as e:
            error_simulator.record_recovery()
            if isinstance(e, (ValueError, KeyError)):
                return {
                    "success": False,
                    "error": str(e),
                    "fallback_query": "SELECT 1"
                }
            raise
    
    generator.generate_query = generate_with_errors
    return generator


def test_should_recover_from_connection_error(generator, error_simulator):
    """Test recovery from database connection error."""
    error_simulator.set_next_error(ConnectionError("DB connection failed"))
    
    result = generator.generate_query("Show users")
    
    assert not result["success"]
    assert "connection failed" in result["error"].lower()
    assert error_simulator.recovery_attempts == 1


def test_should_handle_timeout(generator, error_simulator):
    """Test handling of timeout error."""
    error_simulator.set_next_error(TimeoutError("Query timeout"))
    
    result = generator.generate_query("Show users")
    
    assert not result["success"]
    assert "timeout" in result["error"].lower()
    assert "fallback_query" in result


def test_should_retry_on_deadlock(generator, error_simulator):
    """Test retry on deadlock error."""
    class DeadlockError(Exception):
        pass
    
    error_simulator.set_next_error(DeadlockError("Deadlock detected"))
    
    result = generator.generate_query("Update user status")
    
    assert not result["success"]
    assert "deadlock" in result["error"].lower()
    assert error_simulator.recovery_attempts >= 1


def test_should_handle_syntax_error(generator, error_simulator):
    """Test handling of SQL syntax error."""
    error_simulator.set_next_error(ValueError("Invalid SQL syntax"))
    
    result = generator.generate_query("Invalid query")
    
    assert not result["success"]
    assert "syntax" in result["error"].lower()
    assert "fallback_query" in result


def test_should_handle_schema_error(generator, error_simulator):
    """Test handling of schema error."""
    error_simulator.set_next_error(KeyError("Table not found"))
    
    result = generator.generate_query("Show missing_table")
    
    assert not result["success"]
    assert "table not found" in result["error"].lower()
    assert "fallback_query" in result


def test_should_handle_concurrent_errors(generator, error_simulator):
    """Test handling of errors in concurrent requests."""
    async def make_requests():
        tasks = []
        for _ in range(5):
            error_simulator.set_next_error(ValueError("Random error"))
            task = asyncio.create_task(
                asyncio.to_thread(generator.generate_query, "Test query")
            )
            tasks.append(task)
        return await asyncio.gather(*tasks, return_exceptions=True)
    
    results = asyncio.run(make_requests())
    assert all(not r["success"] for r in results)
    assert error_simulator.recovery_attempts == 5


def test_should_handle_memory_error(generator, error_simulator):
    """Test handling of memory error."""
    error_simulator.set_next_error(MemoryError("Out of memory"))
    
    result = generator.generate_query("Large query")
    
    assert not result["success"]
    assert "memory" in result["error"].lower()
    assert error_simulator.recovery_attempts == 1


def test_should_handle_validation_error(generator, error_simulator):
    """Test handling of validation error."""
    class ValidationError(Exception):
        pass
    
    error_simulator.set_next_error(ValidationError("Invalid query structure"))
    
    result = generator.generate_query("Invalid structure")
    
    assert not result["success"]
    assert "invalid" in result["error"].lower()
    assert error_simulator.recovery_attempts == 1


def test_should_handle_resource_exhaustion(generator, error_simulator):
    """Test handling of resource exhaustion."""
    error_simulator.set_next_error(RuntimeError("Too many connections"))
    
    result = generator.generate_query("Resource heavy query")
    
    assert not result["success"]
    assert "connections" in result["error"].lower()
    assert error_simulator.recovery_attempts == 1


def test_should_handle_partial_failure(generator, error_simulator):
    """Test handling of partial query failure."""
    class PartialFailureError(Exception):
        pass
    
    error_simulator.set_next_error(PartialFailureError("Some parts failed"))
    
    result = generator.generate_query("Complex query")
    
    assert not result["success"]
    assert "partial" in result["error"].lower()
    assert "fallback_query" in result


def test_should_handle_cascading_errors(generator, error_simulator):
    """Test handling of cascading errors."""
    errors = [
        ValueError("First error"),
        RuntimeError("Second error"),
        TimeoutError("Third error")
    ]
    
    results = []
    for error in errors:
        error_simulator.set_next_error(error)
        result = generator.generate_query("Test query")
        results.append(result)
    
    assert all(not r["success"] for r in results)
    assert error_simulator.recovery_attempts == len(errors)


def test_should_handle_recovery_failure(generator, error_simulator):
    """Test handling of recovery failure."""
    class RecoveryError(Exception):
        pass
    
    def fail_twice(*args, **kwargs):
        if error_simulator.recovery_attempts < 2:
            error_simulator.record_recovery()
            raise RecoveryError("Recovery failed")
        return {"success": True, "query": "SELECT 1"}
    
    generator.generate_query = fail_twice
    
    result = generator.generate_query("Test query")
    
    assert result["success"]
    assert error_simulator.recovery_attempts == 2


def test_should_maintain_consistency(generator, error_simulator):
    """Test maintaining data consistency during errors."""
    class ConsistencyError(Exception):
        pass
    
    error_simulator.set_next_error(ConsistencyError("Consistency check failed"))
    
    result = generator.generate_query("Update data")
    
    assert not result["success"]
    assert "consistency" in result["error"].lower()
    assert error_simulator.recovery_attempts == 1


def test_should_handle_cleanup_error(generator, error_simulator):
    """Test handling of cleanup error after main error."""
    class CleanupError(Exception):
        pass
    
    def cleanup_error(*args, **kwargs):
        error_simulator.record_recovery()
        raise CleanupError("Cleanup failed")
    
    generator.cleanup = cleanup_error
    error_simulator.set_next_error(ValueError("Main error"))
    
    result = generator.generate_query("Test query")
    
    assert not result["success"]
    assert error_simulator.recovery_attempts >= 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
