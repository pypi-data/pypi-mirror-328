# Installation

## Requirements

- Python 3.11 or higher
- pip or poetry for package management

## Using pip

```bash
pip install adpa
```

## Using poetry

```bash
poetry add adpa
```

## Development Installation

For development purposes, clone the repository and install with development dependencies:

```bash
git clone https://github.com/achimdehnert/adpa.git
cd adpa
poetry install --with dev
```

## Environment Variables

Create a `.env` file in your project root with the following variables:

```env
# API Keys Configuration
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
AZURE_API_KEY=your_azure_key
AZURE_ENDPOINT=your_azure_endpoint
GROQ_API_KEY=your_groq_key

# Search APIs (Optional)
TAVILY_API_KEY=your_tavily_key
BRAVE_API_KEY=your_brave_key
GOOGLE_API_KEY=your_google_key
GOOGLE_SERPER_API_KEY=your_serper_key
SERPAPI_API_KEY=your_serpapi_key
SCRAPINGBEE_API_KEY=your_scrapingbee_key
GEMINI_API_KEY=your_gemini_key

# Database Configuration
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DATABASE=your_database
```

## Verifying Installation

Run the following Python code to verify your installation:

```python
from adpa import __version__
print(f"ADPA Framework version: {__version__}")
```

## Next Steps

- [Quick Start Guide](quickstart.md)
- [Configuration Guide](configuration.md)
- [Basic Examples](../examples/basic.md)
