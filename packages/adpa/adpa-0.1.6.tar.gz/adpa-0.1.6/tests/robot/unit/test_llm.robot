*** Settings ***
Documentation     Unit tests for LLM functionality
Resource          ../resources/common.robot
Library           ../../adpa/llm/llm_utils.py
Library           Collections

*** Variables ***
${TEST_MODEL}         gpt-4
${TEST_PROMPT}        This is a test prompt
${TEST_API_KEY}       ${OPENAI_API_KEY}

*** Test Cases ***
Test LLM Connection
    [Documentation]    Test LLM API connection
    ${result}=    Connect To LLM    ${TEST_MODEL}    ${TEST_API_KEY}
    Should Not Be Equal    ${result}    ${None}

Test Send Prompt
    [Documentation]    Test sending prompt to LLM
    ${llm}=    Connect To LLM    ${TEST_MODEL}    ${TEST_API_KEY}
    ${response}=    Send Prompt    ${llm}    ${TEST_PROMPT}
    Should Not Be Empty    ${response}

Test Model Configuration
    [Documentation]    Test LLM model configuration
    ${llm}=    Connect To LLM    ${TEST_MODEL}    ${TEST_API_KEY}
    Configure Model    ${llm}    temperature=0.7    max_tokens=100
    ${config}=    Get Model Configuration    ${llm}
    Should Be Equal As Numbers    ${config.temperature}    0.7
    Should Be Equal As Numbers    ${config.max_tokens}    100

Test Error Handling
    [Documentation]    Test LLM error handling
    Run Keyword And Expect Error    *    Connect To LLM    invalid_model    ${TEST_API_KEY}

*** Keywords ***
Connect To LLM
    [Arguments]    ${model}    ${api_key}
    ${llm}=    Create LLM Connection    model=${model}    api_key=${api_key}
    RETURN    ${llm}

Send Prompt
    [Arguments]    ${llm}    ${prompt}
    ${response}=    Generate Response    ${llm}    ${prompt}
    RETURN    ${response}

Configure Model
    [Arguments]    ${llm}    ${temperature}=0.7    ${max_tokens}=100
    Set Model Configuration    ${llm}    temperature=${temperature}    max_tokens=${max_tokens}

Get Model Configuration
    [Arguments]    ${llm}
    ${config}=    Get Configuration    ${llm}
    RETURN    ${config}
