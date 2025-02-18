*** Settings ***
Documentation     Test suite for YouTube transcript functionality
Library           SeleniumLibrary
Library           DatabaseLibrary
Library           RequestsLibrary
Library           OperatingSystem
Resource          resources/common.robot
Suite Setup       Open Application
Suite Teardown    Close All Browsers

*** Variables ***
${BROWSER}        chrome
${URL}            http://localhost:8501
${TEST_VIDEO_URL}    https://www.youtube.com/watch?v=dQw4w9WgXcQ
${DB_NAME}        adpa
${DB_USER}        adpa
${DB_PASS}        ${EMPTY}
${DB_HOST}        localhost
${DB_PORT}        5432

*** Test Cases ***
Verify YouTube Transcript Page Loads
    [Documentation]    Verify that the YouTube transcript page loads correctly
    Go To    ${URL}
    Click Link    YouTube Transcript
    Wait Until Page Contains Element    css=h1:contains("YouTube Transcript")
    Page Should Contain    Enter YouTube URL

Test Video URL Input
    [Documentation]    Test entering a video URL
    Input Text    css=[aria-label="Enter YouTube URL"]    ${TEST_VIDEO_URL}
    Wait Until Page Contains    Processing video...

Verify Transcript Generation
    [Documentation]    Verify that transcript is generated
    Wait Until Page Contains    Transcript    timeout=60s
    Page Should Contain Element    css=textarea
    ${transcript}=    Get Text    css=textarea
    Should Not Be Empty    ${transcript}

Test Transcript Storage
    [Documentation]    Verify that transcript is stored in database
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    ${result}=    Query    SELECT COUNT(*) FROM agents_db.videos WHERE url LIKE '%dQw4w9WgXcQ%'
    Should Be Equal As Numbers    ${result[0][0]}    1
    Disconnect From Database

Test Transcript Summarization
    [Documentation]    Test transcript summarization functionality
    Click Button    Summarize Transcript
    Wait Until Page Contains    Summary    timeout=30s
    Page Should Not Contain    Error: Could not generate summary

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Set Window Size    1920    1080
    Wait Until Page Contains    ADPA
