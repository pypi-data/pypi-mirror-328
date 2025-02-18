*** Settings ***
Documentation     UI tests for Streamlit interface
Resource         ../../resources/common.robot
Suite Setup      Open Application
Suite Teardown   Close Application
Force Tags       ui    regression

*** Variables ***
${BROWSER}               chrome
${APP_URL}              http://localhost:8501
${VALID_QUERY}          Select all employees from HR department
${INVALID_QUERY}        Select * from nonexistent_table
${WAIT_TIMEOUT}         10s

*** Test Cases ***
Test Should Display Main Interface Components
    [Documentation]    Verify all main interface components are present
    [Tags]    smoke    critical    stable
    Page Should Contain    ADPA Framework
    Page Should Contain Element    id:query-input
    Page Should Contain Element    id:submit-button
    Page Should Contain Element    id:results-area
    Page Should Contain Element    id:history-sidebar

Test Should Process Valid Query Successfully
    [Documentation]    Test successful query processing
    [Tags]    query    high    stable
    Input Text    id:query-input    ${VALID_QUERY}
    Click Button    id:submit-button
    Wait Until Element Is Visible    id:results-area    ${WAIT_TIMEOUT}
    Element Should Contain    id:results-area    SELECT * FROM employees
    Element Should Contain    id:status-message    Query executed successfully

Test Should Handle Invalid Query Appropriately
    [Documentation]    Test handling of invalid queries
    [Tags]    query    error    high    stable
    Input Text    id:query-input    ${INVALID_QUERY}
    Click Button    id:submit-button
    Wait Until Element Is Visible    id:error-message    ${WAIT_TIMEOUT}
    Element Should Contain    id:error-message    Table 'nonexistent_table' does not exist

Test Should Save Query To History
    [Documentation]    Test query history functionality
    [Tags]    history    medium    stable
    ${query_text}=    Set Variable    Select count(*) from employees
    Input Text    id:query-input    ${query_text}
    Click Button    id:submit-button
    Wait Until Element Is Visible    id:history-sidebar    ${WAIT_TIMEOUT}
    Element Should Contain    id:history-sidebar    ${query_text}

Test Should Load Query From History
    [Documentation]    Test loading queries from history
    [Tags]    history    medium    stable
    Click Element    xpath://div[@id='history-sidebar']//div[contains(text(),'${VALID_QUERY}')]
    ${input_value}=    Get Element Attribute    id:query-input    value
    Should Be Equal    ${input_value}    ${VALID_QUERY}

Test Should Show Query Execution Progress
    [Documentation]    Test query execution progress indication
    [Tags]    ui    medium    stable
    Input Text    id:query-input    ${VALID_QUERY}
    Click Button    id:submit-button
    Element Should Be Visible    id:progress-bar
    Wait Until Element Is Not Visible    id:progress-bar    ${WAIT_TIMEOUT}
    Element Should Contain    id:status-message    Query executed successfully

Test Should Allow Query Modification
    [Documentation]    Test query modification functionality
    [Tags]    query    medium    stable
    Input Text    id:query-input    ${VALID_QUERY}
    Click Button    id:edit-button
    Input Text    id:query-input    ${VALID_QUERY} ORDER BY salary DESC
    Click Button    id:submit-button
    Wait Until Element Is Visible    id:results-area    ${WAIT_TIMEOUT}
    Element Should Contain    id:results-area    ORDER BY salary DESC

Test Should Support Query Export
    [Documentation]    Test query export functionality
    [Tags]    export    medium    stable
    Input Text    id:query-input    ${VALID_QUERY}
    Click Button    id:submit-button
    Wait Until Element Is Visible    id:results-area    ${WAIT_TIMEOUT}
    Click Button    id:export-button
    Wait Until Element Is Visible    id:export-success    ${WAIT_TIMEOUT}
    File Should Exist    ${DOWNLOAD_DIR}/query_results.csv

Test Should Handle Session Timeout
    [Documentation]    Test session timeout handling
    [Tags]    session    medium    stable
    Set Session Timeout
    Wait Until Element Is Visible    id:session-expired    ${WAIT_TIMEOUT}
    Element Should Contain    id:session-expired    Session expired
    Click Button    id:reconnect-button
    Wait Until Element Is Visible    id:query-input    ${WAIT_TIMEOUT}

Test Should Validate Input Length
    [Documentation]    Test input validation for query length
    [Tags]    validation    medium    stable
    ${long_query}=    Generate Long Query
    Input Text    id:query-input    ${long_query}
    Element Should Be Visible    id:length-warning
    Element Should Contain    id:length-warning    Query too long

*** Keywords ***
Open Application
    [Documentation]    Open the Streamlit application
    Open Browser    ${APP_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id:query-input    ${WAIT_TIMEOUT}

Generate Long Query
    [Documentation]    Generate a query that exceeds length limits
    ${query}=    Set Variable    SELECT * FROM employees
    FOR    ${i}    IN RANGE    100
        ${query}=    Set Variable    ${query} JOIN department_${i}
    END
    [Return]    ${query}

Set Session Timeout
    [Documentation]    Simulate session timeout
    Execute JavaScript    localStorage.clear();
    Reload Page
