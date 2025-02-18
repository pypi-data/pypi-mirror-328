*** Settings ***
Documentation     Test initialization and common setup
Library           Browser    timeout=20s
Library           OperatingSystem
Library           String
Library           DateTime

*** Variables ***
${BROWSER}        chromium
${HEADLESS}       True
${BASE_URL}       http://localhost:8505
${TIMEOUT}        20s
${SCREENSHOT_DIR}    ${CURDIR}${/}..${/}screenshots
${TEST_DATA_DIR}    ${CURDIR}${/}..${/}test_data

*** Keywords ***
Setup Test Environment
    Create Directory    ${SCREENSHOT_DIR}
    Create Directory    ${TEST_DATA_DIR}
    Set Browser Timeout    ${TIMEOUT}

Cleanup Test Environment
    Remove Directory    ${SCREENSHOT_DIR}    recursive=True
    Remove Directory    ${TEST_DATA_DIR}    recursive=True

Start Browser Session
    New Browser    browser=${BROWSER}    headless=${HEADLESS}
    New Context    viewport={'width': 1920, 'height': 1080}
    New Page       ${BASE_URL}
    Wait For Elements State    h1:text("ADPA")    visible    timeout=${TIMEOUT}

End Browser Session
    Take Screenshot    fullPage=True
    Close Browser

Start Mobile Browser Session
    New Browser    browser=${BROWSER}    headless=${HEADLESS}
    New Context    viewport={'width': 375, 'height': 812}
    New Page       ${BASE_URL}
    Wait For Elements State    h1:text("ADPA")    visible    timeout=${TIMEOUT}

Wait For Page Load
    Wait For Elements State    [data-testid="loading-indicator"]    detached    timeout=${TIMEOUT}

Take Error Screenshot
    ${timestamp}=    Get Current Date    result_format=%Y%m%d_%H%M%S
    Take Screenshot    filename=error_${timestamp}    fullPage=True
