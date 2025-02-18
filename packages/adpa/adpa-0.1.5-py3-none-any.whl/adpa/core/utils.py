"""Utility functions for ADPA framework."""
import asyncio
import functools
import inspect
import logging
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager, contextmanager
from typing import (
    Any,
    AsyncGenerator,
    AsyncIterator,
    Awaitable,
    Callable,
    Generator,
    Generic,
    ParamSpec,
    TypeVar,
    cast,
    overload,
)
from typing_extensions import override

from .types import JSON, Callback, T

logger = logging.getLogger(__name__)
P = ParamSpec("P")
R = TypeVar("R")


def async_retry(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[Callable[P, Awaitable[R]]], Callable[P, Awaitable[R]]]:
    """Retry async function with exponential backoff.

    Args:
        retries: Maximum number of retries
        delay: Initial delay between retries in seconds
        backoff: Backoff multiplier
        exceptions: Tuple of exceptions to catch

    Returns:
        Decorated function
    """

    def decorator(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
        @functools.wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exception: Exception | None = None
            current_delay = delay

            for attempt in range(retries + 1):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == retries:
                        break
                    logger.warning(
                        f"Attempt {attempt + 1}/{retries} failed: {str(e)}. "
                        f"Retrying in {current_delay:.1f}s"
                    )
                    await asyncio.sleep(current_delay)
                    current_delay *= backoff

            assert last_exception is not None
            raise last_exception

        return wrapper

    return decorator


class AsyncBatcher(Generic[T]):
    """Batch async operations for improved performance."""

    def __init__(
        self,
        batch_size: int,
        flush_interval: float,
        processor: Callable[[list[T]], Awaitable[None]],
    ) -> None:
        """Initialize AsyncBatcher.

        Args:
            batch_size: Maximum batch size
            flush_interval: Maximum time to wait before processing a batch
            processor: Function to process batches
        """
        self.batch_size = batch_size
        self.flush_interval = flush_interval
        self.processor = processor
        self.items: list[T] = []
        self._flush_task: asyncio.Task[None] | None = None
        self._lock = asyncio.Lock()

    async def add(self, item: T) -> None:
        """Add item to batch.

        Args:
            item: Item to add
        """
        async with self._lock:
            self.items.append(item)
            if len(self.items) >= self.batch_size:
                await self._flush()
            elif self._flush_task is None:
                self._flush_task = asyncio.create_task(self._delayed_flush())

    async def _delayed_flush(self) -> None:
        """Flush batch after interval."""
        await asyncio.sleep(self.flush_interval)
        await self._flush()

    async def _flush(self) -> None:
        """Process current batch."""
        async with self._lock:
            if not self.items:
                return
            items = self.items
            self.items = []
            if self._flush_task is not None:
                self._flush_task.cancel()
                self._flush_task = None

        try:
            await self.processor(items)
        except Exception as e:
            logger.error(f"Error processing batch: {e}")
            self.items.extend(items)

    async def flush(self) -> None:
        """Flush remaining items."""
        if self._flush_task is not None:
            self._flush_task.cancel()
        await self._flush()

    @asynccontextmanager
    async def batch_context(self) -> AsyncGenerator[None, None]:
        """Context manager for batching operations."""
        try:
            yield
        finally:
            await self.flush()


class ThreadPoolManager:
    """Thread pool manager for CPU-bound tasks."""

    def __init__(self, max_workers: int | None = None) -> None:
        """Initialize ThreadPoolManager.

        Args:
            max_workers: Maximum number of worker threads
        """
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    @contextmanager
    def get_executor(self) -> Generator[ThreadPoolExecutor, None, None]:
        """Get thread pool executor.

        Yields:
            ThreadPoolExecutor instance
        """
        try:
            yield self.executor
        finally:
            pass

    async def run_in_thread(
        self, func: Callable[P, R], *args: P.args, **kwargs: P.kwargs
    ) -> R:
        """Run function in thread pool.

        Args:
            func: Function to run
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Function result
        """
        return await asyncio.get_event_loop().run_in_executor(
            self.executor, functools.partial(func, *args, **kwargs)
        )

    def shutdown(self, wait: bool = True) -> None:
        """Shutdown thread pool.

        Args:
            wait: Wait for pending tasks to complete
        """
        self.executor.shutdown(wait=wait)


@overload
def memoize(func: Callable[P, R]) -> Callable[P, R]:
    ...


@overload
def memoize(*, maxsize: int | None = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    ...


def memoize(
    func: Callable[P, R] | None = None, *, maxsize: int | None = None
) -> Callable[[Callable[P, R]], Callable[P, R]] | Callable[P, R]:
    """Memoize function results.

    Args:
        func: Function to memoize
        maxsize: Maximum cache size

    Returns:
        Decorated function
    """

    def decorator(fn: Callable[P, R]) -> Callable[P, R]:
        cache: dict[tuple[Any, ...], R] = {}

        @functools.wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache:
                if maxsize and len(cache) >= maxsize:
                    cache.pop(next(iter(cache)))
                cache[key] = fn(*args, **kwargs)
            return cache[key]

        return wrapper

    if func is None:
        return decorator
    return decorator(func)


def validate_json(obj: Any) -> JSON:
    """Validate and convert object to JSON format.

    Args:
        obj: Object to validate

    Returns:
        JSON-compatible object

    Raises:
        ValueError: If object cannot be converted to JSON
    """
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return cast(JSON, obj)
    if isinstance(obj, dict):
        return {str(k): validate_json(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [validate_json(item) for item in obj]
    if hasattr(obj, "to_json"):
        return validate_json(obj.to_json())
    if hasattr(obj, "__dict__"):
        return validate_json(obj.__dict__)
    raise ValueError(f"Cannot convert {type(obj)} to JSON")
