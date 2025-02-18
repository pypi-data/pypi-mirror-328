"""
Core ADPA Framework implementation.

This module provides the core ADPA (Attention, Desire, Position, Action) framework
implementation for analyzing and processing content.
"""
from typing import Dict, Any, Optional, List, Type
from datetime import datetime
from pydantic import BaseModel, Field, validator

from adpa.core.types import (
    AttentionScore,
    DesireScore,
    PositionScore,
    ActionScore,
    SentimentScore,
    ContentType,
    AnalysisOptions
)
from adpa.core.state import State
from adpa.core.events import EventEmitter
from adpa.core.workflow import Workflow
from adpa.core.processor import Processor

class ADPAResult(BaseModel):
    """Result model for ADPA analysis."""
    
    attention_score: AttentionScore = Field(
        ...,
        description="Attention score indicating content visibility and engagement"
    )
    desire_score: DesireScore = Field(
        ...,
        description="Desire score indicating content appeal and motivation"
    )
    position_score: PositionScore = Field(
        ...,
        description="Position score indicating content placement and context"
    )
    action_score: ActionScore = Field(
        ...,
        description="Action score indicating content effectiveness and conversion potential"
    )
    sentiment_score: SentimentScore = Field(
        ...,
        description="Sentiment score indicating content emotional impact"
    )
    recommendations: Dict[str, List[str]] = Field(
        ...,
        description="Improvement recommendations for each aspect"
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="Analysis timestamp"
    )
    
    @validator("recommendations")
    def validate_recommendations(cls, v: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """Validate recommendations structure."""
        required_keys = {"attention", "desire", "position", "action", "sentiment"}
        if not all(key in v for key in required_keys):
            raise ValueError(f"Missing required recommendation categories: {required_keys - v.keys()}")
        return v

class ADPAFramework:
    """Core ADPA Framework class."""
    
    def __init__(
        self,
        state: Optional[State] = None,
        workflow: Optional[Workflow] = None,
        processor: Optional[Processor] = None
    ):
        """Initialize ADPA Framework.
        
        Args:
            state: Optional state manager
            workflow: Optional workflow manager
            processor: Optional content processor
        """
        self.state = state or State()
        self.workflow = workflow or Workflow()
        self.processor = processor or Processor()
        self.events = EventEmitter()
        
    def analyze(
        self,
        content: Dict[str, Any],
        content_type: ContentType,
        options: Optional[AnalysisOptions] = None
    ) -> ADPAResult:
        """Analyze content using ADPA Framework.
        
        Args:
            content: Content to analyze
            content_type: Type of content being analyzed
            options: Optional analysis parameters
            
        Returns:
            ADPAResult with scores and recommendations
            
        Raises:
            ValueError: If content is invalid
            ProcessingError: If analysis fails
        """
        # Validate and preprocess content
        self.processor.validate_content(content, content_type)
        processed_content = self.processor.preprocess(content, content_type)
        
        # Initialize analysis state
        self.state.start_analysis(content_type)
        
        try:
            # Run analysis workflow
            attention = self.workflow.analyze_attention(processed_content, options)
            desire = self.workflow.analyze_desire(processed_content, options)
            position = self.workflow.analyze_position(processed_content, options)
            action = self.workflow.analyze_action(processed_content, options)
            sentiment = self.workflow.analyze_sentiment(processed_content, options)
            
            # Create result
            result = ADPAResult(
                attention_score=attention["score"],
                desire_score=desire["score"],
                position_score=position["score"],
                action_score=action["score"],
                sentiment_score=sentiment["score"],
                recommendations={
                    "attention": attention["recommendations"],
                    "desire": desire["recommendations"],
                    "position": position["recommendations"],
                    "action": action["recommendations"],
                    "sentiment": sentiment["recommendations"]
                }
            )
            
            # Emit analysis complete event
            self.events.emit("analysis_complete", result)
            
            return result
            
        finally:
            # Clean up analysis state
            self.state.end_analysis()
    
    def register_plugin(self, plugin_type: str, plugin: Any) -> None:
        """Register a plugin with the framework.
        
        Args:
            plugin_type: Type of plugin (e.g., "attention", "desire")
            plugin: Plugin instance to register
        """
        self.workflow.register_plugin(plugin_type, plugin)
    
    def configure(self, config: Dict[str, Any]) -> None:
        """Configure the framework.
        
        Args:
            config: Configuration dictionary
        """
        self.state.update_config(config)
        self.workflow.configure(config)
        self.processor.configure(config)
