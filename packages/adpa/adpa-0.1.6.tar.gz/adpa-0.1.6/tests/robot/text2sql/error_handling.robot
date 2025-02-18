*** Settings ***
Documentation     Test suite for Text2SQL error handling
Resource          ../resources/text2sql_common.robot
Test Setup       Initialize Text2SQL Environment
Test Teardown    Cleanup Text2SQL Environment
Force Tags       text2sql    regression    error

*** Test Cases ***
Test Should Handle Invalid Input Questions
    [Tags]    high    input
    [Documentation]    Test handling of invalid input questions
    Given Schema Is Available
    When User Asks Invalid Question
    Then Error Should Be Returned
    And Error Message Should Be Clear
    And Suggestions Should Be Provided

Test Should Handle Schema Validation Errors
    [Tags]    high    schema
    [Documentation]    Test handling of schema validation errors
    Given Schema Is Available
    When User Asks Question With Invalid Schema
    Then Schema Error Should Be Detected
    And Error Should Explain Schema Issue
    And Valid Alternatives Should Be Suggested

Test Should Handle Execution Errors
    [Tags]    high    execution
    [Documentation]    Test handling of query execution errors
    Given Schema Is Available
    When User Asks Question Leading To Execution Error
    Then Execution Error Should Be Caught
    And Error Should Be Well Formatted
    And Recovery Options Should Be Provided

Test Should Handle Timeout Scenarios
    [Tags]    medium    timeout
    [Documentation]    Test handling of query timeouts
    Given Schema Is Available
    When User Asks Resource Intensive Question
    Then Timeout Should Be Detected
    And Appropriate Error Should Be Returned
    And Optimization Suggestions Should Be Provided

Test Should Handle Context Errors
    [Tags]    medium    context
    [Documentation]    Test handling of context-related errors
    Given Schema Is Available
    When Context Is Corrupted
    Then Context Error Should Be Detected
    And Error Should Explain Context Issue
    And Context Should Be Reset

Test Should Handle Multiple Errors
    [Tags]    high    multiple
    [Documentation]    Test handling of multiple concurrent errors
    Given Schema Is Available
    When Multiple Errors Occur
    Then All Errors Should Be Captured
    And Errors Should Be Prioritized
    And Most Critical Error Should Be Highlighted

*** Keywords ***
User Asks Invalid Question
    ${question}=    Set Variable    ${INVALID_QUERY.question}
    Run Keyword And Expect Error    *    User Asks    ${question}

Error Should Be Returned
    ${error}=    Get Last Error
    Should Not Be Empty    ${error}

Error Message Should Be Clear
    ${error}=    Get Last Error
    Should Match    ${error.message}    ${INVALID_QUERY.expected_error}

Suggestions Should Be Provided
    ${suggestions}=    Get Error Suggestions
    Should Not Be Empty    ${suggestions}

User Asks Question With Invalid Schema
    ${question}=    Set Variable    Show me data from nonexistent_table
    Run Keyword And Expect Error    *    User Asks    ${question}

Schema Error Should Be Detected
    ${error}=    Get Last Error
    Should Be Equal    ${error.type}    SchemaError

Error Should Explain Schema Issue
    ${error}=    Get Last Error
    Should Contain    ${error.message}    table does not exist

Valid Alternatives Should Be Suggested
    ${suggestions}=    Get Schema Suggestions
    Should Not Be Empty    ${suggestions}
    FOR    ${suggestion}    IN    @{suggestions}
        ${exists}=    Table Exists    ${suggestion}
        Should Be True    ${exists}
    END

User Asks Question Leading To Execution Error
    ${question}=    Set Variable    Divide total orders by zero
    Run Keyword And Expect Error    *    User Asks    ${question}

Execution Error Should Be Caught
    ${error}=    Get Last Error
    Should Be Equal    ${error.type}    ExecutionError

Error Should Be Well Formatted
    ${error}=    Get Last Error
    Should Match Regexp    ${error.message}    ^Error:\\s+.*\\s+at\\s+line\\s+\\d+

Recovery Options Should Be Provided
    ${options}=    Get Recovery Options
    Should Not Be Empty    ${options}

User Asks Resource Intensive Question
    ${question}=    Set Variable    Analyze all user interactions for the past decade
    Run Keyword And Expect Error    *    User Asks    ${question}

Timeout Should Be Detected
    ${error}=    Get Last Error
    Should Be Equal    ${error.type}    TimeoutError

Appropriate Error Should Be Returned
    ${error}=    Get Last Error
    Should Contain    ${error.message}    query execution timeout

Optimization Suggestions Should Be Provided
    ${suggestions}=    Get Optimization Suggestions
    Should Not Be Empty    ${suggestions}
    FOR    ${suggestion}    IN    @{suggestions}
        Should Contain    ${suggestion}    index
        Or Should Contain    ${suggestion}    limit
        Or Should Contain    ${suggestion}    partition
    END

Context Is Corrupted
    Corrupt Context
    ${question}=    Set Variable    Show me user orders
    Run Keyword And Expect Error    *    User Asks    ${question}

Context Error Should Be Detected
    ${error}=    Get Last Error
    Should Be Equal    ${error.type}    ContextError

Error Should Explain Context Issue
    ${error}=    Get Last Error
    Should Contain    ${error.message}    context corruption detected

Context Should Be Reset
    ${context}=    Get Current Context
    Should Be Empty    ${context}

Multiple Errors Occur
    ${question}=    Set Variable    Show orders from invalid_table where date = invalid_format
    Run Keyword And Expect Error    *    User Asks    ${question}

All Errors Should Be Captured
    ${errors}=    Get All Errors
    Length Should Be    ${errors}    2

Errors Should Be Prioritized
    ${errors}=    Get All Errors
    ${priorities}=    Get Error Priorities    ${errors}
    Lists Should Be Sorted    ${priorities}

Most Critical Error Should Be Highlighted
    ${errors}=    Get All Errors
    ${critical}=    Get Most Critical Error    ${errors}
    Should Be Equal    ${critical.priority}    1
