"""
FastAPI application factory.
"""
from typing import Optional
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
import time

from adpa.api.types import APIConfig, APIResponse
from adpa.api.routes import router
from adpa.database.connection import get_engine
from adpa.database.session import SessionLocal

def create_app(config: Optional[APIConfig] = None) -> FastAPI:
    """Create FastAPI application.
    
    Args:
        config: Optional API configuration
    
    Returns:
        FastAPI application
    """
    if config is None:
        config = APIConfig.from_env()
    
    app = FastAPI(
        title="ADPA API",
        description="ADPA Framework REST API",
        version="1.0.0",
        docs_url=config.docs_url,
        redoc_url=config.redoc_url,
        openapi_url=config.openapi_url
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    
    # Add database session middleware
    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        """Add database session to request state."""
        request.state.db = SessionLocal()
        try:
            response = await call_next(request)
        finally:
            request.state.db.close()
        return response
    
    # Add request timing middleware
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        """Add request processing time to response headers."""
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
    
    # Add error handlers
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Handle request validation errors."""
        return JSONResponse(
            status_code=422,
            content=APIResponse(
                success=False,
                message="Validation error",
                error=str(exc)
            ).dict()
        )
    
    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
        """Handle database errors."""
        return JSONResponse(
            status_code=500,
            content=APIResponse(
                success=False,
                message="Database error",
                error=str(exc)
            ).dict()
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """Handle general errors."""
        return JSONResponse(
            status_code=500,
            content=APIResponse(
                success=False,
                message="Internal server error",
                error=str(exc)
            ).dict()
        )
    
    # Add health check endpoint
    @app.get("/health")
    async def health_check():
        """Check API health."""
        try:
            engine = get_engine()
            with engine.connect() as conn:
                conn.execute("SELECT 1")
            return APIResponse(
                success=True,
                message="API is healthy",
                data={
                    "database": "connected",
                    "status": "healthy"
                }
            )
        except Exception as e:
            return APIResponse(
                success=False,
                message="API is unhealthy",
                data={
                    "database": "disconnected",
                    "status": "unhealthy"
                },
                error=str(e)
            )
    
    # Include API routes
    app.include_router(
        router,
        prefix=config.api_prefix
    )
    
    return app
