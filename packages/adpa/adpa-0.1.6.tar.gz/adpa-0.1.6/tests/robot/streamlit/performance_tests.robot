*** Settings ***
Documentation     Performance tests for Store Advisor
Resource          ${CURDIR}/resources/streamlit_common.robot
Library           SeleniumLibrary
Library           Process
Library           OperatingSystem
Library           ${CURDIR}/resources/test_data_generator.py
Test Setup       Setup Performance Test
Test Teardown    Cleanup Performance Test

*** Variables ***
${PERF_DATA_DIR}    ${CURDIR}/test_data/performance
${RESULTS_DIR}      ${CURDIR}/results/performance
${NUM_ITERATIONS}   10

*** Keywords ***
Setup Performance Test
    Create Directory    ${RESULTS_DIR}
    ${generator}=    Get Library Instance    test_data_generator.TestDataGenerator
    Generate Test Suite    ${PERF_DATA_DIR}

Cleanup Performance Test
    Remove Directory    ${PERF_DATA_DIR}    recursive=True
    Close All Browsers

Measure Response Time
    [Arguments]    ${action}    ${expected_element}
    ${start_time}=    Get Time    epoch
    Run Keyword    ${action}
    Wait Until Page Contains Element    ${expected_element}    timeout=30s
    ${end_time}=    Get Time    epoch
    ${response_time}=    Evaluate    ${end_time} - ${start_time}
    [Return]    ${response_time}

Record Performance Metric
    [Arguments]    ${test_name}    ${metric_name}    ${value}
    Append To File    ${RESULTS_DIR}/${test_name}.csv    ${metric_name},${value}\n

Run Load Test
    [Arguments]    ${num_requests}    ${delay}=1
    FOR    ${i}    IN RANGE    ${num_requests}
        Get Recommendations
        Sleep    ${delay}
    END

Monitor Resource Usage
    [Arguments]    ${duration}=60
    ${start_time}=    Get Time    epoch
    ${end_time}=    Evaluate    ${start_time} + ${duration}
    WHILE    True
        ${current_time}=    Get Time    epoch
        Exit For Loop If    ${current_time} >= ${end_time}
        ${memory}=    Get Process Memory    streamlit
        ${cpu}=    Get Process Cpu    streamlit
        Record Performance Metric    resource_usage    memory    ${memory}
        Record Performance Metric    resource_usage    cpu    ${cpu}
        Sleep    1s
    END

*** Test Cases ***
Page Load Performance Test
    [Documentation]    Measure initial page load performance
    [Tags]    performance    load
    FOR    ${i}    IN RANGE    ${NUM_ITERATIONS}
        Open Browser    ${STREAMLIT_URL}    ${BROWSER}
        ${load_time}=    Measure Response Time
        ...    Go To    ${STREAMLIT_URL}
        ...    xpath://h1[contains(text(), 'RAG/Vector Store Advisor')]
        Record Performance Metric    page_load    response_time    ${load_time}
        Close Browser
    END

Recommendation Response Time Test
    [Documentation]    Measure recommendation generation performance
    [Tags]    performance    recommendations
    Open Browser    ${STREAMLIT_URL}    ${BROWSER}
    FOR    ${i}    IN RANGE    ${NUM_ITERATIONS}
        Select Use Case Parameters
        ...    Small (<100K docs)
        ...    Static (rarely updated)
        ...    Low (<100ms)
        ...    Self-hosted
        ...    Low (<$100/month)
        ${response_time}=    Measure Response Time
        ...    Get Recommendations
        ...    css:div[data-testid="stExpander"]
        Record Performance Metric    recommendations    response_time    ${response_time}
    END

Load Test
    [Documentation]    Test system under load
    [Tags]    performance    load
    Open Browser    ${STREAMLIT_URL}    ${BROWSER}
    Run Load Test    50    0.5
    Verify No Streamlit Errors

Resource Usage Test
    [Documentation]    Monitor system resource usage
    [Tags]    performance    resources
    Open Browser    ${STREAMLIT_URL}    ${BROWSER}
    Start Process    streamlit    run    ${CURDIR}/../../../adpa/ui/pages/store_advisor.py
    Monitor Resource Usage    60
    Terminate All Processes

Concurrent Users Test
    [Documentation]    Test system with concurrent users
    [Tags]    performance    concurrent
    FOR    ${i}    IN RANGE    5
        Start Process    
        ...    robot    
        ...    --test    Recommendation Response Time Test    
        ...    --output    ${RESULTS_DIR}/concurrent_${i}.xml    
        ...    ${CURDIR}/store_advisor.robot
    END
    Sleep    30s
    Terminate All Processes
