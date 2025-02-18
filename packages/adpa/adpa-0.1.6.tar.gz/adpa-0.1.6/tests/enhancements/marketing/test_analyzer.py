"""Tests for Marketing Impact Analyzer."""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime
from adpa.enhancements.marketing import MarketingImpactAnalyzer, MarketingMetrics

@pytest.fixture
def sample_sales_data():
    """Create sample sales data for testing."""
    return pd.DataFrame({
        'location_id': ['01067', '01069', '01097'] * 4,
        'year': [2023, 2023, 2023, 2024, 2024, 2024] * 2,
        'kw': [41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42],
        'value': [1000, 1200, 800, 1100, 1300, 750, 1050, 1250, 820, 1150, 1350, 770],
        'percentage_change': [0, 0, 0, 10, 8.3, -6.25, 5, 4.2, 2.5, 9.5, 8, -6],
        'households': [1000, 1200, 800, 1000, 1200, 800, 1000, 1200, 800, 1000, 1200, 800],
        'market_id': [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]
    })

@pytest.fixture
def sample_campaign_data():
    """Create sample campaign data for testing."""
    return pd.DataFrame({
        'location_id': ['01067', '01069', '01097'] * 2,
        'kw': [41, 41, 41, 42, 42, 42],
        'budget': [1000, 1200, 800, 1050, 1250, 820],
        'ai': [10000, 12000, 8000, 10500, 12500, 8200],
        'engagements': [500, 600, 400, 525, 625, 410],
        'er': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
    })

@pytest.fixture
def mock_db_engine(mocker):
    """Create a mock database engine."""
    mock_engine = mocker.Mock()
    mock_engine.execute = mocker.Mock()
    return mock_engine

def test_analyzer_initialization(mock_db_engine):
    """Test analyzer initialization."""
    analyzer = MarketingImpactAnalyzer(mock_db_engine)
    assert analyzer.campaign_weeks == range(41, 53)
    assert analyzer.year == 2024

def test_correlation_analysis(mock_db_engine, sample_sales_data, sample_campaign_data, mocker):
    """Test correlation analysis functionality."""
    analyzer = MarketingImpactAnalyzer(mock_db_engine)
    
    # Mock data loading
    mocker.patch.object(
        analyzer,
        'load_data',
        return_value=(sample_sales_data, sample_campaign_data)
    )
    
    correlations = analyzer.analyze_correlations()
    
    assert 'ai_sales' in correlations
    assert 'engagement_sales' in correlations
    assert 'er_sales' in correlations
    assert all(isinstance(v, float) for v in correlations.values())

def test_performance_comparison(mock_db_engine, sample_sales_data, sample_campaign_data, mocker):
    """Test performance comparison functionality."""
    analyzer = MarketingImpactAnalyzer(mock_db_engine)
    
    # Mock data loading
    mocker.patch.object(
        analyzer,
        'load_data',
        return_value=(sample_sales_data, sample_campaign_data)
    )
    
    performance = analyzer.compare_performance()
    
    assert 'reinforced_growth' in performance
    assert 'normal_growth' in performance
    assert 'difference' in performance
    assert performance['difference'] == performance['reinforced_growth'] - performance['normal_growth']

def test_budget_threshold_analysis(mock_db_engine, sample_sales_data, sample_campaign_data, mocker):
    """Test budget threshold analysis."""
    analyzer = MarketingImpactAnalyzer(mock_db_engine)
    
    # Mock data loading
    mocker.patch.object(
        analyzer,
        'load_data',
        return_value=(sample_sales_data, sample_campaign_data)
    )
    
    threshold = analyzer.find_budget_threshold()
    assert isinstance(threshold, (float, type(None)))

def test_negative_performance_analysis(mock_db_engine, sample_sales_data, sample_campaign_data, mocker):
    """Test negative performance analysis."""
    analyzer = MarketingImpactAnalyzer(mock_db_engine)
    
    # Mock data loading
    mocker.patch.object(
        analyzer,
        'load_data',
        return_value=(sample_sales_data, sample_campaign_data)
    )
    
    analysis = analyzer.analyze_negative_performers()
    assert isinstance(analysis, pd.DataFrame)
    assert not analysis.empty
    assert all(col in analysis.columns for col in [
        'budget', 'percentage_change', 'households', 'market_id'
    ])

def test_report_generation(mock_db_engine, sample_sales_data, sample_campaign_data, mocker):
    """Test report generation."""
    analyzer = MarketingImpactAnalyzer(mock_db_engine)
    
    # Mock data loading and analysis methods
    mocker.patch.object(
        analyzer,
        'load_data',
        return_value=(sample_sales_data, sample_campaign_data)
    )
    
    report = analyzer.generate_report()
    assert isinstance(report, str)
    assert "Marketing Campaign Impact Metrics" in report
