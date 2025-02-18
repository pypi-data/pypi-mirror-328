"""
API types and models.
"""
from typing import Optional, Dict, Any, List, Union
from datetime import datetime
from pydantic import BaseModel, Field, validator

class APIConfig(BaseModel):
    """API configuration."""
    
    host: str = Field(
        default="0.0.0.0",
        description="Host to bind to"
    )
    port: int = Field(
        default=8000,
        description="Port to listen on"
    )
    debug: bool = Field(
        default=False,
        description="Enable debug mode"
    )
    cors_origins: List[str] = Field(
        default=["*"],
        description="Allowed CORS origins"
    )
    api_prefix: str = Field(
        default="/api/v1",
        description="API route prefix"
    )
    docs_url: str = Field(
        default="/docs",
        description="OpenAPI documentation URL"
    )
    redoc_url: str = Field(
        default="/redoc",
        description="ReDoc documentation URL"
    )
    openapi_url: str = Field(
        default="/openapi.json",
        description="OpenAPI schema URL"
    )
    rate_limit: int = Field(
        default=100,
        description="Rate limit per minute"
    )
    jwt_secret: str = Field(
        description="JWT secret key"
    )
    jwt_algorithm: str = Field(
        default="HS256",
        description="JWT algorithm"
    )
    jwt_expires_minutes: int = Field(
        default=30,
        description="JWT expiration time in minutes"
    )
    
    @validator("port")
    def validate_port(cls, v: int) -> int:
        """Validate port number."""
        if not 1 <= v <= 65535:
            raise ValueError("Port must be between 1 and 65535")
        return v
    
    @validator("rate_limit")
    def validate_rate_limit(cls, v: int) -> int:
        """Validate rate limit."""
        if v < 1:
            raise ValueError("Rate limit must be positive")
        return v
    
    @classmethod
    def from_env(cls) -> "APIConfig":
        """Create configuration from environment variables.
        
        Returns:
            API configuration
        
        Environment Variables:
            API_HOST: Host to bind to
            API_PORT: Port to listen on
            API_DEBUG: Enable debug mode
            API_CORS_ORIGINS: Comma-separated list of allowed origins
            API_PREFIX: API route prefix
            API_DOCS_URL: OpenAPI documentation URL
            API_REDOC_URL: ReDoc documentation URL
            API_OPENAPI_URL: OpenAPI schema URL
            API_RATE_LIMIT: Rate limit per minute
            API_JWT_SECRET: JWT secret key
            API_JWT_ALGORITHM: JWT algorithm
            API_JWT_EXPIRES: JWT expiration time in minutes
        """
        import os
        
        return cls(
            host=os.getenv("API_HOST", "0.0.0.0"),
            port=int(os.getenv("API_PORT", "8000")),
            debug=os.getenv("API_DEBUG", "").lower() == "true",
            cors_origins=os.getenv("API_CORS_ORIGINS", "*").split(","),
            api_prefix=os.getenv("API_PREFIX", "/api/v1"),
            docs_url=os.getenv("API_DOCS_URL", "/docs"),
            redoc_url=os.getenv("API_REDOC_URL", "/redoc"),
            openapi_url=os.getenv("API_OPENAPI_URL", "/openapi.json"),
            rate_limit=int(os.getenv("API_RATE_LIMIT", "100")),
            jwt_secret=os.getenv("API_JWT_SECRET", ""),
            jwt_algorithm=os.getenv("API_JWT_ALGORITHM", "HS256"),
            jwt_expires_minutes=int(os.getenv("API_JWT_EXPIRES", "30"))
        )

class APIResponse(BaseModel):
    """API response model."""
    
    success: bool = Field(
        description="Whether the request was successful"
    )
    message: str = Field(
        description="Response message"
    )
    data: Optional[Any] = Field(
        default=None,
        description="Response data"
    )
    error: Optional[str] = Field(
        default=None,
        description="Error message if any"
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="Response timestamp"
    )
    
    class Config:
        """Model configuration."""
        
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
