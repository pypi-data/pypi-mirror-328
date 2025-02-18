"""
ADPA Agents Module.

This module provides a framework for creating and managing autonomous agents.
"""

from adpa.agents.base import BaseAgent
from adpa.agents.manager import AgentManager
from adpa.agents.moderator import AgentModerator
from adpa.agents.router import MessageRouter
from adpa.agents.specialized import (
    AnalystAgent, ResearchAgent,
    TechnicalAgent, SupportAgent
)
from adpa.agents.types import (
    AgentConfig, AgentMessage, AgentMetrics,
    AgentPriority, AgentStatus, AgentType,
    MonitoringConfig, ResourceLimits, SecurityConfig,
    TaskResult
)

__all__ = [
    # Base classes
    "BaseAgent",
    "AgentManager",
    "AgentModerator",
    "MessageRouter",
    
    # Specialized agents
    "AnalystAgent",
    "ResearchAgent",
    "TechnicalAgent",
    "SupportAgent",
    
    # Types and configs
    "AgentConfig",
    "AgentMessage",
    "AgentMetrics",
    "AgentPriority",
    "AgentStatus",
    "AgentType",
    "MonitoringConfig",
    "ResourceLimits",
    "SecurityConfig",
    "TaskResult"
]
