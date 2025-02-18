*** Settings ***
Documentation     Test suite for Text2SQL functionality
Resource         ../resources/common.robot
Resource         ../resources/database.robot
Resource         text2sql_keywords.robot

Suite Setup      Initialize Text2SQL Suite
Suite Teardown   Cleanup Text2SQL Suite
Test Setup      Reset Test Environment
Test Teardown   Log Test Results

Force Tags      text2sql    regression
Default Tags    stable    critical

*** Variables ***
${SCHEMA_FILE}    ${CURDIR}${/}test_data${/}sample_schema.json
${QUERY_FILE}     ${CURDIR}${/}test_data${/}test_queries.json
${TEST_DB_URL}    postgresql://adpa_test:adpa_test@localhost:5432/adpa_test

*** Test Cases ***
Test Should Generate Valid SQL From Simple Natural Language Query
    [Documentation]    Test basic natural language to SQL conversion
    [Tags]    smoke    query_generation    positive
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    When User Enters Query "Show all users"
    Then Generated SQL Should Be "SELECT * FROM users"
    And SQL Should Be Valid
    And No Validation Errors Should Be Present

Test Should Handle Complex Joins In Natural Language Query
    [Documentation]    Test handling of complex join scenarios
    [Tags]    complex    joins    positive
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    When User Enters Query "Show orders with customer names and product details"
    Then Generated SQL Should Contain "JOIN"
    And SQL Should Include Table "orders"
    And SQL Should Include Table "customers"
    And SQL Should Include Table "products"
    And SQL Should Be Valid

Test Should Prevent SQL Injection Attempts
    [Documentation]    Test SQL injection prevention
    [Tags]    security    negative    critical
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    When User Enters Query "Show users; DROP TABLE users;"
    Then SQL Generation Should Fail
    And Error Message Should Contain "SQL injection detected"
    And Database Should Remain Unchanged

Test Should Optimize Complex Query
    [Documentation]    Test query optimization features
    [Tags]    performance    optimization    positive
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    And Query Performance Monitoring Is Enabled
    When User Enters Complex Query From File "complex_query.sql"
    Then Generated SQL Should Be Optimized
    And Suggested Indexes Should Be Generated
    And Query Execution Plan Should Be Available

Test Should Handle Invalid Schema References
    [Documentation]    Test handling of invalid schema references
    [Tags]    validation    negative    medium
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    When User Enters Query "Show data from nonexistent_table"
    Then SQL Generation Should Fail
    And Error Message Should Contain "Table 'nonexistent_table' not found"
    And Suggestion Should Be Provided

Test Should Support Query Templates
    [Documentation]    Test query template functionality
    [Tags]    templates    positive    medium
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    And Template "user_orders" Is Available
    When User Applies Template With Parameters
    ...    template=user_orders
    ...    user_id=123
    Then Generated SQL Should Be Valid
    And SQL Should Contain "WHERE user_id = 123"

Test Should Validate Column Types
    [Documentation]    Test column type validation
    [Tags]    validation    types    medium
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    When User Enters Query "Find users where age > 'invalid'"
    Then SQL Generation Should Fail
    And Error Message Should Contain "Invalid type for column 'age'"

Test Should Generate Proper Aggregations
    [Documentation]    Test aggregation handling
    [Tags]    aggregation    positive    medium
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    When User Enters Query "Show total orders per customer"
    Then Generated SQL Should Contain "COUNT"
    And SQL Should Contain "GROUP BY"
    And SQL Should Be Valid

Test Should Handle Special Characters
    [Documentation]    Test handling of special characters
    [Tags]    validation    special_chars    medium
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    When User Enters Query 'Find products with name containing "100% Natural"'
    Then Generated SQL Should Be Valid
    And SQL Should Properly Escape Special Characters

Test Should Support Multiple Dialects
    [Documentation]    Test SQL dialect support
    [Tags]    dialects    positive    medium
    Given Schema Is Loaded From "${SCHEMA_FILE}"
    ${dialects}=    Create List    postgresql    mysql    sqlite
    FOR    ${dialect}    IN    @{dialects}
        Set SQL Dialect    ${dialect}
        When User Enters Query "Show recent orders"
        Then Generated SQL Should Be Valid For ${dialect}
    END
