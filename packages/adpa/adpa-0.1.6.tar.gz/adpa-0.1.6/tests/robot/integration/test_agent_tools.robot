*** Settings ***
Documentation     Integration tests for Agent-Tool interaction
Resource          ../resources/common.robot
Library           ../../adpa/agents/agent.py
Library           ../../adpa/tools/tool_utils.py
Library           Collections

*** Variables ***
${AGENT_NAME}     ToolAgent
${TOOL_NAME}      TestTool
${PROMPT}         You are a helpful AI assistant that uses tools.

*** Test Cases ***
Test Agent Tool Integration
    [Documentation]    Test basic integration between Agent and Tools
    [Tags]    integration    smoke
    ${agent}=    Create Agent With Tool
    ${result}=    Execute Agent Tool    ${agent}    Run test command
    Should Not Be Empty    ${result}

Test Multiple Tools
    [Documentation]    Test agent using multiple tools
    [Tags]    integration    multi-tool
    ${agent}=    Create Agent With Tools
    ${result1}=    Execute Agent Tool    ${agent}    tool1    Run tool 1
    ${result2}=    Execute Agent Tool    ${agent}    tool2    Run tool 2
    Should Not Be Empty    ${result1}
    Should Not Be Empty    ${result2}

Test Tool Error Handling
    [Documentation]    Test agent's handling of tool errors
    [Tags]    integration    error-handling
    ${agent}=    Create Agent With Tool
    Run Keyword And Expect Error    *    Execute Agent Tool    ${agent}    Invalid command
    ${result}=    Execute Agent Tool    ${agent}    Run valid command
    Should Not Be Empty    ${result}

Test Tool Chain
    [Documentation]    Test agent using tools in sequence
    [Tags]    integration    tool-chain
    ${agent}=    Create Agent With Tools
    ${result}=    Execute Tool Chain    ${agent}
    Should Not Be Empty    ${result}

Test Tool Permission
    [Documentation]    Test tool permission handling
    [Tags]    integration    permissions
    ${agent}=    Create Agent With Tool    require_permission=True
    Run Keyword And Expect Error    *Permission denied*    
    ...    Execute Agent Tool    ${agent}    Run restricted command
    ${result}=    Execute Agent Tool    ${agent}    Run allowed command
    Should Not Be Empty    ${result}

*** Keywords ***
Create Agent With Tool
    [Arguments]    ${require_permission}=False
    ${tool}=    Create Tool Instance    
    ...    name=${TOOL_NAME}    
    ...    require_permission=${require_permission}
    ${agent}=    Create Agent Instance    
    ...    name=${AGENT_NAME}    
    ...    prompt=${PROMPT}
    Add Tool To Agent    ${agent}    ${tool}
    RETURN    ${agent}

Create Agent With Tools
    ${tool1}=    Create Tool Instance    name=tool1
    ${tool2}=    Create Tool Instance    name=tool2
    ${agent}=    Create Agent Instance    
    ...    name=${AGENT_NAME}    
    ...    prompt=${PROMPT}
    Add Tool To Agent    ${agent}    ${tool1}
    Add Tool To Agent    ${agent}    ${tool2}
    RETURN    ${agent}

Execute Agent Tool
    [Arguments]    ${agent}    ${command}
    ${result}=    Run Tool Command    ${agent}    ${command}
    RETURN    ${result}

Execute Tool Chain
    [Arguments]    ${agent}
    ${result1}=    Run Tool Command    ${agent}    Step 1
    ${result2}=    Run Tool Command    ${agent}    Step 2
    ${result3}=    Run Tool Command    ${agent}    Step 3
    RETURN    ${result3}

Add Tool To Agent
    [Arguments]    ${agent}    ${tool}
    Add Tool    ${agent}    ${tool}
    RETURN    ${agent}
