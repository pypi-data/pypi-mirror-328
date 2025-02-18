*** Settings ***
Documentation     Text2SQL UI Test Suite
Resource          ../../resources/keywords/text2sql_keywords.robot
Suite Setup       Initialize Text2SQL Application
Suite Teardown    Cleanup Test Environment
Test Setup       Reset Application State
Test Teardown    Capture Screenshot On Failure
Force Tags       text2sql    ui
Default Tags     smoke    regression

*** Test Cases ***
Test Should Generate Valid SQL When Given Simple Query
    [Documentation]    Tests basic query translation functionality
    [Tags]    critical    query_translation    positive
    Given Application Is Ready
    When Input Natural Language Query    Show me all employees
    Then SQL Query Should Contain    SELECT * FROM employees
    And Query Results Should Be Visible
    And Query Should Be Added To History

Test Should Handle Complex Query With Multiple Tables
    [Documentation]    Tests handling of complex queries involving multiple tables
    [Tags]    high    query_translation    positive
    Given Application Is Ready
    When Input Natural Language Query    Show departments with average salary above 50000
    Then SQL Query Should Contain    SELECT d.name FROM departments d JOIN employees e
    And SQL Query Should Contain    GROUP BY d.name HAVING AVG(salary) > 50000
    And Query Results Should Be Visible

Test Should Show Error For Invalid Query
    [Documentation]    Tests error handling for invalid queries
    [Tags]    high    error_handling    negative
    Given Application Is Ready
    When Input Natural Language Query    ThisIsNotAValidQuery###
    Then Error Message Should Be Visible
    And Error Message Should Contain    Could not understand query

Test Should Maintain Query History
    [Documentation]    Tests query history functionality
    [Tags]    medium    history    positive
    Given Application Is Ready
    When Execute Multiple Queries
    Then Query History Should Contain All Queries
    And Latest Query Should Be At Top

Test Should Clear Query History
    [Documentation]    Tests query history clearing
    [Tags]    medium    history    positive
    Given Query History Has Items
    When Clear Query History
    Then Query History Should Be Empty

Test Should Handle Special Characters
    [Documentation]    Tests handling of special characters in queries
    [Tags]    medium    input_validation    positive
    Given Application Is Ready
    When Input Query With Special Characters
    Then Query Should Be Processed Successfully

Test Should Validate Database Connection
    [Documentation]    Tests database connection validation
    [Tags]    critical    database    positive
    Given Application Is Ready
    When Test Database Connection
    Then Connection Should Be Successful

Test Should Handle Long Running Queries
    [Documentation]    Tests handling of long-running queries
    [Tags]    high    performance    positive
    Given Application Is Ready
    When Execute Long Running Query
    Then Progress Indicator Should Be Visible
    And Query Should Complete Successfully

*** Keywords ***
Reset Application State
    [Documentation]    Resets application state before each test
    Refresh Browser
    Clear Query History

Application Is Ready
    [Documentation]    Verifies application is ready for testing
    Wait Until Element Is Visible    ${QUERY_INPUT}
    Element Should Be Enabled    ${SUBMIT_BUTTON}

SQL Query Should Contain
    [Documentation]    Verifies SQL query contains expected text
    [Arguments]    ${expected_text}
    Wait Until Element Is Visible    ${SQL_OUTPUT}
    Element Should Contain    ${SQL_OUTPUT}    ${expected_text}

Query Results Should Be Visible
    [Documentation]    Verifies query results are visible
    Wait Until Element Is Visible    ${RESULTS_TABLE}
    Element Should Be Visible    css=${RESULTS_TABLE} tr

Error Message Should Be Visible
    [Documentation]    Verifies error message is visible
    Wait Until Element Is Visible    ${ERROR_MESSAGE}

Error Message Should Contain
    [Documentation]    Verifies error message contains expected text
    [Arguments]    ${expected_text}
    Element Should Contain    ${ERROR_MESSAGE}    ${expected_text}

Execute Multiple Queries
    [Documentation]    Executes multiple test queries
    FOR    ${query}    IN    @{SAMPLE_QUERIES}
        Input Natural Language Query    ${query}
        Sleep    1s
    END

Query History Should Contain All Queries
    [Documentation]    Verifies all test queries are in history
    Wait Until Element Is Visible    ${HISTORY_LIST}
    FOR    ${query}    IN    @{SAMPLE_QUERIES}
        Element Should Contain    ${HISTORY_LIST}    ${query}
    END

Latest Query Should Be At Top
    [Documentation]    Verifies the latest query is at the top of history
    ${latest_query}=    Get Text    css=${HISTORY_LIST} li:first-child
    Should Be Equal    ${latest_query}    ${SAMPLE_QUERIES}[-1]

Query History Has Items
    [Documentation]    Ensures query history has items
    Execute Multiple Queries
    Wait Until Element Is Visible    ${HISTORY_LIST}

Input Query With Special Characters
    [Documentation]    Tests query with special characters
    Input Natural Language Query    Show employees where name contains "O'Connor" & salary > $50,000

Query Should Be Processed Successfully
    [Documentation]    Verifies query was processed without errors
    Wait Until Element Is Visible    ${SQL_OUTPUT}
    Element Should Not Be Visible    ${ERROR_MESSAGE}

Execute Long Running Query
    [Documentation]    Executes a long-running query
    Input Natural Language Query    Calculate average salary grouped by department, position, and year

Progress Indicator Should Be Visible
    [Documentation]    Verifies progress indicator is shown
    Wait Until Element Is Visible    css=.stProgress

Capture Screenshot On Failure
    [Documentation]    Captures screenshot on test failure
    Run Keyword If Test Failed    Capture Page Screenshot
