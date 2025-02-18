*** Settings ***
Documentation     Test suite for Tools functionality
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections
Library           RequestsLibrary
Resource          resources/common.robot
Suite Setup       Initialize Tool Tests
Suite Teardown    Clean Up Tool Tests

*** Variables ***
${TEST_URL}       https://www.youtube.com/watch?v=dQw4w9WgXcQ
${TEST_TEXT}      This is a test text for summarization.
${TEST_QUERY}     machine learning algorithms

*** Test Cases ***
Test YouTube Transcript Tool
    [Documentation]    Test YouTube transcript extraction
    Go To    ${URL}
    Click Link    YouTube Transcript
    Input Text    url    ${TEST_URL}
    Click Button    Get Transcript
    Wait Until Element Is Visible    css=.transcript-text
    Element Should Not Be Empty    css=.transcript-text

Test Text Summarization Tool
    [Documentation]    Test text summarization functionality
    Go To    ${URL}
    Click Link    Text Tools
    Input Text    text    ${TEST_TEXT}
    Click Button    Summarize
    Wait Until Element Is Visible    css=.summary-text
    Element Should Not Be Empty    css=.summary-text

Test Search Tool
    [Documentation]    Test search functionality
    Go To    ${URL}
    Click Link    Search
    Input Text    query    ${TEST_QUERY}
    Click Button    Search
    Wait Until Element Is Visible    css=.search-results
    Element Should Not Be Empty    css=.search-results

Test File Processing Tool
    [Documentation]    Test file processing functionality
    Go To    ${URL}
    Click Link    File Tools
    Choose File    file-input    ${CURDIR}/test_files/test.txt
    Click Button    Process
    Wait Until Element Is Visible    css=.processing-results
    Element Should Not Be Empty    css=.processing-results

Test Tool Error Handling
    [Documentation]    Test error handling for invalid inputs
    Go To    ${URL}
    Click Link    YouTube Transcript
    Input Text    url    invalid_url
    Click Button    Get Transcript
    Wait Until Page Contains    Error: Invalid YouTube URL

*** Keywords ***
Initialize Tool Tests
    Create Test Files
    Open Browser    ${URL}    ${BROWSER}
    Set Window Size    1920    1080
    Wait Until Page Contains    ADPA

Clean Up Tool Tests
    Remove Test Files
    Close All Browsers

Create Test Files
    Create Directory    ${CURDIR}/test_files
    Create File    ${CURDIR}/test_files/test.txt    This is a test file content.

Remove Test Files
    Remove Directory    ${CURDIR}/test_files    recursive=True
