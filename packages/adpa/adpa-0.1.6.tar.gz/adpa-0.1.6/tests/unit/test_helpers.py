"""Test helper utilities."""

import asyncio
import functools
from typing import Callable, Any

def async_test(func: Callable) -> Callable:
    """Decorator to run async test functions.
    
    Args:
        func: Async function to run
        
    Returns:
        Wrapped function that runs in event loop
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Create a new event loop for each test
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            return loop.run_until_complete(func(*args, **kwargs))
        finally:
            loop.close()
            asyncio.set_event_loop(None)
    return wrapper
