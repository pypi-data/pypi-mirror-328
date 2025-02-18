*** Settings ***
Documentation     API endpoint tests for ADPA Framework
Resource         ../../resources/common.robot
Suite Setup      Initialize API Tests
Suite Teardown   Cleanup API Tests
Force Tags       api    regression

*** Variables ***
${API_BASE_URL}    http://localhost:8000/api/v1
${AUTH_TOKEN}      ${EMPTY}
${VALID_HEADERS}    {"Content-Type": "application/json", "Authorization": "Bearer ${AUTH_TOKEN}"}

*** Test Cases ***
Test Should Authenticate API Requests
    [Documentation]    Test API authentication process
    [Tags]    auth    critical    stable
    ${credentials}=    Create Dictionary    username=test_user    password=test_pass
    ${response}=    POST    ${API_BASE_URL}/auth/token    json=${credentials}
    Should Be Equal As Numbers    ${response.status_code}    200
    Dictionary Should Contain Key    ${response.json()}    access_token
    Set Suite Variable    ${AUTH_TOKEN}    ${response.json()}[access_token]

Test Should Create New Query
    [Documentation]    Test query creation endpoint
    [Tags]    query    high    stable
    ${query_data}=    Create Dictionary
    ...    text=Select all employees
    ...    metadata={"department": "HR"}
    ${response}=    POST    ${API_BASE_URL}/queries    json=${query_data}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    201
    Dictionary Should Contain Key    ${response.json()}    id
    Set Test Variable    ${QUERY_ID}    ${response.json()}[id]

Test Should Retrieve Query By ID
    [Documentation]    Test query retrieval endpoint
    [Tags]    query    high    stable
    ${response}=    GET    ${API_BASE_URL}/queries/${QUERY_ID}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    200
    Dictionary Should Contain Key    ${response.json()}    text
    Dictionary Should Contain Key    ${response.json()}    status

Test Should Update Query Status
    [Documentation]    Test query status update endpoint
    [Tags]    query    high    stable
    ${status_data}=    Create Dictionary    status=completed
    ${response}=    PATCH    ${API_BASE_URL}/queries/${QUERY_ID}    json=${status_data}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    200
    Should Be Equal    ${response.json()}[status]    completed

Test Should List Queries With Filters
    [Documentation]    Test query listing with filters
    [Tags]    query    medium    stable
    ${params}=    Create Dictionary    status=completed    limit=10    offset=0
    ${response}=    GET    ${API_BASE_URL}/queries    params=${params}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    200
    Length Should Be    ${response.json()}[items]    10

Test Should Handle Rate Limiting
    [Documentation]    Test API rate limiting
    [Tags]    security    medium    stable
    FOR    ${i}    IN RANGE    100
        ${response}=    GET    ${API_BASE_URL}/queries    headers=${VALID_HEADERS}
        Run Keyword If    ${response.status_code} == 429    Exit For Loop
    END
    Should Be Equal As Numbers    ${response.status_code}    429
    Dictionary Should Contain Key    ${response.json()}    retry_after

Test Should Execute Query
    [Documentation]    Test query execution endpoint
    [Tags]    query    high    stable
    ${query_data}=    Create Dictionary
    ...    text=Select count(*) from employees
    ...    parameters={"department": "HR"}
    ${response}=    POST    ${API_BASE_URL}/queries/execute    json=${query_data}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    200
    Dictionary Should Contain Key    ${response.json()}    results
    Dictionary Should Contain Key    ${response.json()}    execution_time

Test Should Handle Invalid SQL
    [Documentation]    Test handling of invalid SQL queries
    [Tags]    error    medium    stable
    ${query_data}=    Create Dictionary
    ...    text=SELECT * FROM nonexistent_table
    ${response}=    POST    ${API_BASE_URL}/queries/execute    json=${query_data}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    400
    Dictionary Should Contain Key    ${response.json()}    error
    Dictionary Should Contain Key    ${response.json()}    error_details

Test Should Support Batch Query Execution
    [Documentation]    Test batch query execution
    [Tags]    query    high    stable
    ${queries}=    Create List
    ...    Select count(*) from employees
    ...    Select avg(salary) from employees
    ${batch_data}=    Create Dictionary    queries=${queries}
    ${response}=    POST    ${API_BASE_URL}/queries/batch    json=${batch_data}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    200
    Length Should Be    ${response.json()}[results]    2

Test Should Handle Large Result Sets
    [Documentation]    Test handling of large result sets
    [Tags]    performance    medium    stable
    ${query_data}=    Create Dictionary
    ...    text=Select * from large_table
    ...    page_size=1000
    ${response}=    POST    ${API_BASE_URL}/queries/execute    json=${query_data}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    200
    Dictionary Should Contain Key    ${response.json()}    next_page_token

Test Should Support Query Templates
    [Documentation]    Test query template functionality
    [Tags]    templates    medium    stable
    ${template_data}=    Create Dictionary
    ...    name=employee_stats
    ...    template=SELECT {fields} FROM employees WHERE department = :department
    ${response}=    POST    ${API_BASE_URL}/templates    json=${template_data}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    201
    Set Test Variable    ${TEMPLATE_ID}    ${response.json()}[id]

Test Should Execute Template Query
    [Documentation]    Test execution of template-based query
    [Tags]    templates    medium    stable
    ${params}=    Create Dictionary
    ...    fields=COUNT(*)
    ...    department=HR
    ${response}=    POST    ${API_BASE_URL}/templates/${TEMPLATE_ID}/execute    json=${params}    headers=${VALID_HEADERS}
    Should Be Equal As Numbers    ${response.status_code}    200
    Dictionary Should Contain Key    ${response.json()}    results

*** Keywords ***
Initialize API Tests
    [Documentation]    Initialize API test environment
    Create Test Database
    Start API Server
    Wait Until Keyword Succeeds    30s    1s    API Should Be Available

API Should Be Available
    [Documentation]    Check if API is available
    ${response}=    GET    ${API_BASE_URL}/health
    Should Be Equal As Numbers    ${response.status_code}    200

Cleanup API Tests
    [Documentation]    Clean up after API tests
    Stop API Server
    Drop Test Database
