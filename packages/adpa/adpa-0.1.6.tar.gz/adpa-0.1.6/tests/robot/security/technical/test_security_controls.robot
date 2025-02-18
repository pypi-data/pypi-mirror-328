*** Settings ***
Documentation     Technical security tests for system controls
Resource          ../../resources/security.resource
Resource          ../../resources/api.resource
Library           RequestsLibrary
Library           SSHLibrary
Library           DatabaseLibrary
Library           Process

*** Variables ***
${AUTH_ENDPOINT}      ${API_BASE_URL}/auth
${SECURE_ENDPOINT}    ${API_BASE_URL}/secure
${TEST_USER}         test_user
${TEST_PASSWORD}     test_pass
${JWT_TOKEN}         ${EMPTY}

*** Test Cases ***
Test Authentication Mechanism
    [Documentation]    Test authentication system security
    [Tags]    security    auth    critical
    ${weak_passwords}=    Create List    password    123456    admin    root
    FOR    ${password}    IN    @{weak_passwords}
        ${response}=    Attempt Login    ${TEST_USER}    ${password}
        Should Be Equal As Integers    ${response.status_code}    401
    END
    ${response}=    Attempt Login    ${TEST_USER}    ${TEST_PASSWORD}
    Should Be Equal As Integers    ${response.status_code}    200
    Should Have Valid JWT    ${response.json()['token']}

Test Authorization Controls
    [Documentation]    Test role-based access control
    [Tags]    security    authorization    critical
    ${token}=    Get Valid Token
    @{endpoints}=    Create List    /admin    /users    /data
    FOR    ${endpoint}    IN    @{endpoints}
        ${response}=    Access Endpoint    ${endpoint}    ${token}
        Verify Authorization    ${response}    ${endpoint}
    END

Test SQL Injection Prevention
    [Documentation]    Test SQL injection vulnerabilities
    [Tags]    security    injection    critical
    @{injection_attempts}=    Create List
    ...    "' OR '1'='1"
    ...    "; DROP TABLE users; --"
    ...    "' UNION SELECT * FROM sensitive_data; --"
    FOR    ${attempt}    IN    @{injection_attempts}
        ${response}=    Attempt SQL Injection    ${attempt}
        Should Be Equal As Integers    ${response.status_code}    400
        Should Not Contain    ${response.text}    error
    END

Test XSS Prevention
    [Documentation]    Test Cross-Site Scripting prevention
    [Tags]    security    xss    critical
    @{xss_payloads}=    Create List
    ...    <script>alert('xss')</script>
    ...    javascript:alert('xss')
    ...    <img src="x" onerror="alert('xss')">
    FOR    ${payload}    IN    @{xss_payloads}
        ${response}=    Submit Content    ${payload}
        Should Not Contain    ${response.text}    ${payload}
        Should Be Escaped    ${response.text}
    END

Test CSRF Protection
    [Documentation]    Test Cross-Site Request Forgery protection
    [Tags]    security    csrf    critical
    ${token}=    Get Valid Token
    ${response}=    Send Request Without CSRF
    Should Be Equal As Integers    ${response.status_code}    403
    ${response}=    Send Request With CSRF    ${token}
    Should Be Equal As Integers    ${response.status_code}    200

Test File Upload Security
    [Documentation]    Test secure file upload handling
    [Tags]    security    upload    critical
    @{malicious_files}=    Create List
    ...    test.js    test.php    test.exe
    FOR    ${file}    IN    @{malicious_files}
        ${response}=    Upload File    ${file}
        Should Be Equal As Integers    ${response.status_code}    400
    END
    ${response}=    Upload Safe File    test.txt
    Should Be Equal As Integers    ${response.status_code}    200

Test API Rate Limiting
    [Documentation]    Test API rate limiting protection
    [Tags]    security    rate-limit
    ${token}=    Get Valid Token
    FOR    ${i}    IN RANGE    100
        ${response}=    Quick Request    ${token}
        Run Keyword If    ${response.status_code} == 429    Exit For Loop
    END
    Should Be Equal As Integers    ${response.status_code}    429

Test Session Management
    [Documentation]    Test session security features
    [Tags]    security    session    critical
    ${session}=    Create Session
    Verify Session Properties    ${session}
    ${response}=    Logout
    Verify Session Terminated    ${session}
    ${response}=    Use Old Session    ${session}
    Should Be Equal As Integers    ${response.status_code}    401

Test Data Encryption
    [Documentation]    Test data encryption in transit and at rest
    [Tags]    security    encryption    critical
    ${sensitive_data}=    Create Sensitive Data
    ${stored_data}=    Store Sensitive Data    ${sensitive_data}
    Should Be Encrypted    ${stored_data}
    ${transmitted_data}=    Transmit Sensitive Data    ${sensitive_data}
    Should Use TLS    ${transmitted_data}

Test Security Headers
    [Documentation]    Test security-related HTTP headers
    [Tags]    security    headers
    ${response}=    Get Secure Page
    Verify Security Headers    ${response.headers}

*** Keywords ***
Should Have Valid JWT
    [Arguments]    ${token}
    ${parts}=    Split String    ${token}    .
    Length Should Be    ${parts}    3
    Should Not Be Empty    ${parts}[1]

Verify Authorization
    [Arguments]    ${response}    ${endpoint}
    ${expected_status}=    Get Expected Status    ${endpoint}
    Should Be Equal As Integers    ${response.status_code}    ${expected_status}

Should Be Escaped
    [Arguments]    ${content}
    Should Not Contain    ${content}    <script>
    Should Not Contain    ${content}    javascript:
    Should Not Contain    ${content}    onerror=

Verify Security Headers
    [Arguments]    ${headers}
    Dictionary Should Contain Key    ${headers}    Strict-Transport-Security
    Dictionary Should Contain Key    ${headers}    X-Content-Type-Options
    Dictionary Should Contain Key    ${headers}    X-Frame-Options
    Dictionary Should Contain Key    ${headers}    Content-Security-Policy
