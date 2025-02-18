"""Test attention components."""
import pytest
from datetime import datetime
from adpa.core.attention.focus import FocusManager, FocusMetrics

def test_should_create_focus_metrics():
    """Test creating focus metrics."""
    metrics = FocusMetrics(
        priority=0.8,
        relevance=0.9,
        urgency=0.7,
        complexity=0.5
    )
    assert metrics.priority == 0.8
    assert metrics.relevance == 0.9
    assert metrics.urgency == 0.7
    assert metrics.complexity == 0.5

def test_should_set_focus(focus_manager):
    """Test setting focus."""
    metrics = FocusMetrics(
        priority=0.8,
        relevance=0.9,
        urgency=0.7,
        complexity=0.5
    )
    target = {"task": "test_task"}
    
    focus_manager.set_focus(target, metrics)
    current_focus = focus_manager.get_current_focus()
    
    assert current_focus["target"] == target
    assert current_focus["metrics"] == metrics
    assert isinstance(current_focus["timestamp"], datetime)

def test_should_clear_focus(focus_manager):
    """Test clearing focus."""
    metrics = FocusMetrics(
        priority=0.8,
        relevance=0.9,
        urgency=0.7,
        complexity=0.5
    )
    target = {"task": "test_task"}
    
    focus_manager.set_focus(target, metrics)
    focus_manager.clear_focus()
    
    assert focus_manager.get_current_focus() is None

def test_should_maintain_focus_history(focus_manager):
    """Test focus history maintenance."""
    metrics1 = FocusMetrics(
        priority=0.8,
        relevance=0.9,
        urgency=0.7,
        complexity=0.5
    )
    metrics2 = FocusMetrics(
        priority=0.6,
        relevance=0.7,
        urgency=0.8,
        complexity=0.4
    )
    
    target1 = {"task": "task1"}
    target2 = {"task": "task2"}
    
    focus_manager.set_focus(target1, metrics1)
    focus_manager.set_focus(target2, metrics2)
    
    assert len(focus_manager.focus_history) == 2
    assert focus_manager.focus_history[0]["target"] == target1
    assert focus_manager.focus_history[1]["target"] == target2
