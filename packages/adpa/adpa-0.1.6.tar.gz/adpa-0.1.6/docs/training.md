# Domain-Specific Training

Version 0.7.0

## Overview

The ADPA framework provides comprehensive support for domain-specific training and fine-tuning of language models. This module enables you to adapt pre-trained models to specific domains or tasks while maintaining high performance and efficiency.

## Components

### DomainTrainer

The main component for managing domain-specific training:

```python
from adpa.training import DomainTrainer, DomainTrainingConfig

config = DomainTrainingConfig(
    name="medical-bert",
    description="Fine-tuned BERT for medical domain",
    base_model="bert-base-uncased",
    training_data_path="data/medical_texts.csv",
    validation_data_path="data/medical_validation.csv",
    batch_size=8,
    learning_rate=2e-5,
    num_epochs=3
)

trainer = DomainTrainer(config)
trainer.train()
```

### Data Processing

Handles data preparation and preprocessing:

```python
from adpa.training import DataProcessor, DataProcessingConfig

proc_config = DataProcessingConfig(
    input_format="csv",
    text_column="text",
    label_column="label",
    max_length=512,
    preprocessing_steps=["lower", "strip"]
)

processor = DataProcessor(proc_config)
dataset = processor.prepare_dataset("data/raw_data.csv")
```

### Metrics and Evaluation

Tracks and computes training metrics:

```python
from adpa.training import MetricsTracker, ModelEvaluator

evaluator = ModelEvaluator(metrics=["accuracy", "f1", "precision", "recall"])
results = evaluator.evaluate(model, eval_data)
```

## Configuration

### Training Configuration

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| name | str | Name of the training run | Required |
| description | str | Description of the model/training | Required |
| base_model | str | Base model to fine-tune | Required |
| training_data_path | str | Path to training data | Required |
| validation_data_path | str | Path to validation data | None |
| batch_size | int | Training batch size | 4 |
| learning_rate | float | Learning rate | 2e-5 |
| num_epochs | int | Number of training epochs | 3 |
| max_steps | int | Maximum training steps | None |
| warmup_steps | int | Number of warmup steps | 100 |
| evaluation_strategy | str | When to evaluate | "steps" |
| eval_steps | int | Steps between evaluations | 500 |
| save_steps | int | Steps between checkpoints | 1000 |
| metrics | List[str] | Metrics to track | ["accuracy", "f1"] |

### Data Processing Configuration

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| input_format | str | Format of input data | Required |
| text_column | str | Column name for text | None |
| label_column | str | Column name for labels | None |
| max_length | int | Maximum sequence length | 512 |
| train_split | float | Train/validation split ratio | 0.8 |
| preprocessing_steps | List[str] | Preprocessing steps | None |
| custom_tokenizer | str | Path to custom tokenizer | None |

## Best Practices

1. **Data Preparation**:
   - Clean and preprocess your data thoroughly
   - Use appropriate text preprocessing steps
   - Ensure balanced dataset splits

2. **Training Configuration**:
   - Start with small learning rates (1e-5 to 5e-5)
   - Use appropriate batch sizes for your GPU memory
   - Enable gradient accumulation for larger effective batch sizes

3. **Model Selection**:
   - Choose appropriate base models for your domain
   - Consider model size vs. performance trade-offs
   - Use domain-specific tokenizers when available

4. **Evaluation**:
   - Monitor multiple metrics during training
   - Use appropriate validation sets
   - Implement early stopping to prevent overfitting

## Examples

### Medical Domain Fine-tuning

```python
from adpa.training import (
    DomainTrainer,
    DomainTrainingConfig,
    DataProcessor,
    DataProcessingConfig
)

# Data processing
proc_config = DataProcessingConfig(
    input_format="csv",
    text_column="medical_text",
    label_column="condition",
    preprocessing_steps=["lower", "strip"],
    max_length=256
)

processor = DataProcessor(proc_config)
dataset = processor.prepare_dataset("medical_data.csv")

# Training
train_config = DomainTrainingConfig(
    name="medical-bert",
    description="BERT fine-tuned on medical texts",
    base_model="microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract",
    training_data_path=dataset["train"],
    validation_data_path=dataset["validation"],
    batch_size=16,
    learning_rate=2e-5,
    num_epochs=5,
    metrics=["accuracy", "f1", "precision", "recall"]
)

trainer = DomainTrainer(train_config)
trainer.train()
```

### Legal Domain Fine-tuning

```python
# Data processing
proc_config = DataProcessingConfig(
    input_format="jsonl",
    text_column="legal_text",
    label_column="category",
    preprocessing_steps=["lower", "strip"],
    max_length=512
)

processor = DataProcessor(proc_config)
dataset = processor.prepare_dataset("legal_data.jsonl")

# Training
train_config = DomainTrainingConfig(
    name="legal-bert",
    description="BERT fine-tuned on legal texts",
    base_model="nlpaueb/legal-bert-base-uncased",
    training_data_path=dataset["train"],
    validation_data_path=dataset["validation"],
    batch_size=8,
    learning_rate=1e-5,
    num_epochs=3,
    metrics=["accuracy", "f1"]
)

trainer = DomainTrainer(train_config)
trainer.train()
```

## Troubleshooting

### Common Issues

1. **Out of Memory Errors**:
   - Reduce batch size
   - Reduce maximum sequence length
   - Use gradient accumulation
   - Use mixed precision training

2. **Poor Performance**:
   - Check data quality and preprocessing
   - Adjust learning rate
   - Increase number of epochs
   - Try different base models

3. **Slow Training**:
   - Use appropriate hardware (GPU)
   - Optimize batch size
   - Enable mixed precision training
   - Use efficient data loading

### Logging and Monitoring

The training module provides comprehensive logging:

```python
import logging
logging.basicConfig(level=logging.INFO)

# Training logs will show:
# - Data processing progress
# - Training progress
# - Evaluation metrics
# - Best model checkpoints
```

## Future Improvements

1. Support for more advanced training techniques:
   - Knowledge distillation
   - Few-shot learning
   - Active learning

2. Additional model architectures:
   - T5 fine-tuning
   - GPT model adaptation
   - Custom architecture support

3. Enhanced evaluation capabilities:
   - Cross-validation
   - Statistical significance tests
   - Custom metric support
