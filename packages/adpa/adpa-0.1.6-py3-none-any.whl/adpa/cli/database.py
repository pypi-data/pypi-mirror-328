"""
Database CLI module.
"""
import click
from typing import Optional
import json

from adpa.database import DatabaseManager
from adpa.database.config import DBConfig


@click.group(name="database")
def database_cli():
    """Database management commands."""
    pass


@database_cli.command()
@click.option("--config", help="Database configuration file")
def migrate(config: Optional[str]):
    """Run database migrations."""
    db_config = _load_config(config)
    db = DatabaseManager(db_config)
    db.migrate()
    click.echo("Migrations completed successfully")


@database_cli.command()
@click.option("--config", help="Database configuration file")
def rollback(config: Optional[str]):
    """Rollback last migration."""
    db_config = _load_config(config)
    db = DatabaseManager(db_config)
    db.rollback()
    click.echo("Rollback completed successfully")


@database_cli.command()
@click.argument("query")
@click.option("--config", help="Database configuration file")
@click.option("--output", "-o", help="Output file path")
@click.option("--format", "output_format", type=click.Choice(["json", "csv"]), default="json")
def query(query: str, config: Optional[str], output: Optional[str], output_format: str):
    """Execute SQL query."""
    db_config = _load_config(config)
    db = DatabaseManager(db_config)
    
    results = db.execute_query(query)
    
    if output_format == "json":
        data = [dict(row) for row in results]
        if output:
            with open(output, "w") as f:
                json.dump(data, f, indent=2)
            click.echo(f"Results written to {output}")
        else:
            click.echo(json.dumps(data, indent=2))
    else:  # csv
        import csv
        if not results:
            click.echo("No results found")
            return
            
        headers = results[0].keys()
        if output:
            with open(output, "w", newline="") as f:
                writer = csv.DictWriter(f, headers)
                writer.writeheader()
                writer.writerows(results)
            click.echo(f"Results written to {output}")
        else:
            writer = csv.DictWriter(click.get_text_stream("stdout"), headers)
            writer.writeheader()
            writer.writerows(results)


@database_cli.command()
@click.option("--config", help="Database configuration file")
def status(config: Optional[str]):
    """Get database status."""
    db_config = _load_config(config)
    db = DatabaseManager(db_config)
    status = db.get_status()
    click.echo(json.dumps(status, indent=2))


@database_cli.command()
@click.argument("backup_path")
@click.option("--config", help="Database configuration file")
def backup(backup_path: str, config: Optional[str]):
    """Backup database."""
    db_config = _load_config(config)
    db = DatabaseManager(db_config)
    db.backup(backup_path)
    click.echo(f"Database backed up to {backup_path}")


@database_cli.command()
@click.argument("backup_path")
@click.option("--config", help="Database configuration file")
def restore(backup_path: str, config: Optional[str]):
    """Restore database from backup."""
    db_config = _load_config(config)
    db = DatabaseManager(db_config)
    db.restore(backup_path)
    click.echo("Database restored successfully")


def _load_config(config_path: Optional[str]) -> DBConfig:
    """Load database configuration."""
    if config_path:
        with open(config_path) as f:
            config_data = json.load(f)
        return DBConfig(**config_data)
    return DBConfig.from_env()


def main():
    """Entry point for database CLI."""
    database_cli()
