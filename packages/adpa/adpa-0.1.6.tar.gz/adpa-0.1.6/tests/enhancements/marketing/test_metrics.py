"""Tests for Marketing Metrics."""

import pytest
from adpa.enhancements.marketing import MarketingMetrics

@pytest.fixture
def sample_metrics():
    """Create sample metrics for testing."""
    return MarketingMetrics(
        correlation_ai_sales=0.75,
        correlation_engagement_sales=0.65,
        correlation_er_sales=0.45,
        reinforced_vs_normal_growth=5.5,
        reinforced_performance=2.5,
        normal_performance=-3.0,
        budget_threshold=1000.0,
        budget_effectiveness=0.0055,
        campaign_reach=85.5,
        campaign_engagement=4.5,
        campaign_conversion=2.2
    )

def test_metrics_initialization(sample_metrics):
    """Test metrics initialization."""
    assert sample_metrics.correlation_ai_sales == 0.75
    assert sample_metrics.correlation_engagement_sales == 0.65
    assert sample_metrics.correlation_er_sales == 0.45
    assert sample_metrics.reinforced_vs_normal_growth == 5.5
    assert sample_metrics.budget_threshold == 1000.0

def test_metrics_to_dict(sample_metrics):
    """Test conversion to dictionary."""
    metrics_dict = sample_metrics.to_dict()
    
    assert isinstance(metrics_dict, dict)
    assert 'correlations' in metrics_dict
    assert 'performance' in metrics_dict
    assert 'budget' in metrics_dict
    assert 'campaign' in metrics_dict
    
    assert metrics_dict['correlations']['ai_sales'] == 0.75
    assert metrics_dict['performance']['reinforced_vs_normal'] == 5.5
    assert metrics_dict['budget']['threshold'] == 1000.0
    assert metrics_dict['campaign']['reach'] == 85.5

def test_metrics_summary(sample_metrics):
    """Test summary generation."""
    summary = sample_metrics.get_summary()
    
    assert isinstance(summary, str)
    assert "Marketing Campaign Impact Metrics" in summary
    assert "Correlation Analysis" in summary
    assert "Performance Comparison" in summary
    assert "Budget Analysis" in summary
    assert "Campaign Metrics" in summary
    
    # Check specific values
    assert "0.750" in summary  # ai_sales correlation
    assert "5.50%" in summary  # reinforced vs normal growth
    assert "1000.0" in summary  # budget threshold
    assert "85.50%" in summary  # campaign reach
