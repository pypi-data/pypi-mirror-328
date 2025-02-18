"""Database configuration."""
from __future__ import annotations

import os
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class DatabaseConfig(BaseModel):
    """Database configuration."""

    host: str = Field(default="localhost", description="Database host")
    port: int = Field(default=5432, description="Database port")
    database: str = Field(description="Database name")
    user: str = Field(description="Database user")
    password: str = Field(description="Database password")
    schema: str = Field(default="public", description="Database schema")
    pool_size: int = Field(default=5, description="Connection pool size")
    max_overflow: int = Field(default=10, description="Maximum number of connections")
    pool_timeout: int = Field(default=30, description="Pool timeout in seconds")
    pool_recycle: int = Field(default=1800, description="Pool recycle time in seconds")
    echo: bool = Field(default=False, description="Echo SQL statements")
    driver: str = Field(default="postgresql", description="Database driver")

    @classmethod
    def from_env(cls) -> DatabaseConfig:
        """Create database configuration from environment variables.

        Returns:
            Database configuration
        """
        return cls(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=int(os.getenv("POSTGRES_PORT", "5432")),
            database=os.getenv("POSTGRES_DATABASE", ""),
            user=os.getenv("POSTGRES_USER", ""),
            password=os.getenv("POSTGRES_PASSWORD", ""),
            schema=os.getenv("POSTGRES_SCHEMA", "public"),
            pool_size=int(os.getenv("POSTGRES_POOL_SIZE", "5")),
            max_overflow=int(os.getenv("POSTGRES_MAX_OVERFLOW", "10")),
            pool_timeout=int(os.getenv("POSTGRES_POOL_TIMEOUT", "30")),
            pool_recycle=int(os.getenv("POSTGRES_POOL_RECYCLE", "1800")),
            echo=bool(os.getenv("POSTGRES_ECHO", False)),
            driver=os.getenv("POSTGRES_DRIVER", "postgresql"),
        )

    def get_url(self) -> str:
        """Get database URL.

        Returns:
            Database URL
        """
        if self.driver == "sqlite":
            return f"sqlite:///{self.database}?check_same_thread=False"

        return (
            f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}"
            f"/{self.database}"
        )

    def get_engine_config(self) -> Dict[str, Any]:
        """Get SQLAlchemy engine configuration.

        Returns:
            Engine configuration
        """
        config: Dict[str, Any] = {
            "future": True,
            "echo": self.echo,
        }

        if self.driver == "sqlite":
            config["connect_args"] = {"check_same_thread": False}
        else:
            config.update({
                "pool_size": self.pool_size,
                "max_overflow": self.max_overflow,
                "pool_timeout": self.pool_timeout,
                "pool_recycle": self.pool_recycle,
            })

        return config
