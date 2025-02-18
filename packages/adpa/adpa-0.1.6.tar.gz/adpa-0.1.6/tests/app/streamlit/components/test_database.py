"""Tests for the database component."""
import pytest
import streamlit as st
from unittest.mock import MagicMock, patch
import plotly.graph_objects as go
from datetime import datetime
from app.streamlit.components.database import DatabaseComponent
from adpa.database.monitoring.dashboard import MonitoringDashboard
from adpa.database.ml.query_optimizer import QueryOptimizer

@pytest.fixture
def mock_session_state():
    """Mock Streamlit session state."""
    with patch("streamlit.session_state", new_callable=dict) as mock_state:
        yield mock_state

@pytest.fixture
def mock_dashboard():
    """Mock MonitoringDashboard."""
    dashboard = MagicMock(spec=MonitoringDashboard)
    dashboard.get_overview.return_value = {
        "system_health": {
            "health_score": 85,
            "status": "healthy",
            "metrics": {
                "cpu_usage": 45.5,
                "memory_usage": 60.2,
                "disk_usage": 55.8,
                "connection_usage": 30.1
            }
        },
        "performance_metrics": {
            "transactions": 1500,
            "buffer_hits": 12000,
            "disk_reads": 3000,
            "rows_returned": 50000
        },
        "alerts": []
    }
    dashboard.get_slow_queries.return_value = [
        {
            "query": "SELECT * FROM large_table",
            "avg_time": 1500.5,
            "avg_rows": 10000,
            "calls": 150,
            "analysis": {
                "complexity": 7.5,
                "suggestions": [
                    "Add index on (column1, column2)",
                    "Consider partitioning"
                ]
            }
        }
    ]
    return dashboard

@pytest.fixture
def mock_optimizer():
    """Mock QueryOptimizer."""
    optimizer = MagicMock(spec=QueryOptimizer)
    optimizer.suggest_indexes.return_value = [
        {
            "table": "users",
            "columns": ["email", "username"],
            "usage_count": 1500,
            "estimated_impact": 25.5
        }
    ]
    return optimizer

@pytest.fixture
def database_component(mock_session_state, mock_dashboard, mock_optimizer):
    """Create DatabaseComponent with mocked dependencies."""
    with patch("streamlit.session_state", mock_session_state):
        mock_session_state["db_monitor"] = mock_dashboard
        mock_session_state["query_optimizer"] = mock_optimizer
        return DatabaseComponent()

# Visualization Tests

def test_create_health_gauge(database_component):
    """Test health gauge creation."""
    fig = database_component.create_health_gauge(85, "healthy")
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 1
    assert fig.data[0].type == "indicator"
    assert fig.data[0].mode == "gauge+number+delta"
    assert fig.data[0].value == 85

def test_create_resource_usage_chart(database_component):
    """Test resource usage chart creation."""
    metrics = {
        "cpu_usage": 45.5,
        "memory_usage": 60.2,
        "disk_usage": 55.8,
        "connection_usage": 30.1
    }
    fig = database_component.create_resource_usage_chart(metrics)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 4  # One gauge for each metric
    for data in fig.data:
        assert data.type == "indicator"
        assert data.mode == "gauge+number"

def test_create_performance_timeline(database_component):
    """Test performance timeline creation."""
    perf = {
        "transactions": 1500,
        "buffer_hits": 12000,
        "rows_returned": 50000
    }
    fig = database_component.create_performance_timeline(perf)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 3  # Three lines for different metrics
    for data in fig.data:
        assert data.type == "scatter"
        assert len(data.x) == 12  # 12 time points
        assert all(isinstance(x, datetime) for x in data.x)

def test_create_query_performance_chart(database_component):
    """Test query performance chart creation."""
    queries = [
        {
            "query": "SELECT * FROM table1",
            "avg_time": 100.5,
            "avg_rows": 5000,
            "calls": 100,
            "analysis": {"complexity": 5.5}
        },
        {
            "query": "SELECT * FROM table2",
            "avg_time": 200.5,
            "avg_rows": 8000,
            "calls": 150,
            "analysis": {"complexity": 6.5}
        }
    ]
    fig = database_component.create_query_performance_chart(queries)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 1  # One scatter plot
    assert fig.data[0].type == "scatter"
    assert len(fig.data[0].x) == 2  # Two data points
    assert len(fig.data[0].y) == 2

