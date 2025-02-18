*** Settings ***
Documentation     End-to-end tests for Text2SQL functionality
Resource          ../resources/text2sql_common.robot
Test Setup       Initialize Text2SQL Environment
Test Teardown    Cleanup Text2SQL Environment
Force Tags       text2sql    regression    e2e

*** Variables ***
${TIMEOUT}              10s
${PERFORMANCE_LIMIT}    2s
${MIN_CONFIDENCE}       0.8

*** Test Cases ***
Test Should Convert Simple Question To Valid SQL
    [Tags]    smoke    critical    conversion
    [Documentation]    Test basic natural language to SQL conversion
    Given Clean Database Environment
    And Sample Data Is Loaded
    When User Asks "Show me all users from New York"
    Then SQL Should Be Generated Within Timeout
    And SQL Should Be Syntactically Valid
    And SQL Should Reference Correct Tables
    And Query Should Execute Successfully
    And Results Should Match Expected Data

Test Should Handle Complex Analytical Question
    [Tags]    high    analytics
    [Documentation]    Test complex analytical query conversion
    Given Clean Database Environment
    And Sample Data Is Loaded
    When User Asks "What is the average order value by customer segment for each month in 2024"
    Then SQL Should Be Generated Within Timeout
    And SQL Should Include Required Analytics
    And Query Performance Should Be Acceptable
    And Results Should Show Clear Trends

Test Should Improve Query Based On Results
    [Tags]    high    feedback
    [Documentation]    Test query improvement through feedback loop
    Given Clean Database Environment
    And Sample Data Is Loaded
    When User Asks "Find our best customers"
    Then Initial SQL Should Be Generated
    And Query Should Be Improved Through Feedback
    And Final Query Should Be More Specific
    And Results Should Be More Relevant

Test Should Handle Schema Changes
    [Tags]    high    schema
    [Documentation]    Test handling of schema modifications
    Given Clean Database Environment
    And Initial Schema Is Recorded
    When Schema Is Modified
    And User Asks "Show me all orders"
    Then SQL Should Adapt To New Schema
    And Query Should Execute Successfully
    And Results Should Reflect Schema Changes

Test Should Maintain Context Between Questions
    [Tags]    medium    context
    [Documentation]    Test context maintenance between queries
    Given Clean Database Environment
    And Sample Data Is Loaded
    When User Asks Sequential Questions
    Then Each Query Should Build On Previous Context
    And Results Should Be Progressively More Specific
    And Context Should Be Properly Maintained

*** Keywords ***
Clean Database Environment
    [Documentation]    Ensure clean database state
    Execute SQL    TRUNCATE TABLE users CASCADE;
    Execute SQL    TRUNCATE TABLE orders CASCADE;
    Execute SQL    TRUNCATE TABLE products CASCADE;

Sample Data Is Loaded
    [Documentation]    Load sample test data
    ${users_data}=    Get File    ${TEST_DATA_DIR}/users.sql
    ${orders_data}=    Get File    ${TEST_DATA_DIR}/orders.sql
    ${products_data}=    Get File    ${TEST_DATA_DIR}/products.sql
    Execute Multiple SQL    ${users_data}    ${orders_data}    ${products_data}

SQL Should Be Generated Within Timeout
    [Documentation]    Verify SQL generation within timeout
    Wait Until Keyword Succeeds    ${TIMEOUT}    1s    
    ...    Should Not Be Empty    ${RESPONSE.sql}

SQL Should Be Syntactically Valid
    [Documentation]    Verify SQL syntax
    ${is_valid}=    Validate SQL Syntax    ${RESPONSE.sql}
    Should Be True    ${is_valid}

SQL Should Reference Correct Tables
    [Documentation]    Verify table references
    ${tables}=    Extract Referenced Tables    ${RESPONSE.sql}
    Should Contain    ${tables}    users
    Should Not Contain    ${tables}    nonexistent_table

Query Should Execute Successfully
    [Documentation]    Verify query execution
    ${start_time}=    Get Current Time
    ${results}=    Execute SQL    ${RESPONSE.sql}
    ${end_time}=    Get Current Time
    ${duration}=    Subtract Date From Date    ${end_time}    ${start_time}
    Should Be True    ${duration} < ${PERFORMANCE_LIMIT}
    Should Not Be Empty    ${results}

