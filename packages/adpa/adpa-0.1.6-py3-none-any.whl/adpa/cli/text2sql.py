"""
Text2SQL CLI module.
"""
import click
from typing import Optional

from adpa.text2sql import Text2SQLConverter


@click.group(name="text2sql")
def text2sql_cli():
    """Text2SQL conversion commands."""
    pass


@text2sql_cli.command()
@click.argument("query")
@click.option("--dialect", default="postgresql", help="SQL dialect to use")
@click.option("--schema", help="Database schema file path")
@click.option("--output", "-o", help="Output file path")
def convert(query: str, dialect: str, schema: Optional[str], output: Optional[str]):
    """Convert natural language to SQL."""
    converter = Text2SQLConverter(dialect=dialect)
    if schema:
        converter.load_schema(schema)
    
    sql = converter.convert(query)
    
    if output:
        with open(output, "w") as f:
            f.write(sql)
        click.echo(f"SQL written to {output}")
    else:
        click.echo(sql)


@text2sql_cli.command()
@click.argument("file_path")
@click.option("--dialect", default="postgresql", help="SQL dialect to use")
def validate(file_path: str, dialect: str):
    """Validate SQL query."""
    converter = Text2SQLConverter(dialect=dialect)
    with open(file_path) as f:
        sql = f.read()
    
    is_valid = converter.validate(sql)
    if is_valid:
        click.echo("SQL is valid")
    else:
        click.echo("SQL is invalid", err=True)
        exit(1)


def main():
    """Entry point for text2sql CLI."""
    text2sql_cli()
