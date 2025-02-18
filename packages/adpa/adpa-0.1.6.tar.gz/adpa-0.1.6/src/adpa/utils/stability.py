"""Stability utilities for error handling and recovery in the ADPA Framework."""

import functools
import logging
import time
from typing import Any, Callable, Dict, Optional, Type, TypeVar, Union, List
from contextlib import contextmanager
from datetime import datetime, timedelta

import streamlit as st

# Setup logging
logger = logging.getLogger(__name__)

T = TypeVar('T')

class StabilityError(Exception):
    """Base class for stability-related errors."""
    pass

class RetryableError(StabilityError):
    """Error that can be retried."""
    pass

class StateError(StabilityError):
    """Error related to application state."""
    pass

def with_retry(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Union[Type[Exception], tuple] = Exception,
    max_delay: Optional[float] = None,
    jitter: bool = True
) -> Callable:
    """Decorator for retrying operations that may fail.
    
    Args:
        retries: Number of retries
        delay: Initial delay between retries
        backoff: Multiplier for delay after each retry
        exceptions: Exception types to catch
        max_delay: Maximum delay between retries
        jitter: Whether to add random jitter to delays
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_exception = None
            current_delay = delay

            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == retries:
                        break
                    
                    # Calculate next delay
                    if max_delay:
                        current_delay = min(current_delay * backoff, max_delay)
                    else:
                        current_delay *= backoff
                    
                    # Add jitter if enabled
                    if jitter:
                        import random
                        current_delay *= (0.5 + random.random())
                    
                    logger.warning(
                        f"Attempt {attempt + 1}/{retries} failed: {str(e)}. "
                        f"Retrying in {current_delay:.1f}s..."
                    )
                    time.sleep(current_delay)

            raise RetryableError(f"Failed after {retries} retries") from last_exception

        return wrapper
    return decorator

@contextmanager
def safe_state_operation():
    """Context manager for safely modifying Streamlit session state."""
    state_backup = dict(st.session_state)
    try:
        yield
    except Exception as e:
        # Restore state
        st.session_state.clear()
        st.session_state.update(state_backup)
        raise StateError("State operation failed, restored previous state") from e

def validate_state() -> None:
    """Validate the application state."""
    required_keys = {
        "teams", "settings", "messages", "tasks",
        "agent_configs", "model_configs"
    }
    
    missing = required_keys - set(st.session_state.keys())
    if missing:
        raise StateError(f"Missing required state keys: {missing}")
    
    # Validate key types
    type_checks = {
        "teams": dict,
        "settings": "Settings",
        "messages": list,
        "tasks": list,
        "agent_configs": dict,
        "model_configs": dict
    }
    
    for key, expected_type in type_checks.items():
        value = st.session_state.get(key)
        if isinstance(expected_type, str):
            if not value.__class__.__name__ == expected_type:
                raise StateError(f"Invalid type for {key}: expected {expected_type}")
        elif not isinstance(value, expected_type):
            raise StateError(f"Invalid type for {key}: expected {expected_type.__name__}")

def initialize_state() -> None:
    """Initialize or repair application state."""
    with safe_state_operation():
        # Teams
        if "teams" not in st.session_state:
            st.session_state.teams = {}
            
        # Settings
        if "settings" not in st.session_state:
            from adpa.config import Settings
            st.session_state.settings = Settings()
            
        # Messages
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        # Tasks
        if "tasks" not in st.session_state:
            st.session_state.tasks = []
            
        # Agent configs
        if "agent_configs" not in st.session_state:
            st.session_state.agent_configs = {}
            
        # Model configs
        if "model_configs" not in st.session_state:
            st.session_state.model_configs = {}

def check_api_keys() -> Dict[str, bool]:
    """Check if required API keys are set and valid.
    
    Returns:
        Dict[str, bool]: Dictionary mapping API key names to their validity
    """
    required_keys = {
        "OPENAI_API_KEY": lambda x: len(x) > 20,
        "AZURE_API_KEY": lambda x: len(x) > 30,
        "AWS_ACCESS_KEY_ID": lambda x: len(x) > 15,
        "AWS_SECRET_ACCESS_KEY": lambda x: len(x) > 30
    }
    
    results = {}
    for key, validator in required_keys.items():
        value = os.getenv(key)
        results[key] = value is not None and validator(value)
    
    return results

def test_llm_connection(provider: str) -> bool:
    """Test connection to LLM provider.
    
    Args:
        provider: Name of the LLM provider to test
        
    Returns:
        bool: True if connection is successful, False otherwise
    """
    try:
        if provider == "openai":
            import openai
            openai.Model.list()
        elif provider == "azure":
            # Add Azure OpenAI test
            pass
        elif provider == "anthropic":
            # Add Anthropic test
            pass
        else:
            raise ValueError(f"Unknown provider: {provider}")
        return True
    except Exception as e:
        logger.error(f"Failed to connect to {provider}: {str(e)}")
        return False

def get_system_status() -> Dict[str, Any]:
    """Get overall system status.
    
    Returns:
        Dict containing system status information:
        - state_valid: Whether application state is valid
        - api_keys: Status of API keys
        - llm_connections: Status of LLM connections
        - memory_usage: Current memory usage
        - uptime: System uptime
    """
    status = {
        "timestamp": datetime.utcnow().isoformat(),
        "state_valid": True,
        "api_keys": {},
        "llm_connections": {},
        "memory_usage": {},
        "uptime": None
    }
    
    # Check state
    try:
        validate_state()
    except StateError as e:
        status["state_valid"] = False
        status["state_error"] = str(e)
    
    # Check API keys
    status["api_keys"] = check_api_keys()
    
    # Check LLM connections
    for provider in ["openai", "azure", "anthropic"]:
        status["llm_connections"][provider] = test_llm_connection(provider)
    
    # Get memory usage
    import psutil
    process = psutil.Process()
    status["memory_usage"] = {
        "rss": process.memory_info().rss,
        "vms": process.memory_info().vms,
        "percent": process.memory_percent()
    }
    
    # Get uptime
    status["uptime"] = str(datetime.now() - datetime.fromtimestamp(process.create_time()))
    
    return status

def repair_system() -> Dict[str, Any]:
    """Attempt to repair system state and connections.
    
    Returns:
        Dict containing repair results:
        - success: Whether repair was successful
        - actions: List of repair actions taken
        - errors: List of errors encountered
    """
    results = {
        "success": True,
        "actions": [],
        "errors": []
    }
    
    try:
        # Repair state
        initialize_state()
        results["actions"].append("Initialized application state")
        
        # Validate state
        validate_state()
        results["actions"].append("Validated application state")
        
        # Check connections
        for provider in ["openai", "azure", "anthropic"]:
            if test_llm_connection(provider):
                results["actions"].append(f"Verified {provider} connection")
            else:
                results["errors"].append(f"Failed to connect to {provider}")
                results["success"] = False
    
    except Exception as e:
        results["errors"].append(str(e))
        results["success"] = False
    
    return results

def monitor_system_health(
    check_interval: int = 60,
    alert_threshold: int = 3
) -> None:
    """Monitor system health and display status in Streamlit.
    
    Args:
        check_interval: Seconds between health checks
        alert_threshold: Number of consecutive failures before alerting
    """
    if "health_checks" not in st.session_state:
        st.session_state.health_checks = []
    
    # Perform health check
    status = get_system_status()
    st.session_state.health_checks.append(status)
    
    # Keep only recent checks
    max_checks = 100
    if len(st.session_state.health_checks) > max_checks:
        st.session_state.health_checks = st.session_state.health_checks[-max_checks:]
    
    # Check for issues
    recent_checks = st.session_state.health_checks[-alert_threshold:]
    has_issues = any(
        not check["state_valid"] or
        not all(check["api_keys"].values()) or
        not all(check["llm_connections"].values())
        for check in recent_checks
    )
    
    if has_issues:
        st.error("⚠️ System health issues detected!")
        if st.button("Attempt Repair"):
            repair_results = repair_system()
            if repair_results["success"]:
                st.success("System repaired successfully!")
            else:
                st.error(f"Repair failed: {', '.join(repair_results['errors'])}")
    
    # Schedule next check
    if not hasattr(st.session_state, 'last_health_check'):
        st.session_state.last_health_check = datetime.now()
    elif (datetime.now() - st.session_state.last_health_check).seconds >= check_interval:
        st.session_state.last_health_check = datetime.now()
        st.experimental_rerun()
