"""Type definitions for monitoring module."""
from typing import Dict, Any, List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime


class MetricValue(BaseModel):
    """Single metric value."""
    
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Time when metric was recorded"
    )
    name: str = Field(
        ...,
        description="Metric name"
    )
    value: float = Field(
        ...,
        description="Metric value"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metric metadata"
    )


class MetricSummary(BaseModel):
    """Summary statistics for a metric."""
    
    mean: float = Field(
        ...,
        description="Mean value"
    )
    std: float = Field(
        ...,
        description="Standard deviation"
    )
    min: float = Field(
        ...,
        description="Minimum value"
    )
    max: float = Field(
        ...,
        description="Maximum value"
    )
    last: float = Field(
        ...,
        description="Most recent value"
    )


class Alert(BaseModel):
    """Alert model."""
    
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Time when alert was triggered"
    )
    category: str = Field(
        ...,
        description="Alert category"
    )
    name: str = Field(
        ...,
        description="Alert name"
    )
    value: float = Field(
        ...,
        description="Value that triggered alert"
    )
    threshold: float = Field(
        ...,
        description="Alert threshold"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional alert metadata"
    )


class AlertConfig(BaseModel):
    """Alert configuration."""
    
    thresholds: Dict[str, float] = Field(
        default_factory=dict,
        description="Alert thresholds by metric name"
    )
    channels: List[str] = Field(
        default_factory=list,
        description="Alert channels to use"
    )
    templates: Dict[str, str] = Field(
        default_factory=dict,
        description="Alert message templates"
    )
