*** Settings ***
Documentation     Test suite for advanced Text2SQL queries
Resource          ../resources/text2sql_common.robot
Test Setup       Initialize Text2SQL Environment
Test Teardown    Cleanup Text2SQL Environment
Force Tags       text2sql    regression    advanced

*** Test Cases ***
Test Should Handle Complex Aggregations
    [Tags]    high    aggregation
    [Documentation]    Test complex aggregation functions
    Given Schema Is Available
    When User Asks "Calculate monthly revenue growth rate for 2024"
    Then SQL Should Be Generated
    And SQL Should Use Window Functions
    And SQL Should Calculate Growth Rate
    And Results Should Show Monthly Trends

Test Should Support Subqueries
    [Tags]    high    subquery
    [Documentation]    Test subquery handling
    Given Schema Is Available
    When User Asks "Find users who spent more than average"
    Then SQL Should Be Generated
    And SQL Should Contain Subquery
    And Subquery Should Calculate Average
    And Results Should Be Correctly Filtered

Test Should Handle Multiple JOINs
    [Tags]    high    join
    [Documentation]    Test multiple JOIN operations
    Given Schema Is Available
    When User Asks "Show product categories with their revenue by customer segment"
    Then SQL Should Be Generated
    And SQL Should Have Multiple JOINs
    And JOINs Should Be In Correct Order
    And Results Should Include All Related Data

Test Should Support HAVING Clause
    [Tags]    medium    having
    [Documentation]    Test HAVING clause functionality
    Given Schema Is Available
    When User Asks "Find customer segments with average order value over $100"
    Then SQL Should Be Generated
    And SQL Should Contain HAVING Clause
    And Results Should Be Filtered By Group

Test Should Handle Date Functions
    [Tags]    medium    date
    [Documentation]    Test date manipulation functions
    Given Schema Is Available
    When User Asks "Show daily order trends for last 30 days"
    Then SQL Should Be Generated
    And SQL Should Use Date Functions
    And Date Range Should Be Correct
    And Results Should Show Daily Trends

Test Should Support Complex Conditions
    [Tags]    high    conditions
    [Documentation]    Test complex WHERE conditions
    Given Schema Is Available
    When User Asks "Find high-value customers who haven't ordered in 3 months"
    Then SQL Should Be Generated
    And SQL Should Have Complex WHERE
    And SQL Should Use Date Comparison
    And Results Should Match Criteria

*** Keywords ***
SQL Should Use Window Functions
    Should Match Regexp    ${RESPONSE.sql}    (?i)OVER\\s*\\(

SQL Should Calculate Growth Rate
    Should Match Regexp    ${RESPONSE.sql}    (?i)LAG|LEAD

Results Should Show Monthly Trends
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    FOR    ${row}    IN    @{results}
        Should Have Key    ${row}    growth_rate
        Should Have Key    ${row}    month
    END

SQL Should Contain Subquery
    Should Match Regexp    ${RESPONSE.sql}    (?i)\\(\\s*SELECT

Subquery Should Calculate Average
    Should Match Regexp    ${RESPONSE.sql}    (?i)AVG\\s*\\(

Results Should Be Correctly Filtered
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    ${avg_result}=    Execute Test Query    SELECT AVG(total_spent) FROM user_spending
    FOR    ${row}    IN    @{results}
        Should Be True    ${row.total_spent} > ${avg_result[0].avg}
    END

SQL Should Have Multiple JOINs
    ${join_count}=    Get Count    ${RESPONSE.sql}    JOIN
    Should Be True    ${join_count} >= 2

JOINs Should Be In Correct Order
    Should Match Regexp    ${RESPONSE.sql}    (?i)FROM.*JOIN.*JOIN

Results Should Include All Related Data
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    ${first_row}=    Set Variable    ${results}[0]
    Should Have Key    ${first_row}    category
    Should Have Key    ${first_row}    segment
    Should Have Key    ${first_row}    revenue

SQL Should Contain HAVING Clause
    Should Match Regexp    ${RESPONSE.sql}    (?i)HAVING

Results Should Be Filtered By Group
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    FOR    ${row}    IN    @{results}
        Should Be True    ${row.avg_order_value} > 100
    END

SQL Should Use Date Functions
    Should Match Regexp    ${RESPONSE.sql}    (?i)DATE|INTERVAL

Date Range Should Be Correct
    Should Match Regexp    ${RESPONSE.sql}    (?i)INTERVAL\\s+'30 days'

Results Should Show Daily Trends
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    FOR    ${row}    IN    @{results}
        Should Have Key    ${row}    date
        Should Have Key    ${row}    order_count
    END

SQL Should Have Complex WHERE
    ${condition_count}=    Get Count    ${RESPONSE.sql}    AND|OR
    Should Be True    ${condition_count} >= 2

SQL Should Use Date Comparison
    Should Match Regexp    ${RESPONSE.sql}    (?i)INTERVAL\\s+'3 months'

Results Should Match Criteria
    ${results}=    Execute Test Query    ${RESPONSE.sql}
    Verify Query Results    ${results}
    FOR    ${row}    IN    @{results}
        Should Be True    ${row.total_spent} >= 1000
        ${months_since_order}=    Calculate Months Since Order    ${row.last_order_date}
        Should Be True    ${months_since_order} >= 3
    END

Calculate Months Since Order
    [Arguments]    ${last_order_date}
    ${current_date}=    Get Current Date
    ${diff}=    Subtract Date From Date    ${current_date}    ${last_order_date}
    ${months}=    Evaluate    ${diff.days} / 30
    [Return]    ${months}
