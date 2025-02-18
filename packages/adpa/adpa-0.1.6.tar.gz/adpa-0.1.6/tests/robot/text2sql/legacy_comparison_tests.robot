*** Settings ***
Documentation     Test suite comparing hybrid architecture with legacy_v1
Resource          resources/text2sql_keywords.robot
Suite Setup       Initialize Comparison Environment
Suite Teardown    Clean Up Comparison Environment
Test Setup       Reset Test State
Test Teardown    Record Comparison Metrics
Force Tags       text2sql    comparison    regression

*** Variables ***
${LEGACY_MODULE}    adpa.text2sql.legacy_v1
${HYBRID_MODULE}    adpa.text2sql.hybrid
@{TEST_QUERIES}    show all users    find orders from last week    count products by category

*** Test Cases ***
Test Should Compare Performance Between Versions
    [Documentation]    Compares query processing performance
    [Tags]    performance    critical    stable
    Given Test Queries Are Prepared
    When Queries Are Executed On Both Versions
    Then Hybrid Version Should Be Faster
    And Memory Usage Should Be Lower
    And CPU Usage Should Be More Efficient

Test Should Compare Accuracy Between Versions
    [Documentation]    Compares query conversion accuracy
    [Tags]    accuracy    critical    stable
    Given Complex Test Queries Are Prepared
    When Queries Are Executed On Both Versions
    Then Hybrid Version Should Be More Accurate
    And Error Rate Should Be Lower
    And Edge Cases Should Be Handled Better

Test Should Compare Security Features Between Versions
    [Documentation]    Compares security capabilities
    [Tags]    security    high    stable
    Given Security Test Cases Are Prepared
    When Security Tests Are Executed On Both Versions
    Then Hybrid Version Should Detect More Threats
    And False Positives Should Be Lower
    And Protection Should Be More Comprehensive

Test Should Compare Schema Adaptation Between Versions
    [Documentation]    Compares schema handling capabilities
    [Tags]    schema    medium    stable
    Given Schema Changes Are Prepared
    When Schema Tests Are Executed On Both Versions
    Then Hybrid Version Should Adapt Better
    And Schema Learning Should Be More Accurate
    And Context Updates Should Be Faster

Test Should Compare Error Handling Between Versions
    [Documentation]    Compares error handling capabilities
    [Tags]    errors    medium    stable
    Given Error Test Cases Are Prepared
    When Error Tests Are Executed On Both Versions
    Then Hybrid Version Should Handle Errors Better
    And Error Messages Should Be More Descriptive
    And Recovery Should Be More Robust

*** Keywords ***
Initialize Comparison Environment
    [Documentation]    Sets up environment for version comparison
    Initialize Test Database
    Load Sample Data
    Initialize Both Versions

Initialize Both Versions
    [Documentation]    Initializes both legacy and hybrid versions
    ${legacy_config}=    Create Legacy Config
    ${hybrid_config}=    Create Hybrid Config
    Initialize Legacy Engine    ${legacy_config}
    Initialize Hybrid Engine    ${hybrid_config}

Test Queries Are Prepared
    [Documentation]    Prepares test queries for comparison
    @{queries}=    Create List    ${TEST_QUERIES}
    Set Test Variable    ${COMPARISON_QUERIES}    ${queries}

Complex Test Queries Are Prepared
    [Documentation]    Prepares complex test queries
    @{queries}=    Load Complex Queries
    Set Test Variable    ${COMPARISON_QUERIES}    ${queries}

Queries Are Executed On Both Versions
    [Documentation]    Executes queries on both versions
    ${legacy_results}=    Execute Legacy Queries    ${COMPARISON_QUERIES}
    ${hybrid_results}=    Execute Hybrid Queries    ${COMPARISON_QUERIES}
    Set Test Variable    ${LEGACY_RESULTS}    ${legacy_results}
    Set Test Variable    ${HYBRID_RESULTS}    ${hybrid_results}

