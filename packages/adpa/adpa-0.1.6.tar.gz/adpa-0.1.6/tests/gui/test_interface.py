"""Tests for GUI interface."""
import pytest
from unittest.mock import Mock, patch, AsyncMock
from sqlalchemy.orm import Session

from adpa.models import WorkflowData

class TestGUIWindow:
    """Tests for GUI window functionality."""
    
    def test_window_creation(self, mock_gui_window):
        """Test window creation."""
        assert not mock_gui_window.closed
        assert isinstance(mock_gui_window.elements, dict)
    
    def test_window_close(self, mock_gui_window):
        """Test window close."""
        mock_gui_window.close()
        assert mock_gui_window.closed
    
    def test_element_access(self, mock_gui_window):
        """Test element access."""
        element = mock_gui_window.find_element("test_key")
        assert element is not None
        assert mock_gui_window.elements["test_key"] == element
    
    def test_window_read(self, mock_gui_window):
        """Test window read."""
        event, values = mock_gui_window.read()
        assert event is None
        assert values is None

class TestGUIInteractions:
    """Tests for GUI element interactions."""
    
    def test_button_click(self, mock_gui_window):
        """Test button click."""
        button = mock_gui_window.find_element("submit_button")
        button.click()
        button.click.assert_called_once()
    
    def test_input_update(self, mock_gui_window):
        """Test input update."""
        input_field = mock_gui_window.find_element("input_field")
        input_field.update("Test input")
        input_field.update.assert_called_once_with("Test input")
    
    def test_output_display(self, mock_gui_window):
        """Test output display."""
        output_field = mock_gui_window.find_element("output_field")
        output_field.update("Test output")
        output_field.update.assert_called_once_with("Test output")

class TestGUIIntegration:
    """Tests for GUI integration with other components."""
    
    @pytest.mark.asyncio
    async def test_llm_integration(self, mock_chat_model, status_field):
        """Test GUI integration with LLM."""
        # Test LLM response
        response = await mock_chat_model.ainvoke("Test query")
        status_field.update("LLM response received")
        
        assert response == "Test response"
        status_field.update.assert_called_with("LLM response received")
    
    @pytest.mark.asyncio
    async def test_database_integration(self, session, status_field):
        """Test GUI integration with database."""
        from adpa.models import WorkflowData
        
        try:
            # Save test data
            workflow_data = WorkflowData(content="Test data")
            session.add(workflow_data)
            session.commit()
            status_field.update("Data saved successfully")
            
            # Verify data
            result = session.query(WorkflowData).first()
            assert result.content == "Test data"
            status_field.update.assert_called_with("Data saved successfully")
            
        except Exception as e:
            status_field.update(f"Error: {str(e)}")
            raise
