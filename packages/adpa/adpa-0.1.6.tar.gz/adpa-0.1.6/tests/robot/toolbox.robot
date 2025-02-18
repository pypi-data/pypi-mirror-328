*** Settings ***
Documentation     Test suite for Toolbox functionality
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections
Resource          resources/common.robot
Suite Setup       Initialize Toolbox Tests
Suite Teardown    Clean Up Toolbox Tests

*** Variables ***
${TOOL_NAME}      TestTool
${TOOL_CONFIG}    {"api_key": "test_key", "endpoint": "test_endpoint"}

*** Test Cases ***
Test Tool Management
    [Documentation]    Test adding and managing tools
    Go To    ${URL}
    Click Link    Toolbox
    Click Button    Add Tool
    Input Text    name    ${TOOL_NAME}
    Input Text    config    ${TOOL_CONFIG}
    Click Button    Save
    Wait Until Page Contains    Tool added successfully
    Page Should Contain    ${TOOL_NAME}

Test Tool Configuration
    [Documentation]    Test configuring tool settings
    Go To Tool Settings    ${TOOL_NAME}
    Input Text    endpoint    new_endpoint
    Click Button    Update Settings
    Wait Until Page Contains    Settings updated
    Page Should Contain    endpoint: new_endpoint

Test Tool Integration
    [Documentation]    Test tool integration with agents
    Go To    ${URL}
    Click Link    Toolbox
    Click Element    css=[data-tool="${TOOL_NAME}"] .integrate-btn
    Select From List By Value    agent    TestAgent
    Click Button    Integrate
    Wait Until Page Contains    Tool integrated successfully
    Page Should Contain    Integrated with TestAgent

Test Tool Execution
    [Documentation]    Test executing tool functions
    Go To    ${URL}
    Click Link    Toolbox
    Click Element    css=[data-tool="${TOOL_NAME}"] .execute-btn
    Input Text    params    {"param1": "value1"}
    Click Button    Execute
    Wait Until Element Is Visible    css=.execution-results
    Element Should Not Be Empty    css=.execution-results

Test Tool Permissions
    [Documentation]    Test tool permission management
    Go To    ${URL}
    Click Link    Toolbox
    Click Element    css=[data-tool="${TOOL_NAME}"] .permissions-btn
    Select Checkbox    allow_agent_use
    Select Checkbox    require_confirmation
    Click Button    Save Permissions
    Wait Until Page Contains    Permissions updated
    Checkbox Should Be Selected    allow_agent_use
    Checkbox Should Be Selected    require_confirmation

Test Tool Deletion
    [Documentation]    Test deleting a tool
    Go To    ${URL}
    Click Link    Toolbox
    Click Element    css=[data-tool="${TOOL_NAME}"] .delete-btn
    Handle Alert    accept
    Wait Until Page Contains    Tool deleted
    Page Should Not Contain    ${TOOL_NAME}

*** Keywords ***
Initialize Toolbox Tests
    Open Browser    ${URL}    ${BROWSER}
    Set Window Size    1920    1080
    Wait Until Page Contains    ADPA

Clean Up Toolbox Tests
    Delete All Test Tools
    Close All Browsers

Go To Tool Settings
    [Arguments]    ${name}
    Go To    ${URL}/toolbox
    Click Element    css=[data-tool="${name}"] .settings-btn

Delete All Test Tools
    Go To    ${URL}/toolbox
    @{test_tools}=    Get WebElements    css=[data-tool^="Test"]
    FOR    ${tool}    IN    @{test_tools}
        Click Element    ${tool} .delete-btn
        Handle Alert    accept
        Wait Until Page Contains    Tool deleted
