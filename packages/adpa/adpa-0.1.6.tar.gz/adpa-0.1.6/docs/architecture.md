# ADPA Framework Architecture

Version: 1.3.0
Last Updated: 2025-02-06

## Overview

ADPA (Async Database-Powered Agents) is a scalable system that combines traditional Object-Oriented Programming (OOP) with modern agent-based architectures. Built with LangChain/Langraph and SQLite, it implements a hybrid approach where specialized agents and OOP components work together to handle complex tasks efficiently, including natural language to SQL conversion, while maintaining conversation history in a persistent database.

## Framework Structure

The ADPA framework is organized into the following key components:

### Core (adpa/core/)
- `framework.py`: Main ADPA framework implementation
- `attention/`: Attention analysis components
- `desire/`: Desire analysis components
- `position/`: Position analysis components
- `action/`: Action analysis components

### Agents (adpa/agents/)
- `base.py`: Base agent implementation
- `teams/`: Team management and coordination
- `actions/`: Agent action definitions and handlers

### Database (adpa/database/)
- `models/`: SQLAlchemy models
  - `base.py`: Base model class
  - `user.py`: User model
  - `project.py`: Project model
  - `agent.py`: Agent model
- `repository/`: Data access layer

### Text2SQL (adpa/text2sql/)
- `app.py`: Streamlit application
- `models/`: Query models and processing
- `core/`: Core text-to-SQL functionality

### API (adpa/api/)
- `routes/`: API endpoint definitions
- REST API implementation

### Monitoring (adpa/monitoring/)
- `health.py`: System health monitoring
- Performance metrics collection

### Utils (adpa/utils/)
- `logging.py`: Logging utilities
- Common helper functions

## System Components

### 1. Text2SQL Module

The Text2SQL module represents our hybrid architecture approach, combining traditional OOP with agent-based components for enhanced flexibility and performance.

#### Core OOP Components
- **DatabaseManager**: Handles database connections and operations
  - Connection pooling
  - Query execution
  - Transaction management
- **QueryValidator**: Validates and sanitizes SQL queries
  - Syntax validation
  - Security checks
  - Schema compliance

#### Agent Components
- **NLPAgent**: Natural language processing
  - Intent extraction
  - Entity recognition
  - Context understanding
- **OptimizerAgent**: Query optimization
  - Performance tuning
  - Index suggestions
  - Query rewriting
- **SecurityAgent**: Security and compliance
  - Injection prevention
  - Access control
  - Audit logging
- **MonitorAgent**: System monitoring
  - Performance metrics
  - Resource usage
  - Error tracking

#### Hybrid Coordinator
- Component orchestration
- Async operation management
- Error handling
- Performance tracking

### 2. Database Layer

#### Schema
- **Users**: Stores user information and preferences
- **Conversations**: Tracks chat sessions with metadata
- **Messages**: Stores all messages with role and content
- **Team Assignments**: Records team assignments for conversations
- **QueryHistory**: Stores executed queries with performance metrics

#### Features
- Fully asynchronous with aiosqlite
- Alembic migrations for schema management
- Repository pattern for data access
- JSON metadata support for extensibility
- Query performance tracking

### 3. Agents

#### Moderator Agent
- **Purpose**: Monitors conversation flow and user interactions
- **Responsibilities**:
  - Content moderation
  - Conversation monitoring
  - Query escalation
  - Context maintenance

#### Life Coach Agent
- **Purpose**: Provides personalized guidance
- **Responsibilities**:
  - Personal advice
  - Goal setting
  - Progress tracking
  - Motivational support

#### IT Architect Agent
- **Purpose**: System architecture oversight
- **Responsibilities**:
  - Architecture guidance
  - Security best practices
  - Tool recommendations
  - Documentation review

#### Router Agent
- **Purpose**: Task distribution
- **Responsibilities**:
  - Query analysis
  - Team selection
  - Priority management
  - Route optimization

### 4. Teams

Teams are dynamic groups of agents working together to solve complex tasks.

#### Structure
- Teams contain 1+ agents
- Shared context between team members
- Dynamic task allocation
- Cross-team collaboration support

#### Current Teams
1. Support Team
   - Members: Moderator Agent, Life Coach Agent
   - Focus: User support and guidance

2. Technical Team
   - Members: IT Architect Agent, NLP Agent
   - Focus: System architecture and query processing

3. Query Processing Team
   - Members: NLP Agent, Optimizer Agent, Security Agent
   - Focus: SQL query generation and optimization

### 5. Toolbox

Shared utilities available to all agents and teams.

#### Available Tools
1. API Tool
   - External API interactions
   - Request management

2. Logging Tool
   - Structured logging
   - Debug support

3. Data Transform Tool
   - JSON operations
   - Data filtering
   - Sorting operations

4. Query Analysis Tool
   - Performance metrics
   - Query optimization
   - Security validation

## System Requirements

- Python 11.9 or higher
- PostgreSQL 15.0 or higher
- Modern web browser (Chrome, Firefox, Safari)

