*** Settings ***
Documentation     Keywords for testing Text-to-SQL functionality
Resource         ../../resources/common.robot
Library          DatabaseLibrary
Library          Collections
Library          OperatingSystem
Library          String

*** Variables ***
${TEST_DB_PATH}    ${CURDIR}${/}..${/}..${/}test_data${/}test.db
${SCHEMA_FILE}     ${CURDIR}${/}..${/}..${/}test_data${/}test_schema.sql
${VECTOR_STORE}    ${CURDIR}${/}..${/}..${/}test_data${/}vector_store

*** Keywords ***
Initialize Test Database
    [Documentation]    Sets up a clean test database with schema
    [Arguments]    ${schema_file}=${SCHEMA_FILE}
    Remove File    ${TEST_DB_PATH}
    Execute SQL Script    ${schema_file}
    Connect To Database    SQLite3    ${TEST_DB_PATH}

Initialize Text2SQL Engine
    [Documentation]    Creates a new instance of the Text2SQL engine
    [Arguments]    ${enable_security}=True    ${enable_monitoring}=True    ${optimization_level}=2
    ${config}=    Create Dictionary
    ...    connection_params={"url": "sqlite:///${TEST_DB_PATH}"}
    ...    enable_security=${enable_security}
    ...    enable_monitoring=${enable_monitoring}
    ...    optimization_level=${optimization_level}
    ...    timeout_seconds=30
    ${engine}=    Create Text2SQL Engine    ${config}
    Set Test Variable    ${ENGINE}    ${engine}

Execute Natural Language Query
    [Documentation]    Executes a natural language query and returns the result
    [Arguments]    ${query_text}
    ${result}=    Convert To SQL    ${ENGINE}    ${query_text}
    [Return]    ${result}

Verify SQL Query Structure
    [Documentation]    Verifies that the SQL query has correct structure
    [Arguments]    ${sql_query}    ${expected_tables}    ${expected_columns}    ${expected_conditions}=None
    Should Match Regexp    ${sql_query}    (?i)^\\s*SELECT\\s+.*\\s+FROM\\s+.*
    FOR    ${table}    IN    @{expected_tables}
        Should Contain    ${sql_query}    ${table}
    END
    FOR    ${column}    IN    @{expected_columns}
        Should Contain    ${sql_query}    ${column}
    END
    Run Keyword If    "${expected_conditions}" != "None"
    ...    Should Contain    ${sql_query}    WHERE

Verify Query Result
    [Documentation]    Verifies that the query result matches expectations
    [Arguments]    ${result}    ${expected_row_count}=None    ${expected_columns}=None
    Should Not Be Empty    ${result.sql}
    Should Be True    ${result.confidence} >= 0.0 and ${result.confidence} <= 1.0
    Should Be True    ${result.processing_time} > 0
    
    Run Keyword If    "${expected_row_count}" != "None"
    ...    Length Should Be    ${result.rows}    ${expected_row_count}
    
    Run Keyword If    "${expected_columns}" != "None"
    ...    Verify Result Columns    ${result}    ${expected_columns}

Verify Result Columns
    [Documentation]    Verifies that the result contains expected columns
    [Arguments]    ${result}    ${expected_columns}
    FOR    ${column}    IN    @{expected_columns}
        List Should Contain Value    ${result.columns}    ${column}
    END

Clean Up Test Environment
    [Documentation]    Cleans up test resources
    Disconnect From Database
    Remove File    ${TEST_DB_PATH}
    Remove Directory    ${VECTOR_STORE}    recursive=True
