*** Settings ***
Documentation     Text2SQL API Test Suite
Resource          ../../resources/keywords/text2sql_keywords.robot
Suite Setup       Initialize API Test Environment
Suite Teardown    Cleanup API Test Environment
Test Setup       Reset API State
Test Teardown    Log API Response
Force Tags       text2sql    api
Default Tags     smoke    regression

*** Test Cases ***
Test Should Return Valid SQL For REST API Query
    [Documentation]    Tests the REST API query endpoint
    [Tags]    critical    api    query_translation
    Given API Is Available
    When Send Query Request    Show me all employees
    Then Response Status Should Be    200
    And Response Should Contain Valid SQL
    And Response Time Should Be Less Than    ${TIMEOUT_SHORT}

Test Should Handle Multiple API Requests
    [Documentation]    Tests handling of multiple concurrent requests
    [Tags]    high    api    performance
    Given API Is Available
    When Send Multiple Query Requests
    Then All Responses Should Be Valid
    And Response Times Should Be Consistent

Test Should Validate API Input
    [Documentation]    Tests API input validation
    [Tags]    high    api    validation
    Given API Is Available
    When Send Invalid Query Request
    Then Response Status Should Be    400
    And Response Should Contain Error Message

Test Should Return Proper Error For Unauthorized Access
    [Documentation]    Tests API authentication
    [Tags]    critical    api    security
    Given API Is Available
    When Send Request Without Authentication
    Then Response Status Should Be    401
    And Response Should Contain Auth Error

Test Should Handle API Rate Limiting
    [Documentation]    Tests API rate limiting
    [Tags]    high    api    security
    Given API Is Available
    When Send Requests Above Rate Limit
    Then Response Status Should Be    429
    And Response Should Contain Rate Limit Message

Test Should Return Query History Via API
    [Documentation]    Tests query history API endpoint
    [Tags]    medium    api    history
    Given API Is Available
    When Request Query History
    Then Response Status Should Be    200
    And History Should Be In Correct Format

Test Should Handle Large Result Sets
    [Documentation]    Tests handling of large result sets
    [Tags]    high    api    performance
    Given API Is Available
    When Request Large Result Set
    Then Response Should Be Paginated
    And Response Should Contain Next Page Token

Test Should Support Different Output Formats
    [Documentation]    Tests different output format support
    [Tags]    medium    api    format
    Given API Is Available
    When Request Different Output Formats
    Then All Format Responses Should Be Valid

*** Keywords ***
Initialize API Test Environment
    [Documentation]    Sets up the API test environment
    Create Session    text2sql_api    ${BASE_URL}
    Set Headers

Reset API State
    [Documentation]    Resets API state before each test
    Clear API Cache
    Reset Rate Limits

API Is Available
    [Documentation]    Verifies API is available
    ${response}=    GET On Session    text2sql_api    /health
    Should Be Equal As Strings    ${response.status_code}    200

Send Query Request
    [Documentation]    Sends a query request to the API
    [Arguments]    ${query}
    ${data}=    Create Dictionary    query=${query}
    ${response}=    POST On Session    text2sql_api    /api/query    json=${data}
    Set Test Variable    ${RESPONSE}    ${response}

Response Should Contain Valid SQL
    [Documentation]    Verifies response contains valid SQL
    ${json}=    Set Variable    ${RESPONSE.json()}
    Should Contain    ${json['sql']}    SELECT
    Should Not Contain    ${json['sql']}    ERROR

Send Multiple Query Requests
    [Documentation]    Sends multiple concurrent API requests
    @{responses}=    Create List
    FOR    ${query}    IN    @{SAMPLE_QUERIES}
        ${response}=    Send Query Request    ${query}
        Append To List    ${responses}    ${response}
    END
    Set Test Variable    ${RESPONSES}    ${responses}

All Responses Should Be Valid
    [Documentation]    Verifies all responses are valid
    FOR    ${response}    IN    @{RESPONSES}
        Should Be Equal As Strings    ${response.status_code}    200
        Response Should Contain Valid SQL
    END

Send Invalid Query Request
    [Documentation]    Sends an invalid query request
    ${data}=    Create Dictionary    query=INVALID###QUERY
    ${response}=    POST On Session    text2sql_api    /api/query    json=${data}
    Set Test Variable    ${RESPONSE}    ${response}

Send Request Without Authentication
    [Documentation]    Sends request without auth token
    Remove Headers
    ${response}=    POST On Session    text2sql_api    /api/query
    Set Test Variable    ${RESPONSE}    ${response}

Send Requests Above Rate Limit
    [Documentation]    Tests rate limiting
    FOR    ${i}    IN RANGE    100
        Send Query Request    Show me all employees
    END

Request Query History
    [Documentation]    Requests query history
    ${response}=    GET On Session    text2sql_api    /api/history
    Set Test Variable    ${RESPONSE}    ${response}

History Should Be In Correct Format
    [Documentation]    Verifies history format
    ${json}=    Set Variable    ${RESPONSE.json()}
    Should Be True    isinstance($json, list)
    Length Should Be    ${json}    greater than    0

Request Large Result Set
    [Documentation]    Requests a large result set
    ${data}=    Create Dictionary    query=Show all data    limit=1000
    ${response}=    POST On Session    text2sql_api    /api/query    json=${data}
    Set Test Variable    ${RESPONSE}    ${response}

Response Should Be Paginated
    [Documentation]    Verifies response pagination
    ${json}=    Set Variable    ${RESPONSE.json()}
    Should Contain    ${json}    next_page_token
    Should Contain    ${json}    total_count

Request Different Output Formats
    [Documentation]    Tests different output formats
    @{formats}=    Create List    json    csv    xml
    @{responses}=    Create List
    FOR    ${format}    IN    @{formats}
        ${response}=    GET On Session    text2sql_api    /api/query    params=format=${format}
        Append To List    ${responses}    ${response}
    END
    Set Test Variable    ${RESPONSES}    ${responses}

All Format Responses Should Be Valid
    [Documentation]    Verifies all format responses
    FOR    ${response}    IN    @{RESPONSES}
        Should Be Equal As Strings    ${response.status_code}    200
    END

Log API Response
    [Documentation]    Logs API response for debugging
    Run Keyword If Test Failed    Log    ${RESPONSE.text}