Hybrid Version Should Be Faster
    [Documentation]    Verifies hybrid version performance
    ${legacy_time}=    Get Average Processing Time    ${LEGACY_RESULTS}
    ${hybrid_time}=    Get Average Processing Time    ${HYBRID_RESULTS}
    Should Be True    ${hybrid_time} < ${legacy_time}

Memory Usage Should Be Lower
    [Documentation]    Verifies memory efficiency
    ${legacy_memory}=    Get Average Memory Usage    ${LEGACY_RESULTS}
    ${hybrid_memory}=    Get Average Memory Usage    ${HYBRID_RESULTS}
    Should Be True    ${hybrid_memory} < ${legacy_memory}

CPU Usage Should Be More Efficient
    [Documentation]    Verifies CPU efficiency
    ${legacy_cpu}=    Get Average CPU Usage    ${LEGACY_RESULTS}
    ${hybrid_cpu}=    Get Average CPU Usage    ${HYBRID_RESULTS}
    Should Be True    ${hybrid_cpu} < ${legacy_cpu}

Security Test Cases Are Prepared
    [Documentation]    Prepares security test cases
    @{cases}=    Load Security Test Cases
    Set Test Variable    ${SECURITY_CASES}    ${cases}

Security Tests Are Executed On Both Versions
    [Documentation]    Executes security tests
    ${legacy_security}=    Test Legacy Security    ${SECURITY_CASES}
    ${hybrid_security}=    Test Hybrid Security    ${SECURITY_CASES}
    Set Test Variable    ${LEGACY_SECURITY}    ${legacy_security}
    Set Test Variable    ${HYBRID_SECURITY}    ${hybrid_security}

Hybrid Version Should Detect More Threats
    [Documentation]    Verifies threat detection
    ${legacy_threats}=    Count Detected Threats    ${LEGACY_SECURITY}
    ${hybrid_threats}=    Count Detected Threats    ${HYBRID_SECURITY}
    Should Be True    ${hybrid_threats} > ${legacy_threats}

Schema Changes Are Prepared
    [Documentation]    Prepares schema change tests
    @{changes}=    Load Schema Changes
    Set Test Variable    ${SCHEMA_CHANGES}    ${changes}

Schema Tests Are Executed On Both Versions
    [Documentation]    Executes schema adaptation tests
    ${legacy_schema}=    Test Legacy Schema    ${SCHEMA_CHANGES}
    ${hybrid_schema}=    Test Hybrid Schema    ${SCHEMA_CHANGES}
    Set Test Variable    ${LEGACY_SCHEMA}    ${legacy_schema}
    Set Test Variable    ${HYBRID_SCHEMA}    ${hybrid_schema}

Hybrid Version Should Adapt Better
    [Documentation]    Verifies schema adaptation
    ${legacy_adapt}=    Get Adaptation Score    ${LEGACY_SCHEMA}
    ${hybrid_adapt}=    Get Adaptation Score    ${HYBRID_SCHEMA}
    Should Be True    ${hybrid_adapt} > ${legacy_adapt}

Error Test Cases Are Prepared
    [Documentation]    Prepares error test cases
    @{cases}=    Load Error Test Cases
    Set Test Variable    ${ERROR_CASES}    ${cases}

Error Tests Are Executed On Both Versions
    [Documentation]    Executes error handling tests
    ${legacy_errors}=    Test Legacy Errors    ${ERROR_CASES}
    ${hybrid_errors}=    Test Hybrid Errors    ${ERROR_CASES}
    Set Test Variable    ${LEGACY_ERRORS}    ${legacy_errors}
    Set Test Variable    ${HYBRID_ERRORS}    ${hybrid_errors}

Hybrid Version Should Handle Errors Better
    [Documentation]    Verifies error handling
    ${legacy_score}=    Get Error Handling Score    ${LEGACY_ERRORS}
    ${hybrid_score}=    Get Error Handling Score    ${HYBRID_ERRORS}
    Should Be True    ${hybrid_score} > ${legacy_score}

Record Comparison Metrics
    [Documentation]    Records comparison metrics
    ${metrics}=    Create Comparison Report
    Log    ${metrics}    console=True
    Append To File    ${METRICS_FILE}    ${metrics}
