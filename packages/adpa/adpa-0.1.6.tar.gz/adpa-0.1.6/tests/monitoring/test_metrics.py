"""Test monitoring metrics."""
import pytest
from unittest.mock import patch
from adpa.monitoring.metrics import MetricsCollector

@pytest.fixture
def metrics_collector():
    """Create MetricsCollector instance."""
    return MetricsCollector()

def test_should_record_request(metrics_collector):
    """Test recording requests."""
    with patch('prometheus_client.Counter.inc') as mock_inc:
        metrics_collector.record_request()
        mock_inc.assert_called_once()

def test_should_record_error(metrics_collector):
    """Test recording errors."""
    with patch('prometheus_client.Counter.inc') as mock_inc:
        metrics_collector.record_error()
        mock_inc.assert_called_once()

def test_should_update_active_agents(metrics_collector):
    """Test updating active agents count."""
    with patch('prometheus_client.Gauge.set') as mock_set:
        metrics_collector.update_active_agents(5)
        mock_set.assert_called_once_with(5)

def test_should_update_queue_size(metrics_collector):
    """Test updating queue size."""
    with patch('prometheus_client.Gauge.set') as mock_set:
        metrics_collector.update_queue_size(10)
        mock_set.assert_called_once_with(10)

def test_should_record_processing_time(metrics_collector):
    """Test recording processing time."""
    with patch('prometheus_client.Histogram.observe') as mock_observe:
        metrics_collector.record_processing_time(0.5)
        mock_observe.assert_called_once_with(0.5)

def test_should_handle_multiple_metrics(metrics_collector):
    """Test handling multiple metrics simultaneously."""
    with patch('prometheus_client.Counter.inc') as mock_inc, \
         patch('prometheus_client.Gauge.set') as mock_set, \
         patch('prometheus_client.Histogram.observe') as mock_observe:
        
        # Record multiple metrics
        metrics_collector.record_request()
        metrics_collector.record_error()
        metrics_collector.update_active_agents(5)
        metrics_collector.update_queue_size(10)
        metrics_collector.record_processing_time(0.5)
        
        assert mock_inc.call_count == 2
        assert mock_set.call_count == 2
        assert mock_observe.call_count == 1
