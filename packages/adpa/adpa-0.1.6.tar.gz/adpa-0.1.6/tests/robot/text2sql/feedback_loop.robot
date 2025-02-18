*** Settings ***
Documentation     Test suite for Text2SQL feedback loop functionality
Resource          ../resources/text2sql_common.robot
Test Setup       Initialize Text2SQL Environment
Test Teardown    Cleanup Text2SQL Environment
Force Tags       text2sql    regression    feedback

*** Test Cases ***
Test Should Improve Query Through Feedback
    [Tags]    critical    feedback
    [Documentation]    Test query improvement through feedback loop
    Given Schema Is Available
    When User Asks Complex Question
    Then Initial SQL Should Be Generated
    And Feedback Loop Should Improve Query
    And Final Query Should Be Better
    And Results Should Be More Accurate

Test Should Learn From Previous Queries
    [Tags]    high    learning
    [Documentation]    Test learning from query history
    Given Schema Is Available
    And Previous Queries Exist
    When User Asks Similar Question
    Then Generated SQL Should Use Context
    And Query Should Be More Efficient
    And Results Should Be Consistent

Test Should Handle Failed Attempts Gracefully
    [Tags]    high    error_handling
    [Documentation]    Test handling of failed query attempts
    Given Schema Is Available
    When User Asks Problematic Question
    Then Multiple Attempts Should Be Made
    And Each Attempt Should Be Different
    And Final Result Should Be Valid

Test Should Maintain Context Between Queries
    [Tags]    medium    context
    [Documentation]    Test context maintenance
    Given Schema Is Available
    When User Asks Sequential Questions
    Then Context Should Be Updated
    And Later Queries Should Use Context
    And Results Should Be Related

Test Should Validate Query Improvements
    [Tags]    high    validation
    [Documentation]    Test validation of query improvements
    Given Schema Is Available
    When User Asks Question Requiring Improvement
    Then Initial Query Should Be Validated
    And Improvements Should Be Suggested
    And Final Query Should Pass Validation

Test Should Track Performance Metrics
    [Tags]    medium    performance
    [Documentation]    Test performance tracking
    Given Schema Is Available
    When User Asks Performance Sensitive Question
    Then Performance Metrics Should Be Collected
    And Metrics Should Show Improvement
    And Final Query Should Be Efficient

*** Keywords ***
User Asks Complex Question
    ${question}=    Set Variable    Calculate quarterly revenue growth by product category
    User Asks    ${question}

Initial SQL Should Be Generated
    Set Test Variable    ${INITIAL_SQL}    ${RESPONSE.sql}
    Should Not Be Empty    ${INITIAL_SQL}

Feedback Loop Should Improve Query
    ${improved}=    Apply Feedback Loop    ${INITIAL_SQL}
    Set Test Variable    ${IMPROVED_SQL}    ${improved}

Final Query Should Be Better
    ${initial_score}=    Evaluate Query Quality    ${INITIAL_SQL}
    ${final_score}=    Evaluate Query Quality    ${IMPROVED_SQL}
    Should Be True    ${final_score} > ${initial_score}

Results Should Be More Accurate
    ${initial_results}=    Execute Test Query    ${INITIAL_SQL}
    ${final_results}=    Execute Test Query    ${IMPROVED_SQL}
    ${accuracy_improved}=    Compare Results Accuracy    ${initial_results}    ${final_results}
    Should Be True    ${accuracy_improved}

Previous Queries Exist
    Load Historical Queries
    ${history}=    Get Query History
    Should Not Be Empty    ${history}

User Asks Similar Question
    ${similar_question}=    Get Similar Question
    User Asks    ${similar_question}

Generated SQL Should Use Context
    ${context_usage}=    Analyze Context Usage    ${RESPONSE.sql}
    Should Be True    ${context_usage.score} > ${CONTEXT_THRESHOLD}

Query Should Be More Efficient
    ${metrics}=    Get Query Metrics
    Should Be True    ${metrics.execution_time} < ${PERFORMANCE_THRESHOLD}

Results Should Be Consistent
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Results Consistency    ${results}

User Asks Problematic Question
    ${question}=    Set Variable    Show me everything wrong with the database
    User Asks    ${question}

Multiple Attempts Should Be Made
    ${attempts}=    Get Attempt Count
    Should Be True    ${attempts} > 1

Each Attempt Should Be Different
    ${attempts}=    Get All Attempts
    Verify Attempts Uniqueness    ${attempts}

Final Result Should Be Valid
    Verify Query Validity    ${RESPONSE.sql}

User Asks Sequential Questions
    @{questions}=    Create List
    ...    Show me all users
    ...    Show their recent orders
    ...    Calculate their average order value
    FOR    ${question}    IN    @{questions}
        User Asks    ${question}
        Verify Progressive Context    ${question}
    END

Context Should Be Updated
    ${context}=    Get Current Context
    Verify Context Updates    ${context}

Later Queries Should Use Context
    ${context_usage}=    Analyze Context Usage    ${RESPONSE.sql}
    Should Be True    ${context_usage.progressive_score} > ${CONTEXT_THRESHOLD}

Results Should Be Related
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Results Relationship    ${results}

User Asks Question Requiring Improvement
    ${question}=    Set Variable    Find users who ordered most in terms of value
    User Asks    ${question}

Initial Query Should Be Validated
    ${validation}=    Validate Query    ${RESPONSE.sql}
    Set Test Variable    ${INITIAL_VALIDATION}    ${validation}

Improvements Should Be Suggested
    ${suggestions}=    Get Improvement Suggestions    ${INITIAL_VALIDATION}
    Should Not Be Empty    ${suggestions}

Final Query Should Pass Validation
    ${final_validation}=    Validate Query    ${RESPONSE.sql}
    Should Be True    ${final_validation.passed}

User Asks Performance Sensitive Question
    ${question}=    Set Variable    Analyze daily order patterns for the past year
    User Asks    ${question}

Performance Metrics Should Be Collected
    ${metrics}=    Get Query Metrics
    Should Not Be Empty    ${metrics}

Metrics Should Show Improvement
    ${metrics_history}=    Get Metrics History
    Verify Metrics Improvement    ${metrics_history}

Final Query Should Be Efficient
    ${metrics}=    Get Query Metrics
    Should Be True    ${metrics.execution_time} < ${PERFORMANCE_THRESHOLD}
    Should Be True    ${metrics.memory_usage} < 1000  # MB
