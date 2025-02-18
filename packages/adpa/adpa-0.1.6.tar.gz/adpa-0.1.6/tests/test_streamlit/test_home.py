"""Tests for the Home page."""

import pytest
import streamlit as st
from streamlit_app.Home import init_session_state, display_metrics, display_test_results, main

def test_init_session_state(mock_streamlit, mock_session_state):
    """Test session state initialization."""
    init_session_state()
    assert "teams" in st.session_state
    assert "agents" in st.session_state
    assert "tasks" in st.session_state
    assert "messages" in st.session_state

def test_display_metrics(mock_streamlit, mock_session_state):
    """Test metrics display."""
    display_metrics()
    # No assertions needed as we're just verifying it runs without errors

def test_display_test_results(mock_streamlit, mock_session_state):
    """Test test results display."""
    display_test_results()
    # No assertions needed as we're just verifying it runs without errors

def test_main(mock_streamlit, mock_session_state):
    """Test main function."""
    main()
    # Verify session state is initialized
    assert "teams" in st.session_state
    assert "agents" in st.session_state
    assert "tasks" in st.session_state
    assert "messages" in st.session_state