Results Should Match Expected Data
    [Documentation]    Verify result correctness
    ${results}=    Execute SQL    ${RESPONSE.sql}
    ${expected}=    Get Expected Results
    Compare Results    ${results}    ${expected}

SQL Should Include Required Analytics
    [Documentation]    Verify analytical components
    ${sql}=    Set Variable    ${RESPONSE.sql}
    Should Match Regexp    ${sql}    (?i)AVG\\(.*\\)
    Should Match Regexp    ${sql}    (?i)GROUP BY
    Should Match Regexp    ${sql}    (?i)ORDER BY
    Should Match Regexp    ${sql}    (?i)2024

Query Performance Should Be Acceptable
    [Documentation]    Verify query performance
    ${metrics}=    Get Query Metrics
    Should Be True    ${metrics.execution_time} < ${PERFORMANCE_LIMIT}
    Should Be True    ${metrics.memory_usage} < 1000

Initial SQL Should Be Generated
    [Documentation]    Verify initial query generation
    Should Not Be Empty    ${RESPONSE.sql}
    Set Test Variable    ${INITIAL_SQL}    ${RESPONSE.sql}

Query Should Be Improved Through Feedback
    [Documentation]    Verify query improvement
    ${improved_sql}=    Apply Feedback Loop    ${INITIAL_SQL}
    Set Test Variable    ${IMPROVED_SQL}    ${improved_sql}
    Should Not Be Equal    ${INITIAL_SQL}    ${IMPROVED_SQL}

Final Query Should Be More Specific
    [Documentation]    Verify query specificity improvement
    ${initial_specificity}=    Calculate Query Specificity    ${INITIAL_SQL}
    ${final_specificity}=    Calculate Query Specificity    ${IMPROVED_SQL}
    Should Be True    ${final_specificity} > ${initial_specificity}

Results Should Be More Relevant
    [Documentation]    Verify result relevance improvement
    ${initial_results}=    Execute SQL    ${INITIAL_SQL}
    ${final_results}=    Execute SQL    ${IMPROVED_SQL}
    ${relevance_improved}=    Compare Result Relevance
    ...    ${initial_results}    ${final_results}
    Should Be True    ${relevance_improved}

Initial Schema Is Recorded
    [Documentation]    Record initial schema state
    ${schema}=    Get Database Schema
    Set Test Variable    ${INITIAL_SCHEMA}    ${schema}

Schema Is Modified
    [Documentation]    Modify database schema
    Execute SQL    ALTER TABLE users ADD COLUMN new_field TEXT;
    ${new_schema}=    Get Database Schema
    Set Test Variable    ${NEW_SCHEMA}    ${new_schema}

SQL Should Adapt To New Schema
    [Documentation]    Verify schema adaptation
    Should Not Be Empty    ${RESPONSE.sql}
    Should Contain    ${RESPONSE.sql}    new_field

User Asks Sequential Questions
    [Documentation]    Ask series of related questions
    @{QUESTIONS}=    Create List
    ...    Show me all users
    ...    Show their recent orders
    ...    Calculate their average order value
    FOR    ${question}    IN    @{QUESTIONS}
        User Asks    ${question}
        Query Should Build On Previous
    END

Each Query Should Build On Previous Context
    [Documentation]    Verify context utilization
    ${context_score}=    Calculate Context Usage
    Should Be True    ${context_score} > 0.7

Results Should Be Progressively More Specific
    [Documentation]    Verify increasing specificity
    ${specificity_trend}=    Calculate Specificity Trend
    Should Be True    ${specificity_trend} > 0

Context Should Be Properly Maintained
    [Documentation]    Verify context maintenance
    ${context}=    Get Current Context
    Verify Context Integrity    ${context}

Query Should Build On Previous
    [Documentation]    Verify query builds on context
    ${context_usage}=    Analyze Context Usage    ${RESPONSE.sql}
    Should Be True    ${context_usage} > ${MIN_CONFIDENCE}
