"""Configuration for RAG testing UI components."""

from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, validator
from enum import Enum
import json
import os
from pathlib import Path

from adpa.utils.file_utils import ensure_dir, safe_file_write
from adpa.utils.logger import get_logger

# Setup logging
logger = get_logger(__name__)


class MetricType(str, Enum):
    """Types of metrics for RAG testing."""
    ACCURACY = "accuracy"
    RELEVANCE = "relevance"
    LATENCY = "latency"
    CONSISTENCY = "consistency"
    GROUNDEDNESS = "groundedness"
    CUSTOM = "custom"


class TestCase(BaseModel):
    """Test case configuration."""
    id: str = Field(..., description="Unique test case identifier")
    query: str = Field(..., description="Input query to test")
    expected_answer: str = Field(..., description="Expected answer or pattern")
    context_files: List[str] = Field(default_factory=list, description="List of context files to use")
    metrics: List[MetricType] = Field(
        default_factory=lambda: [MetricType.ACCURACY, MetricType.RELEVANCE],
        description="Metrics to evaluate"
    )
    metadata: Dict[str, Union[str, int, float, bool]] = Field(
        default_factory=dict,
        description="Additional metadata for the test case"
    )

    class Config:
        """Pydantic model configuration."""
        frozen = True
        json_encoders = {
            MetricType: lambda v: v.value
        }

    @validator("id")
    def validate_id(cls, v: str) -> str:
        """Validate test case ID format."""
        if not v.strip():
            raise ValueError("ID cannot be empty")
        return v.strip()

    @validator("query")
    def validate_query(cls, v: str) -> str:
        """Validate query is not empty."""
        if not v.strip():
            raise ValueError("Query cannot be empty")
        return v.strip()


class TestSuite(BaseModel):
    """Test suite configuration."""
    name: str = Field(..., description="Test suite name")
    description: str = Field(..., description="Test suite description")
    version: str = Field(..., description="Test suite version")
    test_cases: List[TestCase] = Field(..., description="List of test cases")
    config: Dict[str, Union[str, int, float, bool]] = Field(
        default_factory=dict,
        description="Suite-wide configuration"
    )

    class Config:
        """Pydantic model configuration."""
        frozen = True

    @validator("test_cases")
    def validate_test_cases(cls, v: List[TestCase]) -> List[TestCase]:
        """Validate test cases are unique."""
        ids = set()
        for case in v:
            if case.id in ids:
                raise ValueError(f"Duplicate test case ID: {case.id}")
            ids.add(case.id)
        return v


def load_test_suite(path: Union[str, Path]) -> TestSuite:
    """Load test suite from file.
    
    Args:
        path: Path to test suite JSON file
        
    Returns:
        TestSuite: Loaded test suite
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file content is invalid
    """
    try:
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Test suite file not found: {path}")
            
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        return TestSuite(**data)
    
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse test suite file: {str(e)}")
        raise ValueError(f"Invalid JSON in test suite file: {str(e)}")
    except Exception as e:
        logger.error(f"Failed to load test suite: {str(e)}")
        raise


def save_test_suite(suite: TestSuite, path: Union[str, Path]) -> None:
    """Save test suite to file.
    
    Args:
        suite: Test suite to save
        path: Path to save JSON file
        
    Raises:
        IOError: If file cannot be written
    """
    try:
        path = Path(path)
        ensure_dir(path)
        
        data = json.loads(suite.json(indent=2))
        safe_file_write(path, json.dumps(data, indent=2))
        
        logger.info(f"Test suite saved to {path}")
        
    except Exception as e:
        logger.error(f"Failed to save test suite: {str(e)}")
        raise


def get_default_config() -> Dict[str, Union[str, int, float, bool]]:
    """Get default RAG testing configuration.
    
    Returns:
        Dict containing default configuration values
    """
    return {
        "max_context_length": 2048,
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 256,
        "chunk_size": 512,
        "chunk_overlap": 128,
        "similarity_threshold": 0.8,
        "max_context_chunks": 5
    }
