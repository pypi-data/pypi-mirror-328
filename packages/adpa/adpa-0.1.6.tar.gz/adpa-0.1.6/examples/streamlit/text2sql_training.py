"""Example script for training a Text2SQL model."""
import os
from pathlib import Path
import json
import logging

from adpa.training.text2sql.trainer import (
    Text2SQLTrainer,
    SQLTrainingConfig,
    SQLSchemaProcessor
)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example database schema
SCHEMA = {
    "tables": [
        {
            "name": "employees",
            "columns": [
                {"name": "id", "type": "INTEGER", "primary_key": True},
                {"name": "name", "type": "TEXT"},
                {"name": "department", "type": "TEXT"},
                {"name": "salary", "type": "INTEGER"}
            ]
        },
        {
            "name": "departments",
            "columns": [
                {"name": "id", "type": "INTEGER", "primary_key": True},
                {"name": "name", "type": "TEXT"},
                {"name": "budget", "type": "INTEGER"}
            ],
            "foreign_keys": [
                {
                    "from": "id",
                    "to": "employees.department"
                }
            ]
        }
    ]
}

# Example training data
TRAINING_DATA = [
    {
        "question": "What is the average salary of employees in the IT department?",
        "query": "SELECT AVG(salary) FROM employees WHERE department = 'IT'"
    },
    {
        "question": "List all departments with their total employee count",
        "query": """
            SELECT d.name, COUNT(e.id) as employee_count
            FROM departments d
            LEFT JOIN employees e ON d.name = e.department
            GROUP BY d.name
        """
    }
]

def main():
    # Create directories
    base_dir = Path("training_runs/text2sql")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Save schema
    schema_path = base_dir / "schema.json"
    with open(schema_path, "w") as f:
        json.dump(SCHEMA, f, indent=2)
    
    # Save training data
    train_path = base_dir / "train.json"
    with open(train_path, "w") as f:
        json.dump(TRAINING_DATA, f, indent=2)
    
    # Configure training
    config = SQLTrainingConfig(
        name="sql-gpt",
        description="GPT model fine-tuned for SQL generation",
        base_model="gpt-3.5-turbo",
        training_data_path=str(train_path),
        schema_path=str(schema_path),
        sql_dialect="sqlite",
        batch_size=4,
        learning_rate=1e-5,
        num_epochs=5,
        include_schema_context=True,
        schema_serialization_type="natural",
        evaluation_metrics=["exact_match", "semantic_accuracy"]
    )
    
    # Initialize trainer
    trainer = Text2SQLTrainer(config)
    
    # Prepare data
    logger.info("Preparing training data...")
    trainer.prepare_training_data()
    
    # Train model
    logger.info("Starting training...")
    trainer.train()
    
    # Evaluate
    logger.info("Evaluating model...")
    eval_data = {
        "predictions": [
            "SELECT AVG(salary) FROM employees WHERE department = 'IT'"
        ],
        "references": [
            "SELECT AVG(salary) FROM employees WHERE department = 'IT'"
        ],
        "db_path": str(base_dir / "test.db")
    }
    metrics = trainer.evaluate(eval_data)
    
    logger.info("Evaluation metrics:")
    for metric, value in metrics.items():
        logger.info(f"{metric}: {value:.4f}")
    
    # Generate example
    question = "How many employees earn more than the average salary?"
    logger.info(f"\nGenerating SQL for question: {question}")
    # TODO: Implement query generation

if __name__ == "__main__":
    main()
