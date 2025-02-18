# API Reference

## Core Module

### CoreManager

The `CoreManager` class is the main entry point for ADPA's core functionality.

```python
from adpa.core import CoreManager
from adpa.core.types import CoreConfig

config = CoreConfig(
    max_threads=2,
    queue_size=100,
    batch_size=10
)
manager = CoreManager(config)
```

#### Methods

##### `process_request`
```python
async def process_request(
    self,
    request: Dict[str, Any]
) -> ProcessingResult:
    """Process a request.
    
    Args:
        request: Request dictionary containing:
            - type: Request type
            - data: Request data
            
    Returns:
        ProcessingResult containing:
            - success: Whether processing succeeded
            - data: Processed data
            - error: Error message if failed
            
    Raises:
        ValueError: If request is invalid
    """
```

### DataProcessor

Handles data processing operations.

```python
from adpa.core import DataProcessor
from adpa.core.types import CoreConfig

processor = DataProcessor(config)
```

#### Methods

##### `process`
```python
async def process(
    self,
    data: Dict[str, Any]
) -> ProcessingResult:
    """Process data.
    
    Args:
        data: Data to process
            
    Returns:
        ProcessingResult containing processed data
    """
```

## Text2SQL Module

### SQLGenerator

Generates SQL queries from natural language.

```python
from adpa.text2sql import SQLGenerator
from adpa.text2sql.types import GeneratorConfig

generator = SQLGenerator(GeneratorConfig(
    model="gpt-4",
    temperature=0.7
))
```

#### Methods

##### `generate_query`
```python
async def generate_query(
    self,
    text: str,
    schema: Dict[str, Any]
) -> SQLResult:
    """Generate SQL query from text.
    
    Args:
        text: Natural language query
        schema: Database schema
            
    Returns:
        SQLResult containing:
            - query: Generated SQL query
            - confidence: Confidence score
            - explanation: Query explanation
    """
```

## Agent System

### AgentManager

Manages distributed processing agents.

```python
from adpa.agents import AgentManager
from adpa.agents.types import AgentConfig

manager = AgentManager(AgentConfig(
    max_agents=5,
    timeout=30
))
```

#### Methods

##### `deploy_agent`
```python
async def deploy_agent(
    self,
    agent_type: str,
    config: Dict[str, Any]
) -> Agent:
    """Deploy new agent.
    
    Args:
        agent_type: Type of agent to deploy
        config: Agent configuration
            
    Returns:
        Deployed agent instance
    """
```

##### `list_agents`
```python
async def list_agents(
    self,
    status: Optional[str] = None
) -> List[Agent]:
    """List deployed agents.
    
    Args:
        status: Filter by agent status
            
    Returns:
        List of matching agents
    """
```

## Monitoring System

### MetricsCollector

Collects system and application metrics.

```python
from adpa.monitoring import MetricsCollector
from adpa.monitoring.types import CollectorConfig

collector = MetricsCollector(CollectorConfig(
    interval=60,
    retention_days=7
))
```

#### Methods

##### `collect_metrics`
```python
async def collect_metrics(
    self,
    metric_types: List[str]
) -> Dict[str, Any]:
    """Collect specified metrics.
    
    Args:
        metric_types: Types of metrics to collect
            
    Returns:
        Dictionary of collected metrics
    """
```

##### `get_metrics`
```python
async def get_metrics(
    self,
    metric_type: str,
    start_time: datetime,
    end_time: datetime
) -> List[MetricPoint]:
    """Get historical metrics.
    
    Args:
        metric_type: Type of metrics to retrieve
        start_time: Start of time range
        end_time: End of time range
            
    Returns:
        List of metric points
    """
```

## Security Module

### SecurityManager

Handles security features.

```python
from adpa.security import SecurityManager
from adpa.security.types import SecurityConfig

security = SecurityManager(SecurityConfig(
    max_login_attempts=3,
    session_timeout=3600
))
```

#### Methods

##### `validate_request`
```python
async def validate_request(
    self,
    request: Request
) -> ValidationResult:
    """Validate request security.
    
    Args:
        request: Request to validate
            
    Returns:
        ValidationResult containing:
            - valid: Whether request is valid
            - issues: List of security issues
    """
```

##### `generate_token`
```python
async def generate_token(
    self,
    user_id: str,
    scopes: List[str]
) -> Token:
    """Generate security token.
    
    Args:
        user_id: User identifier
        scopes: Token scopes
            
    Returns:
        Generated token
    """
```

## API Module

### APIServer

FastAPI-based API server.

```python
from adpa.api import APIServer
from adpa.api.types import ServerConfig

server = APIServer(ServerConfig(
    host="localhost",
    port=8000
))
```

#### Methods

##### `start`
```python
async def start(self) -> None:
    """Start API server."""
```

##### `stop`
```python
async def stop(self) -> None:
    """Stop API server."""
```

## Utility Functions

### Data Processing

```python
from adpa.utils import process_batch, validate_data

# Process data in batches
results = await process_batch(
    items,
    batch_size=100,
    processor=process_item
)

# Validate data against schema
is_valid = validate_data(data, schema)
```

### Security

```python
from adpa.utils import hash_password, verify_password

# Hash password
hashed = hash_password(password)

# Verify password
is_valid = verify_password(password, hashed)
```

### Configuration

```python
from adpa.utils import load_config, validate_config

# Load configuration
config = load_config("config.yaml")

# Validate configuration
is_valid = validate_config(config, schema)
```

## Error Types

### Core Errors

```python
from adpa.core.errors import (
    ProcessingError,
    ValidationError,
    ConfigurationError
)
```

### Text2SQL Errors

```python
from adpa.text2sql.errors import (
    QueryGenerationError,
    SchemaError,
    ValidationError
)
```

### Agent Errors

```python
from adpa.agents.errors import (
    AgentError,
    DeploymentError,
    CommunicationError
)
```

### Security Errors

```python
from adpa.security.errors import (
    SecurityError,
    AuthenticationError,
    AuthorizationError
)
```

## Configuration Types

### Core Configuration

```python
from adpa.core.types import CoreConfig

config = CoreConfig(
    max_threads=10,
    queue_size=1000,
    batch_size=100,
    timeout=30
)
```

### Text2SQL Configuration

```python
from adpa.text2sql.types import GeneratorConfig

config = GeneratorConfig(
    model="gpt-4",
    temperature=0.7,
    max_tokens=1000,
    timeout=60
)
```

### Agent Configuration

```python
from adpa.agents.types import AgentConfig

config = AgentConfig(
    max_agents=5,
    timeout=30,
    retry_attempts=3,
    heartbeat_interval=10
)
```

### Security Configuration

```python
from adpa.security.types import SecurityConfig

config = SecurityConfig(
    max_login_attempts=3,
    session_timeout=3600,
    token_expiry=86400,
    min_password_length=12
)
```

## Response Types

### Processing Results

```python
from adpa.core.types import ProcessingResult

result = ProcessingResult(
    success=True,
    data={"key": "value"},
    error=None
)
```

### SQL Results

```python
from adpa.text2sql.types import SQLResult

result = SQLResult(
    query="SELECT * FROM users",
    confidence=0.95,
    explanation="Query to fetch all users"
)
```

### Agent Results

```python
from adpa.agents.types import DeploymentResult

result = DeploymentResult(
    agent_id="agent123",
    status="running",
    resources={"cpu": 0.5, "memory": 100}
)
```

### Security Results

```python
from adpa.security.types import ValidationResult

result = ValidationResult(
    valid=True,
    issues=[],
    risk_score=0.1
)
```
