*** Settings ***
Documentation    Research Component GUI Tests with self-healing mechanisms
Resource    ../resources/gui_locators.resource
Resource    ../resources/common.resource

Test Setup    Begin Web Test
Test Teardown    End Web Test

*** Test Cases ***
User Can Perform Basic Literature Search
    [Documentation]    Verify basic literature search functionality
    [Tags]    gui    research    search    basic
    Go To Research
    Select Literature Review Tab
    Perform Basic Search
    Verify Search Results
    Verify Result Sorting

User Can Apply Advanced Search Filters
    [Documentation]    Verify advanced search functionality
    [Tags]    gui    research    search    advanced
    Go To Research
    Select Literature Review Tab
    Open Advanced Search
    Apply Date Range Filter
    Apply Author Filter
    Apply Journal Filter
    Verify Filtered Results
    Clear All Filters
    Verify Original Results

User Can Save Search Results
    [Documentation]    Verify saving search results
    [Tags]    gui    research    save
    Go To Research
    Select Literature Review Tab
    Perform Basic Search
    Save Search Results
    Verify Results Saved
    Access Saved Results
    Verify Saved Results Match

User Can Analyze Dataset
    [Documentation]    Verify dataset analysis functionality
    [Tags]    gui    research    analysis
    Go To Research
    Select Data Analysis Tab
    Upload Analysis Dataset
    Verify Dataset Loaded
    Perform Basic Analysis
    Verify Analysis Results
    Perform Advanced Analysis
    Verify Advanced Results

User Can Generate Research Report
    [Documentation]    Verify report generation
    [Tags]    gui    research    report
    Go To Research
    Select Research Report Tab
    Input Report Details
    Add Methods Section
    Add Results Section
    Add Conclusions
    Generate Report
    Verify Report Content
    Export Report
    Verify Report Export

User Can Collaborate On Research
    [Documentation]    Verify research collaboration features
    [Tags]    gui    research    collaboration
    Go To Research
    Share Research Project
    Verify Sharing Settings
    Add Collaborator
    Verify Collaborator Access
    Remove Collaborator
    Verify Access Removed

Research Component Should Handle Large Datasets
    [Documentation]    Verify handling of large datasets
    [Tags]    gui    research    performance
    Go To Research
    Select Data Analysis Tab
    Upload Large Dataset
    Verify Loading Indicator
    Verify Progressive Loading
    Perform Analysis On Large Dataset
    Verify Performance Metrics

Research Component Should Work Offline
    [Documentation]    Verify offline functionality
    [Tags]    gui    research    offline
    Go To Research
    Enable Offline Mode
    Verify Offline Indicator
    Access Cached Data
    Perform Offline Analysis
    Verify Offline Results
    Disable Offline Mode
    Verify Online Status

*** Keywords ***
Select Literature Review Tab
    ${lit_review_tab_locators}=    Get Dynamic Tab Locator    Literature Review
    Wait For And Click Element    css:[data-testid="lit-review-tab"]    ${lit_review_tab_locators}

Perform Basic Search
    ${search_input_locators}=    Get Dynamic Input Locator    Search Query
    Wait For And Input Text    css:[data-testid="search-query"]    ${search_input_locators}    machine learning
    ${search_btn_locators}=    Get Dynamic Button Locator    Search Literature
    Wait For And Click Element    css:[data-testid="search-btn"]    ${search_btn_locators}

Open Advanced Search
    ${advanced_btn_locators}=    Get Dynamic Button Locator    Advanced Search
    Wait For And Click Element    css:[data-testid="advanced-search"]    ${advanced_btn_locators}

Apply Date Range Filter
    ${date_start_locators}=    Get Dynamic Input Locator    Start Date
    ${date_end_locators}=    Get Dynamic Input Locator    End Date
    Wait For And Input Text    css:[data-testid="date-start"]    ${date_start_locators}    2020-01-01
    Wait For And Input Text    css:[data-testid="date-end"]    ${date_end_locators}    2025-01-01

Upload Analysis Dataset
    ${file_path}=    Create Analysis Dataset
    Choose File    css:[data-testid="analysis-uploader"]    ${file_path}

Perform Basic Analysis
    ${analyze_btn_locators}=    Get Dynamic Button Locator    Analyze Dataset
    Wait For And Click Element    css:[data-testid="analyze-btn"]    ${analyze_btn_locators}

Input Report Details
    ${title_input_locators}=    Get Dynamic Input Locator    Report Title
    ${author_input_locators}=    Get Dynamic Input Locator    Authors
    Wait For And Input Text    css:[data-testid="report-title"]    ${title_input_locators}    Test Research Report
    Wait For And Input Text    css:[data-testid="report-authors"]    ${author_input_locators}    John Doe, Jane Smith

Create Analysis Dataset
    ${file_path}=    Set Variable    ${TEST_DATA_DIR}/analysis_data.csv
    ${content}=    Catenate    SEPARATOR=\n
    ...    id,feature1,feature2,target,timestamp
    ...    1,0.5,0.7,1,2025-01-01
    ...    2,0.3,0.2,0,2025-01-02
    ...    3,0.8,0.9,1,2025-01-03
    ...    4,0.1,0.3,0,2025-01-04
    ...    5,0.7,0.6,1,2025-01-05
    Create File    ${file_path}    ${content}
    RETURN    ${file_path}

Enable Offline Mode
    Execute Javascript    window.localStorage.setItem('offlineMode', 'true')
    Reload Page

Verify Offline Indicator
    Element Should Be Visible With Healing    
    ...    css:[data-testid="offline-indicator"]
    ...    xpath://div[contains(@class, "offline-badge")]

Access Cached Data
    ${cached_data_btn_locators}=    Get Dynamic Button Locator    Cached Data
    Wait For And Click Element    css:[data-testid="cached-data"]    ${cached_data_btn_locators}

Verify Performance Metrics
    Element Should Be Visible With Healing    
    ...    css:[data-testid="performance-metrics"]
    ...    xpath://div[contains(@class, "performance-stats")]
    ${load_time}=    Get Element Attribute    css:[data-testid="load-time"]    data-value
    Should Be True    ${load_time} < 5000    Loading time should be less than 5 seconds
