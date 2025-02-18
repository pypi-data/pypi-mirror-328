*** Settings ***
Documentation     Performance tests for Text2SQL functionality
Resource          ../../resources/common.robot
Library           RequestsLibrary
Library           Collections
Library           Process
Test Setup       Setup Performance Test
Test Teardown    Teardown Performance Test
Force Tags       text2sql    performance

*** Variables ***
${API_BASE_URL}         http://localhost:8000
${HEADERS}             {"Content-Type": "application/json"}
${CONCURRENT_USERS}    10
${TEST_DURATION}       60
${RAMP_UP_TIME}        30

*** Test Cases ***
Test Should Handle Concurrent Simple Queries
    [Documentation]    Test performance with concurrent simple queries
    [Tags]    performance    load    critical
    ${test_plan}=    Create Dictionary
    ...    query=Find all users
    ...    schema=${SIMPLE_SCHEMA}
    ...    concurrent_users=${CONCURRENT_USERS}
    ...    duration=${TEST_DURATION}
    ...    ramp_up=${RAMP_UP_TIME}
    ${result}=    Run Load Test    ${test_plan}
    Verify Performance Metrics    ${result}    1000    99    500

Test Should Handle Complex Query Performance
    [Documentation]    Test performance with complex queries
    [Tags]    performance    load    high
    ${test_plan}=    Create Dictionary
    ...    query=Find all users who ordered products in Electronics category with total amount greater than $1000
    ...    schema=${COMPLEX_SCHEMA}
    ...    concurrent_users=${CONCURRENT_USERS}
    ...    duration=${TEST_DURATION}
    ...    ramp_up=${RAMP_UP_TIME}
    ${result}=    Run Load Test    ${test_plan}
    Verify Performance Metrics    ${result}    2000    95    1000

Test Should Handle Batch Query Performance
    [Documentation]    Test performance of batch query processing
    [Tags]    performance    load    high
    ${queries}=    Create List
    ...    Find all users
    ...    Find all orders
    ...    Find users who joined today
    ${test_plan}=    Create Dictionary
    ...    queries=${queries}
    ...    schema=${COMPLEX_SCHEMA}
    ...    concurrent_users=${CONCURRENT_USERS}
    ...    duration=${TEST_DURATION}
    ...    ramp_up=${RAMP_UP_TIME}
    ${result}=    Run Load Test    ${test_plan}    endpoint=/api/v1/translate-batch
    Verify Performance Metrics    ${result}    3000    95    1500

Test Should Handle Query Template Performance
    [Documentation]    Test performance with query templates
    [Tags]    performance    load    medium
    ${test_plan}=    Create Dictionary
    ...    query=Find users where age > 25 and city = 'New York'
    ...    template_id=find_by_criteria
    ...    schema=${COMPLEX_SCHEMA}
    ...    concurrent_users=${CONCURRENT_USERS}
    ...    duration=${TEST_DURATION}
    ...    ramp_up=${RAMP_UP_TIME}
    ${result}=    Run Load Test    ${test_plan}    endpoint=/api/v1/translate-template
    Verify Performance Metrics    ${result}    1500    97    750

Test Should Handle Long-Running Query Performance
    [Documentation]    Test performance with long-running queries
    [Tags]    performance    load    high
    ${test_plan}=    Create Dictionary
    ...    query=Find users who made more than 10 orders with total amount greater than $1000 in Electronics category last month
    ...    schema=${COMPLEX_SCHEMA}
    ...    concurrent_users=${CONCURRENT_USERS}
    ...    duration=${TEST_DURATION}
    ...    ramp_up=${RAMP_UP_TIME}
    ${result}=    Run Load Test    ${test_plan}
    Verify Performance Metrics    ${result}    5000    90    2500

*** Keywords ***
Setup Performance Test
    Create Session    text2sql    ${API_BASE_URL}
    Start Monitoring Resources

Teardown Performance Test
    Delete All Sessions
    Stop Monitoring Resources
    Generate Performance Report

Run Load Test
    [Arguments]    ${test_plan}    ${endpoint}=/api/v1/translate
    ${result}=    Start Process
    ...    locust
    ...    -f    ${EXECDIR}/performance/locustfile.py
    ...    --host=${API_BASE_URL}
    ...    --users=${test_plan["concurrent_users"]}
    ...    --spawn-rate=${test_plan["ramp_up"]}
    ...    --run-time=${test_plan["duration"]}s
    ...    --headless
    ...    --only-summary
    ...    --json
    ...    endpoint=${endpoint}
    ...    test_plan=${test_plan}
    Wait For Process    ${result}
    [Return]    ${result.stdout}

Verify Performance Metrics
    [Arguments]    ${result}    ${max_response_time}    ${success_rate}    ${avg_response_time}
    ${metrics}=    Evaluate    json.loads('''${result}''')    json
    Should Be True    ${metrics["max_response_time"]} <= ${max_response_time}
    Should Be True    ${metrics["success_rate"]} >= ${success_rate}
    Should Be True    ${metrics["avg_response_time"]} <= ${avg_response_time}

Start Monitoring Resources
    Start Process
    ...    python
    ...    ${EXECDIR}/performance/monitor.py
    ...    --output=${EXECDIR}/results/resources.csv
    ...    alias=monitor

Stop Monitoring Resources
    Terminate Process    monitor

Generate Performance Report
    ${report}=    Start Process
    ...    python
    ...    ${EXECDIR}/performance/report.py
    ...    --results=${EXECDIR}/results
    ...    --output=${EXECDIR}/results/report.html
    Wait For Process    ${report}

${SIMPLE_SCHEMA}=    Set Variable
...    {"tables": ["users"], "columns": {"users": ["id", "name", "email"]}}

${COMPLEX_SCHEMA}=    Set Variable
...    {"tables": ["users", "orders", "products"], "columns": {"users": ["id", "name", "email", "joined_at"], "orders": ["id", "user_id", "product_id", "amount"], "products": ["id", "name", "price", "category"]}, "relationships": [["orders.user_id", "users.id"], ["orders.product_id", "products.id"]]}
