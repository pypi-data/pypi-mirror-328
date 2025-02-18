"""Tests for the Settings page."""

import pytest
import streamlit as st
from streamlit_app.pages.Settings import init_settings, display_api_settings, display_app_settings, display_team_settings, main

def test_init_settings(mock_streamlit, mock_session_state):
    """Test settings initialization."""
    init_settings()
    assert "settings" in st.session_state

def test_display_api_settings(mock_streamlit, mock_session_state):
    """Test API settings display."""
    display_api_settings()
    # No assertions needed as we're just verifying it runs without errors

def test_display_app_settings(mock_streamlit, mock_session_state):
    """Test app settings display."""
    display_app_settings()
    # No assertions needed as we're just verifying it runs without errors

def test_display_team_settings(mock_streamlit, mock_session_state):
    """Test team settings display."""
    display_team_settings()
    # No assertions needed as we're just verifying it runs without errors

def test_main(mock_streamlit, mock_session_state):
    """Test main function."""
    main()
    # Verify settings are initialized
    assert "settings" in st.session_state
