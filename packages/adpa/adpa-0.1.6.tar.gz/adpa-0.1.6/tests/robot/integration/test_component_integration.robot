*** Settings ***
Documentation     Integration tests between different system components
Resource          ../resources/test_utils.resource
Resource          ../resources/common.resource
Resource          ../resources/api.resource
Resource          ../resources/web.resource
Resource          ../resources/workflow.resource

*** Test Cases ***
Test Web UI To API Integration
    [Documentation]    Test data flow from Web UI to API endpoints
    [Tags]    integration    web    api
    Given Web UI Is Running
    And API Server Is Available
    When User Submits Data Through UI
    Then Data Should Reach API Endpoint
    And Response Should Be Properly Handled By UI

Test API To Database Integration
    [Documentation]    Test data persistence through API
    [Tags]    integration    api    database
    Given API Server Is Running
    And Database Is Connected
    When API Receives Data Mutation Request
    Then Data Should Be Persisted In Database
    And Database Triggers Should Execute

Test Workflow To Tools Integration
    [Documentation]    Test workflow tool execution
    [Tags]    integration    workflow    tools
    Given Workflow Engine Is Running
    And Required Tools Are Available
    When Workflow Triggers Tool Execution
    Then Tool Should Process Data
    And Results Should Return To Workflow

Test Research Pipeline Integration
    [Documentation]    Test complete research workflow
    [Tags]    integration    research    pipeline
    Given Research Project Is Created
    When Analysis Pipeline Is Triggered
    Then Data Should Flow Through Components
    And Results Should Be Properly Aggregated
    And Reports Should Be Generated

Test Real-time Collaboration Integration
    [Documentation]    Test multi-user collaboration features
    [Tags]    integration    collaboration
    Given Multiple Users Are Connected
    When Users Work On Same Data
    Then Changes Should Sync Across Sessions
    And Conflicts Should Be Prevented
    And Notifications Should Be Delivered

Test Security Integration
    [Documentation]    Test security across components
    [Tags]    integration    security
    Given User Authentication Is Required
    When Accessing Protected Resources
    Then Auth Should Be Verified At All Layers
    And Access Should Be Properly Logged
    And Security Policies Should Be Enforced

*** Keywords ***
Given Web UI Is Running
    Connect To Web Server
    Verify UI Components

Given API Server Is Available
    Connect To API
    Verify API Health

When User Submits Data Through UI
    ${test_data}=    Generate Random Test Data    string
    Submit Form Data    ${test_data}
    Set Test Variable    ${SUBMITTED_DATA}    ${test_data}

Then Data Should Reach API Endpoint
    ${api_data}=    Get API Data
    Should Be Equal    ${api_data}    ${SUBMITTED_DATA}

And Response Should Be Properly Handled By UI
    Wait Until Element Contains    id=response    success
    Verify UI Update

Given Workflow Engine Is Running
    Connect To Workflow Engine
    Verify Engine Status

When Workflow Triggers Tool Execution
    ${workflow}=    Create Test Workflow
    Start Workflow    ${workflow}
    Set Test Variable    ${CURRENT_WORKFLOW}    ${workflow}

Then Tool Should Process Data
    Wait Until Keyword Succeeds    1 min    5 sec    Check Tool Execution
    Verify Tool Results

And Results Should Return To Workflow
    ${results}=    Get Workflow Results    ${CURRENT_WORKFLOW}
    Verify Results Quality    ${results}

Given Multiple Users Are Connected
    ${users}=    Create Test Users
    Connect Users    ${users}
    Set Test Variable    ${TEST_USERS}    ${users}

When Users Work On Same Data
    ${shared_data}=    Create Shared Resource
    Simulate Concurrent Access    ${TEST_USERS}    ${shared_data}
    Set Test Variable    ${SHARED_DATA}    ${shared_data}

Then Changes Should Sync Across Sessions
    Wait Until Synchronized    ${TEST_USERS}    ${SHARED_DATA}
    Verify Data Consistency    ${TEST_USERS}    ${SHARED_DATA}
