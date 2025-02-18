*** Settings ***
Documentation     Performance tests for ADPA Framework
Resource         ../../resources/common.robot
Suite Setup      Initialize Performance Test
Suite Teardown   Cleanup Performance Test
Force Tags       performance    regression

*** Variables ***
${CONCURRENT_USERS}    10
${TEST_DURATION}       300
${THINK_TIME}         2
${TARGET_RPS}         50
${ACCEPTABLE_RESPONSE_TIME}    500

*** Test Cases ***
Test Should Handle Multiple Concurrent Users
    [Documentation]    Test system performance with multiple concurrent users
    [Tags]    load    critical    stable
    ${users}=    Create List    @{RANGE}    ${CONCURRENT_USERS}
    FOR    ${user}    IN    @{users}
        Start User Session    ${user}
    END
    Wait For All Sessions
    Verify Performance Metrics

Test Should Maintain Response Time Under Load
    [Documentation]    Test response time stays within acceptable limits under load
    [Tags]    response_time    high    stable
    ${start_time}=    Get Current Time
    WHILE    Time Since    ${start_time} < ${TEST_DURATION}
        Execute Query Request
        Verify Response Time    ${ACCEPTABLE_RESPONSE_TIME}
        Sleep    ${THINK_TIME}
    END
    Verify Average Response Time

Test Should Handle Burst Traffic
    [Documentation]    Test system handling of sudden traffic spikes
    [Tags]    burst    high    stable
    FOR    ${i}    IN RANGE    10
        ${requests}=    Generate Burst Requests    20
        Execute Concurrent Requests    ${requests}
        Verify System Stability
        Sleep    5s
    END

Test Should Process Large Datasets Efficiently
    [Documentation]    Test system performance with large datasets
    [Tags]    data_processing    high    stable
    ${large_dataset}=    Generate Large Dataset
    ${start_time}=    Get Current Time
    Process Dataset    ${large_dataset}
    ${processing_time}=    Get Time Since    ${start_time}
    Should Be Less Than    ${processing_time}    60s
    Verify Data Processing Accuracy

Test Should Handle Long-Running Queries
    [Documentation]    Test system behavior with long-running queries
    [Tags]    query_performance    medium    stable
    ${queries}=    Create List    @{LONG_RUNNING_QUERIES}
    FOR    ${query}    IN    @{queries}
        ${start_time}=    Get Current Time
        Execute Long Running Query    ${query}
        ${execution_time}=    Get Time Since    ${start_time}
        Log    Query Execution Time: ${execution_time}
        Verify Query Results
    END

*** Keywords ***
Initialize Performance Test
    [Documentation]    Set up the test environment
    Connect To Database
    Clear Test Data
    Initialize Monitoring
    Set Test Variables

Cleanup Performance Test
    [Documentation]    Clean up after performance tests
    Export Performance Metrics
    Generate Performance Report
    Disconnect From Database

Start User Session
    [Arguments]    ${user_id}
    [Documentation]    Start a simulated user session
    ${session}=    Create Session    ${user_id}
    Set Session Variables    ${session}
    Start Session Activity

Wait For All Sessions
    [Documentation]    Wait for all user sessions to complete
    ${active_sessions}=    Get Active Sessions
    WHILE    ${active_sessions} > 0
        Sleep    1s
        ${active_sessions}=    Get Active Sessions
    END

Verify Performance Metrics
    [Documentation]    Verify various performance metrics
    ${metrics}=    Get Performance Metrics
    Should Be Less Than    ${metrics.average_response_time}    ${ACCEPTABLE_RESPONSE_TIME}
    Should Be Greater Than    ${metrics.throughput}    ${TARGET_RPS}
    Should Be Less Than    ${metrics.error_rate}    1

Execute Query Request
    [Documentation]    Execute a single query request
    ${query}=    Generate Random Query
    ${response}=    Send Query Request    ${query}
    Record Response Time    ${response.time}

Verify Response Time
    [Arguments]    ${threshold}
    [Documentation]    Verify response time is within acceptable limits
    ${current_response_time}=    Get Last Response Time
    Should Be Less Than    ${current_response_time}    ${threshold}

Generate Burst Requests
    [Arguments]    ${count}
    [Documentation]    Generate a burst of concurrent requests
    ${requests}=    Create List
    FOR    ${i}    IN RANGE    ${count}
        ${request}=    Generate Random Request
        Append To List    ${requests}    ${request}
    END
    [Return]    ${requests}

Execute Concurrent Requests
    [Arguments]    ${requests}
    [Documentation]    Execute multiple requests concurrently
    ${responses}=    Send Concurrent Requests    ${requests}
    Verify Responses    ${responses}

Verify System Stability
    [Documentation]    Verify system remains stable under load
    ${metrics}=    Get System Metrics
    Should Be Less Than    ${metrics.cpu_usage}    80
    Should Be Less Than    ${metrics.memory_usage}    80
    Should Be Less Than    ${metrics.error_rate}    1
