"""Tests for CLI functionality."""
import pytest
from click.testing import CliRunner
from adpa.cli.main import cli

@pytest.fixture
def runner():
    """Create a CLI runner."""
    return CliRunner()

def test_cli_help(runner):
    """Test CLI help command."""
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Usage:' in result.output

def test_cli_version(runner):
    """Test CLI version command."""
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert 'ADPA version' in result.output

def test_cli_research(runner):
    """Test research command."""
    result = runner.invoke(cli, ['research', 'test query'])
    assert result.exit_code == 0
    assert 'Research Results' in result.output

def test_cli_team_list(runner):
    """Test team list command."""
    result = runner.invoke(cli, ['team', 'list'])
    assert result.exit_code == 0
    assert 'Available Teams' in result.output

def test_cli_agent_list(runner):
    """Test agent list command."""
    result = runner.invoke(cli, ['agent', 'list'])
    assert result.exit_code == 0
    assert 'Available Agents' in result.output

def test_cli_settings(runner):
    """Test settings command."""
    result = runner.invoke(cli, ['settings', 'show'])
    assert result.exit_code == 0
    assert 'Current Settings' in result.output

def test_cli_task_run(runner):
    """Test task run command."""
    result = runner.invoke(cli, ['task', 'run', 'test task'])
    assert result.exit_code == 0
    assert 'Task Results' in result.output

def test_cli_invalid_command(runner):
    """Test invalid command handling."""
    result = runner.invoke(cli, ['invalid'])
    assert result.exit_code == 2
    assert 'Error' in result.output
