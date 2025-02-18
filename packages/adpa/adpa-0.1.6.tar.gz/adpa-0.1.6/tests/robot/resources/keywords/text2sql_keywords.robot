*** Settings ***
Documentation     Keywords for Text2SQL functionality testing
Library          SeleniumLibrary
Library          RequestsLibrary
Library          DatabaseLibrary
Resource         ../variables.robot

*** Keywords ***
Connect To Text2SQL Database
    [Documentation]    Establishes connection to the test database
    [Arguments]    ${db_name}=${DATABASE_NAME}
    Connect To Database    psycopg2
    ...    ${db_name}    ${DB_USER}    ${DB_PASSWORD}    ${DB_HOST}    ${DB_PORT}

Initialize Text2SQL Application
    [Documentation]    Sets up the Text2SQL application for testing
    Connect To Text2SQL Database
    Create Session    text2sql    ${BASE_URL}
    Set Selenium Speed    ${SELENIUM_SPEED}
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window

Input Natural Language Query
    [Documentation]    Inputs a natural language query into the application
    [Arguments]    ${query}
    Wait Until Element Is Visible    id=query-input
    Input Text    id=query-input    ${query}
    Click Button    id=submit-query

Verify SQL Query Generated
    [Documentation]    Verifies that a valid SQL query was generated
    [Arguments]    ${expected_tables}
    Wait Until Element Is Visible    id=sql-output
    ${sql_query}=    Get Text    id=sql-output
    Should Contain    ${sql_query}    SELECT
    FOR    ${table}    IN    @{expected_tables}
        Should Contain    ${sql_query}    ${table}
    END

Verify Query Results
    [Documentation]    Verifies the query results are displayed correctly
    [Arguments]    ${expected_count}
    Wait Until Element Is Visible    id=results-table
    ${rows}=    Get Element Count    css=table#results-table tr
    Should Be Equal As Numbers    ${rows}    ${expected_count + 1}    # +1 for header row

Check Error Handling
    [Documentation]    Verifies error handling for invalid queries
    [Arguments]    ${error_message}
    Wait Until Element Is Visible    id=error-message
    Element Should Contain    id=error-message    ${error_message}

Save Query To History
    [Documentation]    Saves the current query to history
    Click Button    id=save-query
    Wait Until Element Is Visible    id=history-list
    ${latest_query}=    Get Text    css=#history-list li:first-child
    Should Not Be Empty    ${latest_query}

Verify Query History
    [Documentation]    Verifies query history functionality
    [Arguments]    ${expected_query}
    Wait Until Element Is Visible    id=history-list
    Element Should Contain    id=history-list    ${expected_query}

Clear Query History
    [Documentation]    Clears the query history
    Click Button    id=clear-history
    Wait Until Element Is Not Visible    css=#history-list li

Test Database Connection
    [Documentation]    Tests the database connection
    ${status}=    Execute SQL String    SELECT 1;
    Should Be Equal As Strings    ${status}    None

Cleanup Test Environment
    [Documentation]    Cleans up the test environment
    Close All Browsers
    Disconnect From Database
