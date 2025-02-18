"""Tests for agent type definitions."""

from datetime import datetime, timedelta

from adpa.agents.types import (
    AgentConfig, AgentHealth, AgentMessage, AgentMetrics,
    AgentPriority, AgentStatus, AgentType, ResourceLimits,
    ResourceUsage, RetryConfig, SecurityConfig, TaskResult
)


def test_agent_status():
    """Test agent status enum."""
    assert AgentStatus.IDLE.value == "idle"
    assert AgentStatus.RUNNING.value == "running"
    assert AgentStatus.ERROR.value == "error"
    assert AgentStatus.TERMINATED.value == "terminated"


def test_agent_type():
    """Test agent type enum."""
    assert AgentType.PROCESSOR.value == "processor"
    assert AgentType.MONITOR.value == "monitor"
    assert AgentType.COLLECTOR.value == "collector"
    assert AgentType.ANALYZER.value == "analyzer"


def test_agent_priority():
    """Test agent priority enum."""
    assert AgentPriority.LOW.value == 0
    assert AgentPriority.MEDIUM.value == 1
    assert AgentPriority.HIGH.value == 2
    assert AgentPriority.CRITICAL.value == 3


def test_resource_limits():
    """Test resource limits dataclass."""
    limits = ResourceLimits(
        max_memory="1G",
        max_cpu=1.0,
        max_disk="2G",
        max_network="200M"
    )
    assert limits.max_memory == "1G"
    assert limits.max_cpu == 1.0
    assert limits.max_disk == "2G"
    assert limits.max_network == "200M"


def test_retry_config():
    """Test retry configuration dataclass."""
    config = RetryConfig(
        max_attempts=5,
        initial_delay=0.1,
        max_delay=30.0,
        backoff_factor=1.5
    )
    assert config.max_attempts == 5
    assert config.initial_delay == 0.1
    assert config.max_delay == 30.0
    assert config.backoff_factor == 1.5


def test_security_config():
    """Test security configuration dataclass."""
    config = SecurityConfig(
        enable_encryption=True,
        encryption_key_rotation=43200,
        allowed_hosts=["localhost"],
        allowed_ports=[8000, 8001]
    )
    assert config.enable_encryption
    assert config.encryption_key_rotation == 43200
    assert "localhost" in config.allowed_hosts
    assert 8000 in config.allowed_ports


def test_agent_config():
    """Test agent configuration dataclass."""
    config = AgentConfig(
        agent_type=AgentType.PROCESSOR,
        priority=AgentPriority.HIGH,
        resource_limits=ResourceLimits(),
        retry_config=RetryConfig(),
        metadata={"version": "1.0.0"}
    )
    assert config.agent_type == AgentType.PROCESSOR
    assert config.priority == AgentPriority.HIGH
    assert isinstance(config.resource_limits, ResourceLimits)
    assert isinstance(config.retry_config, RetryConfig)
    assert config.metadata["version"] == "1.0.0"


def test_agent_metrics():
    """Test agent metrics dataclass."""
    metrics = AgentMetrics(
        timestamp=datetime.now(),
        cpu_usage=0.5,
        memory_usage=0.3,
        disk_usage=0.2,
        network_usage=0.1
    )
    assert 0.0 <= metrics.cpu_usage <= 1.0
    assert 0.0 <= metrics.memory_usage <= 1.0
    assert 0.0 <= metrics.disk_usage <= 1.0
    assert 0.0 <= metrics.network_usage <= 1.0


def test_agent_health():
    """Test agent health dataclass."""
    health = AgentHealth(
        is_healthy=True,
        status=AgentStatus.RUNNING,
        last_heartbeat=datetime.now(),
        uptime=3600.0,
        memory_usage=0.5,
        cpu_usage=0.4,
        active_tasks=3,
        queue_size=10,
        error_count=0,
        warnings=[]
    )
    assert health.is_healthy
    assert health.status == AgentStatus.RUNNING
    assert health.active_tasks == 3
    assert health.error_count == 0


def test_task_result():
    """Test task result dataclass."""
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=1)
    result = TaskResult(
        task_id="task-123",
        success=True,
        result={"data": "processed"},
        start_time=start_time,
        end_time=end_time,
        duration=1.0,
        retries=0
    )
    assert result.task_id == "task-123"
    assert result.success
    assert result.result["data"] == "processed"
    assert result.duration == 1.0


def test_agent_message():
    """Test agent message dataclass."""
    message = AgentMessage(
        sender_id="agent-1",
        receiver_id="agent-2",
        message_type="request",
        payload={"action": "process"},
        correlation_id="corr-123",
        priority=AgentPriority.HIGH
    )
    assert message.sender_id == "agent-1"
    assert message.receiver_id == "agent-2"
    assert message.message_type == "request"
    assert message.payload["action"] == "process"
    assert message.correlation_id == "corr-123"
    assert message.priority == AgentPriority.HIGH


def test_resource_usage():
    """Test resource usage dataclass."""
    usage = ResourceUsage(
        memory=0.5,
        cpu=0.4,
        disk=0.3,
        network=0.2,
        io_read=1000.0,
        io_write=500.0,
        threads=4,
        open_files=10,
        connections=2
    )
    assert 0.0 <= usage.memory <= 1.0
    assert 0.0 <= usage.cpu <= 1.0
    assert 0.0 <= usage.disk <= 1.0
    assert 0.0 <= usage.network <= 1.0
    assert usage.threads == 4
    assert usage.open_files == 10
    assert usage.connections == 2
