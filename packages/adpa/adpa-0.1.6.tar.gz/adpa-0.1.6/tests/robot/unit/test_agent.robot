*** Settings ***
Documentation     Unit tests for Agent functionality
Resource          ../resources/common.robot
Library           ../../adpa/agents/agent.py
Library           Collections

*** Variables ***
${AGENT_NAME}     TestAgent
${PROMPT}         This is a test prompt
${MODEL}          gpt-4
${API_KEY}        ${OPENAI_API_KEY}

*** Test Cases ***
Test Agent Creation
    [Documentation]    Test creating a new agent
    ${agent}=    Create Test Agent
    Should Not Be Empty    ${agent}
    Should Be Equal    ${agent.name}    ${AGENT_NAME}

Test Agent Response
    [Documentation]    Test agent response generation
    ${agent}=    Create Test Agent
    ${response}=    Get Agent Response    ${agent}    Hello
    Should Not Be Empty    ${response}
    Should Be String    ${response}

Test Agent Memory
    [Documentation]    Test agent memory/history
    ${agent}=    Create Test Agent
    Send Message    ${agent}    Hello
    Send Message    ${agent}    How are you?
    ${history}=    Get History    ${agent}
    Length Should Be    ${history}    4

Test Agent Configuration
    [Documentation]    Test agent configuration
    ${agent}=    Create Test Agent    CustomAgent    temperature=0.8
    Should Be Equal    ${agent.name}    CustomAgent
    Should Be Equal    ${agent.temperature}    0.8

Test Agent Error Handling
    [Documentation]    Test agent error handling
    ${agent}=    Create Test Agent
    Run Keyword And Expect Error    *    Send Invalid Message    ${agent}

*** Keywords ***
Create Test Agent
    [Arguments]    ${name}=${AGENT_NAME}    ${temperature}=0.7
    ${agent}=    Create Agent Instance    
    ...    name=${name}    
    ...    temperature=${temperature}    
    ...    model=${MODEL}    
    ...    api_key=${API_KEY}
    RETURN    ${agent}

Get Agent Response
    [Arguments]    ${agent}    ${message}
    ${response}=    Send Message    ${agent}    ${message}
    RETURN    ${response}

Send Invalid Message
    [Arguments]    ${agent}
    Send Message    ${agent}    ${EMPTY}

Get History
    [Arguments]    ${agent}
    ${history}=    Get Conversation History    ${agent}
    RETURN    ${history}
