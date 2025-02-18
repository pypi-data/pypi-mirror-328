"""Shared test fixtures for ADPA tests.

This module provides common test fixtures used across the ADPA test suite.
It includes fixtures for configuration, mocking, and test environment setup.

Test Categories:
1. Unit Tests: Test individual components in isolation
2. Integration Tests: Test component interactions
3. End-to-End Tests: Test complete workflows
4. Performance Tests: Test system performance
5. Security Tests: Test security features

Usage:
    Import fixtures directly in test files:
    ```python
    def test_something(core_config, mock_database):
        # Test implementation
        pass
    ```

Configuration:
    - Test environment variables
    - Core configuration
    - API configuration
    - Monitoring configuration
    - Database configuration
"""

import os
import pytest
import tempfile
from typing import Generator, Dict, Any
from pathlib import Path

from adpa.core.types import CoreConfig
from adpa.api.types import APIConfig
from adpa.monitoring.types import MonitoringConfig
from adpa.security.types import SecurityConfig
from adpa.sql.types import SQLConfig

@pytest.fixture(scope="session")
def test_dir() -> Generator[Path, None, None]:
    """Create temporary test directory.
    
    Yields:
        Path: Temporary directory path for test artifacts
        
    Usage:
        def test_file_operations(test_dir):
            file_path = test_dir / "test.txt"
            # Test implementation
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)

@pytest.fixture(scope="session")
def env_vars() -> Dict[str, str]:
    """Get test environment variables.
    
    Returns:
        Dict[str, str]: Test environment variables including:
            - ADPA_ENV: Test environment
            - ADPA_LOG_LEVEL: Debug log level
            - ADPA_API_KEY: Test API key
            - ADPA_DATABASE_URL: In-memory SQLite
            - ADPA_SECURITY_KEY: Test security key
            
    Usage:
        def test_configuration(env_vars):
            os.environ.update(env_vars)
            # Test implementation
    """
    return {
        "ADPA_ENV": "test",
        "ADPA_LOG_LEVEL": "DEBUG",
        "ADPA_API_KEY": "test_key",
        "ADPA_DATABASE_URL": "sqlite:///:memory:",
        "ADPA_SECURITY_KEY": "test_security_key",
        "ADPA_MAX_THREADS": "2",
        "ADPA_QUEUE_SIZE": "100",
        "ADPA_BATCH_SIZE": "10",
        "ADPA_TIMEOUT": "30"
    }

@pytest.fixture
def core_config() -> CoreConfig:
    """Create test core configuration.
    
    Returns:
        CoreConfig: Test core configuration with:
            - max_threads: Maximum worker threads
            - queue_size: Task queue size
            - batch_size: Batch processing size
            - timeout: Operation timeout
            
    Usage:
        def test_core_feature(core_config):
            core = Core(core_config)
            # Test implementation
    """
    return CoreConfig(
        max_threads=2,
        queue_size=100,
        batch_size=10,
        timeout=30
    )

@pytest.fixture
def api_config() -> APIConfig:
    """Create test API configuration.
    
    Returns:
        APIConfig: Test API configuration with:
            - host: API host
            - port: API port
            - workers: API worker count
            - debug: API debug mode
            
    Usage:
        def test_api_feature(api_config):
            api = API(api_config)
            # Test implementation
    """
    return APIConfig(
        host="localhost",
        port=8000,
        workers=1,
        debug=True
    )

@pytest.fixture
def monitoring_config() -> MonitoringConfig:
    """Create test monitoring configuration.
    
    Returns:
        MonitoringConfig: Test monitoring configuration with:
            - interval: Monitoring interval
            - batch_size: Monitoring batch size
            - retention_days: Monitoring data retention
            
    Usage:
        def test_monitoring_feature(monitoring_config):
            monitoring = Monitoring(monitoring_config)
            # Test implementation
    """
    return MonitoringConfig(
        interval=1,
        batch_size=10,
        retention_days=1
    )

@pytest.fixture
def mock_database():
    """Create mock database.
    
    Returns:
        Mock database connection
        
    Usage:
        def test_database_feature(mock_database):
            # Test implementation
            pass
    """
    # Create in-memory SQLite database
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///:memory:")
    
    # Create tables
    from adpa.core.models import Base
    Base.metadata.create_all(engine)
    
    return engine

@pytest.fixture
def mock_cache():
    """Create mock cache.
    
    Returns:
        Mock cache
        
    Usage:
        def test_cache_feature(mock_cache):
            # Test implementation
            pass
    """
    cache = {}
    
    async def get(key: str) -> Any:
        return cache.get(key)
    
    async def set(key: str, value: Any) -> None:
        cache[key] = value
    
    return type("MockCache", (), {
        "get": get,
        "set": set,
        "cache": cache
    })

@pytest.fixture
def mock_event_bus():
    """Create mock event bus.
    
    Returns:
        Mock event bus
        
    Usage:
        def test_event_bus_feature(mock_event_bus):
            # Test implementation
            pass
    """
    events = []
    
    async def emit(event_type: str, data: Any) -> None:
        events.append((event_type, data))
    
    return type("MockEventBus", (), {
        "emit": emit,
        "events": events
    })

"""Pytest configuration for ADPA framework tests."""
import pytest
from pathlib import Path
import sys

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import ADPA components
from adpa.core.attention.focus import FocusManager, FocusMetrics
from adpa.core.desire.goals import GoalManager, Goal
from adpa.core.position.context import ContextManager, ContextData
from adpa.core.action.execution import ActionExecutor, ActionResult
from adpa.agents.base import BaseAgent, AgentConfig
from adpa.monitoring.metrics import MetricsCollector

@pytest.fixture
def focus_manager():
    """Create FocusManager instance."""
    return FocusManager()

@pytest.fixture
def goal_manager():
    """Create GoalManager instance."""
    return GoalManager()

@pytest.fixture
def context_manager():
    """Create ContextManager instance."""
    return ContextManager()

@pytest.fixture
def action_executor():
    """Create ActionExecutor instance."""
    return ActionExecutor()

@pytest.fixture
def metrics_collector():
    """Create MetricsCollector instance."""
    return MetricsCollector()

@pytest.fixture
def base_agent():
    """Create BaseAgent instance."""
    config = AgentConfig(name="test_agent", type="test")
    return BaseAgent(config)
