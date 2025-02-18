# ADPA Framework

[![PyPI version](https://badge.fury.io/py/adpa.svg)](https://badge.fury.io/py/adpa)
[![Python](https://img.shields.io/pypi/pyversions/adpa.svg)](https://pypi.org/project/adpa/)
[![License](https://img.shields.io/github/license/achimdehnert/adpa.svg)](https://github.com/achimdehnert/adpa/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/adpa/badge/?version=latest)](https://adpa.readthedocs.io/en/latest/?badge=latest)

## Overview

ADPA (Attention-Desire-Position-Action) is a comprehensive framework for building AI-driven applications. It provides a structured approach to implementing complex AI workflows, with a focus on:

- Natural language processing with Text2SQL capabilities
- Agent-based architecture for task delegation
- Modern UI components for interactive applications
- Robust testing and monitoring infrastructure

## Key Features

### Text2SQL Engine
- Natural language to SQL translation
- Schema validation and type checking
- Query optimization and security
- Support for multiple database dialects

### Agent System
- Configurable agent behaviors
- Task delegation and coordination
- Resource management
- Error handling and recovery

### UI Components
- Modern Streamlit-based interface
- Interactive data visualization
- Real-time updates
- Responsive design

### Development Tools
- Comprehensive testing suite
- Performance monitoring
- Security features
- Documentation generation

## Installation

```bash
pip install adpa
```

## Quick Example

```python
from adpa import Text2SQL, Agent

# Initialize Text2SQL engine
text2sql = Text2SQL()

# Create an agent
agent = Agent(
    name="query_executor",
    type="database",
    tools=["sql_execution"]
)

# Convert natural language to SQL
query = "Find all users who joined last month"
sql = text2sql.translate(query)

# Execute query through agent
result = agent.execute(sql)
print(result)
```

## Documentation

For detailed documentation, please visit:

- [Getting Started](getting-started/installation.md)
- [User Guide](user-guide/overview.md)
- [API Reference](api/core.md)
- [Examples](examples/basic.md)

## Contributing

We welcome contributions! Please see our [Contributing Guide](contributing.md) for details.