## Memory System Architecture

The ADPA Framework implements a three-tier memory system for managing development state and configuration:

1. **Development Status Memory**
   - Current version tracking
   - Component status
   - Documentation state
   - Known issues and next steps

2. **Configuration System Memory**
   - Environment variable management
   - Validation rules
   - Security settings
   - Configuration templates

3. **Test Suite Memory**
   - Test infrastructure state
   - Test categories and guidelines
   - Execution procedures
   - Best practices

### Memory Initialization Process

The memory system is initialized sequentially through the `startup.py` script:

1. Development status verification
2. Configuration validation
3. Test environment setup

Each memory tier depends on the successful initialization of the previous tier, ensuring a consistent and reliable startup process.

## Configuration Management

### Environment Configuration
The application uses a structured environment configuration system based on Pydantic models. This ensures type safety, validation, and proper organization of all configuration settings.

```
Configuration Structure
├── APIConfig
│   ├── OpenAI and Related APIs
│   └── Search APIs
├── DatabaseConfig
│   └── Postgres Settings
└── ApplicationConfig
    ├── Flask Settings
    └── General Settings
```

### Validation System
The configuration validation system provides:
- Type checking and conversion
- Value range validation
- Format validation (e.g., URLs, API keys)
- Cross-field validation (e.g., database URI)
- Comprehensive error reporting

### Configuration Files
- `.env`: Main configuration file (not in version control)
- `.env.template`: Template with documentation
- `config_validator.py`: Validation logic

### Usage Example
```python
from adpa.text2sql.models.config_validator import validate_environment

def initialize_app():
    # Validate configuration
    result = validate_environment()
    if result["status"] == "error":
        raise SystemExit("Configuration error: " + ", ".join(result["issues"]))
    
    # Continue with app initialization
    ...
```

### Security Considerations
- Sensitive values are never committed to version control
- API keys are validated for proper format
- Database credentials are properly handled
- Configuration is immutable during runtime

## Dependencies

### Python Version
- Python 11.9 or higher required

### Core Dependencies
- `streamlit`: Web application framework
- `pydantic`: Data validation
- `sqlalchemy`: Database ORM
- `pandas`: Data manipulation

### Development Dependencies
- `pytest`: Testing framework
- `black`: Code formatting
- `isort`: Import sorting
- `mypy`: Type checking

## Implementation Details

### Technology Stack
- Python 3.12+
- SQLite with aiosqlite
- Alembic for migrations
- SQLAlchemy for ORM
- LangChain/Langraph
- OpenAI GPT-4
- Click (CLI framework)
- Pytest (testing)
- Pydantic for data validation
- sentence-transformers>=2.2.0
- faiss-cpu>=1.7.0
- psutil>=5.8.0

### Key Features
1. **Hybrid Architecture**
   - OOP components for stability
   - Agent-based components for flexibility
   - Efficient coordination
   - Clear separation of concerns

2. **Persistence**
   - SQLite database backend
   - Asynchronous operations
   - Schema migrations
   - Data versioning

3. **Modularity**
   - Independent components
   - Clear interfaces
   - Easy extensibility

4. **Asynchronous Operations**
   - Non-blocking database access
   - Efficient resource usage
   - Scalable architecture

5. **Type Safety**
   - Full type hints
   - Pydantic models
   - Runtime validation

## Database Schema

### Users
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    external_id VARCHAR(255) NOT NULL UNIQUE,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
```

### Conversations
```sql
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    started_at DATETIME NOT NULL,
    ended_at DATETIME,
    meta_data JSON,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### Messages
```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    conversation_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    role VARCHAR(50) NOT NULL,
    created_at DATETIME NOT NULL,
    meta_data JSON,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
);
```

### Team Assignments
```sql
CREATE TABLE team_assignments (
    id INTEGER PRIMARY KEY,
    conversation_id INTEGER NOT NULL,
    team_name VARCHAR(255) NOT NULL,
    assigned_at DATETIME NOT NULL,
    completed_at DATETIME,
    meta_data JSON,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
);
```

### Query History
```sql
CREATE TABLE query_history (
    id INTEGER PRIMARY KEY,
    conversation_id INTEGER NOT NULL,
    original_query TEXT NOT NULL,
    processed_query TEXT NOT NULL,
    execution_time FLOAT,
    success BOOLEAN,
    error_message TEXT,
    created_at DATETIME NOT NULL,
    meta_data JSON,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
);
```

## Future Enhancements

1. **Text2SQL Module**
   - Enhanced query optimization
   - Additional security features
   - Extended monitoring capabilities
   - Performance improvements
   - Additional agent types

2. **Database**
   - Migration to PostgreSQL for production
   - Connection pooling
   - Read replicas support

3. **Agents**
   - More specialized agents
   - Better context sharing
   - Enhanced routing logic

4. **Teams**
   - Dynamic team formation
   - Load balancing
   - Team performance metrics

5. **Monitoring**
   - Prometheus metrics
   - Grafana dashboards
   - Performance tracking
