"""Common test fixtures for Streamlit tests."""

import pytest
import streamlit as st
from adpa.config import Settings
from adpa.teams.support import SupportTeam
from adpa.teams.technical import TechnicalTeam
from adpa.teams.research_team import ResearchTeam
from adpa.agents.research_agent import ResearchAgent
from adpa.agents.support_agent import SupportAgent
from adpa.agents.technical_agent import TechnicalAgent

class MockColumn:
    """Mock Streamlit column."""
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        pass

@pytest.fixture
def mock_streamlit(monkeypatch):
    """Mock streamlit functions."""
    def mock_metric(*args, **kwargs):
        return None
    
    def mock_markdown(*args, **kwargs):
        return None
    
    def mock_success(*args, **kwargs):
        return None
    
    def mock_warning(*args, **kwargs):
        return None
    
    def mock_info(*args, **kwargs):
        return None
    
    def mock_columns(*args, **kwargs):
        return [MockColumn() for _ in range(args[0])]
    
    monkeypatch.setattr(st, "metric", mock_metric)
    monkeypatch.setattr(st, "markdown", mock_markdown)
    monkeypatch.setattr(st, "success", mock_success)
    monkeypatch.setattr(st, "warning", mock_warning)
    monkeypatch.setattr(st, "info", mock_info)
    monkeypatch.setattr(st, "columns", mock_columns)
    monkeypatch.setattr(st, "caption", mock_markdown)
    monkeypatch.setattr(st, "title", mock_markdown)
    monkeypatch.setattr(st, "header", mock_markdown)
    monkeypatch.setattr(st, "subheader", mock_markdown)
    monkeypatch.setattr(st, "sidebar", st)
    monkeypatch.setattr(st, "set_page_config", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "expander", lambda *args, **kwargs: MockColumn())
    monkeypatch.setattr(st, "button", lambda *args, **kwargs: False)
    monkeypatch.setattr(st, "checkbox", lambda *args, **kwargs: True)
    monkeypatch.setattr(st, "selectbox", lambda *args, **kwargs: kwargs.get("options", [""])[0])
    monkeypatch.setattr(st, "multiselect", lambda *args, **kwargs: kwargs.get("default", []))
    monkeypatch.setattr(st, "text_input", lambda *args, **kwargs: kwargs.get("value", ""))
    monkeypatch.setattr(st, "number_input", lambda *args, **kwargs: kwargs.get("value", 0))
    monkeypatch.setattr(st, "slider", lambda *args, **kwargs: kwargs.get("value", 0.7))
    monkeypatch.setattr(st, "tabs", lambda *args, **kwargs: [MockColumn() for _ in args[0]])

@pytest.fixture
def mock_session_state(monkeypatch):
    """Mock session state."""
    class MockSessionState(dict):
        def __init__(self):
            super().__init__()
            settings = Settings()
            self.settings = settings
            self.teams = {
                "research": ResearchTeam(),
                "support": SupportTeam(),
                "technical": TechnicalTeam()
            }
            self.agents = {
                "research": ResearchAgent(name="Research Agent", openai_api_key="test_key", tavily_api_key="test_key"),
                "support": SupportAgent(config=settings),
                "technical": TechnicalAgent(config=settings)
            }
            self.tasks = []
            self.messages = []
            
            # Initialize dict with same values
            self.update({
                "settings": settings,
                "teams": self.teams,
                "agents": self.agents,
                "tasks": self.tasks,
                "messages": self.messages
            })
        
        def __getattr__(self, name):
            """Get attribute if not found in instance dict."""
            try:
                return self[name]
            except KeyError:
                raise AttributeError(f"'MockSessionState' object has no attribute '{name}'")
    
    monkeypatch.setattr(st, "session_state", MockSessionState())
