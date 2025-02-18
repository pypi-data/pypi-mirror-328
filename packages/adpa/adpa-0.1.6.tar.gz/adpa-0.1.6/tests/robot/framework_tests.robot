*** Settings ***
Documentation    Core ADPA Framework Tests
Resource         resources/framework.resource
Library          SeleniumLibrary
Library          OperatingSystem
Library          String
Library          Collections
Library          ../PythonLibrary/ADPATestLibrary.py

Test Setup       Initialize ADPA Framework
Test Teardown    Cleanup ADPA Framework

*** Variables ***
${TEST_DATA_DIR}    ${CURDIR}/test_data
${CONFIG_FILE}      ${CURDIR}/config/test_config.yaml

*** Test Cases ***
Framework Can Initialize
    [Documentation]    Verify ADPA Framework initializes correctly
    [Tags]    core    smoke
    Framework Should Be Initialized
    Verify Core Components

Framework Can Process Attention
    [Documentation]    Test attention processing capabilities
    [Tags]    core    attention
    ${test_content}=    Get Test Content    attention
    ${result}=    Process Attention    ${test_content}
    Verify Attention Score    ${result}
    Verify Attention Recommendations    ${result}

Framework Can Process Desire
    [Documentation]    Test desire processing capabilities
    [Tags]    core    desire
    ${test_content}=    Get Test Content    desire
    ${result}=    Process Desire    ${test_content}
    Verify Desire Score    ${result}
    Verify Desire Recommendations    ${result}

Framework Can Process Position
    [Documentation]    Test position processing capabilities
    [Tags]    core    position
    ${test_content}=    Get Test Content    position
    ${result}=    Process Position    ${test_content}
    Verify Position Score    ${result}
    Verify Position Recommendations    ${result}

Framework Can Process Action
    [Documentation]    Test action processing capabilities
    [Tags]    core    action
    ${test_content}=    Get Test Content    action
    ${result}=    Process Action    ${test_content}
    Verify Action Score    ${result}
    Verify Action Recommendations    ${result}

Framework Can Handle Custom Agents
    [Documentation]    Test custom agent integration
    [Tags]    core    agents
    ${agent}=    Create Custom Agent    TestAgent
    Register Custom Agent    ${agent}
    Verify Agent Registration
    Run Agent Analysis
    Verify Agent Results

Framework Can Process Multiple Items
    [Documentation]    Test batch processing capabilities
    [Tags]    core    batch
    ${items}=    Create Test Items    5
    ${results}=    Process Items    ${items}
    Verify Batch Results    ${results}
    Verify Processing Time

*** Keywords ***
Initialize ADPA Framework
    Import Library    ../PythonLibrary/ADPATestLibrary.py
    Initialize Framework
    Load Test Configuration    ${CONFIG_FILE}

Cleanup ADPA Framework
    Cleanup Framework Resources
    Remove Test Data
