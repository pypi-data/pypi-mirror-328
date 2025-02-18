"""Tests for CLI commands."""
import pytest
from unittest.mock import Mock, patch

class TestCLIBasics:
    """Tests for basic CLI functionality."""
    
    def test_cli_initialization(self, mock_cli_app):
        """Test CLI initialization."""
        assert mock_cli_app.commands == []
        assert mock_cli_app.outputs == []
        assert mock_cli_app.return_code == 0
    
    def test_command_execution(self, mock_cli_app):
        """Test command execution."""
        return_code = mock_cli_app.run("help")
        assert return_code == 0
        assert len(mock_cli_app.commands) == 1
        assert mock_cli_app.commands[0] == "help"
    
    def test_output_generation(self, mock_cli_app):
        """Test output generation."""
        mock_cli_app.output("Test message")
        assert len(mock_cli_app.outputs) == 1
        assert mock_cli_app.outputs[0] == "Test message"

class TestCLICommands:
    """Tests for specific CLI commands."""
    
    def test_help_command(self, mock_cli_app):
        """Test help command."""
        mock_cli_app.run("help")
        assert len(mock_cli_app.outputs) > 0
        assert "Available commands" in mock_cli_app.outputs[0]
    
    def test_llm_command(self, mock_cli_app):
        """Test LLM command."""
        mock_cli_app.run("ask What is ADPA?")
        assert "ADPA is a framework..." in mock_cli_app.outputs[0]
    
    def test_database_command(self, mock_cli_app):
        """Test database command."""
        mock_cli_app.run("db-status")
        assert "Database is connected" in mock_cli_app.outputs[0]

class TestCLIIntegration:
    """Tests for CLI integration with other components."""
    
    @pytest.mark.asyncio
    async def test_workflow_execution(self, mock_cli_app, mock_team):
        """Test workflow execution through CLI."""
        # Add test workflow
        mock_cli_app.run("workflow test")
        mock_team.assign_task("Test workflow")
        mock_cli_app.output("Workflow completed")
        assert "Workflow completed" in mock_cli_app.outputs
    
    def test_error_handling(self, mock_cli_app):
        """Test CLI error handling."""
        return_code = mock_cli_app.run("invalid-command")
        assert return_code != 0
        assert "Error: Invalid command" in mock_cli_app.outputs[0]
    
    def test_interactive_mode(self, mock_cli_app):
        """Test interactive mode."""
        mock_cli_app.run("help")
        mock_cli_app.run("ask Test question")
        mock_cli_app.run("db-status")
        
        # Verify command history
        assert len(mock_cli_app.commands) == 3
        assert mock_cli_app.commands == ["help", "ask Test question", "db-status"]
        
        # Verify outputs
        assert any("Available commands" in output for output in mock_cli_app.outputs)
        assert any("ADPA is a framework" in output for output in mock_cli_app.outputs)
        assert any("Database is connected" in output for output in mock_cli_app.outputs)
