"""Test utilities."""

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
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(func(*args, **kwargs))
    return wrapper
