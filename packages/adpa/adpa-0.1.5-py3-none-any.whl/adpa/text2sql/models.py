"""Database models and schema definitions."""

from datetime import datetime
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field, validator


class BaseDBModel(BaseModel):
    """Base model with common fields."""
    id: UUID = Field(..., description="Unique identifier")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        frozen = True


class Column(BaseDBModel):
    """Database column definition."""
    name: str = Field(..., description="Column name")
    type: str = Field(..., description="SQL data type")
    nullable: bool = Field(default=True)
    default: Optional[str] = Field(default=None)
    primary_key: bool = Field(default=False)
    unique: bool = Field(default=False)
    foreign_key: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

    @validator("name")
    def validate_name(cls, v: str) -> str:
        """Validate column name."""
        if not v.isidentifier():
            raise ValueError("Column name must be a valid identifier")
        return v


class Index(BaseDBModel):
    """Database index definition."""
    name: str = Field(..., description="Index name")
    table: str = Field(..., description="Table name")
    columns: List[str] = Field(..., description="Columns to index")
    unique: bool = Field(default=False)
    type: str = Field(default="btree")
    partial: Optional[str] = Field(default=None)

    @validator("type")
    def validate_type(cls, v: str) -> str:
        """Validate index type."""
        valid_types = {"btree", "hash", "gist", "gin", "brin"}
        if v.lower() not in valid_types:
            raise ValueError(f"Index type must be one of: {valid_types}")
        return v.lower()


class Table(BaseDBModel):
    """Database table definition."""
    name: str = Field(..., description="Table name")
    columns: List[Column] = Field(..., description="Table columns")
    indexes: List[Index] = Field(default_factory=list)
    constraints: List[str] = Field(default_factory=list)
    description: Optional[str] = Field(default=None)

    @validator("name")
    def validate_name(cls, v: str) -> str:
        """Validate table name."""
        if not v.isidentifier():
            raise ValueError("Table name must be a valid identifier")
        return v


class Schema(BaseDBModel):
    """Complete database schema."""
    name: str = Field(..., description="Schema name")
    tables: Dict[str, Table] = Field(..., description="Schema tables")
    version: str = Field(default="1.0.0")
    dialect: str = Field(default="postgresql")
    metadata: Dict[str, str] = Field(default_factory=dict)

    @validator("dialect")
    def validate_dialect(cls, v: str) -> str:
        """Validate SQL dialect."""
        valid_dialects = {"postgresql", "mysql", "sqlite", "mssql"}
        if v.lower() not in valid_dialects:
            raise ValueError(f"Dialect must be one of: {valid_dialects}")
        return v.lower()


class QueryTemplate(BaseDBModel):
    """SQL query template."""
    name: str = Field(..., description="Template name")
    template: str = Field(..., description="SQL template")
    description: Optional[str] = Field(default=None)
    parameters: Dict[str, str] = Field(default_factory=dict)
    dialect: str = Field(default="postgresql")
    tags: List[str] = Field(default_factory=list)

    def render(self, **kwargs) -> str:
        """Render template with parameters."""
        return self.template.format(**kwargs)
