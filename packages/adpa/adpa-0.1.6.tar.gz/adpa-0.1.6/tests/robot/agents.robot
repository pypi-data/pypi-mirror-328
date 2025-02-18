*** Settings ***
Documentation     Test suite for Agent functionality
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections
Resource          resources/common.robot
Suite Setup       Initialize Agent Tests
Suite Teardown    Clean Up Agent Tests

*** Variables ***
${AGENT_NAME}     TestAgent
${AGENT_TYPE}     research
${AGENT_CONFIG}   {"model": "gpt-4", "temperature": 0.7}

*** Test Cases ***
Create New Agent
    [Documentation]    Test creating a new agent
    Go To    ${URL}
    Click Link    Agents
    Click Button    Create New Agent
    Input Text    name    ${AGENT_NAME}
    Select From List By Value    type    ${AGENT_TYPE}
    Input Text    config    ${AGENT_CONFIG}
    Click Button    Save
    Wait Until Page Contains    Agent created successfully
    Page Should Contain    ${AGENT_NAME}

Configure Agent Settings
    [Documentation]    Test configuring agent settings
    Go To Agent Settings    ${AGENT_NAME}
    Input Text    temperature    0.8
    Click Button    Update Settings
    Wait Until Page Contains    Settings updated
    Page Should Contain    temperature: 0.8

Test Agent Interaction
    [Documentation]    Test basic agent interaction
    Go To Agent Chat    ${AGENT_NAME}
    Input Text    message-input    Hello, can you help me?
    Click Button    Send
    Wait Until Element Is Visible    css=.agent-response
    Element Should Contain    css=.agent-response    help

Delete Agent
    [Documentation]    Test deleting an agent
    Go To    ${URL}/agents
    Click Element    css=[data-agent="${AGENT_NAME}"] .delete-btn
    Handle Alert    accept
    Wait Until Page Contains    Agent deleted
    Page Should Not Contain    ${AGENT_NAME}

*** Keywords ***
Initialize Agent Tests
    Open Browser    ${URL}    ${BROWSER}
    Set Window Size    1920    1080
    Wait Until Page Contains    ADPA

Clean Up Agent Tests
    Delete All Test Agents
    Close All Browsers

Go To Agent Settings
    [Arguments]    ${name}
    Go To    ${URL}/agents
    Click Element    css=[data-agent="${name}"] .settings-btn

Go To Agent Chat
    [Arguments]    ${name}
    Go To    ${URL}/agents
    Click Element    css=[data-agent="${name}"] .chat-btn

Delete All Test Agents
    Go To    ${URL}/agents
    @{test_agents}=    Get WebElements    css=[data-agent^="Test"]
    FOR    ${agent}    IN    @{test_agents}
        Click Element    ${agent} .delete-btn
        Handle Alert    accept
        Wait Until Page Contains    Agent deleted
