*** Settings ***
Documentation     Environment variables for testing

*** Variables ***
# API Keys
${OPENAI_API_KEY}        %{OPENAI_API_KEY}
${AZURE_API_KEY}         %{AZURE_API_KEY}
${AZURE_ENDPOINT}        %{AZURE_ENDPOINT}
${GROQ_API_KEY}         %{GROQ_API_KEY}
${GEMINI_API_KEY}       %{GEMINI_API_KEY}

# Database Configuration
${POSTGRES_DATABASE}    %{POSTGRES_DATABASE}
${POSTGRES_USER}       %{POSTGRES_USER}
${POSTGRES_PASSWORD}   %{POSTGRES_PASSWORD}
${POSTGRES_HOST}       %{POSTGRES_HOST}
${POSTGRES_PORT}       %{POSTGRES_PORT}

# Test Configuration
${BROWSER}            %{BROWSER}
${HEADLESS}          %{HEADLESS}
${TEST_URL}          %{TEST_URL}

# Performance Settings
${RESPONSE_TIME_LIMIT}    %{RESPONSE_TIME_LIMIT}
${CONCURRENT_USERS}       %{CONCURRENT_USERS}
${MEMORY_LIMIT_MB}        %{MEMORY_LIMIT_MB}
