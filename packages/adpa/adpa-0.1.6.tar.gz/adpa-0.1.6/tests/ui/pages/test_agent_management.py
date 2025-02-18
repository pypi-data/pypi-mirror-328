"""Tests for Agent Management page."""
import pytest
from unittest.mock import MagicMock, patch

import streamlit as st
from config.models import AgentStatus, LLMConfig

from examples.streamlit.pages.1_Agent_Management import (
    count_agents_by_provider,
    display_agent_metrics,
    stop_running_agent,
)


@pytest.fixture
def mock_session_state():
    """Fixture for mocked session state."""
    with patch("streamlit.session_state") as mock_state:
        mock_state.agents = []
        mock_state.current_agent = None
        yield mock_state


@pytest.fixture
def sample_agent():
    """Fixture for sample agent data."""
    return {
        "name": "test_agent",
        "description": "Test agent",
        "llm_config": LLMConfig(
            primary_provider="OpenAI",
            model="gpt-4",
            api_key="test-key"
        ),
        "status": AgentStatus.READY
    }


def test_count_agents_by_provider(mock_session_state, sample_agent):
    """Test counting agents by provider."""
    # Test with no agents
    assert count_agents_by_provider("OpenAI") == 0

    # Test with one agent
    mock_session_state.agents.append(sample_agent)
    assert count_agents_by_provider("OpenAI") == 1
    assert count_agents_by_provider("Anthropic") == 0

    # Test with multiple agents
    mock_session_state.agents.append({
        **sample_agent,
        "name": "test_agent_2",
        "llm_config": LLMConfig(
            primary_provider="Anthropic",
            model="claude-2",
            api_key="test-key"
        )
    })
    assert count_agents_by_provider("OpenAI") == 1
    assert count_agents_by_provider("Anthropic") == 1
    assert count_agents_by_provider("Gemini") == 0


def test_stop_running_agent(mock_session_state, sample_agent):
    """Test stopping a running agent."""
    with patch("streamlit.success") as mock_success, \
         patch("streamlit.warning") as mock_warning, \
         patch("streamlit.error") as mock_error:

        # Test with non-existent agent
        stop_running_agent("non_existent")
        mock_warning.assert_called_once_with("Agent not found")

        # Test with existing agent
        running_agent = {**sample_agent, "status": AgentStatus.RUNNING}
        mock_session_state.agents.append(running_agent)
        stop_running_agent("test_agent")
        assert running_agent["status"] == AgentStatus.STOPPED
        mock_success.assert_called_once_with("Agent stopped successfully")

        # Test with invalid agent data
        invalid_agent = {"name": "invalid_agent"}  # Missing required fields
        mock_session_state.agents.append(invalid_agent)
        stop_running_agent("invalid_agent")
        mock_error.assert_called_once()


def test_display_agent_metrics(mock_session_state, sample_agent):
    """Test displaying agent metrics."""
    with patch("streamlit.plotly_chart") as mock_chart, \
         patch("streamlit.info") as mock_info:

        # Test with no agents
        display_agent_metrics()
        mock_info.assert_called_once_with("No agents available")

        # Test with agents
        mock_session_state.agents = [
            {**sample_agent},
            {
                **sample_agent,
                "name": "test_agent_2",
                "llm_config": LLMConfig(
                    primary_provider="Anthropic",
                    model="claude-2",
                    api_key="test-key"
                )
            }
        ]
        display_agent_metrics()
        mock_chart.assert_called_once()


def test_display_agent_metrics_error(mock_session_state):
    """Test error handling in display_agent_metrics."""
    with patch("streamlit.error") as mock_error:
        # Simulate error by setting agents to None
        mock_session_state.agents = None
        display_agent_metrics()
        mock_error.assert_called_once()


def test_display_agent_metrics_invalid_data(mock_session_state, sample_agent):
    """Test handling invalid data in display_agent_metrics."""
    with patch("streamlit.error") as mock_error:
        # Add agent with invalid provider
        invalid_agent = {**sample_agent}
        invalid_agent["llm_config"].primary_provider = "InvalidProvider"
        mock_session_state.agents.append(invalid_agent)
        display_agent_metrics()
        mock_error.assert_called_once()
