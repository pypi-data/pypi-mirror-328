*** Settings ***
Documentation     Common resources for Text2SQL testing
Library          Collections
Library          OperatingSystem
Library          DateTime
Library          ../libraries/Text2SQLLibrary.py

*** Variables ***
${RESOURCES_DIR}         ${CURDIR}/../resources
${TEST_DATA_DIR}        ${RESOURCES_DIR}/test_data
${SCHEMA_FILE}          ${TEST_DATA_DIR}/test_schema.sql
${CONFIG_FILE}          ${TEST_DATA_DIR}/test_config.json
${TEST_DB}             test_database
${CONTEXT_THRESHOLD}    0.7
${PERFORMANCE_THRESHOLD}    2.0  # seconds

# Test Data
&{SIMPLE_QUERY}    question=Show me all users from New York    expected_table=users
&{COMPLEX_QUERY}    question=Calculate average order value by month in 2024    expected_table=orders
&{INVALID_QUERY}    question=This is not a valid database question    expected_error=Invalid question format

*** Keywords ***
Initialize Text2SQL Environment
    [Documentation]    Set up test environment for Text2SQL tests
    Create Test Database
    Load Test Schema
    Load Test Configuration
    Initialize Test Data

Cleanup Text2SQL Environment
    [Documentation]    Clean up test environment after tests
    Drop Test Database
    Remove Test Files
    Clear Test Data

Create Test Database
    [Documentation]    Create test database for Text2SQL tests
    ${result}=    Create Database    ${TEST_DB}
    Should Be True    ${result}

Load Test Schema
    [Documentation]    Load test schema into database
    ${schema}=    Get File    ${SCHEMA_FILE}
    ${result}=    Execute SQL    ${schema}
    Should Be True    ${result}

Load Test Configuration
    [Documentation]    Load test configuration
    ${config}=    Get File    ${CONFIG_FILE}
    Set Suite Variable    ${CONFIG}    ${config}

Initialize Test Data
    [Documentation]    Initialize test data in database
    Load Users Test Data
    Load Orders Test Data
    Load Products Test Data

Load Users Test Data
    [Documentation]    Load test data for users table
    ${data}=    Get File    ${TEST_DATA_DIR}/users.sql
    Execute SQL    ${data}

Load Orders Test Data
    [Documentation]    Load test data for orders table
    ${data}=    Get File    ${TEST_DATA_DIR}/orders.sql
    Execute SQL    ${data}

Load Products Test Data
    [Documentation]    Load test data for products table
    ${data}=    Get File    ${TEST_DATA_DIR}/products.sql
    Execute SQL    ${data}

Verify SQL Generation
    [Arguments]    ${question}    ${expected_table}
    [Documentation]    Verify SQL generation for given question
    ${response}=    Generate SQL    ${question}
    Should Not Be Empty    ${response.sql}
    Should Contain    ${response.sql}    ${expected_table}
    [Return]    ${response}

Verify Query Results
    [Arguments]    ${results}    ${expected_count}=${None}
    [Documentation]    Verify query results
    Should Not Be Empty    ${results}
    Run Keyword If    ${expected_count} is not ${None}    
    ...    Length Should Be    ${results}    ${expected_count}

Verify Performance Metrics
    [Arguments]    ${metrics}
    [Documentation]    Verify query performance metrics
    Should Be True    ${metrics.execution_time} < ${PERFORMANCE_THRESHOLD}
    Should Not Be Empty    ${metrics.result_count}

Get Test Schema
    [Documentation]    Get test database schema
    ${schema}=    Get Database Schema
    [Return]    ${schema}

Execute Test Query
    [Arguments]    ${sql}
    [Documentation]    Execute SQL query and return results
    ${results}=    Execute SQL    ${sql}
    [Return]    ${results}

Verify Error Response
    [Arguments]    ${error}    ${expected_message}
    [Documentation]    Verify error response
    Should Not Be Empty    ${error}
    Should Contain    ${error.message}    ${expected_message}

Clear Test Data
    [Documentation]    Clear all test data from database
    Execute SQL    TRUNCATE TABLE users CASCADE;
    Execute SQL    TRUNCATE TABLE orders CASCADE;
    Execute SQL    TRUNCATE TABLE products CASCADE;
