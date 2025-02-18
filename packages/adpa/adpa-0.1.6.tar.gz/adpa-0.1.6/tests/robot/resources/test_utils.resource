*** Settings ***
Documentation     Common test utilities and helper functions
Library           Collections
Library           DateTime
Library           OperatingSystem
Library           String
Library           Process

*** Variables ***
${TIMEOUT}              30s
${RETRY_INTERVAL}       1s
${DEFAULT_BROWSER}      chrome
${TEST_DATA_DIR}        ${CURDIR}/../test_data
${SCREENSHOT_DIR}       ${CURDIR}/../screenshots

*** Keywords ***
Setup Test Environment
    [Arguments]    ${test_name}
    Create Directory    ${TEST_DATA_DIR}
    Create Directory    ${SCREENSHOT_DIR}
    Set Test Variable    ${TEST_START_TIME}    ${NONE}
    Start Test Timer

Teardown Test Environment
    [Arguments]    ${test_name}
    Capture Final State
    Clean Test Data
    Stop Test Timer
    Generate Test Report

Wait Until Condition
    [Arguments]    ${condition}    ${timeout}=${TIMEOUT}    ${message}=Condition not met
    Wait Until Keyword Succeeds    ${timeout}    ${RETRY_INTERVAL}    Run Keyword    ${condition}

Capture Test Metrics
    [Arguments]    ${test_name}
    ${metrics}=    Create Dictionary
    ...    duration=${TEST_DURATION}
    ...    memory_usage=${MEMORY_USAGE}
    ...    cpu_usage=${CPU_USAGE}
    Log Dictionary    ${metrics}
    [Return]    ${metrics}

Generate Random Test Data
    [Arguments]    ${data_type}    ${size}=10
    ${data}=    Run Keyword If    '${data_type}' == 'string'    Generate Random String    ${size}
    ...    ELSE IF    '${data_type}' == 'number'    Evaluate    random.randint(1, ${size})    random
    ...    ELSE IF    '${data_type}' == 'list'    Create List    @{range(${size})}
    [Return]    ${data}

Verify Test Results
    [Arguments]    ${actual}    ${expected}    ${tolerance}=0
    Run Keyword If    isinstance($actual, (int, float)) and isinstance($expected, (int, float))
    ...    Should Be True    abs($actual - $expected) <= ${tolerance}
    ...    ELSE    Should Be Equal    ${actual}    ${expected}

Clean Test Data
    Remove Directory    ${TEST_DATA_DIR}    recursive=True
    Create Directory    ${TEST_DATA_DIR}

Start Test Timer
    ${TEST_START_TIME}=    Get Time    epoch
    Set Test Variable    ${TEST_START_TIME}

Stop Test Timer
    ${end_time}=    Get Time    epoch
    ${duration}=    Evaluate    ${end_time} - ${TEST_START_TIME}
    Set Test Variable    ${TEST_DURATION}    ${duration}

Capture Final State
    Take Screenshot
    ${memory}=    Get Memory Usage
    ${cpu}=    Get CPU Usage
    Set Test Variable    ${MEMORY_USAGE}    ${memory}
    Set Test Variable    ${CPU_USAGE}    ${cpu}

Take Screenshot
    [Arguments]    ${name}=screenshot
    Capture Page Screenshot    ${SCREENSHOT_DIR}/${name}.png

Get Memory Usage
    ${memory}=    Run Process    wmic    OS    get    FreePhysicalMemory    /Value
    [Return]    ${memory.stdout}

Get CPU Usage
    ${cpu}=    Run Process    wmic    CPU    get    LoadPercentage    /Value
    [Return]    ${cpu.stdout}

Generate Test Report
    ${report}=    Create Dictionary
    ...    duration=${TEST_DURATION}
    ...    memory=${MEMORY_USAGE}
    ...    cpu=${CPU_USAGE}
    ...    screenshots=@{SCREENSHOT_DIR}
    Create File    ${TEST_DATA_DIR}/report.json    ${report}
