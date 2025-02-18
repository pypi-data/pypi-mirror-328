"""
ADPA Command Line Interface.
"""
import click

from .text2sql import text2sql_cli
from .agent import agent_cli
from .monitor import monitor_cli
from .database import database_cli


@click.group()
@click.version_option()
def main():
    """ADPA Command Line Interface."""
    pass


main.add_command(text2sql_cli)
main.add_command(agent_cli)
main.add_command(monitor_cli)
main.add_command(database_cli)


if __name__ == "__main__":
    main()
