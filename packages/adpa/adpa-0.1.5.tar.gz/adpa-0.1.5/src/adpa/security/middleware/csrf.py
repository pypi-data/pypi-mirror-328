"""CSRF protection middleware for ADPA Framework."""
from typing import Optional, Callable, Any, Set
from datetime import datetime, timedelta
import secrets
import hmac
import hashlib
from fastapi import Request, Response, HTTPException
from pydantic import BaseModel, Field, validator


class CSRFToken(BaseModel):
    """CSRF token model with validation."""
    
    token: str = Field(
        ...,
        min_length=32,
        max_length=64,
        description="CSRF token string"
    )
    expires: datetime = Field(
        ...,
        description="Token expiration timestamp"
    )
    
    @validator("expires")
    def validate_expiry(cls, v: datetime) -> datetime:
        """Validate token expiration.
        
        Args:
            v: Expiration timestamp
            
        Returns:
            Validated timestamp
            
        Raises:
            ValueError: If token is already expired
        """
        if v < datetime.utcnow():
            raise ValueError("Token is already expired")
        return v
    
    class Config:
        """Pydantic model configuration."""
        frozen = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class CSRFConfig(BaseModel):
    """CSRF middleware configuration."""
    
    secret_key: str = Field(
        ...,
        min_length=32,
        description="Secret key for token generation"
    )
    token_expiry: int = Field(
        default=3600,
        gt=0,
        description="Token expiry time in seconds"
    )
    safe_methods: Set[str] = Field(
        default={"GET", "HEAD", "OPTIONS"},
        description="HTTP methods that don't require CSRF protection"
    )
    token_header: str = Field(
        default="X-CSRF-Token",
        description="Name of the CSRF token header"
    )
    cookie_name: str = Field(
        default="csrf_token",
        description="Name of the CSRF token cookie"
    )
    cookie_secure: bool = Field(
        default=True,
        description="Whether to set Secure flag on cookie"
    )
    cookie_httponly: bool = Field(
        default=True,
        description="Whether to set HttpOnly flag on cookie"
    )
    cookie_samesite: str = Field(
        default="Lax",
        description="SameSite cookie policy"
    )
    
    class Config:
        """Pydantic model configuration."""
        frozen = True


class CSRFMiddleware:
    """CSRF protection middleware."""
    
    def __init__(self, config: CSRFConfig) -> None:
        """Initialize CSRF middleware.
        
        Args:
            config: CSRF middleware configuration
        """
        self.config = config
        self._secret_key = config.secret_key.encode()

    async def __call__(
        self,
        request: Request,
        call_next: Callable
    ) -> Response:
        """Process the request and apply CSRF protection.
        
        Args:
            request: FastAPI request object
            call_next: Next middleware in chain
            
        Returns:
            Response from next middleware
            
        Raises:
            HTTPException: If CSRF validation fails
        """
        if request.method in self.config.safe_methods:
            response = await call_next(request)
            if request.method == "GET":
                self._set_csrf_token(response)
            return response

        # Validate CSRF token
        token = request.headers.get(self.config.token_header)
        cookie_token = request.cookies.get(self.config.cookie_name)

        if not token or not cookie_token:
            raise HTTPException(
                status_code=403,
                detail="CSRF token missing"
            )

        try:
            self._validate_token(token, cookie_token)
        except ValueError as e:
            raise HTTPException(
                status_code=403,
                detail=str(e)
            )

        response = await call_next(request)
        return response

    def _generate_token(self) -> CSRFToken:
        """Generate a new CSRF token.
        
        Returns:
            CSRFToken object containing token and expiry
        """
        token = secrets.token_urlsafe(32)
        expires = datetime.utcnow() + timedelta(seconds=self.config.token_expiry)
        return CSRFToken(token=token, expires=expires)

    def _validate_token(self, token: str, cookie_token: str) -> None:
        """Validate CSRF token against cookie token.
        
        Args:
            token: Token from request header
            cookie_token: Token from cookie
            
        Raises:
            ValueError: If token validation fails
        """
        if not hmac.compare_digest(token, cookie_token):
            raise ValueError("Invalid CSRF token")

        try:
            csrf_token = CSRFToken.parse_raw(cookie_token)
            if csrf_token.expires < datetime.utcnow():
                raise ValueError("CSRF token expired")
        except Exception as e:
            raise ValueError(f"Invalid CSRF token format: {str(e)}")

    def _set_csrf_token(self, response: Response) -> None:
        """Set CSRF token cookie in response.
        
        Args:
            response: FastAPI response object
        """
        token = self._generate_token()
        response.set_cookie(
            key=self.config.cookie_name,
            value=token.json(),
            max_age=self.config.token_expiry,
            secure=self.config.cookie_secure,
            httponly=self.config.cookie_httponly,
            samesite=self.config.cookie_samesite
        )
