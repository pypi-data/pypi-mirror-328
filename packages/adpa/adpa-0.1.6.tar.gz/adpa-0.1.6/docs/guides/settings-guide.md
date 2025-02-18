# ADPA Settings Guide

Version 0.7.0

## Overview
The ADPA settings system provides a centralized way to manage configuration for the entire application. It handles everything from API keys to application behavior settings.

## Settings Location
Settings are stored in the following location:
- Config directory: `~/.adpa/`
- Config file: `~/.adpa/config.json`

## Available Settings

### API Settings
- `openai_api_key`: OpenAI API key for language model access
- `tavily_api_key`: Tavily API key for search functionality

### Application Settings
- `debug_mode`: Enable detailed logging and debug information (default: false)
- `max_tokens`: Maximum tokens per API request (default: 2000)
- `version`: Application version string

## Setting Values

### Via Environment Variables
API keys can be set using environment variables:
```bash
export OPENAI_API_KEY="your-key-here"
export TAVILY_API_KEY="your-key-here"
```

### Via Configuration File
Create or edit `~/.adpa/config.json`:
```json
{
    "openai_api_key": "your-key-here",
    "tavily_api_key": "your-key-here",
    "debug_mode": false,
    "max_tokens": 2000
}
```

### Via UI
Settings can be modified through the Settings page in the ADPA web interface:
1. Navigate to the Settings page
2. Expand the relevant settings section
3. Modify values as needed
4. Changes are automatically saved

## Programmatic Usage

### Loading Settings
```python
from adpa.config import Settings

# Initialize settings (automatically loads from config)
settings = Settings()

# Access settings
api_key = settings.openai_api_key
max_tokens = settings.max_tokens
```

### Saving Settings
```python
# Modify and save settings
settings.debug_mode = True
settings.save()
```

## Best Practices
1. Never hardcode API keys in your code
2. Use environment variables for sensitive information
3. Use the Settings class instead of accessing the config file directly
4. Always handle potential configuration errors gracefully

## Troubleshooting

### Missing API Keys
1. Check environment variables are set correctly
2. Verify config file exists and has correct permissions
3. Ensure keys are valid and active

### Configuration Issues
1. Delete config file to reset to defaults
2. Check file permissions
3. Verify JSON syntax in config file

## Security Notes
- API keys are sensitive information
- Never commit API keys to version control
- Use environment variables in production
- Regularly rotate API keys for security
