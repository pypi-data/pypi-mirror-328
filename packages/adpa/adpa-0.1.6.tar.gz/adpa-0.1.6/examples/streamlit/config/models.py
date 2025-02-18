"""Configuration models for Streamlit application."""
import os
from enum import Enum
from typing import Dict, List, Optional, Union

import yaml
from pydantic import BaseModel, BaseSettings, Field, HttpUrl


class Environment(str, Enum):
    """Runtime environment."""

    DEV = "Development"
    STAGING = "Staging"
    PROD = "Production"


class LogLevel(str, Enum):
    """Logging level."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class AuthMethod(str, Enum):
    """Authentication method."""

    JWT = "JWT"
    OAUTH2 = "OAuth2"
    API_KEY = "API Key"


class VectorStore(str, Enum):
    """Vector store provider."""

    CHROMA = "Chroma"
    FAISS = "FAISS"
    PINECONE = "Pinecone"
    WEAVIATE = "Weaviate"


class DocumentStore(str, Enum):
    """Storage provider."""

    LOCAL = "Local"
    S3 = "S3"
    GCS = "GCS"


class CoreSettings(BaseModel):
    """Core settings."""

    environment: Environment = Field(default=Environment.DEV, description="Runtime environment")
    max_concurrent_ops: int = Field(
        default=100, ge=1, le=1000, description="Maximum concurrent operations"
    )
    log_level: LogLevel = Field(default=LogLevel.INFO, description="Logging level")
    debug_mode: bool = Field(default=False, description="Enable debug mode")
    perf_monitoring: bool = Field(default=True, description="Enable performance monitoring")
    auto_scaling: bool = Field(default=True, description="Enable auto-scaling")


class SecuritySettings(BaseModel):
    """Security settings."""

    admin_username: str = Field(..., min_length=3, description="Admin username")
    admin_password: str = Field(..., min_length=8, description="Admin password")
    auth_method: AuthMethod = Field(default=AuthMethod.JWT, description="Authentication method")
    session_timeout: int = Field(
        default=60, ge=5, le=1440, description="Session timeout in minutes"
    )
    enable_2fa: bool = Field(default=False, description="Enable two-factor authentication")
    ip_whitelist: bool = Field(default=False, description="Enable IP whitelisting")


class CircuitBreaker(BaseModel):
    """Circuit breaker configuration."""

    enabled: bool = Field(default=True, description="Enable circuit breaker")
    failure_threshold: int = Field(
        default=5, ge=1, le=100, description="Number of failures before breaking"
    )
    recovery_timeout: int = Field(
        default=60, ge=1, le=3600, description="Recovery timeout in seconds"
    )


class RetryPolicy(BaseModel):
    """Retry policy configuration."""

    max_retries: int = Field(default=3, ge=0, le=10, description="Maximum retry attempts")
    backoff_factor: float = Field(
        default=1.5, ge=1.0, le=10.0, description="Exponential backoff factor"
    )
    retry_delay: int = Field(default=1, ge=1, le=60, description="Initial retry delay in seconds")


class FailoverConfig(BaseModel):
    """Failover configuration."""

    enabled: bool = Field(default=True, description="Enable failover")
    backup_providers: List[str] = Field(default=[], description="List of backup providers")
    failover_timeout: int = Field(
        default=30, ge=1, le=300, description="Failover timeout in seconds"
    )


class LLMProvider(BaseModel):
    """LLM provider configuration."""

    name: str = Field(..., description="Provider name")
    api_key: str = Field(..., description="API key")
    base_url: HttpUrl = Field(..., description="Base API URL")
    organization_id: Optional[str] = Field(None, description="Organization ID")
    circuit_breaker: CircuitBreaker = Field(default_factory=CircuitBreaker)
    retry_policy: RetryPolicy = Field(default_factory=RetryPolicy)
    failover: FailoverConfig = Field(default_factory=FailoverConfig)


class VectorStoreConfig(BaseModel):
    """Vector store configuration."""

    provider: VectorStore = Field(..., description="Vector store provider")
    connection_string: str = Field(..., description="Connection string")
    api_key: Optional[str] = Field(None, description="API key if required")
    dimension: int = Field(default=1536, ge=1, le=4096, description="Vector dimension")
    index_shards: int = Field(default=1, ge=1, le=10, description="Number of index shards")
    distance_metric: str = Field(default="cosine", description="Distance metric")


class StorageConfig(BaseModel):
    """Storage configuration."""

    provider: DocumentStore = Field(..., description="Storage provider")
    bucket_name: Optional[str] = Field(None, description="Bucket name for cloud storage")
    access_key: Optional[str] = Field(None, description="Access key")
    secret_key: Optional[str] = Field(None, description="Secret key")
    region: Optional[str] = Field(None, description="Region")


class AgentConfig(BaseModel):
    """Agent configuration."""

    name: str = Field(..., description="Agent name")
    type: str = Field(
        ..., description="Agent type", examples=["research", "development", "analytics", "testing"]
    )
    team: str = Field(
        ...,
        description="Team assignment",
        examples=["Research Team", "Engineering Team", "Data Science Team"],
    )
    description: str = Field(..., description="Agent description")
    tools: List[str] = Field(
        default_factory=list,
        description="Available tools",
        examples=[
            "web_search",
            "document_analysis",
            "summarization",
            "code_analysis",
            "code_generation",
            "code_review",
            "data_analysis",
            "visualization",
            "statistics",
            "test_generation",
            "test_execution",
            "bug_reporting",
            "doc_generation",
            "markdown_editing",
            "api_docs",
            "infrastructure_management",
            "deployment",
            "monitoring",
            "security_scan",
            "vulnerability_assessment",
            "threat_analysis",
            "task_management",
            "resource_planning",
            "reporting",
        ],
    )
    llm_config: Dict[str, str] = Field(
        default_factory=lambda: {"primary_provider": "OpenAI", "model": "gpt-4"},
        description="LLM configuration",
    )
    max_concurrent_tasks: int = Field(
        default=5, ge=1, le=100, description="Maximum concurrent tasks"
    )
    timeout: int = Field(default=300, ge=1, le=3600, description="Task timeout in seconds")

    class Config:
        """Pydantic model configuration."""

        title = "Agent Configuration"
        json_schema_extra = {
            "example": {
                "name": "Research Assistant",
                "type": "research",
                "team": "Research Team",
                "description": "Specialized in research and analysis tasks",
                "tools": ["web_search", "document_analysis", "summarization"],
                "llm_config": {"primary_provider": "OpenAI", "model": "gpt-4"},
                "max_concurrent_tasks": 5,
                "timeout": 300,
            }
        }


class TeamConfig(BaseModel):
    """Team configuration."""

    name: str = Field(..., description="Team name")
    description: Optional[str] = Field(None, description="Team description")
    members: List[str] = Field(default=[], description="Team members")
    agents: List[str] = Field(default=[], description="Assigned agents")
    tools: List[str] = Field(default=[], description="Available tools")
    max_tasks: int = Field(default=20, ge=1, le=100, description="Maximum concurrent tasks")
    task_timeout: int = Field(default=15, ge=1, le=60, description="Task timeout in minutes")


class SystemConfig(BaseSettings):
    """System-wide configuration."""

    core: CoreSettings = Field(default_factory=CoreSettings)
    security: SecuritySettings
    llm_providers: Dict[str, LLMProvider] = Field(default_factory=dict)
    vector_store: VectorStoreConfig
    storage: StorageConfig
    agents: Dict[str, AgentConfig] = Field(default_factory=dict)
    teams: Dict[str, TeamConfig] = Field(default_factory=dict)

    def save_to_yaml(self, path: str) -> None:
        """Save configuration to YAML file."""
        with open(path, "w") as f:
            yaml.dump(self.dict(), f)

    @classmethod
    def load_from_yaml(cls, path: str) -> "SystemConfig":
        """Load configuration from YAML file."""
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)
