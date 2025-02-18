"""Test desire components."""
import pytest
from datetime import datetime, timedelta
from adpa.core.desire.goals import Goal, GoalManager

def test_should_create_goal():
    """Test goal creation with all fields."""
    deadline = datetime.utcnow() + timedelta(days=1)
    goal = Goal(
        id="test_goal_1",
        description="Test goal",
        priority=0.8,
        deadline=deadline,
        dependencies=["goal_2", "goal_3"],
        metadata={"owner": "test_user"}
    )
    
    assert goal.id == "test_goal_1"
    assert goal.description == "Test goal"
    assert goal.priority == 0.8
    assert goal.deadline == deadline
    assert goal.dependencies == ["goal_2", "goal_3"]
    assert goal.status == "pending"
    assert goal.metadata == {"owner": "test_user"}

def test_should_manage_goals(goal_manager):
    """Test goal management operations."""
    goal = Goal(
        id="test_goal_1",
        description="Test goal",
        priority=0.8
    )
    
    # Add goal
    goal_manager.add_goal(goal)
    assert len(goal_manager.goals) == 1
    assert goal_manager.goals["test_goal_1"] == goal
    
    # Update goal status
    goal_manager.update_goal("test_goal_1", "completed")
    assert goal_manager.goals["test_goal_1"].status == "completed"
    
    # Get active goals
    active_goals = goal_manager.get_active_goals()
    assert len(active_goals) == 0

def test_should_handle_multiple_goals(goal_manager):
    """Test handling multiple goals."""
    goals = [
        Goal(id=f"goal_{i}", 
             description=f"Goal {i}", 
             priority=0.5 + i/10) 
        for i in range(3)
    ]
    
    for goal in goals:
        goal_manager.add_goal(goal)
    
    assert len(goal_manager.goals) == 3
    assert len(goal_manager.get_active_goals()) == 3
    
    # Update some goals
    goal_manager.update_goal("goal_0", "completed")
    goal_manager.update_goal("goal_1", "failed")
    
    active_goals = goal_manager.get_active_goals()
    assert len(active_goals) == 1
    assert active_goals[0].id == "goal_2"

def test_should_handle_goal_dependencies(goal_manager):
    """Test goal dependency handling."""
    parent_goal = Goal(
        id="parent_goal",
        description="Parent goal",
        priority=0.9
    )
    
    child_goal = Goal(
        id="child_goal",
        description="Child goal",
        priority=0.8,
        dependencies=["parent_goal"]
    )
    
    goal_manager.add_goal(parent_goal)
    goal_manager.add_goal(child_goal)
    
    assert len(goal_manager.get_active_goals()) == 2
    
    # Complete parent goal
    goal_manager.update_goal("parent_goal", "completed")
    active_goals = goal_manager.get_active_goals()
    assert len(active_goals) == 1
    assert active_goals[0].id == "child_goal"
