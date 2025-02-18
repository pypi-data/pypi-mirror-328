*** Settings ***
Documentation     Test suite for LLM functionality
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections
Library           RequestsLibrary
Resource          resources/common.robot
Suite Setup       Initialize LLM Tests
Suite Teardown    Clean Up LLM Tests

*** Variables ***
${TEST_PROMPT}    Summarize this text: The quick brown fox jumps over the lazy dog.
${GROQ_MODEL}     mixtral-8x7b-32768
${GEMINI_MODEL}   gemini-pro

*** Test Cases ***
Test Groq LLM Integration
    [Documentation]    Test Groq LLM functionality
    [Setup]    Skip If No Groq Key
    Go To    ${URL}
    Click Link    LLM Tools
    Select From List By Value    model    ${GROQ_MODEL}
    Input Text    prompt    ${TEST_PROMPT}
    Click Button    Generate
    Wait Until Element Is Visible    css=.response-text
    Element Should Not Be Empty    css=.response-text

Test Gemini LLM Integration
    [Documentation]    Test Google's Gemini functionality
    [Setup]    Skip If No Google Key
    Go To    ${URL}
    Click Link    LLM Tools
    Select From List By Value    model    ${GEMINI_MODEL}
    Input Text    prompt    ${TEST_PROMPT}
    Click Button    Generate
    Wait Until Element Is Visible    css=.response-text
    Element Should Not Be Empty    css=.response-text

Test LLM Error Handling
    [Documentation]    Test error handling for invalid inputs
    Go To    ${URL}
    Click Link    LLM Tools
    Input Text    prompt    ${EMPTY}
    Click Button    Generate
    Wait Until Page Contains    Error: Prompt cannot be empty

Test Model Configuration
    [Documentation]    Test model configuration settings
    Go To    ${URL}
    Click Link    LLM Tools
    Click Link    Configure Models
    Input Text    temperature    0.7
    Input Text    max_tokens    1000
    Click Button    Save Configuration
    Wait Until Page Contains    Configuration saved
    Page Should Contain    temperature: 0.7
    Page Should Contain    max_tokens: 1000

*** Keywords ***
Initialize LLM Tests
    Open Browser    ${URL}    ${BROWSER}
    Set Window Size    1920    1080
    Wait Until Page Contains    ADPA

Clean Up LLM Tests
    Close All Browsers

Skip If No Groq Key
    ${groq_key}=    Get Environment Variable    GROQ_API_KEY    ${EMPTY}
    Skip If    '${groq_key}' == '${EMPTY}'    Groq API key not found

Skip If No Google Key
    ${google_key}=    Get Environment Variable    GOOGLE_API_KEY    ${EMPTY}
    Skip If    '${google_key}' == '${EMPTY}'    Google API key not found
