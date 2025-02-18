*** Settings ***
Documentation     Test setup and teardown resources
Library           Browser
Library           OperatingSystem
Library           String
Library           DateTime
Library           Collections

*** Variables ***
${BROWSER}         chromium
${HEADLESS}        True
${BASE_URL}        http://localhost:8505
${TIMEOUT}         20s
${RETRY_TIMEOUT}   2s
${RETRY_COUNT}     3

*** Keywords ***
Begin Web Test
    New Browser    browser=${BROWSER}    headless=${HEADLESS}
    New Context    viewport={'width': 1920, 'height': 1080}
    New Page       ${BASE_URL}
    Wait For Elements State    h1:text("ADPA")    visible    timeout=${TIMEOUT}
    Initialize Test Environment

End Web Test
    Take Screenshot On Failure
    Close Browser
    Clean Test Environment

Begin Web Test With Mobile View
    New Browser    browser=${BROWSER}    headless=${HEADLESS}
    New Context    viewport={'width': 375, 'height': 812}
    New Page       ${BASE_URL}
    Wait For Elements State    h1:text("ADPA")    visible    timeout=${TIMEOUT}
    Initialize Test Environment

Initialize Test Environment
    Set Browser Timeout    ${TIMEOUT}
    Create Test Directories
    Set Test Variables

Create Test Directories
    Create Directory    ${TEST_DATA_DIR}
    Create Directory    ${SCREENSHOT_DIR}

Set Test Variables
    Set Suite Variable    ${TEST_START_TIME}    ${None}
    ${timestamp}=    Get Current Date    result_format=%Y%m%d_%H%M%S
    Set Suite Variable    ${TEST_START_TIME}    ${timestamp}

Take Screenshot On Failure
    ${timestamp}=    Get Current Date    result_format=%Y%m%d_%H%M%S
    ${screenshot_path}=    Set Variable    ${SCREENSHOT_DIR}/failure_${timestamp}.png
    Take Screenshot    ${screenshot_path}

Clean Test Environment
    Remove Directory    ${TEST_DATA_DIR}    recursive=True
    Create Directory    ${TEST_DATA_DIR}

Wait Until Element With Healing
    [Arguments]    ${primary_locator}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    FOR    ${i}    IN RANGE    ${RETRY_COUNT}
        ${status}=    Run Keyword And Return Status
        ...    Wait For Elements State    ${primary_locator}    visible    timeout=${timeout}
        IF    ${status}    RETURN
        
        IF    ${backup_locators} is not ${None}
            FOR    ${locator}    IN    @{backup_locators}
                ${status}=    Run Keyword And Return Status
                ...    Wait For Elements State    ${locator}    visible    timeout=${RETRY_TIMEOUT}
                IF    ${status}
                    Log    Self-healed: Using backup locator ${locator} instead of ${primary_locator}    level=WARN
                    RETURN
                END
            END
        END
        Sleep    ${RETRY_TIMEOUT}
    END
    Fail    No viable locator found for element (primary: ${primary_locator})

Click Element With Healing
    [Arguments]    ${primary_locator}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    Wait Until Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    Click    ${primary_locator}

Type Text With Healing
    [Arguments]    ${primary_locator}    ${text}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    Wait Until Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    Fill Text    ${primary_locator}    ${text}

Select Option With Healing
    [Arguments]    ${primary_locator}    ${option}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    Wait Until Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    Select Options By    ${primary_locator}    text    ${option}

Upload File With Healing
    [Arguments]    ${primary_locator}    ${file_path}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    Wait Until Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    Upload File By Selector    ${primary_locator}    ${file_path}

Verify Element Text With Healing
    [Arguments]    ${primary_locator}    ${expected_text}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    Wait Until Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    Get Text    ${primary_locator}    ==    ${expected_text}

Verify Element Count With Healing
    [Arguments]    ${primary_locator}    ${expected_count}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    Wait Until Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    ${elements}=    Get Elements    ${primary_locator}
    Length Should Be    ${elements}    ${expected_count}

Wait For Loading State
    Wait For Elements State    [data-testid="loading-indicator"]    detached    timeout=${TIMEOUT}

Navigate To Section
    [Arguments]    ${section_name}
    Click Element With Healing    a:text("${section_name}")
    Wait For Loading State
