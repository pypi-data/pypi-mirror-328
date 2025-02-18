*** Settings ***
Documentation     Technical tests for API endpoints
Resource          ../../resources/api.resource
Library           RequestsLibrary
Library           Collections

*** Variables ***
${API_BASE_URL}    http://localhost:8000/api
${TEST_USER}       test_user
${TEST_TOKEN}      test_token

*** Test Cases ***
Test API Authentication
    [Documentation]    Test API authentication mechanisms
    [Tags]    technical    security    auth
    ${credentials}=    Create Dictionary    username=${TEST_USER}    password=test_pass
    ${response}=    POST    ${API_BASE_URL}/auth    json=${credentials}
    Should Be Equal As Integers    ${response.status_code}    200
    Dictionary Should Contain Key    ${response.json()}    token

Test Rate Limiting
    [Documentation]    Test API rate limiting
    [Tags]    technical    security    rate-limit
    FOR    ${i}    IN RANGE    100
        ${response}=    GET    ${API_BASE_URL}/endpoint
        Run Keyword If    ${response.status_code} == 429    Exit For Loop
    END
    Should Be Equal As Integers    ${response.status_code}    429

Test Endpoint Response Times
    [Documentation]    Test API endpoint performance
    [Tags]    technical    performance
    @{endpoints}=    Create List    /users    /projects    /tasks
    FOR    ${endpoint}    IN    @{endpoints}
        ${start_time}=    Get Time    epoch
        GET    ${API_BASE_URL}${endpoint}
        ${end_time}=    Get Time    epoch
        ${response_time}=    Evaluate    ${end_time} - ${start_time}
        Should Be True    ${response_time} < 1.0
    END

Test Request Validation
    [Documentation]    Test API request validation
    [Tags]    technical    validation
    ${invalid_data}=    Create Dictionary    invalid_field=value
    ${response}=    POST    ${API_BASE_URL}/data    json=${invalid_data}
    Should Be Equal As Integers    ${response.status_code}    400
    Dictionary Should Contain Key    ${response.json()}    errors

Test Response Format
    [Documentation]    Test API response format consistency
    [Tags]    technical    format
    ${response}=    GET    ${API_BASE_URL}/data
    Verify JSON Schema    ${response.json()}    expected_schema.json

Test Concurrent Requests
    [Documentation]    Test API handling of concurrent requests
    [Tags]    technical    concurrency
    ${responses}=    Send Concurrent Requests    ${API_BASE_URL}    10
    FOR    ${response}    IN    @{responses}
        Should Be Equal As Integers    ${response.status_code}    200
    END

Test Error Responses
    [Documentation]    Test API error handling
    [Tags]    technical    error
    ${response}=    GET    ${API_BASE_URL}/nonexistent
    Should Be Equal As Integers    ${response.status_code}    404
    Dictionary Should Contain Key    ${response.json()}    error

Test Content Negotiation
    [Documentation]    Test API content negotiation
    [Tags]    technical    content
    ${headers}=    Create Dictionary    Accept=application/xml
    ${response}=    GET    ${API_BASE_URL}/data    headers=${headers}
    Should Be Equal As Integers    ${response.status_code}    406

Test CORS Configuration
    [Documentation]    Test API CORS settings
    [Tags]    technical    security    cors
    ${headers}=    Create Dictionary    Origin=http://example.com
    ${response}=    OPTIONS    ${API_BASE_URL}/data    headers=${headers}
    Dictionary Should Contain Key    ${response.headers}    Access-Control-Allow-Origin
