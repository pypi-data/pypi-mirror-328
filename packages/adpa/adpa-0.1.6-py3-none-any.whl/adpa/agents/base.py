"""
Base agent implementation for ADPA framework.
"""
from typing import Dict, List, Optional, Any
from datetime import datetime
import asyncio
import logging
from uuid import UUID, uuid4

from adpa.agents.types import (
    AgentConfig, AgentMessage, AgentMetrics,
    AgentPriority, AgentStatus, AgentType,
    MonitoringConfig, ResourceLimits, SecurityConfig
)

logger = logging.getLogger(__name__)

class BaseAgent:
    """Base class for all agents in the system."""
    
    def __init__(
        self,
        agent_id: Optional[str] = None,
        config: Optional[AgentConfig] = None
    ):
        """Initialize base agent.
        
        Args:
            agent_id: Unique agent identifier
            config: Agent configuration
        """
        self.agent_id = agent_id or str(uuid4())
        self.config = config or AgentConfig()
        self.status = AgentStatus.INITIALIZED
        self.metrics = AgentMetrics()
        self._message_queue: asyncio.Queue = asyncio.Queue()
        self._last_heartbeat = datetime.now()
        self._tasks: List[asyncio.Task] = []
    
    async def start(self) -> None:
        """Start the agent."""
        if self.status != AgentStatus.INITIALIZED:
            raise RuntimeError(f"Cannot start agent in {self.status} state")
        
        try:
            # Initialize components
            await self._initialize()
            
            # Start background tasks
            self._tasks.extend([
                asyncio.create_task(self._process_messages()),
                asyncio.create_task(self._monitor_health()),
                asyncio.create_task(self._collect_metrics())
            ])
            
            self.status = AgentStatus.RUNNING
            logger.info(f"Agent {self.agent_id} started")
            
        except Exception as e:
            self.status = AgentStatus.ERROR
            logger.error(f"Failed to start agent {self.agent_id}: {e}")
            raise
    
    async def stop(self) -> None:
        """Stop the agent."""
        if self.status not in [AgentStatus.RUNNING, AgentStatus.ERROR]:
            return
        
        try:
            # Cancel background tasks
            for task in self._tasks:
                task.cancel()
            
            # Wait for tasks to complete
            await asyncio.gather(*self._tasks, return_exceptions=True)
            
            # Cleanup
            await self._cleanup()
            
            self.status = AgentStatus.STOPPED
            logger.info(f"Agent {self.agent_id} stopped")
            
        except Exception as e:
            self.status = AgentStatus.ERROR
            logger.error(f"Error stopping agent {self.agent_id}: {e}")
            raise
    
    async def send_message(self, message: AgentMessage) -> None:
        """Send a message to the agent.
        
        Args:
            message: Message to send
        """
        await self._message_queue.put(message)
    
    async def get_metrics(self) -> AgentMetrics:
        """Get current agent metrics.
        
        Returns:
            Current agent metrics
        """
        return self.metrics
    
    async def check_health(self) -> bool:
        """Check if agent is healthy.
        
        Returns:
            True if agent is healthy
        """
        # Check heartbeat
        if (datetime.now() - self._last_heartbeat).total_seconds() > \
           self.config.monitoring_config.heartbeat_interval:
            return False
        
        # Check resource usage
        if not await self._check_resource_usage():
            return False
        
        return self.status == AgentStatus.RUNNING
    
    async def _initialize(self) -> None:
        """Initialize agent components."""
        pass
    
    async def _cleanup(self) -> None:
        """Cleanup agent resources."""
        pass
    
    async def _process_messages(self) -> None:
        """Process incoming messages."""
        while True:
            try:
                message = await self._message_queue.get()
                await self._handle_message(message)
                self._message_queue.task_done()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error processing message: {e}")
    
    async def _handle_message(self, message: AgentMessage) -> None:
        """Handle a single message.
        
        Args:
            message: Message to handle
        """
        raise NotImplementedError
    
    async def _monitor_health(self) -> None:
        """Monitor agent health."""
        while True:
            try:
                await asyncio.sleep(
                    self.config.monitoring_config.health_check_interval
                )
                self._last_heartbeat = datetime.now()
                
                # Check resource usage
                if not await self._check_resource_usage():
                    logger.warning(
                        f"Agent {self.agent_id} exceeded resource limits"
                    )
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Health monitoring error: {e}")
    
    async def _collect_metrics(self) -> None:
        """Collect agent metrics."""
        while True:
            try:
                await asyncio.sleep(
                    self.config.monitoring_config.metrics_interval
                )
                
                # Update metrics
                self.metrics.last_update = datetime.now()
                self.metrics.message_count = self._message_queue.qsize()
                self.metrics.status = self.status
                
                # Get resource usage
                usage = await self._get_resource_usage()
                self.metrics.cpu_usage = usage.get("cpu", 0.0)
                self.metrics.memory_usage = usage.get("memory", 0.0)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Metrics collection error: {e}")
    
    async def _check_resource_usage(self) -> bool:
        """Check if resource usage is within limits.
        
        Returns:
            True if resource usage is within limits
        """
        usage = await self._get_resource_usage()
        limits = self.config.resource_limits
        
        return (
            usage.get("cpu", 0.0) <= limits.max_cpu and
            usage.get("memory", 0.0) <= limits.max_memory
        )
    
    async def _get_resource_usage(self) -> Dict[str, float]:
        """Get current resource usage.
        
        Returns:
            Dictionary with resource usage metrics
        """
        # Implement resource monitoring
        return {"cpu": 0.0, "memory": 0.0}
