*** Settings ***
Documentation     Keywords for LLM testing
Library           OperatingSystem
Library           Collections
Library           RequestsLibrary
Library           Process
Library           DateTime

*** Variables ***
${CONFIG_FILE}    ${CURDIR}/../../resources/test_config.json
${API_TIMEOUT}    30

*** Keywords ***
Load LLM Configuration
    [Arguments]    ${provider}
    [Documentation]    Load configuration for specified provider
    ${config}=    Get File    ${CONFIG_FILE}
    ${config}=    Evaluate    json.loads('''${config}''')    json
    [Return]    ${config["models"]["${provider}"]}

Generate Text
    [Arguments]    ${provider}    ${prompt}
    [Documentation]    Generate text using specified provider
    ${client}=    Get LLM Client    ${provider}
    ${result}=    Run Keyword    Generate With ${provider}    ${client}    ${prompt}
    [Return]    ${result}

Generate Chat Response
    [Arguments]    ${provider}    ${messages}
    [Documentation]    Generate chat response using specified provider
    ${client}=    Get LLM Client    ${provider}
    ${result}=    Run Keyword    Chat With ${provider}    ${client}    ${messages}
    [Return]    ${result}

Generate Embeddings
    [Arguments]    ${provider}    ${text}
    [Documentation]    Generate embeddings using specified provider
    ${client}=    Get LLM Client    ${provider}
    ${result}=    Run Keyword    Get Embeddings From ${provider}    ${client}    ${text}
    [Return]    ${result}

Get LLM Client
    [Arguments]    ${provider}
    [Documentation]    Get LLM client instance
    ${module}=    Evaluate    importlib.import_module('adpa.llms.${provider}.client')    importlib
    ${config}=    Load LLM Configuration    ${provider}
    ${client}=    Run Keyword    Create ${provider} Client    ${config}
    [Return]    ${client}

Create OpenAI Client
    [Arguments]    ${config}
    [Documentation]    Create OpenAI client instance
    ${client}=    Evaluate    OpenAILLM('${config["id"]}')
    [Return]    ${client}

Create Gemini Client
    [Arguments]    ${config}
    [Documentation]    Create Gemini client instance
    ${client}=    Evaluate    GeminiLLM('${config["id"]}')
    [Return]    ${client}

Create Groq Client
    [Arguments]    ${config}
    [Documentation]    Create Groq client instance
    ${client}=    Evaluate    GroqLLM('${config["id"]}')
    [Return]    ${client}

Generate With OpenAI
    [Arguments]    ${client}    ${prompt}
    [Documentation]    Generate text using OpenAI
    ${result}=    Run Keyword And Return    Generate Async    ${client}    ${prompt}
    [Return]    ${result}

Generate With Gemini
    [Arguments]    ${client}    ${prompt}
    [Documentation]    Generate text using Gemini
    ${result}=    Run Keyword And Return    Generate Async    ${client}    ${prompt}
    [Return]    ${result}

Generate With Groq
    [Arguments]    ${client}    ${prompt}
    [Documentation]    Generate text using Groq
    ${result}=    Run Keyword And Return    Generate Async    ${client}    ${prompt}
    [Return]    ${result}

Chat With OpenAI
    [Arguments]    ${client}    ${messages}
    [Documentation]    Generate chat response using OpenAI
    ${result}=    Run Keyword And Return    Generate Async    ${client}    ${messages}
    [Return]    ${result}

Chat With Gemini
    [Arguments]    ${client}    ${messages}
    [Documentation]    Generate chat response using Gemini
    ${result}=    Run Keyword And Return    Generate Async    ${client}    ${messages}
    [Return]    ${result}

Chat With Groq
    [Arguments]    ${client}    ${messages}
    [Documentation]    Generate chat response using Groq
    ${result}=    Run Keyword And Return    Generate Async    ${client}    ${messages}
    [Return]    ${result}

Get Embeddings From OpenAI
    [Arguments]    ${client}    ${text}
    [Documentation]    Generate embeddings using OpenAI
    ${result}=    Run Keyword And Return    Embed Async    ${client}    ${text}
    [Return]    ${result}

Get Embeddings From Gemini
    [Arguments]    ${client}    ${text}
    [Documentation]    Generate embeddings using Gemini
    ${result}=    Run Keyword And Return    Embed Async    ${client}    ${text}
    [Return]    ${result}

Generate Async
    [Arguments]    ${client}    ${input}
    [Documentation]    Generate response asynchronously
    ${result}=    Evaluate    asyncio.run(${client}.generate(${input}))    asyncio
    [Return]    ${result}

Embed Async
    [Arguments]    ${client}    ${text}
    [Documentation]    Generate embeddings asynchronously
    ${result}=    Evaluate    asyncio.run(${client}.embed(${text}))    asyncio
    [Return]    ${result}

Set Invalid API Key
    [Documentation]    Set invalid API key for testing
    Set Environment Variable    OPENAI_API_KEY    invalid_key
    Set Environment Variable    GOOGLE_API_KEY    invalid_key
    Set Environment Variable    GROQ_API_KEY    invalid_key

Reset API Key
    [Documentation]    Reset API keys to original values
    ${config}=    Get File    ${CONFIG_FILE}
    ${config}=    Evaluate    json.loads('''${config}''')    json
    Set Environment Variable    OPENAI_API_KEY    ${config["api_keys"]["openai"]}
    Set Environment Variable    GOOGLE_API_KEY    ${config["api_keys"]["google"]}
    Set Environment Variable    GROQ_API_KEY    ${config["api_keys"]["groq"]}

Simulate Rate Limit
    [Documentation]    Simulate rate limit condition
    Set Environment Variable    SIMULATE_RATE_LIMIT    true

Reset Rate Limit
    [Documentation]    Reset rate limit simulation
    Set Environment Variable    SIMULATE_RATE_LIMIT    false

Generate Long Text
    [Documentation]    Generate text exceeding token limit
    ${text}=    Evaluate    "test " * 100000
    [Return]    ${text}

Simulate Network Error
    [Documentation]    Simulate network error condition
    Set Environment Variable    SIMULATE_NETWORK_ERROR    true

Reset Network
    [Documentation]    Reset network error simulation
    Set Environment Variable    SIMULATE_NETWORK_ERROR    false

Set Short Timeout
    [Documentation]    Set short timeout for testing
    Set Environment Variable    API_TIMEOUT    0.1

Reset Timeout
    [Documentation]    Reset timeout to default value
    Set Environment Variable    API_TIMEOUT    ${API_TIMEOUT}
