"""Type definitions for the agents module."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union


class AgentStatus(Enum):
    """Status of an agent."""
    IDLE = "idle"
    RUNNING = "running"
    ERROR = "error"
    TERMINATED = "terminated"
    PAUSED = "paused"
    STARTING = "starting"
    STOPPING = "stopping"
    RESTARTING = "restarting"


class AgentType(Enum):
    """Types of agents available."""
    PROCESSOR = "processor"  # Data processing agent
    MONITOR = "monitor"      # System monitoring agent
    COLLECTOR = "collector"  # Data collection agent
    ANALYZER = "analyzer"    # Data analysis agent
    EXECUTOR = "executor"    # Task execution agent
    COORDINATOR = "coordinator"  # Multi-agent coordinator


class AgentPriority(Enum):
    """Priority levels for agent tasks."""
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3


@dataclass(frozen=True)
class ResourceLimits:
    """Resource limits for an agent."""
    max_memory: str = "512M"
    max_cpu: float = 0.5  # 50% of one CPU core
    max_disk: str = "1G"
    max_network: str = "100M"  # 100 MB/s
    max_tasks: int = 10
    max_threads: int = 4


@dataclass(frozen=True)
class RetryConfig:
    """Configuration for retry behavior."""
    max_attempts: int = 3
    initial_delay: float = 1.0  # seconds
    max_delay: float = 60.0  # seconds
    backoff_factor: float = 2.0
    jitter: bool = True


@dataclass(frozen=True)
class MonitoringConfig:
    """Configuration for agent monitoring."""
    heartbeat_interval: int = 5  # seconds
    health_check_interval: int = 30  # seconds
    metrics_interval: int = 60  # seconds
    log_level: str = "INFO"
    alert_threshold: Dict[str, float] = field(default_factory=lambda: {
        "cpu": 0.8,
        "memory": 0.8,
        "disk": 0.8,
        "error_rate": 0.1
    })


@dataclass(frozen=True)
class SecurityConfig:
    """Security configuration for agents."""
    enable_encryption: bool = True
    encryption_key_rotation: int = 86400  # 24 hours
    allowed_hosts: List[str] = field(default_factory=list)
    allowed_ports: List[int] = field(default_factory=list)
    require_authentication: bool = True
    token_expiry: int = 3600  # 1 hour


@dataclass(frozen=True)
class AgentConfig:
    """Configuration for an agent."""
    agent_type: AgentType
    priority: AgentPriority = AgentPriority.MEDIUM
    resource_limits: ResourceLimits = field(default_factory=ResourceLimits)
    retry_config: RetryConfig = field(default_factory=RetryConfig)
    monitoring_config: MonitoringConfig = field(default_factory=MonitoringConfig)
    security_config: SecurityConfig = field(default_factory=SecurityConfig)
    metadata: Dict[str, str] = field(default_factory=dict)


@dataclass
class AgentMetrics:
    """Metrics collected from an agent."""
    timestamp: datetime
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_usage: float
    active_tasks: int
    completed_tasks: int
    failed_tasks: int
    avg_response_time: float
    error_rate: float


@dataclass
class AgentHealth:
    """Health status of an agent."""
    is_healthy: bool
    status: AgentStatus
    last_heartbeat: datetime
    uptime: float  # seconds
    memory_usage: float
    cpu_usage: float
    active_tasks: int
    queue_size: int
    error_count: int
    warnings: List[str]
    metrics: AgentMetrics


@dataclass
class TaskResult:
    """Result of a task execution."""
    task_id: str
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    duration: Optional[float] = None
    retries: int = 0


@dataclass
class AgentMessage:
    """Message exchanged between agents."""
    sender_id: str
    receiver_id: str
    message_type: str
    payload: Dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.now)
    correlation_id: Optional[str] = None
    priority: AgentPriority = AgentPriority.MEDIUM
    ttl: Optional[int] = None  # Time-to-live in seconds


@dataclass
class ResourceUsage:
    """Resource usage statistics for an agent."""
    timestamp: datetime = field(default_factory=datetime.now)
    memory: float = 0.0  # Percentage
    cpu: float = 0.0     # Percentage
    disk: float = 0.0    # Percentage
    network: float = 0.0 # MB/s
    io_read: float = 0.0 # MB/s
    io_write: float = 0.0 # MB/s
    threads: int = 0
    open_files: int = 0
    connections: int = 0
