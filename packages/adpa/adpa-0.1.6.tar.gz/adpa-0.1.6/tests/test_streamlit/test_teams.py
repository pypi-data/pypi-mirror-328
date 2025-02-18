"""Tests for the Teams page."""

import pytest
import streamlit as st
from streamlit_app.pages.Teams import init_teams, display_team_status, display_team_settings, main

def test_init_teams(mock_streamlit, mock_session_state):
    """Test teams initialization."""
    init_teams()
    assert "teams" in st.session_state
    assert len(st.session_state["teams"]) == 3

def test_display_team_status(mock_streamlit, mock_session_state):
    """Test team status display."""
    team = st.session_state["teams"]["research"]
    display_team_status("research", team)
    # No assertions needed as we're just verifying it runs without errors

def test_display_team_settings(mock_streamlit, mock_session_state):
    """Test team settings display."""
    team = st.session_state["teams"]["research"]
    display_team_settings("research", team)
    # No assertions needed as we're just verifying it runs without errors

def test_main(mock_streamlit, mock_session_state):
    """Test main function."""
    main()
    # Verify teams are initialized
    assert "teams" in st.session_state
    assert len(st.session_state["teams"]) == 3
