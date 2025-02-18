"""
Core settings for ADPA framework.
"""
from pathlib import Path
from typing import Dict, Any, Optional, List, Union
import json
import os
from datetime import timedelta

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, validator

class ADPASettings(BaseSettings):
    """Core settings for ADPA framework."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        env_prefix="ADPA_",
        extra="allow"  # Allow extra fields from environment variables
    )
    
    # Base paths
    BASE_DIR: Path = Field(
        default=Path(__file__).parent.parent.parent.parent,
        description="Base directory path"
    )
    CONFIG_DIR: Path = Field(
        default=Path(__file__).parent,
        description="Configuration directory path"
    )
    DATA_DIR: Path = Field(
        default=Path(__file__).parent.parent.parent / "data",
        description="Data directory path"
    )
    
    # LLM Settings
    DEFAULT_LLM_PROVIDER: str = Field(
        default="openai",
        description="Default LLM provider"
    )
    LLM_CONFIG_PATH: Path = Field(
        default=Path(__file__).parent / "llm_config.json",
        description="LLM configuration file path"
    )
    LLM_CACHE_SIZE: int = Field(
        default=1000,
        description="LLM response cache size"
    )
    LLM_TIMEOUT: int = Field(
        default=30,
        description="LLM request timeout in seconds"
    )
    
    # Database Settings
    DATABASE_URL: str = Field(
        default="postgresql://localhost:5432/adpa",
        description="Database connection URL"
    )
    DATABASE_POOL_SIZE: int = Field(
        default=5,
        description="Database connection pool size"
    )
    DATABASE_MAX_OVERFLOW: int = Field(
        default=10,
        description="Maximum database connection overflow"
    )
    DATABASE_POOL_TIMEOUT: int = Field(
        default=30,
        description="Database pool timeout in seconds"
    )
    
    # Logging Settings
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Logging level"
    )
    LOG_FORMAT: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Log message format"
    )
    LOG_FILE: Optional[Path] = Field(
        default=None,
        description="Log file path"
    )
    LOG_ROTATION: str = Field(
        default="1 day",
        description="Log rotation interval"
    )
    LOG_RETENTION: str = Field(
        default="30 days",
        description="Log retention period"
    )
    
    # Agent Settings
    MAX_AGENTS_PER_TEAM: int = Field(
        default=5,
        description="Maximum agents per team"
    )
    DEFAULT_AGENT_TIMEOUT: int = Field(
        default=30,
        description="Default agent timeout in seconds"
    )
    AGENT_RETRY_ATTEMPTS: int = Field(
        default=3,
        description="Agent retry attempts"
    )
    AGENT_RETRY_DELAY: int = Field(
        default=5,
        description="Agent retry delay in seconds"
    )
    
    # Team Settings
    DEFAULT_TEAM_SIZE: int = Field(
        default=3,
        description="Default team size"
    )
    TEAM_COORDINATION_TIMEOUT: int = Field(
        default=60,
        description="Team coordination timeout in seconds"
    )
    
    # Cache Settings
    CACHE_TYPE: str = Field(
        default="redis",
        description="Cache backend type"
    )
    CACHE_URL: str = Field(
        default="redis://localhost:6379/0",
        description="Cache backend URL"
    )
    CACHE_TTL: int = Field(
        default=3600,
        description="Cache TTL in seconds"
    )
    
    # API Settings
    API_HOST: str = Field(
        default="0.0.0.0",
        description="API host"
    )
    API_PORT: int = Field(
        default=8000,
        description="API port"
    )
    API_DEBUG: bool = Field(
        default=False,
        description="Enable API debug mode"
    )
    API_CORS_ORIGINS: List[str] = Field(
        default=["*"],
        description="Allowed CORS origins"
    )
    API_RATE_LIMIT: int = Field(
        default=100,
        description="API rate limit per minute"
    )
    
    @validator("LOG_LEVEL")
    def validate_log_level(cls, v: str) -> str:
        """Validate logging level."""
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if v.upper() not in valid_levels:
            raise ValueError(f"Invalid log level. Must be one of {valid_levels}")
        return v.upper()
    
    @validator("DATABASE_URL")
    def validate_database_url(cls, v: str) -> str:
        """Validate database URL."""
        supported_dialects = {"postgresql", "mysql", "sqlite"}
        dialect = v.split("://")[0]
        if dialect not in supported_dialects:
            raise ValueError(f"Unsupported database dialect. Must be one of {supported_dialects}")
        return v
    
    def get_log_config(self) -> Dict[str, Any]:
        """Get logging configuration dictionary."""
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": self.LOG_FORMAT
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout"
                },
                **({"file": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "formatter": "default",
                    "filename": str(self.LOG_FILE),
                    "when": self.LOG_ROTATION,
                    "backupCount": int(timedelta(days=30) / self._parse_time(self.LOG_ROTATION))
                }} if self.LOG_FILE else {})
            },
            "root": {
                "level": self.LOG_LEVEL,
                "handlers": ["console"] + (["file"] if self.LOG_FILE else [])
            }
        }
    
    def _parse_time(self, time_str: str) -> timedelta:
        """Parse time string into timedelta."""
        value, unit = time_str.split()
        value = int(value)
        unit = unit.lower()
        if unit in {"day", "days"}:
            return timedelta(days=value)
        elif unit in {"hour", "hours"}:
            return timedelta(hours=value)
        elif unit in {"minute", "minutes"}:
            return timedelta(minutes=value)
        elif unit in {"second", "seconds"}:
            return timedelta(seconds=value)
        raise ValueError(f"Invalid time unit: {unit}")

# Create settings instance
settings = ADPASettings()
