"""Core models for ADPA framework."""
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from typing_extensions import override

from .types import (
    JSON,
    AgentConfig,
    DBConfig,
    LLMConfig,
    MetricsConfig,
    SecurityConfig,
    SQLConfig,
)


@dataclass(frozen=True, slots=True)
class CoreConfig:
    """Core configuration for ADPA framework."""

    max_threads: int = field(default=10)
    queue_size: int = field(default=1000)
    batch_size: int = field(default=100)
    timeout: int = field(default=30)

    def __post_init__(self) -> None:
        """Validate configuration values."""
        if self.max_threads <= 0:
            raise ValueError("max_threads must be positive")
        if self.queue_size <= 0:
            raise ValueError("queue_size must be positive")
        if self.batch_size <= 0:
            raise ValueError("batch_size must be positive")
        if self.timeout <= 0:
            raise ValueError("timeout must be positive")


@dataclass(frozen=True, slots=True)
class ProcessingResult:
    """Result of processing operation."""

    success: bool
    data: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None

    @override
    def __str__(self) -> str:
        """Return string representation."""
        if self.success:
            return f"Success: {self.data}"
        return f"Error: {self.error}"


@dataclass(frozen=True, slots=True)
class WorkflowStep:
    """Workflow step definition."""

    name: str
    action: str
    dependencies: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate step configuration."""
        if not self.name:
            raise ValueError("name cannot be empty")
        if not self.action:
            raise ValueError("action cannot be empty")


@dataclass(frozen=True, slots=True)
class Workflow:
    """Workflow definition."""

    steps: List[WorkflowStep]

    def __post_init__(self) -> None:
        """Validate workflow configuration."""
        if not self.steps:
            raise ValueError("workflow must have at least one step")
        self._validate_dependencies()

    def _validate_dependencies(self) -> None:
        """Validate step dependencies."""
        step_names = {step.name for step in self.steps}
        for step in self.steps:
            for dep in step.dependencies:
                if dep not in step_names:
                    raise ValueError(f"Unknown dependency {dep} in step {step.name}")


@dataclass(frozen=True, slots=True)
class Event:
    """Event definition."""

    type: str
    data: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate event configuration."""
        if not self.type:
            raise ValueError("type cannot be empty")


@dataclass(frozen=True, slots=True)
class AppConfig:
    """Application configuration."""

    core: CoreConfig
    llm: LLMConfig
    database: DBConfig
    agent: AgentConfig
    sql: SQLConfig
    security: SecurityConfig
    metrics: MetricsConfig

    def to_json(self) -> JSON:
        """Convert configuration to JSON format."""
        return {
            "core": {
                "max_threads": self.core.max_threads,
                "queue_size": self.core.queue_size,
                "batch_size": self.core.batch_size,
                "timeout": self.core.timeout,
            },
            "llm": dict(self.llm),
            "database": dict(self.database),
            "agent": dict(self.agent),
            "sql": dict(self.sql),
            "security": dict(self.security),
            "metrics": dict(self.metrics),
        }

    @classmethod
    def from_json(cls, data: JSON) -> "AppConfig":
        """Create configuration from JSON format."""
        if not isinstance(data, dict):
            raise ValueError("Invalid JSON format")

        return cls(
            core=CoreConfig(**data.get("core", {})),
            llm=LLMConfig(**data.get("llm", {})),
            database=DBConfig(**data.get("database", {})),
            agent=AgentConfig(**data.get("agent", {})),
            sql=SQLConfig(**data.get("sql", {})),
            security=SecurityConfig(**data.get("security", {})),
            metrics=MetricsConfig(**data.get("metrics", {})),
        )
