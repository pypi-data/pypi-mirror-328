*** Settings ***
Documentation     Keywords for validation in LLM testing
Library           Collections
Library           String

*** Keywords ***
Validate OpenAI Configuration
    [Arguments]    ${config}
    [Documentation]    Validate OpenAI configuration
    Should Not Be Empty    ${config}
    Dictionary Should Contain Key    ${config}    base_model
    Dictionary Should Contain Key    ${config}    temperature
    Dictionary Should Contain Key    ${config}    max_tokens
    Should Match Regexp    ${config["base_model"]}    ^gpt-.*$

Validate Gemini Configuration
    [Arguments]    ${config}
    [Documentation]    Validate Gemini configuration
    Should Not Be Empty    ${config}
    Dictionary Should Contain Key    ${config}    base_model
    Dictionary Should Contain Key    ${config}    temperature
    Dictionary Should Contain Key    ${config}    max_tokens
    Should Match Regexp    ${config["base_model"]}    ^gemini-.*$

Validate Groq Configuration
    [Arguments]    ${config}
    [Documentation]    Validate Groq configuration
    Should Not Be Empty    ${config}
    Dictionary Should Contain Key    ${config}    base_model
    Dictionary Should Contain Key    ${config}    temperature
    Dictionary Should Contain Key    ${config}    max_tokens
    Should Match Regexp    ${config["base_model"]}    ^llama2-.*$

Should Have Required Fields
    [Arguments]    ${config}    @{fields}
    [Documentation]    Validate required fields in configuration
    FOR    ${field}    IN    @{fields}
        Dictionary Should Contain Key    ${config}    ${field}
        Should Not Be Empty    ${config["${field}"]}
    END

Validate Generation Result
    [Arguments]    ${result}
    [Documentation]    Validate text generation result
    Should Not Be Empty    ${result}
    Dictionary Should Contain Key    ${result}    text
    Dictionary Should Contain Key    ${result}    model
    Dictionary Should Contain Key    ${result}    usage
    Validate Usage Data    ${result["usage"]}

Validate Chat Result
    [Arguments]    ${result}
    [Documentation]    Validate chat generation result
    Should Not Be Empty    ${result}
    Dictionary Should Contain Key    ${result}    text
    Dictionary Should Contain Key    ${result}    model
    Dictionary Should Contain Key    ${result}    usage
    Validate Usage Data    ${result["usage"]}

Validate Embedding Result
    [Arguments]    ${result}
    [Documentation]    Validate embedding generation result
    Should Not Be Empty    ${result}
    Dictionary Should Contain Key    ${result}    embeddings
    Dictionary Should Contain Key    ${result}    model
    Dictionary Should Contain Key    ${result}    usage
    Validate Usage Data    ${result["usage"]}
    @{embeddings}=    Set Variable    ${result["embeddings"]}
    Should Not Be Empty    ${embeddings}
    FOR    ${embedding}    IN    @{embeddings}
        Should Be True    ${embedding.__class__.__name__} == 'list'
        Length Should Be Greater Than    ${embedding}    0
    END

Validate Usage Data
    [Arguments]    ${usage}
    [Documentation]    Validate usage data in result
    Dictionary Should Contain Key    ${usage}    total_tokens
    ${total_tokens}=    Convert To Integer    ${usage["total_tokens"]}
    Should Be True    ${total_tokens} > 0
    Run Keyword If    'prompt_tokens' in ${usage}    Validate Token Count    ${usage["prompt_tokens"]}
    Run Keyword If    'completion_tokens' in ${usage}    Validate Token Count    ${usage["completion_tokens"]}

Validate Token Count
    [Arguments]    ${token_count}
    [Documentation]    Validate token count is positive integer
    ${count}=    Convert To Integer    ${token_count}
    Should Be True    ${count} >= 0
