*** Settings ***
Documentation     Performance tests for critical system components
Resource          ../resources/common.robot
Library           ../../adpa/agents/agent.py
Library           ../../adpa/database/database_utils.py
Library           Collections
Library           DateTime

*** Variables ***
${RESPONSE_TIME_THRESHOLD}    5    # seconds
${MEMORY_THRESHOLD}          512   # MB
${CPU_THRESHOLD}            80    # percent
${TEST_DURATION}           300    # seconds
${CONCURRENT_USERS}         10

*** Test Cases ***
Test Agent Response Time
    [Documentation]    Test agent response time under load
    [Tags]    performance    agent    response-time
    ${agent}=    Create Agent Instance    name=PerfTestAgent
    ${start_time}=    Get Current Time
    FOR    ${index}    IN RANGE    100
        ${response_time}=    Measure Response Time    ${agent}    "Test message ${index}"
        Should Be True    ${response_time} < ${RESPONSE_TIME_THRESHOLD}
    END

Test Database Performance
    [Documentation]    Test database performance under load
    [Tags]    performance    database
    Connect To Test Database
    ${start_time}=    Get Current Time
    FOR    ${index}    IN RANGE    1000
        ${query_time}=    Measure Query Time    "SELECT * FROM test_table"
        Should Be True    ${query_time} < ${RESPONSE_TIME_THRESHOLD}
    END
    Disconnect From Database

Test Memory Usage
    [Documentation]    Test memory usage under load
    [Tags]    performance    memory
    ${start_time}=    Get Current Time
    FOR    ${index}    IN RANGE    10
        ${memory_usage}=    Get Process Memory
        Should Be True    ${memory_usage} < ${MEMORY_THRESHOLD}
        Create Large Dataset
        Sleep    1s
    END
    Clean Test Data

Test Concurrent API Calls
    [Documentation]    Test API performance with concurrent requests
    [Tags]    performance    api    concurrent
    ${success_rate}=    Run Concurrent Requests    ${CONCURRENT_USERS}
    Should Be True    ${success_rate} >= 95

Test Long-Running Operations
    [Documentation]    Test system stability during long operations
    [Tags]    performance    stability
    ${start_time}=    Get Current Time
    ${end_time}=    Add Time To Time    ${start_time}    ${TEST_DURATION} seconds
    WHILE    Get Current Time < ${end_time}
        Run Background Tasks
        Monitor System Health
        Sleep    1s
    END

*** Keywords ***
Measure Response Time
    [Arguments]    ${agent}    ${message}
    ${start_time}=    Get Time    epoch
    Send Agent Message    ${agent}    ${message}
    ${end_time}=    Get Time    epoch
    ${response_time}=    Evaluate    ${end_time} - ${start_time}
    RETURN    ${response_time}

Measure Query Time
    [Arguments]    ${query}
    ${start_time}=    Get Time    epoch
    Execute SQL    ${query}
    ${end_time}=    Get Time    epoch
    ${query_time}=    Evaluate    ${end_time} - ${start_time}
    RETURN    ${query_time}

Get Process Memory
    ${memory}=    Get Memory Usage
    RETURN    ${memory}

Run Concurrent Requests
    [Arguments]    ${num_users}
    ${success_count}=    Set Variable    ${0}
    FOR    ${user}    IN RANGE    ${num_users}
        ${status}=    Run API Request
        Run Keyword If    '${status}' == 'SUCCESS'    
        ...    Evaluate    ${success_count} + 1
    END
    ${success_rate}=    Evaluate    (${success_count} / ${num_users}) * 100
    RETURN    ${success_rate}

Monitor System Health
    ${memory}=    Get Process Memory
    ${cpu}=    Get CPU Usage
    Should Be True    ${memory} < ${MEMORY_THRESHOLD}
    Should Be True    ${cpu} < ${CPU_THRESHOLD}
    RETURN    ${TRUE}
