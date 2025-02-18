*** Settings ***
Documentation     Technical tests for web interface components
Resource          ../../resources/web.resource
Library           SeleniumLibrary
Library           Collections

*** Variables ***
${BROWSER}        chrome
${BASE_URL}       http://localhost:8000
${USERNAME}       test_user
${PASSWORD}       test_pass

*** Test Cases ***
Test Page Loading Performance
    [Documentation]    Test page load times
    [Tags]    technical    performance
    Open Browser    ${BASE_URL}    ${BROWSER}
    ${start_time}=    Get Time    epoch
    Go To    ${BASE_URL}/dashboard
    ${end_time}=    Get Time    epoch
    ${load_time}=    Evaluate    ${end_time} - ${start_time}
    Should Be True    ${load_time} < 3.0
    [Teardown]    Close Browser

Test Component Rendering
    [Documentation]    Test UI component rendering
    [Tags]    technical    ui
    Open Browser    ${BASE_URL}    ${BROWSER}
    Page Should Contain Element    id=header
    Page Should Contain Element    id=sidebar
    Page Should Contain Element    id=main-content
    Verify Component Styling    header
    Verify Component Styling    sidebar
    [Teardown]    Close Browser

Test Responsive Design
    [Documentation]    Test responsive layout
    [Tags]    technical    responsive
    @{viewports}=    Create List    
    ...    mobile=375x667    
    ...    tablet=768x1024    
    ...    desktop=1920x1080
    FOR    ${viewport}    IN    @{viewports}
        Set Window Size    ${viewport}
        Verify Responsive Layout
    END

Test User Authentication
    [Documentation]    Test authentication flow
    [Tags]    technical    auth
    Open Browser    ${BASE_URL}/login    ${BROWSER}
    Input Text    username    ${USERNAME}
    Input Password    password    ${PASSWORD}
    Click Button    Login
    Wait Until Page Contains Element    id=dashboard
    Verify Authentication State
    [Teardown]    Close Browser

Test Form Validation
    [Documentation]    Test form input validation
    [Tags]    technical    validation
    Open Browser    ${BASE_URL}/form    ${BROWSER}
    @{test_cases}=    Create List
    ...    valid_input
    ...    invalid_input
    ...    special_chars
    ...    sql_injection
    FOR    ${test}    IN    @{test_cases}
        Run Form Validation Test    ${test}
    END
    [Teardown]    Close Browser

Test API Integration
    [Documentation]    Test frontend-API integration
    [Tags]    technical    api
    Open Browser    ${BASE_URL}/data    ${BROWSER}
    Click Button    Load Data
    Wait For API Response
    Verify Data Display
    Verify Error Handling
    [Teardown]    Close Browser

Test State Management
    [Documentation]    Test application state handling
    [Tags]    technical    state
    Open Browser    ${BASE_URL}    ${BROWSER}
    Perform State Changes
    Verify State Consistency
    Test State Persistence
    [Teardown]    Close Browser

Test Event Handling
    [Documentation]    Test UI event handling
    [Tags]    technical    events
    Open Browser    ${BASE_URL}    ${BROWSER}
    @{events}=    Create List    click    hover    scroll    drag
    FOR    ${event}    IN    @{events}
        Test Event Handler    ${event}
    END
    [Teardown]    Close Browser

Test Error Recovery
    [Documentation]    Test UI error recovery
    [Tags]    technical    error
    Open Browser    ${BASE_URL}    ${BROWSER}
    Simulate Error Conditions
    Verify Error Messages
    Test Recovery Actions
    [Teardown]    Close Browser

Test Performance Optimization
    [Documentation]    Test UI performance
    [Tags]    technical    performance
    Open Browser    ${BASE_URL}    ${BROWSER}
    Measure Page Metrics
    Verify Resource Loading
    Check Memory Usage
    [Teardown]    Close Browser

*** Keywords ***
Verify Component Styling
    [Arguments]    ${component}
    ${styles}=    Get Element Attribute    id=${component}    style
    Should Not Be Empty    ${styles}

Verify Responsive Layout
    Element Should Be Visible    id=header
    Element Should Be Visible    id=main-content
    ${layout}=    Get Window Size
    Run Keyword If    ${layout.width} < 768    Verify Mobile Layout
    ...    ELSE IF    ${layout.width} < 1024    Verify Tablet Layout
    ...    ELSE    Verify Desktop Layout

Run Form Validation Test
    [Arguments]    ${test_case}
    ${input}=    Get Test Input    ${test_case}
    Input Text    test-form    ${input}
    Click Button    Submit
    Verify Validation Result    ${test_case}

Wait For API Response
    Wait Until Element Is Visible    id=data-container    timeout=10s
    ${status}=    Get Element Attribute    id=data-container    data-loaded
    Should Be Equal    ${status}    true
