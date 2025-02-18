*** Settings ***
Documentation     Keywords for Text2SQL testing
Resource         ../resources/common.robot
Library          ../libraries/SQLValidator.py
Library          ../libraries/SchemaLoader.py
Library          ../libraries/QueryAnalyzer.py

*** Keywords ***
Initialize Text2SQL Suite
    [Documentation]    Initialize the test suite
    Connect To Test Database    ${TEST_DB_URL}
    Initialize Schema Loader
    Initialize SQL Validator
    Initialize Query Analyzer

Cleanup Text2SQL Suite
    [Documentation]    Clean up after test suite
    Disconnect From Database
    Reset Schema Loader
    Reset SQL Validator
    Reset Query Analyzer

Reset Test Environment
    [Documentation]    Reset environment before each test
    Clear Query Cache
    Reset Query Context
    Set Default SQL Dialect

Schema Is Loaded From "${schema_file}"
    [Documentation]    Load database schema from file
    ${schema}=    Load Schema From File    ${schema_file}
    Set Test Variable    ${CURRENT_SCHEMA}    ${schema}
    Validate Schema Structure

User Enters Query "${query}"
    [Documentation]    Process natural language query
    Set Test Variable    ${CURRENT_QUERY}    ${query}
    ${result}=    Process Natural Language Query    ${query}    ${CURRENT_SCHEMA}
    Set Test Variable    ${QUERY_RESULT}    ${result}

Generated SQL Should Be "${expected}"
    [Documentation]    Verify generated SQL matches expected
    Should Be Equal As Strings    ${QUERY_RESULT.sql}    ${expected}
    
SQL Should Be Valid
    [Documentation]    Validate generated SQL
    ${is_valid}=    Validate SQL Query    ${QUERY_RESULT.sql}    ${CURRENT_SCHEMA}
    Should Be True    ${is_valid}

No Validation Errors Should Be Present
    [Documentation]    Check for validation errors
    ${errors}=    Get Validation Errors
    Should Be Empty    ${errors}

Generated SQL Should Contain "${text}"
    [Documentation]    Check if SQL contains specific text
    Should Contain    ${QUERY_RESULT.sql}    ${text}

SQL Should Include Table "${table}"
    [Documentation]    Verify SQL references specific table
    ${tables}=    Get Referenced Tables    ${QUERY_RESULT.sql}
    Should Contain    ${tables}    ${table}

SQL Generation Should Fail
    [Documentation]    Verify SQL generation fails as expected
    ${status}=    Get Query Status
    Should Be Equal As Strings    ${status}    FAILED

Error Message Should Contain "${text}"
    [Documentation]    Check error message content
    ${errors}=    Get Error Messages
    Should Contain    ${errors}    ${text}

Database Should Remain Unchanged
    [Documentation]    Verify database integrity
    ${checksum}=    Calculate Database Checksum
    Should Be Equal    ${checksum}    ${INITIAL_CHECKSUM}

Query Performance Monitoring Is Enabled
    [Documentation]    Enable performance monitoring
    Enable Performance Monitoring
    Set Performance Thresholds
    Initialize Metrics Collection

User Enters Complex Query From File "${file}"
    [Documentation]    Load and process complex query
    ${query}=    Get File    ${file}
    Set Test Variable    ${CURRENT_QUERY}    ${query}
    ${result}=    Process Natural Language Query    ${query}    ${CURRENT_SCHEMA}
    Set Test Variable    ${QUERY_RESULT}    ${result}

Generated SQL Should Be Optimized
    [Documentation]    Verify query optimization
    ${metrics}=    Analyze Query Performance    ${QUERY_RESULT.sql}
    Verify Optimization Metrics    ${metrics}
    Should Be Optimized    ${QUERY_RESULT.sql}

Suggested Indexes Should Be Generated
    [Documentation]    Check index suggestions
    ${indexes}=    Get Suggested Indexes    ${QUERY_RESULT.sql}    ${CURRENT_SCHEMA}
    Should Not Be Empty    ${indexes}
    Verify Index Suggestions    ${indexes}

Query Execution Plan Should Be Available
    [Documentation]    Verify execution plan
    ${plan}=    Get Query Execution Plan    ${QUERY_RESULT.sql}
    Should Not Be Empty    ${plan}
    Validate Execution Plan    ${plan}

Suggestion Should Be Provided
    [Documentation]    Check for helpful suggestions
    ${suggestions}=    Get Query Suggestions
    Should Not Be Empty    ${suggestions}
    Should Be Helpful    ${suggestions}

Template "${name}" Is Available
    [Documentation]    Verify template availability
    ${exists}=    Template Exists    ${name}
    Should Be True    ${exists}

User Applies Template With Parameters
    [Documentation]    Apply template with parameters
    [Arguments]    &{params}
    ${result}=    Apply Template    ${params}[template]    ${params}
    Set Test Variable    ${QUERY_RESULT}    ${result}

SQL Should Properly Escape Special Characters
    [Documentation]    Verify proper character escaping
    ${sql}=    Get Generated SQL
    Should Be Properly Escaped    ${sql}

Set SQL Dialect "${dialect}"
    [Documentation]    Set SQL dialect for testing
    Set Dialect    ${dialect}
    Initialize Dialect Specific Validators

Generated SQL Should Be Valid For ${dialect}
    [Documentation]    Validate SQL for specific dialect
    ${is_valid}=    Validate SQL For Dialect    ${QUERY_RESULT.sql}    ${dialect}
    Should Be True    ${is_valid}
