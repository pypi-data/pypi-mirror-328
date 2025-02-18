"""
API routes module.
"""
from fastapi import APIRouter

from adpa.api.routes.auth import router as auth_router
from adpa.api.routes.queries import router as queries_router
from adpa.api.routes.datasets import router as datasets_router
from adpa.api.routes.users import router as users_router

# Create main router
router = APIRouter()

# Include sub-routers
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(queries_router, prefix="/queries", tags=["Queries"])
router.include_router(datasets_router, prefix="/datasets", tags=["Datasets"])
router.include_router(users_router, prefix="/users", tags=["Users"])
