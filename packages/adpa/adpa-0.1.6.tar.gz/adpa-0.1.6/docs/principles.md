# ADPA Development Principles

Version 0.7.0

## Overview
This document outlines the core development principles and philosophy behind the ADPA framework.

For architectural details, see [Architecture Overview](/docs/architecture.md).

## Core Principles

1. **STRICT Standards Adherence**
   - NEVER modify established standards without explicit approval
   - Always ask before making any changes to standard patterns
   - Follow existing patterns exactly as documented

2. **Environment Variables**
   - ALWAYS use .env file for configuration
   - Never hardcode sensitive information
   - Use environment variables exactly as defined:
     ```
     openai_adpa1=<key>  # Primary OpenAI key
     OPENAI_API_KEY=<key>  # Fallback OpenAI key
     GROQ_API_KEY=<key>  # Groq API key
     ```

3. **API Standards**
   - Use official API formats without modification
   - Follow provider documentation exactly
   - Example OpenAI usage:
   ```python
   from openai import OpenAI
   
   client = OpenAI(
       api_key=os.environ.get("openai_adpa1"),  # Primary key from .env
       base_url="https://api.openai.com/v1"
   )
   ```

4. **Error Handling**
   - Pass through API provider error messages
   - Add context but don't modify original errors
   - Log errors for debugging

5. **Configuration**
   - Use .env for all configuration
   - Keep implementation simple and standard
   - Follow established patterns exactly

## Implementation Guidelines

1. **API Keys**
   - ALWAYS read from .env file
   - Use keys exactly as provided
   - Follow established naming conventions

2. **Library Usage**
   - Follow official examples exactly
   - No custom modifications without approval
   - Use stable, documented versions

3. **Error Management**
   - Preserve original error messages
   - Add context through wrapping
   - Maintain error traceability

## Version Control

1. **Dependencies**
   - Pin major versions in requirements.txt
   - Use >= for minor versions
   - Document changes in CHANGELOG.md

2. **API Versions**
   - Follow provider recommendations
   - Update for security fixes
   - Test before version changes
