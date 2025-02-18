*** Settings ***
Documentation     Test suite for basic Text2SQL queries
Resource          ../resources/text2sql_common.robot
Test Setup       Initialize Text2SQL Environment
Test Teardown    Cleanup Text2SQL Environment
Force Tags       text2sql    regression    basic

*** Test Cases ***
Test Should Generate Valid SQL For Simple Select Query
    [Tags]    smoke    critical    select
    [Documentation]    Test basic SELECT query generation
    Given Schema Is Available
    When User Asks "${SIMPLE_QUERY.question}"
    Then SQL Should Be Generated
    And SQL Should Contain SELECT Statement
    And SQL Should Reference Correct Table    ${SIMPLE_QUERY.expected_table}
    And Results Should Be Returned

Test Should Handle Basic WHERE Conditions
    [Tags]    high    where
    [Documentation]    Test handling of WHERE conditions
    Given Schema Is Available
    When User Asks "Find users with email ending in @gmail.com"
    Then SQL Should Be Generated
    And SQL Should Contain WHERE Clause
    And SQL Should Use LIKE Operator
    And Results Should Be Filtered

Test Should Support Basic Aggregations
    [Tags]    high    aggregation
    [Documentation]    Test basic aggregation functions
    Given Schema Is Available
    When User Asks "Count total number of users by city"
    Then SQL Should Be Generated
    And SQL Should Contain COUNT Function
    And SQL Should Have GROUP BY Clause
    And Results Should Be Aggregated

Test Should Handle Basic JOINs
    [Tags]    high    join
    [Documentation]    Test basic JOIN operations
    Given Schema Is Available
    When User Asks "Show user names with their order counts"
    Then SQL Should Be Generated
    And SQL Should Contain JOIN
    And JOIN Should Be On Correct Columns
    And Results Should Include Data From Both Tables

Test Should Support Basic ORDER BY
    [Tags]    medium    order
    [Documentation]    Test ORDER BY functionality
    Given Schema Is Available
    When User Asks "List users ordered by registration date"
    Then SQL Should Be Generated
    And SQL Should Contain ORDER BY Clause
    And Results Should Be Ordered

*** Keywords ***
Schema Is Available
    ${schema}=    Get Test Schema
    Should Not Be Empty    ${schema}

User Asks
    [Arguments]    ${question}
    ${response}=    Generate SQL    ${question}
    Set Test Variable    ${RESPONSE}    ${response}

SQL Should Be Generated
    Should Not Be Empty    ${RESPONSE.sql}

SQL Should Contain SELECT Statement
    Should Match Regexp    ${RESPONSE.sql}    (?i)^\\s*SELECT

SQL Should Reference Correct Table
    [Arguments]    ${table}
    Should Match Regexp    ${RESPONSE.sql}    (?i)FROM\\s+${table}

Results Should Be Returned
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}

SQL Should Contain WHERE Clause
    Should Match Regexp    ${RESPONSE.sql}    (?i)WHERE

SQL Should Use LIKE Operator
    Should Match Regexp    ${RESPONSE.sql}    (?i)LIKE\\s+'%@gmail\\.com'

Results Should Be Filtered
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    FOR    ${row}    IN    @{results}
        Should Match Regexp    ${row.email}    @gmail\\.com$
    END

SQL Should Contain COUNT Function
    Should Match Regexp    ${RESPONSE.sql}    (?i)COUNT\\s*\\(

SQL Should Have GROUP BY Clause
    Should Match Regexp    ${RESPONSE.sql}    (?i)GROUP\\s+BY

Results Should Be Aggregated
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    FOR    ${row}    IN    @{results}
        Should Have Key    ${row}    count

SQL Should Contain JOIN
    Should Match Regexp    ${RESPONSE.sql}    (?i)JOIN

JOIN Should Be On Correct Columns
    Should Match Regexp    ${RESPONSE.sql}    (?i)ON\\s+users\\.id\\s*=\\s*orders\\.user_id

Results Should Include Data From Both Tables
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    ${first_row}=    Set Variable    ${results}[0]
    Should Have Key    ${first_row}    name
    Should Have Key    ${first_row}    order_count

SQL Should Contain ORDER BY Clause
    Should Match Regexp    ${RESPONSE.sql}    (?i)ORDER\\s+BY

Results Should Be Ordered
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    ${dates}=    Create List
    FOR    ${row}    IN    @{results}
        Append To List    ${dates}    ${row.registration_date}
    END
    Lists Should Be Equal    ${dates}    ${dates}    sort=True
