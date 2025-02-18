# -*- coding: utf-8 -*-

*** Settings ***
Documentation     Integration tests for Agent-LLM interactions
Resource          ../resources/common.robot
Variables         ../resources/env.py

Suite Setup       Setup Test Suite
Suite Teardown    Teardown Test Suite
Test Setup       Setup Test Case
Test Teardown    Teardown Test Case

*** Variables ***
${TEST_PROMPT}    What is the capital of France?
${EXPECTED_RESPONSE}    Paris

*** Test Cases ***
Test Agent LLM Integration
    [Documentation]    Test basic integration between Agent and LLM
    ${agent}=    Create Test Agent    name=test_agent
    ${response}=    Send Message    agent=${agent}    message=${TEST_PROMPT}
    Should Contain    ${response}    ${EXPECTED_RESPONSE}

Test Agent Memory
    [Documentation]    Test agent's ability to remember context
    ${agent}=    Create Test Agent    name=test_agent
    Send Message    agent=${agent}    message=My name is John
    ${response}=    Send Message    agent=${agent}    message=What is my name?
    Should Contain    ${response}    John

Test Multiple Agents
    [Documentation]    Test multiple agents interacting with same LLM
    ${agent1}=    Create Test Agent    name=agent1
    ${agent2}=    Create Test Agent    name=agent2
    ${response1}=    Send Message    agent=${agent1}    message=${TEST_PROMPT}
    ${response2}=    Send Message    agent=${agent2}    message=${TEST_PROMPT}
    Should Be Equal    ${response1}    ${response2}

Test Agent Error Recovery
    [Documentation]    Test agent's ability to handle LLM errors
    ${agent}=    Create Test Agent    name=test_agent
    Run Keyword And Expect Error    *    Send Message    agent=${agent}    message=${TEST_PROMPT}

Test Long Conversation
    [Documentation]    Test agent's ability to handle long conversations
    ${agent}=    Create Test Agent    name=test_agent
    FOR    ${i}    IN RANGE    5
        Send Message    agent=${agent}    message=Tell me a fact about number ${i}
    END
    ${response}=    Send Message    agent=${agent}    message=What was the first number we talked about?
    Should Contain    ${response}    0

*** Keywords ***
Setup Test Suite
    [Documentation]    Setup test suite environment
    Set Environment Variable    OPENAI_API_KEY    ${OPENAI_API_KEY}
    Connect To Database

Teardown Test Suite
    [Documentation]    Cleanup test suite environment
    DatabaseLibrary.Disconnect From Database

Setup Test Case
    [Documentation]    Setup for each test case
    Clean Database

Teardown Test Case
    [Documentation]    Cleanup after each test case
    Clean Database
