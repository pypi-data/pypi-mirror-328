"""Integration tests for Streamlit app functionality."""

import pytest
import streamlit as st
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from typing import Dict, Any, List
import os
import json

from streamlit_app.Home import main as home_main
from streamlit_app.pages.team_management import main as team_main
from streamlit_app.pages.agent_management import main as agent_main
from streamlit_app.pages.execute import main as execute_main

from adpa.teams.base import BaseTeam
from adpa.agents.base import BaseAgent
from adpa.agents.config import AgentConfig

# Test data
TEST_MESSAGES = [
    "How do I implement a neural network?",
    "What are the best practices for code review?",
    "Can you help debug this error?"
]

TEST_CONFIG = {
    "name": "test_agent",
    "description": "Test agent",
    "capabilities": ["test"],
    "model_name": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2000
}

@pytest.fixture
def mock_streamlit():
    """Mock streamlit functionality."""
    with patch('streamlit.set_page_config'):
        with patch('streamlit.title'):
            with patch('streamlit.sidebar'):
                yield

@pytest.fixture
def mock_session_state():
    """Mock streamlit session state."""
    state = {
        "teams": {},
        "custom_teams": {},
        "agents": {},
        "settings": MagicMock(),
        "chat_history": {},
        "selected_id": None,
        "execution_mode": "team"
    }
    with patch('streamlit.session_state', state):
        yield state

@pytest.fixture
def mock_team():
    """Create a mock team."""
    team = Mock(spec=BaseTeam)
    team.name = "test_team"
    team.process = AsyncMock(return_value="Team response")
    team.get_capabilities = Mock(return_value=["capability1", "capability2"])
    return team

@pytest.fixture
def mock_agent():
    """Create a mock agent."""
    agent = Mock(spec=BaseAgent)
    agent.name = "test_agent"
    agent.process = AsyncMock(return_value="Agent response")
    agent.get_capabilities = Mock(return_value=["capability1", "capability2"])
    return agent

def test_home_page(mock_streamlit, mock_session_state):
    """Test home page."""
    with patch('streamlit.markdown'):
        home_main()

def test_team_management_page(mock_streamlit, mock_session_state, mock_team):
    """Test team management page."""
    # Mock form inputs
    with patch('streamlit.text_input', return_value="new_team"):
        with patch('streamlit.form'):
            with patch('streamlit.form_submit_button', return_value=True):
                mock_session_state["teams"]["test_team"] = mock_team
                team_main()

def test_agent_management_page(mock_streamlit, mock_session_state, mock_agent):
    """Test agent management page."""
    # Mock form inputs
    with patch('streamlit.text_input', return_value="new_agent"):
        with patch('streamlit.form'):
            with patch('streamlit.form_submit_button', return_value=True):
                mock_session_state["agents"]["test_agent"] = mock_agent
                agent_main()

def test_execute_page(mock_streamlit, mock_session_state, mock_team, mock_agent):
    """Test execute page."""
    # Set up session state
    mock_session_state["teams"]["test_team"] = mock_team
    mock_session_state["agents"]["test_agent"] = mock_agent
    
    # Mock chat input
    with patch('streamlit.chat_input', return_value="test message"):
        with patch('streamlit.chat_message'):
            execute_main()

def test_team_creation(mock_streamlit, mock_session_state):
    """Test team creation functionality."""
    with patch('streamlit.text_input', return_value="new_team"):
        with patch('streamlit.form'):
            with patch('streamlit.form_submit_button', return_value=True):
                team_main()
                assert "new_team" in mock_session_state["teams"]

def test_agent_creation(mock_streamlit, mock_session_state):
    """Test agent creation functionality."""
    with patch('streamlit.text_input', return_value="new_agent"):
        with patch('streamlit.form'):
            with patch('streamlit.form_submit_button', return_value=True):
                agent_main()
                assert "new_agent" in mock_session_state["agents"]

def test_chat_interface(mock_streamlit, mock_session_state, mock_team):
    """Test chat interface."""
    mock_session_state["teams"]["test_team"] = mock_team
    mock_session_state["selected_id"] = id(mock_team)
    mock_session_state["execution_mode"] = "team"
    
    # Mock chat interaction
    with patch('streamlit.chat_input', return_value="test message"):
        with patch('streamlit.chat_message'):
            execute_main()
            mock_team.process.assert_called_once_with("test message")

def test_error_handling(mock_streamlit, mock_session_state, mock_team):
    """Test error handling in UI."""
    mock_team.process = AsyncMock(side_effect=Exception("Test error"))
    mock_session_state["teams"]["test_team"] = mock_team
    
    with patch('streamlit.error') as mock_error:
        with patch('streamlit.chat_input', return_value="test message"):
            execute_main()
            mock_error.assert_called_once()

def test_session_state_management(mock_streamlit, mock_session_state):
    """Test session state management."""
    # Test initialization
    assert "teams" in mock_session_state
    assert "agents" in mock_session_state
    assert "chat_history" in mock_session_state
    
    # Test state updates
    mock_session_state["test_key"] = "test_value"
    assert mock_session_state["test_key"] == "test_value"

def test_ui_components(mock_streamlit, mock_session_state):
    """Test UI component rendering."""
    with patch('streamlit.columns') as mock_columns:
        with patch('streamlit.expander'):
            team_main()
            mock_columns.assert_called()

def test_file_handling(mock_streamlit, mock_session_state, tmp_path):
    """Test file upload and download."""
    test_file = tmp_path / "test.json"
    with open(test_file, 'w') as f:
        json.dump(TEST_CONFIG, f)
    
    # Mock file uploader
    with patch('streamlit.file_uploader', return_value=open(test_file, 'rb')):
        agent_main()

def test_settings_persistence(mock_streamlit, mock_session_state):
    """Test settings persistence."""
    # Update settings
    mock_session_state["settings"].update({"key": "value"})
    
    # Verify persistence
    assert mock_session_state["settings"].key == "value"

def test_concurrent_chat(mock_streamlit, mock_session_state, mock_team):
    """Test handling multiple chat messages."""
    mock_session_state["teams"]["test_team"] = mock_team
    
    # Simulate multiple messages
    for message in TEST_MESSAGES:
        with patch('streamlit.chat_input', return_value=message):
            with patch('streamlit.chat_message'):
                execute_main()
                mock_team.process.assert_called_with(message)
