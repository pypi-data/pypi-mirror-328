# -*- coding: utf-8 -*-
"""Environment variables for Robot Framework tests."""
import os

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'test_openai_key')
AZURE_API_KEY = os.getenv('AZURE_API_KEY', 'test_azure_key')
AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT', 'https://test-azure-endpoint.openai.azure.com/')
GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'test_groq_key')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'test_gemini_key')

# Database Configuration
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE', 'adpa_test')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'adpa_test')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'test_password')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', '5432'))

# Test Configuration
BROWSER = os.getenv('BROWSER', 'chrome')
HEADLESS = os.getenv('HEADLESS', 'True').lower() == 'true'
TEST_URL = os.getenv('TEST_URL', 'http://localhost:8000')

# Performance Settings
RESPONSE_TIME_LIMIT = int(os.getenv('RESPONSE_TIME_LIMIT', '5'))
CONCURRENT_USERS = int(os.getenv('CONCURRENT_USERS', '10'))
MEMORY_LIMIT_MB = int(os.getenv('MEMORY_LIMIT_MB', '512'))
