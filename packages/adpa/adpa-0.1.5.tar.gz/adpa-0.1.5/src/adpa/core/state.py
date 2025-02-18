"""State manager module."""

from typing import Dict, Any

from .types import CoreConfig


class StateManager:
    """State manager class."""

    def __init__(self, config: CoreConfig):
        """Initialize state manager.
        
        Args:
            config: Core configuration
        """
        self.config = config
        self._state: Dict[str, Any] = {}

    async def get_state(self) -> Dict[str, Any]:
        """Get current state.
        
        Returns:
            Current state
        """
        return self._state.copy()

    async def update_state(self, update: Dict[str, Any]) -> None:
        """Update state.
        
        Args:
            update: State update
        """
        self._state.update(update)
