"""Event system module."""

from typing import Dict, Any, Callable, List, Awaitable

from .types import CoreConfig, Event


class EventSystem:
    """Event system class."""

    def __init__(self, config: CoreConfig):
        """Initialize event system.
        
        Args:
            config: Core configuration
        """
        self.config = config
        self._handlers: Dict[str, List[Callable[[Event], Awaitable[None]]]] = {}

    def register_handler(self, event_type: str, handler: Callable[[Event], Awaitable[None]]) -> None:
        """Register event handler.
        
        Args:
            event_type: Event type
            handler: Event handler
        """
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    async def emit(self, event_type: str, data: Dict[str, Any]) -> None:
        """Emit event.
        
        Args:
            event_type: Event type
            data: Event data
        """
        event = Event(type=event_type, data=data)
        
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                await handler(event)
