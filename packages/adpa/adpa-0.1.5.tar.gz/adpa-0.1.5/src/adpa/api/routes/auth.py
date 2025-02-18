"""
Authentication routes.
"""
from typing import Optional
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from adpa.api.types import APIConfig, APIResponse
from adpa.database.models import User
from adpa.database.repository import Repository

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_config() -> APIConfig:
    """Get API configuration."""
    return APIConfig.from_env()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Hash password."""
    return pwd_context.hash(password)

def create_access_token(data: dict, config: APIConfig) -> str:
    """Create JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=config.jwt_expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, config.jwt_secret, algorithm=config.jwt_algorithm)

async def get_current_user(
    request: Request,
    token: str = Depends(oauth2_scheme),
    config: APIConfig = Depends(get_config)
) -> User:
    """Get current authenticated user."""
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.jwt_secret, algorithms=[config.jwt_algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    repo = Repository[User](request.state.db)
    user = repo.get_by_field("username", username)
    if user is None:
        raise credentials_exception
    return user

@router.post("/token")
async def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    config: APIConfig = Depends(get_config)
) -> APIResponse:
    """Login user and get access token."""
    repo = Repository[User](request.state.db)
    user = repo.get_by_field("username", form_data.username)
    
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Update last login
    user.last_login = datetime.utcnow()
    repo.update(user)
    
    # Create access token
    access_token = create_access_token(
        data={"sub": user.username},
        config=config
    )
    
    return APIResponse(
        success=True,
        message="Login successful",
        data={
            "access_token": access_token,
            "token_type": "bearer"
        }
    )

@router.post("/register")
async def register(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends()
) -> APIResponse:
    """Register new user."""
    repo = Repository[User](request.state.db)
    
    # Check if username exists
    if repo.get_by_field("username", form_data.username):
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    # Create user
    user = User(
        username=form_data.username,
        email=form_data.username,  # Use username as email for now
        password_hash=get_password_hash(form_data.password),
        is_active=True
    )
    repo.create(user)
    
    return APIResponse(
        success=True,
        message="Registration successful",
        data={"username": user.username}
    )

@router.get("/me")
async def read_users_me(
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Get current user information."""
    return APIResponse(
        success=True,
        message="User details retrieved",
        data={
            "id": str(current_user.id),
            "username": current_user.username,
            "email": current_user.email,
            "is_active": current_user.is_active,
            "last_login": current_user.last_login
        }
    )
