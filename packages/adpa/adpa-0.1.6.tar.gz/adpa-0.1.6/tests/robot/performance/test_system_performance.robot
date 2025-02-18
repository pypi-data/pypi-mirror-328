*** Settings ***
Documentation     System-wide performance tests
Resource          ../resources/test_utils.resource
Resource          ../resources/common.resource
Library           Collections
Library           Process

*** Variables ***
${LOAD_USERS}        100
${DURATION}          5m
${RAMP_UP}           30s
${THINK_TIME}        2s

*** Test Cases ***
Test System Load Performance
    [Documentation]    Test system performance under load
    [Tags]    performance    load
    Setup Performance Test    ${LOAD_USERS}
    Start Load Generation
    Monitor System Metrics
    Verify Performance Thresholds
    [Teardown]    Cleanup Performance Test

Test Response Time Under Load
    [Documentation]    Test response times for key operations
    [Tags]    performance    response
    @{operations}=    Create List    data_query    analysis    visualization
    FOR    ${operation}    IN    @{operations}
        Measure Operation Response    ${operation}    ${LOAD_USERS}
    END
    Verify Response Times

Test Resource Utilization
    [Documentation]    Test system resource usage
    [Tags]    performance    resources
    Start Resource Monitoring
    Generate System Load
    ${metrics}=    Collect Resource Metrics
    Verify Resource Usage    ${metrics}

Test Database Performance
    [Documentation]    Test database operations performance
    [Tags]    performance    database
    Setup Database Test Data
    Measure Query Performance
    Measure Write Performance
    Measure Index Performance
    Cleanup Test Data

Test Concurrent User Performance
    [Documentation]    Test multi-user concurrent operations
    [Tags]    performance    concurrency
    ${users}=    Create Virtual Users    ${LOAD_USERS}
    Start Concurrent Operations    ${users}
    Monitor User Experience
    Verify Concurrency Handling

Test Memory Management
    [Documentation]    Test memory usage and leaks
    [Tags]    performance    memory
    Start Memory Monitoring
    Execute Memory Intensive Operations
    ${usage}=    Analyze Memory Usage
    Verify No Memory Leaks    ${usage}

*** Keywords ***
Setup Performance Test
    [Arguments]    ${users}
    Initialize Test Environment
    Create Virtual Users    ${users}
    Start Monitoring

Monitor System Metrics
    ${metrics}=    Create Dictionary
    FOR    ${i}    IN RANGE    10
        ${current}=    Get System Metrics
        Update Metrics    ${metrics}    ${current}
        Sleep    30s
    END
    Set Test Variable    ${SYSTEM_METRICS}    ${metrics}

Verify Performance Thresholds
    ${cpu}=    Get Average CPU    ${SYSTEM_METRICS}
    ${memory}=    Get Average Memory    ${SYSTEM_METRICS}
    ${response}=    Get Average Response    ${SYSTEM_METRICS}
    Should Be True    ${cpu} < 80
    Should Be True    ${memory} < 90
    Should Be True    ${response} < 2000

Measure Operation Response
    [Arguments]    ${operation}    ${users}
    ${times}=    Create List
    FOR    ${user}    IN RANGE    ${users}
        ${start}=    Get Time    epoch
        Execute Operation    ${operation}
        ${end}=    Get Time    epoch
        ${duration}=    Evaluate    ${end} - ${start}
        Append To List    ${times}    ${duration}
    END
    Calculate Response Statistics    ${times}

Generate System Load
    Start Parallel Processes    ${LOAD_USERS}
    Sleep    ${DURATION}
    Stop Processes

Collect Resource Metrics
    ${metrics}=    Create Dictionary
    ${metrics.cpu}=    Get CPU Usage
    ${metrics.memory}=    Get Memory Usage
    ${metrics.disk}=    Get Disk Usage
    ${metrics.network}=    Get Network Usage
    [Return]    ${metrics}

Verify Resource Usage
    [Arguments]    ${metrics}
    Should Be True    ${metrics.cpu} < 80
    Should Be True    ${metrics.memory} < 90
    Should Be True    ${metrics.disk} < 85
    Should Be True    ${metrics.network} < 70

Monitor User Experience
    ${ux_metrics}=    Create Dictionary
    FOR    ${i}    IN RANGE    10
        ${current}=    Measure User Experience
        Update UX Metrics    ${ux_metrics}    ${current}
        Sleep    30s
    END
    Set Test Variable    ${UX_METRICS}    ${ux_metrics}

Execute Memory Intensive Operations
    FOR    ${i}    IN RANGE    10
        Run Memory Test    ${i}
        Collect Garbage
        ${usage}=    Get Memory Usage
        Log    Memory Usage: ${usage}
    END
