"""
SQLAlchemy models for ADPA framework.
"""
from datetime import datetime
import uuid
from typing import Any, Dict, List, Optional, TypedDict, final
from typing_extensions import override

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey, JSON, text
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    validates,
)


class Base(DeclarativeBase):
    """Base class for all models."""
    pass


class TimestampMixin:
    """Mixin to add timestamp columns."""
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        server_default=text("CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP"),
        nullable=False
    )


@final
class User(Base, TimestampMixin):
    """User model."""
    
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        server_default=text("hex(randomblob(16))"),
        nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False
    )
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime)
    preferences: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSON)
    
    # Relationships
    queries: Mapped[List["Query"]] = relationship("Query", back_populates="user")
    datasets: Mapped[List["Dataset"]] = relationship("Dataset", back_populates="owner")

    @validates("email")
    def validate_email(self, key: str, value: str) -> str:
        """Validate email address."""
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value.lower()

    @validates("username")
    def validate_username(self, key: str, value: str) -> str:
        """Validate username."""
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")
        return value


@final
class APIKey(Base, TimestampMixin):
    """API key model."""
    
    __tablename__ = "api_keys"
    
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        server_default=text("hex(randomblob(16))"),
        nullable=False
    )
    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id"),
        nullable=False
    )
    key: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    last_used_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    permissions: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSON)
    
    # Relationships
    user: Mapped["User"] = relationship("User")
