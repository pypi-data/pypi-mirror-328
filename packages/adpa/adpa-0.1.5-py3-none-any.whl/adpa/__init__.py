"""
Advanced Data Processing and Analytics (ADPA) Framework.

A comprehensive framework for data processing, analytics, and AI-driven insights.
"""

import os
from pathlib import Path
from typing import Final

# Version
with open(os.path.join(os.path.dirname(__file__), "VERSION")) as f:
    __version__: Final[str] = f.read().strip().split("\n")[1]

# Core exports
from .core import (
    ADPAError,
    CoreManager,
    CoreConfig,
    ProcessingResult,
    WorkflowStep,
    Workflow,
    Event,
    AppConfig,
    DataProcessor,
)

# Type exports
from .core.types import (
    JSON,
    PathLike,
    Callback,
    ModelName,
    ProviderName,
    LLMConfig,
    DBConfig,
    AgentConfig,
    SQLConfig,
    SecurityConfig,
    MetricsConfig,
)

# Agent exports
from .agents import (
    BaseAgent,
    AgentManager,
    AgentConfig,
    AgentState,
)

# Text2SQL exports
from .text2sql import (
    Text2SQLGenerator,
    SchemaLearner,
    QueryContext,
    QueryHistory,
    QueryValidator,
)

# Database exports
from .database import (
    DatabaseManager,
    Connection,
    Transaction,
    QueryResult,
)

# Security exports
from .security import (
    SecurityManager,
    Sanitizer,
    Validator,
    AccessControl,
)

# Monitoring exports
from .monitoring import (
    MetricsCollector,
    Logger,
    Tracer,
)

__all__ = [
    # Version
    "__version__",
    
    # Core
    "ADPAError",
    "CoreManager",
    "CoreConfig",
    "ProcessingResult",
    "WorkflowStep",
    "Workflow",
    "Event",
    "AppConfig",
    "DataProcessor",
    
    # Types
    "JSON",
    "PathLike",
    "Callback",
    "ModelName",
    "ProviderName",
    "LLMConfig",
    "DBConfig",
    "AgentConfig",
    "SQLConfig",
    "SecurityConfig",
    "MetricsConfig",
    
    # Agents
    "BaseAgent",
    "AgentManager",
    "AgentConfig",
    "AgentState",
    
    # Text2SQL
    "Text2SQLGenerator",
    "SchemaLearner",
    "QueryContext",
    "QueryHistory",
    "QueryValidator",
    
    # Database
    "DatabaseManager",
    "Connection",
    "Transaction",
    "QueryResult",
    
    # Security
    "SecurityManager",
    "Sanitizer",
    "Validator",
    "AccessControl",
    
    # Monitoring
    "MetricsCollector",
    "Logger",
    "Tracer",
]