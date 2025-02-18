*** Settings ***
Documentation     Test suite for RAG Agent Interface
Resource          resources/common.robot
Library           SeleniumLibrary
Library           OperatingSystem

Suite Setup       Open Browser To RAG Interface
Suite Teardown    Close All Browsers

*** Variables ***
${SERVER}         localhost
${PORT}           8501
${BROWSER}        chrome
${URL}            http://${SERVER}:${PORT}
${TEST_FILE}      ${CURDIR}${/}test_data${/}sample.txt
${DELAY}          0.5

*** Test Cases ***
Initialize RAG System
    [Documentation]    Test system initialization with vector store and agent
    Select Vector Store    chroma
    Select Embedding Type    openai
    Select Agent    DefaultAgent
    Click Initialize
    Wait Until System Initialized

Upload And Process Document
    [Documentation]    Test document upload and processing
    Upload Test Document    ${TEST_FILE}
    Click Process Documents
    Verify Document Processed

Query Document
    [Documentation]    Test querying processed documents
    Input Query    What is the main topic?
    Click Search Button
    Verify Response Displayed
    Verify Sources Displayed

Test Different Vector Stores
    [Documentation]    Test different vector store configurations
    [Template]    Test Vector Store Configuration
    chroma
    faiss
    milvus

*** Keywords ***
Open Browser To RAG Interface
    Open Browser    ${URL}    ${BROWSER}
    Set Selenium Speed    ${DELAY}
    RAG Interface Should Be Open

RAG Interface Should Be Open
    Title Should Be    RAG Agent Interface
    Page Should Contain    Configuration

Select Vector Store
    [Arguments]    ${store_type}
    Select From List By Value    xpath://select[@key='store_type']    ${store_type}

Select Embedding Type
    [Arguments]    ${embedding_type}
    Select From List By Value    xpath://select[@key='embedding_type']    ${embedding_type}

Select Agent
    [Arguments]    ${agent_name}
    Select From List By Value    xpath://select[@key='agent']    ${agent_name}

Click Initialize
    Click Button    Initialize System

Wait Until System Initialized
    Wait Until Page Contains    System initialized!    timeout=10s

Upload Test Document
    [Arguments]    ${file_path}
    Choose File    xpath://input[@type='file']    ${file_path}

Click Process Documents
    Click Button    Process Documents

Verify Document Processed
    Wait Until Page Contains    Documents processed successfully!    timeout=30s

Input Query
    [Arguments]    ${query_text}
    Input Text    xpath://textarea    ${query_text}

Click Search Button
    Click Button    Search

Verify Response Displayed
    Wait Until Page Contains Element    xpath://h3[text()='Response']
    Page Should Contain Element    xpath://div[contains(@class, 'stMarkdown')]

Verify Sources Displayed
    Wait Until Page Contains Element    xpath://h3[text()='Relevant Sources']
    Page Should Contain Element    xpath://div[contains(@class, 'streamlit-expanderContent')]

Test Vector Store Configuration
    [Arguments]    ${store_type}
    Select Vector Store    ${store_type}
    Click Initialize
    Wait Until System Initialized
    Upload And Process Document
    Query Document