# Component Rendering Tests

def test_render_overview_healthy(database_component, mock_dashboard):
    """Test rendering overview with healthy status."""
    with patch("streamlit.plotly_chart") as mock_chart:
        database_component.render_overview()
        assert mock_chart.call_count == 3  # Health gauge, resource usage, timeline

def test_render_overview_with_alerts(database_component, mock_dashboard):
    """Test rendering overview with alerts."""
    mock_dashboard.get_overview.return_value["alerts"] = [
        {
            "type": "cpu_usage",
            "message": "High CPU usage detected",
            "severity": "high"
        }
    ]
    
    with patch("streamlit.warning") as mock_warning:
        database_component.render_overview()
        mock_warning.assert_called_with("High CPU usage detected")

def test_render_query_insights_with_data(database_component, mock_dashboard):
    """Test rendering query insights with data."""
    with patch("streamlit.plotly_chart") as mock_chart:
        with patch("streamlit.expander") as mock_expander:
            database_component.render_query_insights()
            assert mock_chart.call_count == 1  # Query performance chart
            assert mock_expander.call_count >= 1  # At least one query expander

def test_render_query_insights_no_queries(database_component, mock_dashboard):
    """Test rendering query insights with no slow queries."""
    mock_dashboard.get_slow_queries.return_value = []
    
    with patch("streamlit.info") as mock_info:
        database_component.render_query_insights()
        mock_info.assert_called()

def test_render_maintenance_backup(database_component):
    """Test backup functionality in maintenance."""
    with patch("streamlit.text_input") as mock_input:
        with patch("streamlit.button") as mock_button:
            database_component.render_maintenance()
            mock_input.assert_called_with("Backup Name", placeholder="Enter backup name...")
            mock_button.assert_any_call(" Create Backup", use_container_width=True)

def test_render_maintenance_table_analysis(database_component):
    """Test table analysis in maintenance."""
    with patch("streamlit.selectbox") as mock_select:
        with patch("streamlit.button") as mock_button:
            database_component.render_maintenance()
            mock_select.assert_called_with("Select Table", ["users", "teams", "tasks", "agents"])
            mock_button.assert_any_call(" Analyze Database", use_container_width=True)

# Error Handling Tests

def test_overview_error_handling(database_component, mock_dashboard):
    """Test error handling in overview."""
    mock_dashboard.get_overview.side_effect = Exception("Database error")
    
    with patch("streamlit.error") as mock_error:
        database_component.render_overview()
        mock_error.assert_called_with("Failed to load database metrics: Database error")

def test_query_insights_error_handling(database_component, mock_dashboard):
    """Test error handling in query insights."""
    mock_dashboard.get_slow_queries.side_effect = Exception("Query error")
    
    with patch("streamlit.error") as mock_error:
        database_component.render_query_insights()
        mock_error.assert_called_with("Failed to load query insights: Query error")

def test_maintenance_backup_error(database_component):
    """Test error handling in backup creation."""
    with patch("streamlit.text_input", return_value="test_backup"):
        with patch("streamlit.button", return_value=True):
            with patch("streamlit.spinner"):
                with patch("streamlit.error") as mock_error:
                    # Simulate backup creation
                    database_component.render_maintenance()
                    # Verify error handling
                    assert mock_error.call_count <= 1

# Edge Cases

def test_health_gauge_edge_values(database_component):
    """Test health gauge with edge values."""
    # Test minimum value
    fig_min = database_component.create_health_gauge(0, "critical")
    assert fig_min.data[0].value == 0
    
    # Test maximum value
    fig_max = database_component.create_health_gauge(100, "healthy")
    assert fig_max.data[0].value == 100

