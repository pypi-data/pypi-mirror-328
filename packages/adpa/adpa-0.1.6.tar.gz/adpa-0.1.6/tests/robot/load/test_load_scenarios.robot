*** Settings ***
Documentation     Load testing scenarios for system performance validation
Resource          ../resources/load.resource
Library           Process
Library           Collections
Library           RequestsLibrary
Library           DateTime

*** Variables ***
${CONCURRENT_USERS}    100
${RAMP_UP_TIME}       30
${TEST_DURATION}      300
${THINK_TIME}         2
${TARGET_RPS}         50

*** Test Cases ***
Test API Endpoint Load
    [Documentation]    Test API endpoints under load
    [Tags]    load    api    performance
    ${config}=    Create Dictionary
    ...    users=${CONCURRENT_USERS}
    ...    ramp_up=${RAMP_UP_TIME}
    ...    duration=${TEST_DURATION}
    ...    target_rps=${TARGET_RPS}
    Start Load Test    ${config}    api_endpoints
    Wait For Load Test Completion
    Verify Performance Metrics

Test Database Load
    [Documentation]    Test database performance under load
    [Tags]    load    database    performance
    ${config}=    Create Dictionary
    ...    users=${CONCURRENT_USERS}
    ...    ramp_up=${RAMP_UP_TIME}
    ...    duration=${TEST_DURATION}
    ...    target_rps=${TARGET_RPS}
    Start Load Test    ${config}    database_operations
    Wait For Load Test Completion
    Verify Database Metrics

Test Concurrent Research Operations
    [Documentation]    Test research operations under load
    [Tags]    load    research    performance
    ${config}=    Create Dictionary
    ...    users=${CONCURRENT_USERS}
    ...    ramp_up=${RAMP_UP_TIME}
    ...    duration=${TEST_DURATION}
    Start Load Test    ${config}    research_operations
    Wait For Load Test Completion
    Verify Research Performance

Test File Upload Load
    [Documentation]    Test file upload system under load
    [Tags]    load    upload    performance
    ${config}=    Create Dictionary
    ...    users=${CONCURRENT_USERS}
    ...    ramp_up=${RAMP_UP_TIME}
    ...    duration=${TEST_DURATION}
    Start Load Test    ${config}    file_uploads
    Wait For Load Test Completion
    Verify Upload Performance

Test Search Performance
    [Documentation]    Test search functionality under load
    [Tags]    load    search    performance
    ${config}=    Create Dictionary
    ...    users=${CONCURRENT_USERS}
    ...    ramp_up=${RAMP_UP_TIME}
    ...    duration=${TEST_DURATION}
    Start Load Test    ${config}    search_operations
    Wait For Load Test Completion
    Verify Search Performance

Test Real-time Updates
    [Documentation]    Test real-time update system under load
    [Tags]    load    realtime    performance
    ${config}=    Create Dictionary
    ...    users=${CONCURRENT_USERS}
    ...    ramp_up=${RAMP_UP_TIME}
    ...    duration=${TEST_DURATION}
    Start Load Test    ${config}    realtime_updates
    Wait For Load Test Completion
    Verify Update Performance

*** Keywords ***
Start Load Test
    [Arguments]    ${config}    ${scenario}
    Log    Starting load test for scenario: ${scenario}
    ${test_id}=    Generate Test ID
    Set Test Variable    ${CURRENT_TEST_ID}    ${test_id}
    Start Monitoring    ${test_id}
    Start Load Generation    ${config}    ${scenario}

Wait For Load Test Completion
    ${status}=    Get Test Status    ${CURRENT_TEST_ID}
    WHILE    '${status}' == 'running'
        Sleep    5s
        ${status}=    Get Test Status    ${CURRENT_TEST_ID}
    END
    Stop Load Generation
    Stop Monitoring    ${CURRENT_TEST_ID}

Verify Performance Metrics
    ${metrics}=    Get Test Metrics    ${CURRENT_TEST_ID}
    Verify Response Times    ${metrics}
    Verify Error Rates    ${metrics}
    Verify Resource Usage    ${metrics}
    Generate Performance Report    ${CURRENT_TEST_ID}

Verify Database Metrics
    ${metrics}=    Get Database Metrics    ${CURRENT_TEST_ID}
    Verify Query Performance    ${metrics}
    Verify Connection Pool    ${metrics}
    Verify Database Load    ${metrics}
    Generate Database Report    ${CURRENT_TEST_ID}

Generate Test ID
    ${timestamp}=    Get Current Date    result_format=%Y%m%d_%H%M%S
    ${random}=    Evaluate    random.randint(1000, 9999)
    [Return]    load_test_${timestamp}_${random}

Verify Response Times
    [Arguments]    ${metrics}
    Should Be True    ${metrics.avg_response_time} < 1000
    Should Be True    ${metrics.p95_response_time} < 2000
    Should Be True    ${metrics.p99_response_time} < 3000

Verify Error Rates
    [Arguments]    ${metrics}
    Should Be True    ${metrics.error_rate} < 0.01
    Should Be True    ${metrics.timeout_rate} < 0.005

Verify Resource Usage
    [Arguments]    ${metrics}
    Should Be True    ${metrics.cpu_usage} < 80
    Should Be True    ${metrics.memory_usage} < 85
    Should Be True    ${metrics.network_usage} < 70
