*** Settings ***
Documentation     Test suite for Store Advisor Streamlit page with self-healing capabilities
Library           SeleniumLibrary
Library           ${CURDIR}/resources/StoreAdvisorLibrary.py
Suite Setup       Start Streamlit
Suite Teardown    Close All Browsers
Test Setup       Navigate To Store Advisor
Test Teardown    Export Locators

*** Variables ***
${BROWSER}               chrome
${STREAMLIT_URL}        http://localhost:8501
${LEARNED_LOCATORS}     ${CURDIR}/learned_locators.json

*** Keywords ***
Start Streamlit
    [Documentation]    Start Streamlit server and open browser
    ${streamlit}=    Start Process    streamlit    run    ${CURDIR}/../../../adpa/ui/pages/store_advisor.py
    Sleep    5s    # Wait for server to start
    Open Browser    ${STREAMLIT_URL}    ${BROWSER}
    Set Window Size    1920    1080
    Import Learned Locators    ${LEARNED_LOCATORS}

Navigate To Store Advisor
    [Documentation]    Navigate to Store Advisor page and wait for load
    Go To    ${STREAMLIT_URL}
    Wait Until Element Is Visible    xpath://h1[contains(text(), 'RAG/Vector Store Advisor')]
    Sleep    2s    # Wait for animations

Export Locators
    [Documentation]    Export successful locators for learning
    Export Successful Locators    ${LEARNED_LOCATORS}

Select Use Case Parameters
    [Arguments]    ${data_size}    ${update_freq}    ${query_latency}    ${deployment}    ${budget}
    Select Data Size    ${data_size}
    Select Update Frequency    ${update_freq}
    # Add more parameter selections as needed

Verify Recommendation Quality
    [Arguments]    ${min_confidence}=0.6
    ${recommendations_visible}=    Verify Recommendations Displayed
    Should Be True    ${recommendations_visible}
    # Add more quality checks as needed

*** Test Cases ***
Small Project Recommendation Test
    [Documentation]    Test recommendations for small project scenario
    [Tags]    smoke    recommendations
    Select Use Case Parameters
    ...    Small (<100K docs)
    ...    Static (rarely updated)
    ...    Low (<100ms)
    ...    Self-hosted
    ...    Low (<$100/month)
    Get Recommendations
    Verify Recommendation Quality    0.7

Enterprise Deployment Test
    [Documentation]    Test recommendations for enterprise deployment
    [Tags]    enterprise    recommendations
    Select Use Case Parameters
    ...    Large (1M-10M docs)
    ...    Hourly updates
    ...    Very Low (<50ms)
    ...    Cloud-based
    ...    Enterprise (>$2000/month)
    Get Recommendations
    Verify Recommendation Quality    0.8

Real-time Search Test
    [Documentation]    Test recommendations for real-time search requirements
    [Tags]    realtime    recommendations
    Select Use Case Parameters
    ...    Medium (100K-1M docs)
    ...    Real-time updates
    ...    Very Low (<50ms)
    ...    Hybrid
    ...    High ($500-$2000/month)
    Get Recommendations
    Verify Recommendation Quality    0.7

Hybrid Search Requirements Test
    [Documentation]    Test recommendations for hybrid search needs
    [Tags]    hybrid    recommendations
    Select Use Case Parameters
    ...    Medium (100K-1M docs)
    ...    Daily updates
    ...    Low (<100ms)
    ...    Cloud-based
    ...    Medium ($100-$500/month)
    Get Recommendations
    Verify Recommendation Quality    0.7
