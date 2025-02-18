from typing import Dict, Callable
import streamlit as st

class KeyboardShortcuts:
    def __init__(self):
        self.shortcuts: Dict[str, Callable] = {
            "ctrl+s": self.save_settings,
            "ctrl+l": self.load_settings,
            "ctrl+r": self.refresh_page,
            "ctrl+d": self.toggle_dark_mode,
            "ctrl+h": self.show_help,
            "escape": self.close_popups
        }
    
    def save_settings(self):
        """Save current settings"""
        if hasattr(st.session_state, 'llm_providers'):
            st.session_state.save_triggered = True
    
    def load_settings(self):
        """Load saved settings"""
        if hasattr(st.session_state, 'llm_providers'):
            st.session_state.load_triggered = True
    
    def refresh_page(self):
        """Refresh the current page"""
        st.rerun()
    
    def toggle_dark_mode(self):
        """Toggle dark/light mode"""
        if 'theme' in st.session_state:
            st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'
    
    def show_help(self):
        """Show help dialog"""
        st.session_state.show_help = True
    
    def close_popups(self):
        """Close all popups"""
        if hasattr(st.session_state, 'show_help'):
            st.session_state.show_help = False

    def handle_shortcut(self, event):
        """Handle keyboard shortcut events"""
        key = event.lower()
        if key in self.shortcuts:
            self.shortcuts[key]()
