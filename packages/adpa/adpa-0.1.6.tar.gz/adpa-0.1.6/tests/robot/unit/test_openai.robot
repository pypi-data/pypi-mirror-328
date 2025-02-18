*** Settings ***
Documentation     Unit tests for OpenAI integration
Resource          ../resources/common.robot
Library           ../../adpa/llm/openai_utils.py
Library           Collections

*** Variables ***
${MODEL}         gpt-4
${API_KEY}       ${OPENAI_API_KEY}
${AZURE_KEY}     ${AZURE_API_KEY}
${ENDPOINT}      ${AZURE_ENDPOINT}

*** Test Cases ***
Test OpenAI Connection
    [Documentation]    Test OpenAI API connection
    ${client}=    Create OpenAI Client    ${API_KEY}
    Should Not Be Equal    ${client}    ${None}

Test Azure OpenAI Connection
    [Documentation]    Test Azure OpenAI connection
    ${client}=    Create Azure Client    ${AZURE_KEY}    ${ENDPOINT}
    Should Not Be Equal    ${client}    ${None}

Test Model List
    [Documentation]    Test getting available models
    ${client}=    Create OpenAI Client    ${API_KEY}
    ${models}=    List Models    ${client}
    Should Not Be Empty    ${models}

Test Chat Completion
    [Documentation]    Test chat completion
    ${client}=    Create OpenAI Client    ${API_KEY}
    ${response}=    Generate Chat Response    ${client}    What is 2+2?
    Should Not Be Empty    ${response}

Test Streaming Response
    [Documentation]    Test streaming response
    ${client}=    Create OpenAI Client    ${API_KEY}
    ${stream}=    Generate Streaming Response    ${client}    Count to 3
    @{chunks}=    Create List
    FOR    ${chunk}    IN    @{stream}
        Append To List    ${chunks}    ${chunk}
    END
    Length Should Be    ${chunks}    > 0

Test Error Handling
    [Documentation]    Test error handling
    Run Keyword And Expect Error    *    Create OpenAI Client    invalid_key

*** Keywords ***
Create OpenAI Client
    [Arguments]    ${api_key}
    ${client}=    Initialize OpenAI    api_key=${api_key}
    RETURN    ${client}

Create Azure Client
    [Arguments]    ${api_key}    ${endpoint}
    ${client}=    Initialize Azure OpenAI    api_key=${api_key}    endpoint=${endpoint}
    RETURN    ${client}

List Models
    [Arguments]    ${client}
    ${models}=    Get Available Models    ${client}
    RETURN    ${models}

Generate Chat Response
    [Arguments]    ${client}    ${prompt}
    ${response}=    Chat Complete    ${client}    ${prompt}
    RETURN    ${response}

Generate Streaming Response
    [Arguments]    ${client}    ${prompt}
    ${stream}=    Stream Complete    ${client}    ${prompt}
    RETURN    ${stream}
