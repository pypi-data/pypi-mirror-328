"""
Agent System CLI module.
"""
import click
import json
from typing import Optional

from adpa.agents import AgentSystem
from adpa.agents.types import Task


@click.group(name="agent")
def agent_cli():
    """Agent system commands."""
    pass


@agent_cli.command()
@click.argument("task_file")
@click.option("--config", help="Agent configuration file")
@click.option("--output", "-o", help="Output file path")
def run(task_file: str, config: Optional[str], output: Optional[str]):
    """Run an agent task."""
    # Load task
    with open(task_file) as f:
        task_data = json.load(f)
    
    # Initialize agent system
    agent_system = AgentSystem()
    if config:
        with open(config) as f:
            config_data = json.load(f)
        agent_system.configure(config_data)
    
    # Create and run task
    task = Task(**task_data)
    result = agent_system.execute_task(task)
    
    # Output results
    if output:
        with open(output, "w") as f:
            json.dump(result.dict(), f, indent=2)
        click.echo(f"Results written to {output}")
    else:
        click.echo(json.dumps(result.dict(), indent=2))


@agent_cli.command()
@click.argument("agent_name")
@click.option("--config", help="Agent configuration file")
def status(agent_name: str, config: Optional[str]):
    """Get agent status."""
    agent_system = AgentSystem()
    if config:
        with open(config) as f:
            config_data = json.load(f)
        agent_system.configure(config_data)
    
    status = agent_system.get_agent_status(agent_name)
    click.echo(json.dumps(status.dict(), indent=2))


def main():
    """Entry point for agent CLI."""
    agent_cli()
