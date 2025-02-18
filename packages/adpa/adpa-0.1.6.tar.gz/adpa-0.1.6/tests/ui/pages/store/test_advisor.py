"""Tests for store advisor UI."""

import pytest
from unittest.mock import Mock, patch
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from adpa.ui.pages.store.advisor import StoreAdvisorUI
from adpa.ui.utils.state import UIState
from adpa.knowledge.store_advisor import (
    StoreAdvisor,
    UseCase,
    DataSize,
    UpdateFrequency,
    QueryLatency,
    Deployment,
    Budget,
    StoreRecommendation
)

@pytest.fixture
def app():
    """Create a test instance of StoreAdvisorUI."""
    return StoreAdvisorUI()

@pytest.fixture
def mock_recommendation():
    """Create a mock store recommendation."""
    return StoreRecommendation(
        store_type="chroma",
        embedding_type="openai",
        confidence=0.85,
        explanation="Test explanation",
        configuration={"key": "value"},
        estimated_cost="$100/month",
        pros=["Fast", "Easy to use"],
        cons=["Limited scaling"]
    )

def test_setup_session_state(app):
    """Test session state initialization."""
    app.setup_session_state()
    assert 'recommendations' in st.session_state
    assert st.session_state.recommendations == []

def test_plot_radar_comparison(app, mock_recommendation):
    """Test radar chart generation."""
    fig = app.plot_radar_comparison([mock_recommendation])
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 1
    assert fig.data[0].name == "chroma"

def test_plot_performance_comparison(app, mock_recommendation):
    """Test performance comparison chart generation."""
    fig = app.plot_performance_comparison([mock_recommendation])
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 3  # Three metrics
    assert "Query Latency" in fig.data[0].name

@patch('streamlit.form')
@patch('streamlit.selectbox')
@patch('streamlit.checkbox')
def test_render_advisor_tab(mock_checkbox, mock_selectbox, mock_form, app):
    """Test advisor tab rendering."""
    # Setup mocks
    mock_selectbox.side_effect = [
        "small", "low", "high", "cloud", "low"
    ]
    mock_checkbox.return_value = False
    mock_form.return_value.__enter__.return_value = None
    
    # Create mock advisor
    mock_advisor = Mock()
    mock_advisor.get_recommendations.return_value = [Mock()]
    app.advisor = mock_advisor
    
    # Render tab
    app.render_advisor_tab()
    
    # Verify form elements were created
    assert mock_selectbox.call_count == 5
    assert mock_checkbox.call_count == 3

@patch('streamlit.plotly_chart')
@patch('streamlit.dataframe')
def test_render_comparison_tab(mock_dataframe, mock_plotly, app, mock_recommendation):
    """Test comparison tab rendering."""
    # Setup recommendations
    st.session_state.recommendations = [mock_recommendation]
    
    # Render tab
    app.render_comparison_tab()
    
    # Verify charts were created
    assert mock_plotly.call_count == 2
    assert mock_dataframe.called

@patch('streamlit.download_button')
def test_render_export_tab(mock_download, app, mock_recommendation):
    """Test export tab rendering."""
    # Setup recommendations
    st.session_state.recommendations = [mock_recommendation]
    
    # Render tab
    app.render_export_tab()
    
    # Verify download button was created
    assert mock_download.called

@patch('streamlit.plotly_chart')
@patch('streamlit.dataframe')
def test_render_benchmarks_tab(mock_dataframe, mock_plotly, app):
    """Test benchmarks tab rendering."""
    # Render tab
    app.render_benchmarks_tab()
    
    # Verify benchmark data was displayed
    assert mock_dataframe.called
    assert mock_plotly.called

@patch('streamlit.tabs')
def test_render(mock_tabs, app):
    """Test main UI rendering."""
    # Setup mock tabs
    mock_tabs.return_value = [Mock(), Mock(), Mock(), Mock()]
    
    # Render UI
    app.render()
    
    # Verify tabs were created
    assert mock_tabs.called
    assert len(mock_tabs.return_value) == 4
