"""State management utilities for the UI."""

from typing import Any, Dict, Optional
import streamlit as st

class UIState:
    """Manages UI state across pages."""

    @staticmethod
    def init_session_state() -> None:
        """Initialize session state with default values."""
        defaults = {
            "user": None,
            "selected_vector_store": "chroma",
            "selected_model": "gpt-4",
            "chat_history": [],
            "last_query": None,
            "last_results": None,
            "error": None
        }
        
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    @staticmethod
    def get(key: str, default: Any = None) -> Any:
        """Get value from session state."""
        return st.session_state.get(key, default)

    @staticmethod
    def set(key: str, value: Any) -> None:
        """Set value in session state."""
        st.session_state[key] = value

    @staticmethod
    def clear(key: str) -> None:
        """Clear value from session state."""
        if key in st.session_state:
            del st.session_state[key]

    @staticmethod
    def clear_all() -> None:
        """Clear all session state."""
        for key in list(st.session_state.keys()):
            del st.session_state[key]

    @staticmethod
    def add_to_chat_history(
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """Add message to chat history."""
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        
        message = {
            "role": role,
            "content": content,
            "metadata": metadata or {}
        }
        st.session_state.chat_history.append(message)

    @staticmethod
    def get_chat_history() -> list:
        """Get chat history."""
        return st.session_state.get("chat_history", [])
