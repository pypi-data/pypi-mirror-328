"""SQL middleware for query processing and monitoring."""
from typing import Any, Dict, List, Optional, Set
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import json
import time
import logging
from .generator import SQLGenerator
from .validation import SQLValidator


logger = logging.getLogger(__name__)


class SQLMiddleware(BaseHTTPMiddleware):
    """Middleware for SQL query processing and monitoring."""

    def __init__(
        self,
        app: Any,
        generator: SQLGenerator,
        validator: SQLValidator,
        skip_paths: Optional[Set[str]] = None
    ) -> None:
        """Initialize middleware.

        Args:
            app: FastAPI application
            generator: SQL query generator
            validator: SQL query validator
            skip_paths: Paths to skip processing
        """
        super().__init__(app)
        self.generator = generator
        self.validator = validator
        self.skip_paths = skip_paths or set()
        self.metrics: Dict[str, Any] = {
            "requests": 0,
            "errors": 0,
            "generation_time": 0,
            "validation_time": 0
        }

    async def dispatch(
        self,
        request: Request,
        call_next: Any
    ) -> Response:
        """Process incoming request.

        Args:
            request: FastAPI request
            call_next: Next middleware in chain

        Returns:
            FastAPI response
        """
        # Skip processing for excluded paths
        if request.url.path in self.skip_paths:
            return await call_next(request)

        # Only process POST requests with JSON content
        if request.method != "POST" or \
           request.headers.get("content-type") != "application/json":
            return await call_next(request)

        start_time = time.time()
        self.metrics["requests"] += 1

        try:
            # Extract query from request
            body = await request.json()
            query_text = body.get("query")
            if not query_text:
                return Response(
                    content=json.dumps({
                        "error": "Missing query parameter"
                    }),
                    status_code=400,
                    media_type="application/json"
                )

            # Generate SQL query
            gen_start = time.time()
            generation_result = self.generator.generate_query(query_text)
            self.metrics["generation_time"] += time.time() - gen_start

            if not generation_result["success"]:
                self.metrics["errors"] += 1
                return Response(
                    content=json.dumps({
                        "error": "Query generation failed",
                        "details": generation_result.get("error")
                    }),
                    status_code=400,
                    media_type="application/json"
                )

            # Validate generated query
            val_start = time.time()
            validation_result = self.validator.validate_query(
                generation_result["query"]
            )
            self.metrics["validation_time"] += time.time() - val_start

            if not validation_result.valid:
                self.metrics["errors"] += 1
                return Response(
                    content=json.dumps({
                        "error": "Query validation failed",
                        "details": validation_result.errors
                    }),
                    status_code=400,
                    media_type="application/json"
                )

            # Modify request with processed query
            body["sql"] = generation_result["query"]
            body["validation"] = validation_result.dict()
            body["phases"] = generation_result["phases"]

            # Update request body
            await self._update_request_body(request, body)

            # Log request details
            self._log_request(request, generation_result, validation_result)

            return await call_next(request)

        except Exception as e:
            self.metrics["errors"] += 1
            logger.error(f"SQL middleware error: {str(e)}", exc_info=True)
            return Response(
                content=json.dumps({
                    "error": "Internal server error",
                    "details": str(e)
                }),
                status_code=500,
                media_type="application/json"
            )
        finally:
            # Update timing metrics
            self.metrics["total_time"] = time.time() - start_time

    async def _update_request_body(
        self,
        request: Request,
        new_body: Dict[str, Any]
    ) -> None:
        """Update request body with processed data.

        Args:
            request: FastAPI request
            new_body: New request body
        """
        # Store original body
        if not hasattr(request.state, "original_body"):
            request.state.original_body = await request.json()

        # Update request body
        async def receive():
            return {
                "type": "http.request",
                "body": json.dumps(new_body).encode()
            }

        request._receive = receive

    def _log_request(
        self,
        request: Request,
        generation_result: Dict[str, Any],
        validation_result: Any
    ) -> None:
        """Log request details.

        Args:
            request: FastAPI request
            generation_result: Query generation result
            validation_result: Query validation result
        """
        log_data = {
            "timestamp": time.time(),
            "path": request.url.path,
            "method": request.method,
            "client": request.client.host if request.client else None,
            "generation": {
                "success": generation_result["success"],
                "phases": list(generation_result["phases"].keys())
            },
            "validation": {
                "valid": validation_result.valid,
                "error_count": len(validation_result.errors),
                "warning_count": len(validation_result.warnings)
            },
            "metrics": {
                "generation_time": self.metrics["generation_time"],
                "validation_time": self.metrics["validation_time"]
            }
        }

        logger.info("SQL request processed", extra={"data": log_data})
