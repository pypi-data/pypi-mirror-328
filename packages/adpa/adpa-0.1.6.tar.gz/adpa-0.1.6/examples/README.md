# ADPA Framework Examples

This directory contains example applications and code snippets demonstrating various features of the ADPA Framework.

## Directory Structure

```
examples/
├── core/               # Core functionality examples
│   ├── character/      # Character style examples
│   └── knowledge/      # Knowledge base examples
├── text2sql/          # Text2SQL examples
│   ├── training/      # Training examples
│   └── inference/     # Inference examples
├── streamlit/         # Streamlit UI examples
│   ├── pages/         # Application pages
│   └── static/        # Static assets
└── database/          # Database examples
    ├── schema/        # Schema examples
    └── queries/       # Query examples
```

## Example Categories

### 1. Core Examples
- Character style training and extraction
- Knowledge base integration
- Core functionality demos

### 2. Text2SQL Examples
- Model training examples
- Query generation
- Schema extraction
- Database integration

### 3. Streamlit Examples
- Web UI implementation
- Interactive demos
- Visualization examples
- Configuration samples

### 4. Database Examples
- Schema management
- Query execution
- Data verification
- Connection handling

## Running Examples

### 1. Setup
```bash
# Install dependencies
pip install -e ".[examples]"

# Set up environment
cp .env.example .env
```

### 2. Core Examples
```bash
# Run character style training
python examples/core/character/train.py

# Run knowledge base example
python examples/core/knowledge/demo.py
```

### 3. Text2SQL Examples
```bash
# Run training example
python examples/text2sql/training/train.py

# Run inference example
python examples/text2sql/inference/generate.py
```

### 4. Streamlit Examples
```bash
# Run Streamlit app
streamlit run examples/streamlit/Home.py
```

### 5. Database Examples
```bash
# Run schema example
python examples/database/schema/create.py

# Run query example
python examples/database/queries/execute.py
```

## Contributing Examples

1. Choose appropriate category
2. Follow naming conventions
3. Add documentation
4. Include requirements
5. Provide test data

## Dependencies

Required packages for examples:
```
streamlit>=1.30.0
pandas>=2.1.0
plotly>=5.18.0
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
```
