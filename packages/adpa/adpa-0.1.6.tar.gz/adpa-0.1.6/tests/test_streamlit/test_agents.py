"""Tests for the Agents page."""

import pytest
import streamlit as st
from streamlit_app.pages.Agents import init_agents, display_agent_status, display_agent_settings, main

def test_init_agents(mock_streamlit, mock_session_state):
    """Test agents initialization."""
    init_agents()
    assert "agents" in st.session_state
    assert len(st.session_state["agents"]) == 3

def test_display_agent_status(mock_streamlit, mock_session_state):
    """Test agent status display."""
    agent = st.session_state["agents"]["research"]
    display_agent_status("research", agent)
    # No assertions needed as we're just verifying it runs without errors

def test_display_agent_settings(mock_streamlit, mock_session_state):
    """Test agent settings display."""
    agent = st.session_state["agents"]["research"]
    display_agent_settings("research", agent)
    # No assertions needed as we're just verifying it runs without errors

def test_main(mock_streamlit, mock_session_state):
    """Test main function."""
    main()
    # Verify agents are initialized
    assert "agents" in st.session_state
    assert len(st.session_state["agents"]) == 3
