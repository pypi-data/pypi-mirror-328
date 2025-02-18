"""App state management for Streamlit demo."""
import streamlit as st

def get_providers():
    """Get providers from session state."""
    return st.session_state.get("providers", {})

def get_failover_manager():
    """Get failover manager from session state."""
    return st.session_state.get("failover_manager", None)
