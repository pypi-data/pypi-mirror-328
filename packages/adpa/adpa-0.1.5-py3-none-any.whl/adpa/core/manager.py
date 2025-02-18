"""Core manager module."""

from typing import Dict, Any

from .types import CoreConfig, ProcessingResult
from .processor import DataProcessor
from .workflow import WorkflowEngine
from .events import EventSystem
from .state import StateManager


class CoreManager:
    """Core manager class."""

    def __init__(self, config: CoreConfig):
        """Initialize core manager.
        
        Args:
            config: Core configuration
        """
        self.config = config
        self.processor = DataProcessor(config)
        self.workflow = WorkflowEngine(config)
        self.events = EventSystem(config)
        self.state = StateManager(config)

    async def process_request(self, request: Dict[str, Any]) -> ProcessingResult:
        """Process request.
        
        Args:
            request: Request to process
            
        Returns:
            Processing result
            
        Raises:
            ValueError: If request is invalid
        """
        if "type" not in request:
            raise ValueError("Request must have 'type' field")

        result = await self.processor.process(request)
        
        if result.success:
            await self.events.emit("processing_complete", result.data)
            await self.state.update_state({"last_request": request["type"]})
        
        return result
