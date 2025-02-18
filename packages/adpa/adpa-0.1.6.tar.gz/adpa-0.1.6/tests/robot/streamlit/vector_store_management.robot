*** Settings ***
Documentation     Test suite for Vector Store Management page
Resource          ${CURDIR}/resources/streamlit_common.robot
Library           SeleniumLibrary
Suite Setup       Start Vector Store Tests
Suite Teardown    Stop Vector Store Tests
Test Setup       Navigate To Management Page
Test Teardown    Take Screenshot On Failure    vector_store

*** Variables ***
${MANAGEMENT_URL}    http://localhost:8501/vector_store_management
${TEST_FILE}        ${CURDIR}/test_data/sample.pdf
${CONFIG_FILE}      ${CURDIR}/test_data/config.json

*** Keywords ***
Start Vector Store Tests
    Start Streamlit Server    ${CURDIR}/../../../adpa/ui/pages/vector_store_management.py
    Open Browser    ${MANAGEMENT_URL}    ${BROWSER}
    Set Window Size    1920    1080

Stop Vector Store Tests
    Close All Browsers
    Stop Streamlit Server

Navigate To Management Page
    Go To    ${MANAGEMENT_URL}
    Verify Streamlit Page Loaded    Vector Store Management
    Wait For Streamlit Spinner

Upload Test Document
    [Arguments]    ${file_path}=${TEST_FILE}
    Choose File    css:input[type="file"]    ${file_path}
    Wait For Streamlit Spinner
    Verify No Streamlit Errors

Configure Vector Store
    [Arguments]    ${store_type}    ${embedding_type}
    Select Streamlit Option    xpath://div[contains(text(), 'Store Type')]    ${store_type}
    Select Streamlit Option    xpath://div[contains(text(), 'Embedding Type')]    ${embedding_type}
    Click Streamlit Element    xpath://button[contains(text(), 'Apply Configuration')]
    Wait For Streamlit Spinner

Verify Store Status
    [Arguments]    ${expected_status}
    ${status_text}=    Get Text    css:div[data-testid="stText"]
    Should Contain    ${status_text}    ${expected_status}

*** Test Cases ***
Upload And Configure Store
    [Documentation]    Test document upload and store configuration
    [Tags]    smoke    management
    Upload Test Document
    Configure Vector Store    ChromaDB    OpenAI
    Verify Store Status    Ready

Import Configuration Test
    [Documentation]    Test configuration import functionality
    [Tags]    configuration    management
    Choose File    css:input[type="file"]    ${CONFIG_FILE}
    Wait For Streamlit Spinner
    Verify Store Status    Configuration imported

Query Test
    [Documentation]    Test vector store querying
    [Tags]    query    management
    Upload Test Document
    Configure Vector Store    ChromaDB    OpenAI
    Input Streamlit Text    css:textarea    "test query"
    Click Streamlit Element    xpath://button[contains(text(), 'Search')]
    Wait For Streamlit Spinner
    Page Should Contain Element    css:div[data-testid="stTable"]

Performance Metrics Test
    [Documentation]    Test performance metrics display
    [Tags]    metrics    management
    Upload Test Document
    Configure Vector Store    ChromaDB    OpenAI
    Click Streamlit Element    xpath://button[contains(text(), 'View Metrics')]
    Wait For Streamlit Spinner
    Page Should Contain Element    css:div[data-testid="stVegaLiteChart"]
