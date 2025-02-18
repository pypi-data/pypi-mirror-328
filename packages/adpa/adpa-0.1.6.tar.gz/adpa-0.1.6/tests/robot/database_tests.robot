*** Settings ***
Documentation     Database Component Test Suite
Library          SeleniumLibrary
Library          RequestsLibrary
Library          DatabaseLibrary
Library          OperatingSystem
Library          Collections
Resource         resources/common.robot
Resource         resources/database_keywords.robot
Suite Setup      Start Application
Suite Teardown   Stop Application

*** Variables ***
${BROWSER}               chrome
${APP_URL}              http://localhost:8501
${DB_HOST}              localhost
${DB_PORT}              5432
${DB_NAME}              adpa_db
${DB_USER}              postgres
${RETRY_COUNT}          3
${RETRY_INTERVAL}       5s

*** Test Cases ***
Database Health Check
    [Documentation]    Verify database health monitoring
    [Tags]            health    monitoring    smoke
    Wait Until Element Is Visible    xpath://div[contains(@class, 'stTabs')]    timeout=10s
    Click Element    xpath://div[text()='📊 Overview']
    Page Should Contain Element    xpath://div[contains(@class, 'js-plotly-plot')]
    ${health_score}=    Get Health Score
    Should Be True    ${health_score} >= 0 and ${health_score} <= 100
    Run Keyword And Continue On Failure    Verify Resource Metrics

Query Performance Analysis
    [Documentation]    Test query performance monitoring
    [Tags]            performance    monitoring
    Click Element    xpath://div[text()='🔍 Query Insights']
    Wait Until Element Is Visible    xpath://div[contains(@class, 'stExpander')]    timeout=10s
    @{slow_queries}=    Get Slow Queries
    Run Keyword If    len(@{slow_queries}) > 0    Verify Query Analysis    @{slow_queries}

Database Maintenance Operations
    [Documentation]    Test maintenance operations
    [Tags]            maintenance    operations
    Click Element    xpath://div[text()='⚙️ Maintenance']
    Wait Until Element Is Visible    xpath://button[contains(text(), 'Analyze Database')]    timeout=10s
    Click Button    Analyze Database
    Wait Until Element Contains    xpath://div[contains(@class, 'stSuccess')]    Database analysis completed    timeout=30s
    Run Keyword And Continue On Failure    Create Test Backup

Self-Healing Test
    [Documentation]    Test self-healing capabilities
    [Tags]            self-healing    resilience
    ${result}=    Run Keyword And Return Status    Test Database Connection
    Run Keyword If    not ${result}    Initiate Self Healing
    Wait Until Keyword Succeeds    ${RETRY_COUNT}x    ${RETRY_INTERVAL}    Verify Database Connection

*** Keywords ***
Get Health Score
    ${score_element}=    Get WebElement    xpath://div[contains(@class, 'js-plotly-plot')]//text[contains(@class, 'trace')]
    ${score_text}=    Get Text    ${score_element}
    ${score}=    Convert To Number    ${score_text}
    [Return]    ${score}

Verify Resource Metrics
    @{metrics}=    Create List    CPU    Memory    Disk    Connections
    FOR    ${metric}    IN    @{metrics}
        ${present}=    Run Keyword And Return Status
        ...    Page Should Contain Element    xpath://div[contains(text(), '${metric}')]
        Should Be True    ${present}    Message=Metric ${metric} not found
    END

Get Slow Queries
    ${queries}=    Get WebElements    xpath://div[contains(@class, 'stExpander')]
    [Return]    ${queries}

Verify Query Analysis
    [Arguments]    @{queries}
    FOR    ${query}    IN    @{queries}
        Click Element    ${query}
        Page Should Contain Element    xpath://div[contains(text(), 'Avg Time')]
        Page Should Contain Element    xpath://div[contains(text(), 'Rows')]
        Page Should Contain Element    xpath://div[contains(text(), 'Calls')]
    END

Create Test Backup
    Input Text    xpath://input[@placeholder='Enter backup name...']    test_backup
    Click Button    Create Backup
    Wait Until Element Contains    xpath://div[contains(@class, 'stSuccess')]    Backup test_backup created    timeout=30s

Test Database Connection
    Connect To Database    psycopg    ${DB_NAME}    ${DB_USER}    ${DB_PASSWORD}    ${DB_HOST}    ${DB_PORT}
    ${result}=    Query    SELECT 1
    Should Be Equal As Strings    ${result[0][0]}    1
    Disconnect From Database

Initiate Self Healing
    Log    Starting self-healing process
    ${status}=    Run Keyword And Return Status    Reset Database Connection
    Run Keyword If    not ${status}    Restart Database Service
    Sleep    5s
    ${status}=    Run Keyword And Return Status    Test Database Connection
    Run Keyword If    not ${status}    Notify Administrator

Reset Database Connection
    Disconnect From Database
    Sleep    2s
    Connect To Database    psycopg    ${DB_NAME}    ${DB_USER}    ${DB_PASSWORD}    ${DB_HOST}    ${DB_PORT}

Restart Database Service
    ${result}=    Run Process    net    start    postgresql-x64-15
    Should Be Equal As Integers    ${result.rc}    0    msg=Failed to restart database service

Notify Administrator
    ${timestamp}=    Get Current Date
    Append To File    ${CURDIR}/error.log
    ...    \nDatabase connection failure at ${timestamp}. Manual intervention required.
