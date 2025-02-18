"""CLI tool for managing the Text-to-SQL learning system workflow."""
import click
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import psycopg2
from psycopg2.extensions import connection
import pandas as pd
from tabulate import tabulate

from .engine import TextToSQLEngine
from .schema_learner import SchemaLearner

class WorkflowManager:
    def __init__(self, config_file: str):
        """Initialize workflow manager with configuration."""
        self.config_file = config_file
        self.config = self._load_config()
        self.engine = None
        self._init_engine()

    def _load_config(self) -> Dict:
        """Load configuration from file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            "databases": {},
            "training_data": {},
            "state_dir": "./state"
        }

    def _save_config(self):
        """Save configuration to file."""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def _init_engine(self):
        """Initialize or load the Text-to-SQL engine."""
        if not self.engine and self.config.get("current_db"):
            db_config = self.config["databases"][self.config["current_db"]]
            self.engine = TextToSQLEngine(db_config)
            
            # Load saved state if exists
            state_dir = self.config["state_dir"]
            if os.path.exists(state_dir):
                self.engine.load_state(state_dir)

    def add_database(self, name: str, connection_params: Dict[str, str]):
        """Add a new database configuration."""
        self.config["databases"][name] = connection_params
        self.config["current_db"] = name
        self._save_config()
        self._init_engine()

    def analyze_schema(self) -> Dict:
        """Analyze current database schema."""
        if not self.engine:
            raise click.ClickException("No database selected")
        
        # Force schema relearning
        self.engine.schema_learner.learn_schema()
        
        # Return analysis
        return {
            "tables": len(self.engine.schema_learner.tables),
            "relationships": len(self.engine.schema_learner.relationships),
            "learned_patterns": len(self.engine.schema_learner.common_queries)
        }

    def generate_training_data(self, table_name: str) -> List[Dict]:
        """Generate example questions and SQL for a table."""
        if not self.engine:
            raise click.ClickException("No database selected")

        table_info = self.engine.schema_learner.tables.get(table_name)
        if not table_info:
            raise click.ClickException(f"Table {table_name} not found")

        examples = []
        
        # Basic SELECT examples
        examples.append({
            "question": f"Show me all {table_name}",
            "sql": f"SELECT * FROM {table_name}",
            "type": "basic_select"
        })

        # Column specific examples
        for col_name, col_info in table_info.columns.items():
            # Count example
            examples.append({
                "question": f"How many {table_name} do we have?",
                "sql": f"SELECT COUNT(*) FROM {table_name}",
                "type": "count"
            })

            # Filter example
            if col_info.common_values:
                value = next(iter(col_info.common_values))
                examples.append({
                    "question": f"Find {table_name} where {col_name} is {value}",
                    "sql": f"SELECT * FROM {table_name} WHERE {col_name} = '{value}'",
                    "type": "filter"
                })

        return examples

    def train_system(self, question: str, sql: str, correct: bool):
        """Train the system with feedback."""
        if not self.engine:
            raise click.ClickException("No database selected")

        self.engine.feedback(
            text_input=question,
            sql_query=sql,
            was_correct=correct
        )
        
        # Save state after training
        self.engine.save_state(self.config["state_dir"])

    def query_database(self, question: str) -> Dict:
        """Query database using natural language."""
        if not self.engine:
            raise click.ClickException("No database selected")

        # Convert question to SQL
        sql, info = self.engine.convert_to_sql(question)
        
        if not info["success"]:
            return {
                "success": False,
                "error": info["error"],
                "suggestion": info["suggestion"]
            }

        # Execute query and get results
        try:
            with psycopg2.connect(**self.config["databases"][self.config["current_db"]]) as conn:
                df = pd.read_sql(sql, conn)
                return {
                    "success": True,
                    "sql": sql,
                    "results": tabulate(df, headers='keys', tablefmt='psql')
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "sql": sql
            }

@click.group()
@click.option('--config', default='./config.json', help='Configuration file path')
@click.pass_context
def cli(ctx, config):
    """Text-to-SQL Learning System CLI"""
    ctx.obj = WorkflowManager(config)

@cli.command()
@click.argument('name')
@click.option('--host', prompt=True)
@click.option('--port', prompt=True)
@click.option('--dbname', prompt=True)
@click.option('--user', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
@click.pass_obj
def add_database(manager: WorkflowManager, name: str, host: str, port: str, 
                dbname: str, user: str, password: str):
    """Add a new database connection."""
    manager.add_database(name, {
        "host": host,
        "port": port,
        "dbname": dbname,
        "user": user,
        "password": password
    })
    click.echo(f"Added database {name}")

@cli.command()
@click.pass_obj
def analyze(manager: WorkflowManager):
    """Analyze current database schema."""
    analysis = manager.analyze_schema()
    click.echo("\nSchema Analysis:")
    click.echo(f"Tables: {analysis['tables']}")
    click.echo(f"Relationships: {analysis['relationships']}")
    click.echo(f"Learned Patterns: {analysis['learned_patterns']}")

@cli.command()
@click.argument('table')
@click.option('--output', '-o', help='Output file for examples')
@click.pass_obj
def generate_examples(manager: WorkflowManager, table: str, output: Optional[str]):
    """Generate example questions and SQL for a table."""
    examples = manager.generate_training_data(table)
    
    if output:
        with open(output, 'w') as f:
            json.dump(examples, f, indent=2)
        click.echo(f"Saved {len(examples)} examples to {output}")
    else:
        for ex in examples:
            click.echo("\nQuestion:", ex["question"])
            click.echo("SQL:", ex["sql"])
            click.echo("Type:", ex["type"])

@cli.command()
@click.argument('question')
@click.argument('sql')
@click.option('--correct/--incorrect', default=True)
@click.pass_obj
def train(manager: WorkflowManager, question: str, sql: str, correct: bool):
    """Train the system with a question-SQL pair."""
    manager.train_system(question, sql, correct)
    click.echo("Training example recorded")

@cli.command()
@click.argument('question')
@click.pass_obj
def ask(manager: WorkflowManager, question: str):
    """Ask a question in natural language."""
    result = manager.query_database(question)
    
    if result["success"]:
        click.echo("\nSQL Query:")
        click.echo(result["sql"])
        click.echo("\nResults:")
        click.echo(result["results"])
    else:
        click.echo("\nError:", result["error"])
        if result.get("suggestion"):
            click.echo("Suggestion:", result["suggestion"])

if __name__ == '__main__':
    cli()
