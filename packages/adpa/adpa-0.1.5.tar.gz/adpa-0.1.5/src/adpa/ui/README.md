# ADPA Framework UI Module

## Overview

The UI module provides web-based user interfaces for the ADPA Framework, built with Streamlit.

## Directory Structure

```
ui/
├── config/             # Configuration files
│   ├── database.py    # Database configuration
│   └── rag.py        # RAG configuration
├── pages/             # UI pages
│   ├── knowledge/    # Knowledge base pages
│   ├── rag/         # RAG interface pages
│   └── store/       # Vector store pages
├── components/        # Reusable UI components
│   ├── forms/       # Form components
│   ├── charts/      # Data visualization
│   └── widgets/     # Custom widgets
├── styles/           # CSS styles
│   ├── base.css     # Base styles
│   └── themes/      # Theme styles
└── utils/           # UI utilities
    ├── state.py     # State management
    └── validation.py # Input validation
```

## Features

### 1. Knowledge Query Interface
- Natural language queries
- Result visualization
- Query history
- Export options

### 2. RAG Agent Interface
- Agent configuration
- Testing interface
- Performance metrics
- Debug tools

### 3. Vector Store Management
- Store creation
- Data ingestion
- Index management
- Search interface

### 4. Store Advisor
- Schema recommendations
- Query optimization
- Performance insights
- Best practices

## Usage

### 1. Starting the UI
```bash
streamlit run src/adpa/ui/Home.py
```

### 2. Configuration
```python
from adpa.ui.config import DatabaseConfig, RAGConfig

# Configure database
db_config = DatabaseConfig(
    url="postgresql://localhost:5432/adpa",
    pool_size=5
)

# Configure RAG
rag_config = RAGConfig(
    model="gpt-4",
    embeddings="text-embedding-ada-002"
)
```

### 3. Custom Components
```python
from adpa.ui.components import QueryForm, ResultsChart

# Add query form
query_form = QueryForm()
user_query = query_form.render()

# Display results
chart = ResultsChart()
chart.plot(results)
```

## Development

### 1. Adding New Pages
1. Create page in `pages/`
2. Add to navigation
3. Update documentation
4. Add tests

### 2. Creating Components
1. Design component
2. Implement in `components/`
3. Add documentation
4. Create examples

### 3. Styling
1. Add styles to `styles/`
2. Follow BEM methodology
3. Support themes
4. Test responsiveness

## Testing

### 1. Component Tests
```bash
pytest src/tests/ui/components
```

### 2. Page Tests
```bash
pytest src/tests/ui/pages
```

### 3. Integration Tests
```bash
pytest src/tests/ui/integration
```

## Dependencies

Required packages:
```
streamlit>=1.30.0
plotly>=5.18.0
pandas>=2.1.0
pydantic>=2.5.0
```

## Contributing

1. Follow style guide
2. Add documentation
3. Include tests
4. Update README