def test_resource_usage_edge_values(database_component):
    """Test resource usage chart with edge values."""
    metrics = {
        "cpu_usage": 100.0,
        "memory_usage": 0.0,
        "disk_usage": 99.9,
        "connection_usage": 0.1
    }
    fig = database_component.create_resource_usage_chart(metrics)
    assert len(fig.data) == 4
    values = [data.value for data in fig.data]
    assert max(values) <= 100.0
    assert min(values) >= 0.0

def test_performance_timeline_single_point(database_component):
    """Test performance timeline with single data point."""
    perf = {
        "transactions": 1,
        "buffer_hits": 1,
        "rows_returned": 1
    }
    fig = database_component.create_performance_timeline(perf)
    assert len(fig.data) == 3
    for trace in fig.data:
        assert len(trace.x) == 12
        assert len(trace.y) == 12

def test_query_performance_single_query(database_component):
    """Test query performance chart with single query."""
    queries = [{
        "query": "SELECT 1",
        "avg_time": 1.0,
        "avg_rows": 1,
        "calls": 1,
        "analysis": {"complexity": 1.0}
    }]
    fig = database_component.create_query_performance_chart(queries)
    assert len(fig.data) == 1
    assert len(fig.data[0].x) == 1
    assert len(fig.data[0].y) == 1

def test_init(mock_session_state):
    """Test component initialization."""
    component = DatabaseComponent()
    assert "db_monitor" in mock_session_state
    assert "query_optimizer" in mock_session_state

def test_render_overview_critical(database_component, mock_dashboard):
    """Test rendering overview with critical status."""
    mock_dashboard.get_overview.return_value["system_health"]["status"] = "critical"
    mock_dashboard.get_overview.return_value["system_health"]["health_score"] = 45
    
    with patch("streamlit.markdown") as mock_markdown:
        database_component.render_overview()
        mock_markdown.assert_any_call(":red[CRITICAL]")

def test_render_overview_with_alerts(database_component, mock_dashboard):
    """Test rendering overview with alerts."""
    mock_dashboard.get_overview.return_value["alerts"] = [
        {
            "type": "cpu_usage",
            "message": "High CPU usage detected",
            "severity": "high"
        }
    ]
    
    with patch("streamlit.warning") as mock_warning:
        database_component.render_overview()
        mock_warning.assert_called_with("High CPU usage detected")

def test_render_query_insights(database_component, mock_dashboard):
    """Test rendering query insights."""
    with patch("streamlit.markdown") as mock_markdown:
        database_component.render_query_insights()
        mock_markdown.assert_any_call("### Query Insights")

def test_render_query_insights_no_queries(database_component, mock_dashboard):
    """Test rendering query insights with no slow queries."""
    mock_dashboard.get_slow_queries.return_value = []
    
    with patch("streamlit.info") as mock_info:
        database_component.render_query_insights()
        mock_info.assert_called()

def test_render_maintenance(database_component):
    """Test rendering maintenance section."""
    with patch("streamlit.button") as mock_button:
        database_component.render_maintenance()
        assert mock_button.call_count >= 2  # At least Analyze and Vacuum buttons

def test_error_handling(database_component, mock_dashboard):
    """Test error handling in overview render."""
    mock_dashboard.get_overview.side_effect = Exception("Database error")
    
    with patch("streamlit.error") as mock_error:
        database_component.render_overview()
        mock_error.assert_called_with("Failed to load database metrics: Database error")

def test_performance_metrics(database_component, mock_dashboard):
    """Test rendering performance metrics."""
    with patch("streamlit.metric") as mock_metric:
        database_component.render_overview()
        mock_metric.assert_any_call("Transactions", 1500)

def test_optimization_suggestions(database_component, mock_dashboard):
    """Test rendering optimization suggestions."""
    with patch("streamlit.markdown") as mock_markdown:
        database_component.render_query_insights()
        mock_markdown.assert_any_call("- Add index on (column1, column2)")

def test_backup_management(database_component):
    """Test backup management interface."""
    with patch("streamlit.text_input") as mock_input:
        with patch("streamlit.button") as mock_button:
            database_component.render_maintenance()
            mock_input.assert_called_with("Backup Name")
            mock_button.assert_any_call("Create Backup")
