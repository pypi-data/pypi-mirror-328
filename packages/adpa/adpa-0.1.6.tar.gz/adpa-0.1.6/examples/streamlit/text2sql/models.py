"""Pydantic models for the Text-to-SQL Streamlit app."""
from datetime import datetime
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field, validator, root_validator


class DatabaseConfig(BaseModel):
    """Database configuration model."""
    
    host: str = Field(..., description="Database host")
    port: int = Field(..., ge=1, le=65535, description="Database port")
    user: str = Field(..., min_length=1, description="Database user")
    password: str = Field(..., min_length=1, description="Database password")
    database: str = Field(..., min_length=1, description="Database name")
    uri: str = Field(..., description="Complete database URI")
    
    class Config:
        """Model configuration."""
        frozen = True
        validate_assignment = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
    
    @validator("uri")
    def validate_uri(cls, v: str) -> str:
        """Validate database URI format."""
        if not v.startswith(("postgresql://", "postgres://")):
            raise ValueError("Invalid database URI format")
        return v


class TableColumn(BaseModel):
    """Database table column model."""
    
    name: str = Field(..., description="Column name")
    data_type: str = Field(..., description="Column data type")
    is_nullable: bool = Field(..., description="Whether column can be null")
    default_value: Optional[str] = Field(None, description="Default column value")
    
    class Config:
        """Model configuration."""
        frozen = True
        validate_assignment = True


class TableSchema(BaseModel):
    """Database table schema model."""
    
    name: str = Field(..., description="Table name")
    columns: List[TableColumn] = Field(..., description="Table columns")
    primary_key: Optional[List[str]] = Field(None, description="Primary key columns")
    foreign_keys: Optional[Dict[str, str]] = Field(
        None,
        description="Foreign key relationships"
    )
    
    class Config:
        """Model configuration."""
        frozen = True
        validate_assignment = True


class QueryMetadata(BaseModel):
    """Query metadata model."""
    
    tables_referenced: List[str] = Field(
        default_factory=list,
        description="Tables referenced in the query"
    )
    query_type: str = Field(..., description="Type of SQL query")
    estimated_rows: Optional[int] = Field(
        None,
        ge=0,
        description="Estimated number of rows affected"
    )
    execution_plan: Optional[Dict] = Field(
        None,
        description="Query execution plan"
    )
    
    class Config:
        """Model configuration."""
        frozen = True
        validate_assignment = True


class QueryResult(BaseModel):
    """Query execution result model."""
    
    natural_query: str = Field(..., description="Original natural language query")
    sql_query: str = Field(..., description="Generated SQL query")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    processing_time: float = Field(..., gt=0, description="Processing time in seconds")
    success: bool = Field(..., description="Whether the query was successful")
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Query timestamp"
    )
    error_message: Optional[str] = Field(None, description="Error message if query failed")
    metadata: Optional[QueryMetadata] = Field(None, description="Query metadata")
    
    class Config:
        """Model configuration."""
        frozen = True
        validate_assignment = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class AppConfig(BaseModel):
    """Application configuration model."""
    
    title: str = Field(..., description="Application title")
    icon: str = Field(..., description="Application icon")
    theme_color: str = Field(..., description="Theme color")
    max_history_size: int = Field(..., gt=0, description="Maximum history size")
    example_queries: List[str] = Field(..., description="Example queries")
    schema_info: Dict[str, List[str]] = Field(..., description="Schema information")
    
    class Config:
        """Model configuration."""
        frozen = True
        validate_assignment = True
    
    @validator("theme_color")
    def validate_theme_color(cls, v: str) -> str:
        """Validate theme color format."""
        if not v.startswith("#"):
            raise ValueError("Theme color must be a hex color code")
        return v


class Text2SQLConfig(BaseModel):
    """Text2SQL configuration model."""
    
    connection_params: Dict[str, str] = Field(
        ...,
        description="Database connection parameters"
    )
    enable_security: bool = Field(..., description="Enable security features")
    enable_monitoring: bool = Field(..., description="Enable monitoring")
    optimization_level: int = Field(
        ...,
        ge=0,
        le=3,
        description="Query optimization level"
    )
    timeout_seconds: int = Field(..., gt=0, description="Query timeout in seconds")
    
    class Config:
        """Model configuration."""
        frozen = True
        validate_assignment = True
