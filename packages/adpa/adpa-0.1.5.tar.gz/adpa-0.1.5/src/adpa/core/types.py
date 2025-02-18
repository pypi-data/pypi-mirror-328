"""Type definitions for ADPA framework."""
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Protocol,
    Sequence,
    TypeAlias,
    TypedDict,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import (
    NotRequired,
    Required,
    TypeGuard,
    Unpack,
    override,
)

# Type variables
T = TypeVar("T")
U = TypeVar("U")
K = TypeVar("K")
V = TypeVar("V")

# Common types
JSON: TypeAlias = Union[Dict[str, "JSON"], List["JSON"], str, int, float, bool, None]
PathLike: TypeAlias = Union[str, bytes]
Callback: TypeAlias = Callable[..., Any]

# LLM types
ModelName = Literal[
    "gpt-4-0125-preview",
    "gpt-4-1106-preview",
    "gpt-4",
    "gpt-3.5-turbo-0125",
    "gemini-1.0-pro",
    "gemini-1.0-ultra",
    "claude-3-opus",
    "claude-3-sonnet",
    "mixtral-8x7b",
    "llama2-70b",
]

ProviderName = Literal["openai", "google", "anthropic", "groq"]

class LLMConfig(TypedDict):
    """Configuration for LLM providers."""
    
    provider: Required[ProviderName]
    model: Required[ModelName]
    api_key: Required[str]
    temperature: NotRequired[float]
    max_tokens: NotRequired[int]
    top_p: NotRequired[float]
    frequency_penalty: NotRequired[float]
    presence_penalty: NotRequired[float]

# Database types
class DBConfig(TypedDict):
    """Database configuration."""
    
    host: Required[str]
    port: Required[int]
    user: Required[str]
    password: Required[str]
    database: Required[str]
    ssl: NotRequired[bool]
    pool_size: NotRequired[int]
    max_overflow: NotRequired[int]

# Agent types
AgentRole = Literal["coordinator", "executor", "validator", "monitor"]

class AgentConfig(TypedDict):
    """Agent configuration."""
    
    role: Required[AgentRole]
    name: Required[str]
    llm_config: Required[LLMConfig]
    max_retries: NotRequired[int]
    timeout: NotRequired[float]

# Text2SQL types
class SQLConfig(TypedDict):
    """Text2SQL configuration."""
    
    dialect: Required[Literal["mysql", "postgresql", "sqlite", "mssql"]]
    schema: Required[Dict[str, Any]]
    max_tokens: NotRequired[int]
    temperature: NotRequired[float]
    examples: NotRequired[List[Dict[str, str]]]

# Security types
class SecurityConfig(TypedDict):
    """Security configuration."""
    
    jwt_secret: Required[str]
    token_expiry: Required[int]
    rate_limit: NotRequired[int]
    cors_origins: NotRequired[List[str]]
    allowed_hosts: NotRequired[List[str]]

# Monitoring types
class MetricsConfig(TypedDict):
    """Metrics configuration."""
    
    enabled: Required[bool]
    host: Required[str]
    port: Required[int]
    path: NotRequired[str]
    labels: NotRequired[Dict[str, str]]

# Protocol definitions
class DataProvider(Protocol):
    """Protocol for data providers."""
    
    def get_data(self) -> Any:
        """Get data from the provider."""
        ...
    
    def validate_data(self, data: Any) -> bool:
        """Validate data from the provider."""
        ...

class Processor(Protocol[T]):
    """Protocol for data processors."""
    
    def process(self, data: T) -> T:
        """Process data."""
        ...
    
    def validate(self, data: T) -> TypeGuard[T]:
        """Validate processed data."""
        ...

# Type guards
def is_json(obj: Any) -> TypeGuard[JSON]:
    """Type guard for JSON objects."""
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return True
    if isinstance(obj, dict):
        return all(isinstance(k, str) and is_json(v) for k, v in obj.items())
    if isinstance(obj, list):
        return all(is_json(item) for item in obj)
    return False

def is_db_config(obj: Any) -> TypeGuard[DBConfig]:
    """Type guard for database configuration."""
    required_keys = {"host", "port", "user", "password", "database"}
    if not isinstance(obj, dict):
        return False
    return all(key in obj for key in required_keys)

def is_llm_config(obj: Any) -> TypeGuard[LLMConfig]:
    """Type guard for LLM configuration."""
    required_keys = {"provider", "model", "api_key"}
    if not isinstance(obj, dict):
        return False
    return all(key in obj for key in required_keys)
