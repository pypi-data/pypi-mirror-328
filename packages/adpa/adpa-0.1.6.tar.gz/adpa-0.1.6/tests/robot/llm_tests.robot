*** Settings ***
Documentation     Test suite for LLM functionality
Library           OperatingSystem
Library           Collections
Library           RequestsLibrary
Library           Process
Library           DateTime

Resource          keywords/llm_keywords.robot
Resource          keywords/validation_keywords.robot

Suite Setup       Initialize Test Environment
Suite Teardown    Cleanup Test Environment

*** Variables ***
${TEST_CONFIG}    ${CURDIR}/../resources/test_config.json
${TEST_PROMPTS}   ${CURDIR}/../resources/test_prompts.json
${TIMEOUT}        30s

*** Test Cases ***
Verify OpenAI LLM Configuration
    [Documentation]    Verify OpenAI LLM configuration loading
    [Tags]    config    openai
    ${config}=    Load LLM Configuration    openai
    Validate OpenAI Configuration    ${config}
    Should Have Required Fields    ${config}    model_id    base_model    temperature    max_tokens

Verify Gemini LLM Configuration
    [Documentation]    Verify Gemini LLM configuration loading
    [Tags]    config    gemini
    ${config}=    Load LLM Configuration    gemini
    Validate Gemini Configuration    ${config}
    Should Have Required Fields    ${config}    model_id    base_model    temperature    max_tokens

Verify Groq LLM Configuration
    [Documentation]    Verify Groq LLM configuration loading
    [Tags]    config    groq
    ${config}=    Load LLM Configuration    groq
    Validate Groq Configuration    ${config}
    Should Have Required Fields    ${config}    model_id    base_model    temperature    max_tokens

Test OpenAI Text Generation
    [Documentation]    Test text generation with OpenAI
    [Tags]    generation    openai
    ${prompt}=    Get Test Prompt    openai    simple
    ${result}=    Generate Text    openai    ${prompt}
    Validate Generation Result    ${result}
    Should Not Be Empty    ${result.text}

Test Gemini Text Generation
    [Documentation]    Test text generation with Gemini
    [Tags]    generation    gemini
    ${prompt}=    Get Test Prompt    gemini    simple
    ${result}=    Generate Text    gemini    ${prompt}
    Validate Generation Result    ${result}
    Should Not Be Empty    ${result.text}

Test Groq Text Generation
    [Documentation]    Test text generation with Groq
    [Tags]    generation    groq
    ${prompt}=    Get Test Prompt    groq    simple
    ${result}=    Generate Text    groq    ${prompt}
    Validate Generation Result    ${result}
    Should Not Be Empty    ${result.text}

Test OpenAI Chat Generation
    [Documentation]    Test chat generation with OpenAI
    [Tags]    generation    chat    openai
    ${messages}=    Get Test Chat Messages    openai
    ${result}=    Generate Chat Response    openai    ${messages}
    Validate Chat Result    ${result}
    Should Not Be Empty    ${result.text}

Test Gemini Chat Generation
    [Documentation]    Test chat generation with Gemini
    [Tags]    generation    chat    gemini
    ${messages}=    Get Test Chat Messages    gemini
    ${result}=    Generate Chat Response    gemini    ${messages}
    Validate Chat Result    ${result}
    Should Not Be Empty    ${result.text}

Test OpenAI Embeddings
    [Documentation]    Test embedding generation with OpenAI
    [Tags]    embeddings    openai
    ${text}=    Get Test Text    openai    embedding
    ${result}=    Generate Embeddings    openai    ${text}
    Validate Embedding Result    ${result}
    Length Should Be    ${result.embeddings}    1

Test Gemini Embeddings
    [Documentation]    Test embedding generation with Gemini
    [Tags]    embeddings    gemini
    ${text}=    Get Test Text    gemini    embedding
    ${result}=    Generate Embeddings    gemini    ${text}
    Validate Embedding Result    ${result}
    Length Should Be    ${result.embeddings}    1

Test Error Handling - Invalid API Key
    [Documentation]    Test error handling with invalid API key
    [Tags]    error    auth
    Set Invalid API Key
    Run Keyword And Expect Error    *AuthenticationError*    Generate Text    openai    test
    Reset API Key

Test Error Handling - Rate Limit
    [Documentation]    Test rate limit error handling
    [Tags]    error    rate_limit
    Simulate Rate Limit
    ${error}=    Run Keyword And Expect Error    *RateLimitError*    Generate Rapid Requests
    Should Contain    ${error}    retry_after
    Reset Rate Limit

Test Error Handling - Token Limit
    [Documentation]    Test token limit error handling
    [Tags]    error    token_limit
    ${long_text}=    Generate Long Text
    ${error}=    Run Keyword And Expect Error    *TokenLimitError*    Generate Text    openai    ${long_text}
    Should Contain    ${error}    token_limit

Test Error Handling - Network Error
    [Documentation]    Test network error handling
    [Tags]    error    network
    Simulate Network Error
    ${error}=    Run Keyword And Expect Error    *NetworkError*    Generate Text    openai    test
    Should Contain    ${error}    status_code
    Reset Network

Test Error Handling - Timeout
    [Documentation]    Test timeout error handling
    [Tags]    error    timeout
    Set Short Timeout
    ${error}=    Run Keyword And Expect Error    *TimeoutError*    Generate Text    openai    test
    Should Contain    ${error}    timeout
    Reset Timeout

*** Keywords ***
Initialize Test Environment
    Load Test Configuration
    Set Environment Variables
    Initialize LLM Clients

Cleanup Test Environment
    Reset Environment Variables
    Cleanup LLM Clients
