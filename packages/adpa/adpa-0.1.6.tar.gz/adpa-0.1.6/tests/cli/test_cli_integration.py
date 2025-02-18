"""Integration tests for CLI functionality."""

import pytest
import click
from click.testing import CliRunner
from unittest.mock import Mock, AsyncMock, patch
from typing import Dict, Any, List
import os
import json

from adpa.cli.main import cli
from adpa.teams.base import BaseTeam
from adpa.agents.base import BaseAgent
from adpa.agents.config import AgentConfig

# Test data
TEST_COMMANDS = [
    ["run", "research", "quantum computing"],
    ["run", "support", "how to debug python"],
    ["run", "technical", "code review best practices"]
]

TEST_CONFIG = {
    "name": "test_agent",
    "description": "Test agent",
    "capabilities": ["test"],
    "model_name": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2000
}

@pytest.fixture
def runner():
    """Create a CLI runner."""
    return CliRunner()

@pytest.fixture
def mock_team():
    """Create a mock team."""
    team = Mock(spec=BaseTeam)
    team.process = AsyncMock(return_value="Team response")
    return team

@pytest.fixture
def mock_agent():
    """Create a mock agent."""
    agent = Mock(spec=BaseAgent)
    agent.process = AsyncMock(return_value="Agent response")
    return agent

def test_cli_initialization(runner):
    """Test CLI initialization."""
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Usage:" in result.output

def test_cli_version(runner):
    """Test version command."""
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output.lower()

def test_cli_help(runner):
    """Test help command."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "Options:" in result.output
    assert "Commands:" in result.output

@pytest.mark.asyncio
async def test_run_command(runner, mock_team):
    """Test run command."""
    with patch('adpa.cli.main.get_team', return_value=mock_team):
        for cmd in TEST_COMMANDS:
            result = runner.invoke(cli, cmd)
            assert result.exit_code == 0
            assert "Team response" in result.output

@pytest.mark.asyncio
async def test_agent_command(runner, mock_agent):
    """Test agent command."""
    with patch('adpa.cli.main.get_agent', return_value=mock_agent):
        result = runner.invoke(cli, ["agent", "run", "test_agent", "test task"])
        assert result.exit_code == 0
        assert "Agent response" in result.output

def test_config_command(runner, tmp_path):
    """Test config command."""
    config_file = tmp_path / "config.json"
    
    # Test config set
    result = runner.invoke(cli, [
        "config", "set",
        "--file", str(config_file),
        "--name", "test_key",
        "--value", "test_value"
    ])
    assert result.exit_code == 0
    
    # Test config get
    result = runner.invoke(cli, [
        "config", "get",
        "--file", str(config_file),
        "--name", "test_key"
    ])
    assert result.exit_code == 0
    assert "test_value" in result.output

def test_team_command(runner, mock_team):
    """Test team management commands."""
    with patch('adpa.cli.main.get_team', return_value=mock_team):
        # Test team list
        result = runner.invoke(cli, ["team", "list"])
        assert result.exit_code == 0
        
        # Test team info
        result = runner.invoke(cli, ["team", "info", "test_team"])
        assert result.exit_code == 0

def test_agent_config_command(runner, tmp_path):
    """Test agent configuration commands."""
    config_file = tmp_path / "agent_config.json"
    
    # Write test config
    with open(config_file, 'w') as f:
        json.dump(TEST_CONFIG, f)
    
    # Test agent create
    result = runner.invoke(cli, [
        "agent", "create",
        "--config", str(config_file)
    ])
    assert result.exit_code == 0

def test_error_handling(runner):
    """Test CLI error handling."""
    # Test invalid command
    result = runner.invoke(cli, ["invalid"])
    assert result.exit_code != 0
    
    # Test missing arguments
    result = runner.invoke(cli, ["run"])
    assert result.exit_code != 0
    
    # Test invalid config
    result = runner.invoke(cli, [
        "config", "set",
        "--name", "test_key"
    ])
    assert result.exit_code != 0

def test_interactive_mode(runner):
    """Test interactive mode."""
    with patch('click.prompt', return_value="exit"):
        result = runner.invoke(cli, ["interactive"])
        assert result.exit_code == 0

def test_logging(runner, tmp_path):
    """Test logging functionality."""
    log_file = tmp_path / "test.log"
    
    # Run with logging
    result = runner.invoke(cli, [
        "--log-file", str(log_file),
        "run", "test", "log test"
    ])
    
    assert result.exit_code == 0
    assert os.path.exists(log_file)
    
    with open(log_file) as f:
        log_content = f.read()
        assert "log test" in log_content

def test_environment_handling(runner):
    """Test environment variable handling."""
    # Test with missing API key
    with patch.dict(os.environ, {}, clear=True):
        result = runner.invoke(cli, ["run", "test", "test task"])
        assert result.exit_code != 0
        assert "API key" in result.output
    
    # Test with API key
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
        with patch('adpa.cli.main.get_team', return_value=Mock()):
            result = runner.invoke(cli, ["run", "test", "test task"])
            assert result.exit_code == 0

def test_output_formatting(runner, mock_team):
    """Test output formatting options."""
    with patch('adpa.cli.main.get_team', return_value=mock_team):
        # Test JSON output
        result = runner.invoke(cli, [
            "--output", "json",
            "run", "test", "test task"
        ])
        assert result.exit_code == 0
        # Verify JSON format
        try:
            json.loads(result.output)
        except json.JSONDecodeError:
            pytest.fail("Output is not valid JSON")
        
        # Test plain text output
        result = runner.invoke(cli, [
            "--output", "text",
            "run", "test", "test task"
        ])
        assert result.exit_code == 0
        assert isinstance(result.output, str)
