"""
Message routing and coordination for ADPA agents.
"""
from typing import Dict, List, Optional, Set
import asyncio
import logging
from datetime import datetime

from adpa.agents.base import BaseAgent
from adpa.agents.types import (
    AgentConfig, AgentMessage, AgentType,
    AgentPriority, TaskResult
)

logger = logging.getLogger(__name__)

class MessageRouter:
    """Route messages between agents."""
    
    def __init__(self):
        """Initialize message router."""
        self._routes: Dict[str, Set[str]] = {}
        self._subscriptions: Dict[str, Set[str]] = {}
        self._message_history: List[Dict] = []
        self._max_history = 1000
    
    def add_route(
        self,
        source_id: str,
        target_id: str,
        bidirectional: bool = False
    ) -> None:
        """Add a route between agents.
        
        Args:
            source_id: Source agent ID
            target_id: Target agent ID
            bidirectional: If True, add route in both directions
        """
        if source_id not in self._routes:
            self._routes[source_id] = set()
        self._routes[source_id].add(target_id)
        
        if bidirectional:
            if target_id not in self._routes:
                self._routes[target_id] = set()
            self._routes[target_id].add(source_id)
    
    def remove_route(
        self,
        source_id: str,
        target_id: str,
        bidirectional: bool = False
    ) -> None:
        """Remove a route between agents.
        
        Args:
            source_id: Source agent ID
            target_id: Target agent ID
            bidirectional: If True, remove route in both directions
        """
        if source_id in self._routes:
            self._routes[source_id].discard(target_id)
        
        if bidirectional and target_id in self._routes:
            self._routes[target_id].discard(source_id)
    
    def subscribe(
        self,
        agent_id: str,
        message_type: str
    ) -> None:
        """Subscribe an agent to a message type.
        
        Args:
            agent_id: Agent ID
            message_type: Message type to subscribe to
        """
        if message_type not in self._subscriptions:
            self._subscriptions[message_type] = set()
        self._subscriptions[message_type].add(agent_id)
    
    def unsubscribe(
        self,
        agent_id: str,
        message_type: str
    ) -> None:
        """Unsubscribe an agent from a message type.
        
        Args:
            agent_id: Agent ID
            message_type: Message type to unsubscribe from
        """
        if message_type in self._subscriptions:
            self._subscriptions[message_type].discard(agent_id)
    
    async def route_message(
        self,
        message: AgentMessage,
        agents: Dict[str, BaseAgent]
    ) -> None:
        """Route a message to appropriate agents.
        
        Args:
            message: Message to route
            agents: Dictionary of available agents
        """
        targets = set()
        
        # Check direct routes
        if message.sender_id in self._routes:
            targets.update(self._routes[message.sender_id])
        
        # Check subscriptions
        if message.message_type in self._subscriptions:
            targets.update(self._subscriptions[message.message_type])
        
        # Remove sender from targets
        targets.discard(message.sender_id)
        
        # Store in history
        self._message_history.append({
            "timestamp": datetime.now().isoformat(),
            "message": message.dict(),
            "targets": list(targets)
        })
        
        # Limit history size
        if len(self._message_history) > self._max_history:
            self._message_history.pop(0)
        
        # Send to all targets
        for target_id in targets:
            if target_id in agents:
                try:
                    await agents[target_id].send_message(message)
                except Exception as e:
                    logger.error(
                        f"Error routing message to {target_id}: {e}"
                    )
    
    def get_routes(self, agent_id: str) -> Set[str]:
        """Get all routes for an agent.
        
        Args:
            agent_id: Agent ID
            
        Returns:
            Set of target agent IDs
        """
        return self._routes.get(agent_id, set())
    
    def get_subscriptions(self, message_type: str) -> Set[str]:
        """Get all subscribers for a message type.
        
        Args:
            message_type: Message type
            
        Returns:
            Set of subscribed agent IDs
        """
        return self._subscriptions.get(message_type, set())
    
    def get_history(
        self,
        limit: Optional[int] = None,
        agent_id: Optional[str] = None,
        message_type: Optional[str] = None
    ) -> List[Dict]:
        """Get message routing history.
        
        Args:
            limit: Maximum number of entries to return
            agent_id: Filter by agent ID
            message_type: Filter by message type
            
        Returns:
            List of message history entries
        """
        history = self._message_history
        
        if agent_id:
            history = [
                h for h in history
                if (h["message"]["sender_id"] == agent_id or
                    agent_id in h["targets"])
            ]
        
        if message_type:
            history = [
                h for h in history
                if h["message"]["message_type"] == message_type
            ]
        
        if limit:
            history = history[-limit:]
        
        return history
