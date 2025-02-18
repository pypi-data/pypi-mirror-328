*** Settings ***
Documentation     Test suite for Text-to-SQL hybrid architecture functionality
Resource          resources/text2sql_keywords.robot
Suite Setup       Initialize Test Environment
Suite Teardown    Clean Up Test Environment
Test Setup       Initialize Test Case
Test Teardown    Clean Up Test Case
Force Tags       text2sql    hybrid    regression

*** Variables ***
@{BASIC_TABLES}    users    orders    products
@{USER_COLUMNS}    id    username    email    created_at
@{ORDER_COLUMNS}    id    user_id    total_amount    status

*** Test Cases ***
Test Should Convert Simple Query Using Hybrid Architecture
    [Documentation]    Tests basic query conversion using hybrid components
    [Tags]    smoke    critical    stable
    Given Test Database Contains Sample Data
    When User Executes Query    show me all active users
    Then SQL Should Be Generated    SELECT * FROM users WHERE status = 'active'
    And Query Should Use Core Components
    And Query Should Use Agent Components

Test Should Apply Security Checks In Hybrid Flow
    [Documentation]    Tests security validation in hybrid processing
    [Tags]    security    high    stable
    Given Test Database Contains Sample Data
    When User Executes Query    select all users where id = '1; DROP TABLE users;'
    Then Query Should Be Rejected
    And Security Agent Should Report Injection Attempt
    And Event Should Be Logged

Test Should Optimize Complex Query Using Hybrid Components
    [Documentation]    Tests query optimization in hybrid processing
    [Tags]    performance    high    stable
    Given Test Database Contains Sample Data
    When User Executes Query    find users who ordered more than 5 products last month
    Then SQL Should Be Generated With Optimization
    And Query Should Use Indexes
    And Performance Metrics Should Be Collected

Test Should Handle Schema Changes Through Hybrid Architecture
    [Documentation]    Tests schema adaptation capabilities
    [Tags]    schema    medium    stable
    Given Test Database Contains Sample Data
    When Database Schema Is Modified
    And User Executes Query    show me all users
    Then Schema Should Be Relearned
    And SQL Should Be Generated Correctly
    And Context Should Be Updated

Test Should Process Feedback In Hybrid Architecture
    [Documentation]    Tests feedback processing in hybrid system
    [Tags]    feedback    medium    stable
    Given Previous Query Results Exist
    When User Provides Query Feedback    ${QUERY_ID}    incorrect_results
    Then Feedback Should Be Processed
    And Learning Components Should Be Updated
    And Future Results Should Improve

*** Keywords ***
Initialize Test Environment
    [Documentation]    Set up test environment with sample data
    Initialize Test Database
    Load Sample Data
    Initialize Text2SQL Engine    enable_security=True    enable_monitoring=True

Initialize Test Case
    [Documentation]    Set up for individual test case
    Reset Test State
    Clear Logs

Clean Up Test Case
    [Documentation]    Clean up after individual test case
    Clear Cache
    Reset Agents

Test Database Contains Sample Data
    [Documentation]    Ensures test data is present
    Execute SQL Script    ${CURDIR}/test_data/sample_data.sql
    Verify Data Loaded

User Executes Query
    [Documentation]    Executes a natural language query
    [Arguments]    ${query_text}
    ${result}=    Execute Natural Language Query    ${query_text}
    Set Test Variable    ${QUERY_RESULT}    ${result}

SQL Should Be Generated
    [Documentation]    Verifies SQL query generation
    [Arguments]    ${expected_sql}
    Should Be Equal As Strings    ${QUERY_RESULT.sql}    ${expected_sql}

Query Should Use Core Components
    [Documentation]    Verifies core component usage
    ${metrics}=    Get Processing Metrics
    Dictionary Should Contain Key    ${metrics}    core_components_used
    Should Be True    ${metrics.core_components_used} > 0

Query Should Use Agent Components
    [Documentation]    Verifies agent component usage
    ${metrics}=    Get Processing Metrics
    Dictionary Should Contain Key    ${metrics}    agent_components_used
    Should Be True    ${metrics.agent_components_used} > 0

Query Should Be Rejected
    [Documentation]    Verifies query rejection
    Should Be Equal As Strings    ${QUERY_RESULT.status}    rejected
    Should Not Be Empty    ${QUERY_RESULT.security_issues}

Security Agent Should Report Injection Attempt
    [Documentation]    Verifies security agent detection
    ${security_logs}=    Get Security Logs
    Should Contain    ${security_logs}    SQL injection attempt detected

Event Should Be Logged
    [Documentation]    Verifies event logging
    ${logs}=    Get System Logs
    Should Contain    ${logs}    Security violation detected

SQL Should Be Generated With Optimization
    [Documentation]    Verifies query optimization
    ${metrics}=    Get Processing Metrics
    Should Be True    ${metrics.optimization_applied}
    Should Be True    ${metrics.performance_score} >= 0.8

Query Should Use Indexes
    [Documentation]    Verifies index usage
    ${explain_plan}=    Get Query Explain Plan    ${QUERY_RESULT.sql}
    Should Contain    ${explain_plan}    USING INDEX

Performance Metrics Should Be Collected
    [Documentation]    Verifies performance monitoring
    ${metrics}=    Get Processing Metrics
    Dictionary Should Contain Key    ${metrics}    execution_time
    Dictionary Should Contain Key    ${metrics}    memory_usage
    Dictionary Should Contain Key    ${metrics}    cpu_usage

Database Schema Is Modified
    [Documentation]    Modifies database schema
    Execute SQL Script    ${CURDIR}/test_data/schema_modification.sql
    Verify Schema Changed

Schema Should Be Relearned
    [Documentation]    Verifies schema relearning
    ${metrics}=    Get Processing Metrics
    Should Be True    ${metrics.schema_relearned}

SQL Should Be Generated Correctly
    [Documentation]    Verifies correct SQL generation
    Should Not Be Empty    ${QUERY_RESULT.sql}
    Should Be True    ${QUERY_RESULT.confidence} >= 0.8

Context Should Be Updated
    [Documentation]    Verifies context update
    ${context}=    Get Current Context
    Should Not Be Empty    ${context.schema_version}
    Should Be Equal    ${context.schema_version}    ${EXPECTED_SCHEMA_VERSION}

Previous Query Results Exist
    [Documentation]    Ensures previous query results exist
    ${query_id}=    Execute Test Query
    Set Test Variable    ${QUERY_ID}    ${query_id}

User Provides Query Feedback
    [Documentation]    Provides feedback for a query
    [Arguments]    ${query_id}    ${feedback_type}
    Submit Query Feedback    ${query_id}    ${feedback_type}

Feedback Should Be Processed
    [Documentation]    Verifies feedback processing
    ${metrics}=    Get Processing Metrics
    Should Be True    ${metrics.feedback_processed}

Learning Components Should Be Updated
    [Documentation]    Verifies learning component updates
    ${state}=    Get Learning State
    Should Be True    ${state.updated}
    Should Not Be Empty    ${state.last_update}

Future Results Should Improve
    [Documentation]    Verifies improvement in results
    ${baseline_score}=    Get Baseline Score
    ${new_score}=    Get Current Score
    Should Be True    ${new_score} > ${baseline_score}
