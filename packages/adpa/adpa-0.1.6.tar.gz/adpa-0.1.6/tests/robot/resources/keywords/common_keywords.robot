*** Settings ***
Documentation    Common keywords used across all test suites
Library    SeleniumLibrary
Library    RequestsLibrary
Library    DatabaseLibrary
Library    OperatingSystem
Library    Collections
Resource    ../variables.robot

*** Keywords ***
Setup Test Environment
    [Documentation]    Setup common test environment
    [Arguments]    ${clear_db}=${TRUE}
    Create Session    api    ${API_BASE_URL}
    Run Keyword If    ${clear_db}    Reset Test Database

Reset Test Database
    [Documentation]    Reset the test database to a known state
    Connect To Database    psycopg2    ${TEST_DATABASE}    ${VALID_USERNAME}    ${VALID_PASSWORD}    localhost    5432
    Execute SQL Script    ${SQL_SCRIPTS_DIR}/reset_db.sql
    Disconnect From Database

Start Browser Session
    [Documentation]    Start browser session with common settings
    ${options}=    Create Dictionary    
    ...    args=["--headless"] if ${HEADLESS} else []
    Open Browser    ${BASE_URL}    ${BROWSER}    options=${options}
    Set Selenium Timeout    ${TIMEOUT}
    Set Window Size    1920    1080

End Browser Session
    [Documentation]    Clean up browser session
    Close All Browsers

API Request Should Succeed
    [Documentation]    Verify API request succeeded and return response
    [Arguments]    ${response}
    Status Should Be    200    ${response}
    ${json}=    Set Variable    ${response.json()}
    Should Not Be Empty    ${json}
    [Return]    ${json}

Wait For Processing
    [Documentation]    Wait for background processing to complete
    [Arguments]    ${timeout}=${TIMEOUT}
    Sleep    2s    # Minimum wait time
    # Add additional checks for processing status if needed

Verify Response Time
    [Documentation]    Verify response time is within acceptable range
    [Arguments]    ${start_time}    ${end_time}    ${threshold}=${MAX_RESPONSE_TIME}
    ${response_time}=    Evaluate    (${end_time} - ${start_time}) * 1000
    Should Be True    ${response_time} < ${threshold}
    Log    Response time: ${response_time}ms (threshold: ${threshold}ms)

Generate Test Data
    [Documentation]    Generate test data for the given scenario
    [Arguments]    ${scenario}    ${size}=1
    ${data}=    Run Keyword If    '${scenario}' == 'text2sql'    Generate Text2SQL Test Data    ${size}
    ...    ELSE IF    '${scenario}' == 'agent'    Generate Agent Test Data    ${size}
    ...    ELSE    Fail    Unknown scenario: ${scenario}
    [Return]    ${data}

Cleanup Test Data
    [Documentation]    Clean up test data after test
    [Arguments]    ${test_data}
    Run Keyword If    ${test_data}    Remove Test Data    ${test_data}

Log Performance Metrics
    [Documentation]    Log performance metrics for monitoring
    [Arguments]    ${test_name}    ${response_time}    ${cpu_usage}    ${memory_usage}
    Log    Test: ${test_name}
    Log    Response Time: ${response_time}ms
    Log    CPU Usage: ${cpu_usage}%
    Log    Memory Usage: ${memory_usage}MB
