*** Settings ***
Documentation     Unit tests for tools functionality
Resource          ../resources/common.robot
Library           ../../adpa/tools/tool_utils.py
Library           Collections

*** Variables ***
${TEST_TOOL_NAME}     TestTool
${TEST_DESCRIPTION}   Test tool description
${TEST_INPUT}         test input

*** Test Cases ***
Test Tool Creation
    [Documentation]    Test creating a new tool
    ${tool}=    Create Tool    ${TEST_TOOL_NAME}    ${TEST_DESCRIPTION}
    Should Not Be Equal    ${tool}    ${None}
    Should Be Equal    ${tool.name}    ${TEST_TOOL_NAME}
    Should Be Equal    ${tool.description}    ${TEST_DESCRIPTION}

Test Tool Configuration
    [Documentation]    Test tool configuration
    ${tool}=    Create Tool    ${TEST_TOOL_NAME}    ${TEST_DESCRIPTION}
    Configure Tool    ${tool}    timeout=30    retry_count=3
    ${config}=    Get Tool Configuration    ${tool}
    Should Be Equal As Numbers    ${config.timeout}    30
    Should Be Equal As Numbers    ${config.retry_count}    3

Test Tool Execution
    [Documentation]    Test tool execution
    ${tool}=    Create Tool    ${TEST_TOOL_NAME}    ${TEST_DESCRIPTION}
    ${result}=    Execute Tool    ${tool}    ${TEST_INPUT}
    Should Not Be Empty    ${result}

Test Tool Error Handling
    [Documentation]    Test tool error handling
    ${tool}=    Create Tool    ${TEST_TOOL_NAME}    ${TEST_DESCRIPTION}
    Run Keyword And Expect Error    *    Execute Tool    ${tool}    invalid_input

*** Keywords ***
Create Tool
    [Arguments]    ${name}    ${description}
    ${tool}=    Create Tool Instance    name=${name}    description=${description}
    RETURN    ${tool}

Configure Tool
    [Arguments]    ${tool}    ${timeout}=30    ${retry_count}=3
    Set Tool Configuration    ${tool}    timeout=${timeout}    retry_count=${retry_count}

Get Tool Configuration
    [Arguments]    ${tool}
    ${config}=    Get Configuration    ${tool}
    RETURN    ${config}

Execute Tool
    [Arguments]    ${tool}    ${input}
    ${result}=    Run Tool    ${tool}    ${input}
    RETURN    ${result}
