# -*- coding: utf-8 -*-

*** Settings ***
Documentation     Common keywords and variables for all test suites
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections
Library           String
Library           Process
Library           DatabaseLibrary
Library           adpa.agents.agent
Library           adpa.llm.llm_utils  
Library           adpa.database.database_utils
Library           test_data.py
Resource          database.resource

*** Variables ***
${BROWSER}               chrome
${HEADLESS}             ${True}
${TIMEOUT}              20s
${SCREENSHOT_DIR}       ${EXECDIR}${/}screenshots
${BASE_URL}             http://localhost:8000

*** Keywords ***
Setup Test Suite
    [Documentation]    Setup required for test suite
    OperatingSystem.Set Environment Variable    PYTHONPATH    ${CURDIR}/../..
    Connect To Database

Teardown Test Suite
    [Documentation]    Cleanup after test suite
    Disconnect From Database

Setup Test Case
    [Documentation]    Setup required for test case
    Clean Database
    Seed Test Data

Teardown Test Case
    [Documentation]    Cleanup after test case
    Clean Database

Create Test Agent
    [Documentation]    Create a test agent
    [Arguments]    ${name}=test_agent    ${model}=gpt-4    ${temperature}=0.7
    RETURN    adpa.agents.agent.Create Agent    name=${name}    model=${model}    temperature=${temperature}

Send Message
    [Documentation]    Send a message to an agent and get response
    [Arguments]    ${agent}    ${message}
    RETURN    adpa.agents.agent.Get Agent Response    agent=${agent}    message=${message}
