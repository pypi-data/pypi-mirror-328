# Session Management

Version 0.7.0

ADPA uses SQLAlchemy for database session management and PostgreSQL as the database backend. This document describes how sessions are managed and how to use them in your code.

## Database Configuration

The database connection is configured using environment variables:

```bash
POSTGRES_HOST=your-host
POSTGRES_PORT=5432
POSTGRES_USER=your-user
POSTGRES_PASSWORD=your-password
POSTGRES_DATABASE=your-database
POSTGRES_URI=postgresql://user:password@host:port/database
```

## Session Management

Sessions are managed using SQLAlchemy's session management with connection pooling:

```python
from adpa.database.session import get_db_session

with get_db_session() as session:
    # Use session here
    user = session.query(User).filter_by(id=1).first()
```

The session manager handles:
- Connection pooling
- Transaction management
- Automatic commits and rollbacks
- Resource cleanup

## Repository Pattern

ADPA uses the repository pattern to abstract database operations:

```python
from adpa.database.repository import UserRepository

with get_db_session() as session:
    user_repo = UserRepository(session)
    user = user_repo.get_by_username("johndoe")
```

Available repositories:
- UserRepository: User management
- ProjectRepository: Project management
- AppStateRepository: Application state
- ModelConfigRepository: Model configurations
- SystemHealthRepository: System health monitoring

## Models

All models inherit from a base model that provides common fields:

```python
class Base:
    id: Primary key
    is_active: Soft delete flag
    created_at: Creation timestamp
    updated_at: Last update timestamp
```

Available models:
- Project: Project management
- User: User information
- UserProfile: User profiles
- AppState: Application state
- ModelConfig: Model configurations
- SystemHealth: System health

## Example Usage

Here's a complete example of using sessions and repositories:

```python
from adpa.database.session import get_db_session
from adpa.database.repository import ProjectRepository, UserRepository

def create_project_with_user():
    with get_db_session() as session:
        # Create project
        project_repo = ProjectRepository(session)
        project = project_repo.create(
            project_id="new-project",
            name="New Project",
            description="A new project"
        )
        
        # Create user in project
        user_repo = UserRepository(session)
        user = user_repo.create(
            username="johndoe",
            email="john@example.com",
            project_id=project.id
        )
        
        return project, user
```

## Best Practices

1. Always use the context manager (`with` statement) to ensure proper resource cleanup
2. Use repositories instead of direct session operations
3. Keep transactions short and focused
4. Handle exceptions appropriately
5. Use soft deletes (is_active flag) instead of hard deletes

## Connection Pooling

The session manager is configured with connection pooling:

```python
engine = create_engine(
    db_uri,
    pool_size=5,           # Base pool size
    max_overflow=10,       # Additional connections when needed
    pool_timeout=30,       # Connection wait timeout
    pool_recycle=1800,    # Connection recycle time (30 minutes)
)
```

This ensures efficient connection management and prevents connection leaks.

## Error Handling

The session manager includes built-in error handling:

```python
with get_db_session() as session:
    try:
        # Database operations
        session.commit()
    except Exception:
        session.rollback()
        raise
```

Common errors:
- ConnectionError: Database connection issues
- IntegrityError: Constraint violations
- OperationalError: Database operation issues
