"""
User routes.
"""
from typing import Optional
from fastapi import APIRouter, Depends, Request, Query, HTTPException
from sqlalchemy import desc

from adpa.api.types import APIResponse
from adpa.api.routes.auth import get_current_user, get_password_hash
from adpa.database.models import User
from adpa.database.repository import Repository

router = APIRouter()

@router.get("/profile")
async def get_profile(
    request: Request,
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Get user profile."""
    return APIResponse(
        success=True,
        message="Profile retrieved",
        data={
            "id": str(current_user.id),
            "username": current_user.username,
            "email": current_user.email,
            "is_active": current_user.is_active,
            "last_login": current_user.last_login,
            "preferences": current_user.preferences,
            "created_at": current_user.created_at
        }
    )

@router.put("/profile")
async def update_profile(
    request: Request,
    email: Optional[str] = Query(None, description="New email"),
    preferences: Optional[dict] = Query(None, description="User preferences"),
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Update user profile."""
    repo = Repository[User](request.state.db)
    
    # Update email if provided
    if email:
        # Check if email is taken
        if repo.get_by_field("email", email):
            raise HTTPException(
                status_code=400,
                detail="Email already taken"
            )
        current_user.email = email
    
    # Update preferences if provided
    if preferences:
        current_user.preferences = preferences
    
    # Save changes
    repo.update(current_user)
    
    return APIResponse(
        success=True,
        message="Profile updated",
        data={
            "email": current_user.email,
            "preferences": current_user.preferences
        }
    )

@router.put("/password")
async def change_password(
    request: Request,
    current_password: str = Query(..., description="Current password"),
    new_password: str = Query(..., description="New password"),
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Change user password."""
    from adpa.api.routes.auth import verify_password
    
    # Verify current password
    if not verify_password(current_password, current_user.password_hash):
        raise HTTPException(
            status_code=400,
            detail="Incorrect password"
        )
    
    # Update password
    repo = Repository[User](request.state.db)
    current_user.password_hash = get_password_hash(new_password)
    repo.update(current_user)
    
    return APIResponse(
        success=True,
        message="Password changed successfully"
    )

@router.delete("/")
async def delete_account(
    request: Request,
    password: str = Query(..., description="Current password"),
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Delete user account."""
    from adpa.api.routes.auth import verify_password
    
    # Verify password
    if not verify_password(password, current_user.password_hash):
        raise HTTPException(
            status_code=400,
            detail="Incorrect password"
        )
    
    # Delete account
    repo = Repository[User](request.state.db)
    repo.delete(current_user)
    
    return APIResponse(
        success=True,
        message="Account deleted successfully"
    )
