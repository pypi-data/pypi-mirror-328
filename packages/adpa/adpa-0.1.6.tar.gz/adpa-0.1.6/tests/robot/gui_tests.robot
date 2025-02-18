*** Settings ***
Documentation    GUI Tests for ADPA with self-healing mechanisms
Resource    resources/gui_locators.resource
Library    SeleniumLibrary
Library    OperatingSystem
Library    String
Library    DateTime

Test Setup    Begin Web Test
Test Teardown    End Web Test

*** Variables ***
${TEST_DATA_DIR}    ${CURDIR}/test_data
${TEST_CSV_FILE}    ${TEST_DATA_DIR}/sample_dataset.csv

*** Test Cases ***
User Can Access Dashboard
    [Documentation]    Verify user can access the dashboard
    [Tags]    gui    smoke    dashboard
    Go To Dashboard
    Verify Dashboard Elements

User Can Upload Dataset
    [Documentation]    Verify user can upload a dataset
    [Tags]    gui    data    upload
    Go To Data Management
    Select Upload Dataset Tab
    Upload Test Dataset
    Verify Dataset Upload Success

User Can View Dataset
    [Documentation]    Verify user can view uploaded dataset
    [Tags]    gui    data    view
    Go To Data Management
    Select View Datasets Tab
    Select First Dataset
    Verify Dataset View Elements

User Can Perform Research
    [Documentation]    Verify research functionality
    [Tags]    gui    research
    Go To Research
    Perform Literature Search
    Verify Search Results

User Can Access Database Health
    [Documentation]    Verify database health monitoring
    [Tags]    gui    database    monitoring
    Go To Database
    Verify Database Health Elements
    Check Database Metrics

*** Keywords ***
Begin Web Test
    Create Webdriver    Chrome    options=add_argument("--headless")
    Set Window Size    1920    1080
    Set Selenium Timeout    ${TIMEOUT}
    Go To    ${BASE_URL}

End Web Test
    Close All Browsers

Go To Dashboard
    ${dashboard_btn_locators}=    Get Dynamic Button Locator    Dashboard
    Wait For And Click Element    css:[data-testid="dashboard-nav"]    ${dashboard_btn_locators}
    Wait Until Page Contains    Dashboard    timeout=${TIMEOUT}

Verify Dashboard Elements
    Element Should Be Visible With Healing    
    ...    css:[data-testid="dashboard-metrics"]
    ...    xpath://div[contains(@class, "stMetric")]

Go To Data Management
    ${data_btn_locators}=    Get Dynamic Button Locator    Data Management
    Wait For And Click Element    css:[data-testid="data-nav"]    ${data_btn_locators}
    Wait Until Page Contains    Data Management    timeout=${TIMEOUT}

Select Upload Dataset Tab
    ${upload_tab_locators}=    Get Dynamic Tab Locator    Upload Dataset
    Wait For And Click Element    css:[data-testid="upload-dataset-tab"]    ${upload_tab_locators}

Upload Test Dataset
    Create Test Dataset If Not Exists
    Choose File    css:[data-testid="file-uploader"]    ${TEST_CSV_FILE}
    ${name_input_locators}=    Get Dynamic Input Locator    Dataset Name
    Wait For And Input Text    css:[data-testid="dataset-name"]    ${name_input_locators}    Test Dataset
    ${desc_input_locators}=    Get Dynamic Input Locator    Description
    Wait For And Input Text    css:[data-testid="dataset-desc"]    ${desc_input_locators}    Test dataset for automation
    ${process_btn_locators}=    Get Dynamic Button Locator    Process Dataset
    Wait For And Click Element    css:[data-testid="process-dataset"]    ${process_btn_locators}

Verify Dataset Upload Success
    Wait Until Page Contains    Dataset processed successfully!    timeout=${TIMEOUT}
    Element Should Be Visible With Healing    
    ...    css:[data-testid="data-preview"]
    ...    xpath://div[contains(@class, "stDataFrame")]

Select View Datasets Tab
    ${view_tab_locators}=    Get Dynamic Tab Locator    View Datasets
    Wait For And Click Element    css:[data-testid="view-datasets-tab"]    ${view_tab_locators}

Select First Dataset
    ${dataset_select_locators}=    Create List
    ...    css:[data-testid="dataset-select"]
    ...    xpath://div[contains(@class, "stSelectbox")]//select
    Wait For And Click Element    css:[data-testid="dataset-select"]    ${dataset_select_locators}
    Press Keys    None    ARROW_DOWN
    Press Keys    None    ENTER

Verify Dataset View Elements
    Element Should Be Visible With Healing    
    ...    css:[data-testid="data-explorer"]
    ...    xpath://div[contains(@class, "stDataFrame")]
    Element Should Be Visible With Healing    
    ...    css:[data-testid="visualization-section"]
    ...    xpath://div[contains(@class, "stPlotlyChart")]

Go To Research
    ${research_btn_locators}=    Get Dynamic Button Locator    Research
    Wait For And Click Element    css:[data-testid="research-nav"]    ${research_btn_locators}
    Wait Until Page Contains    Research    timeout=${TIMEOUT}

Perform Literature Search
    ${search_input_locators}=    Get Dynamic Input Locator    Search Query
    Wait For And Input Text    css:[data-testid="search-query"]    ${search_input_locators}    machine learning
    ${search_btn_locators}=    Get Dynamic Button Locator    Search Literature
    Wait For And Click Element    css:[data-testid="search-btn"]    ${search_btn_locators}

Verify Search Results
    Wait Until Page Contains Element    css:[data-testid="search-results"]    timeout=${TIMEOUT}
    Page Should Contain    Advanced Data Processing in Research

Go To Database
    ${database_btn_locators}=    Get Dynamic Button Locator    Database
    Wait For And Click Element    css:[data-testid="database-nav"]    ${database_btn_locators}
    Wait Until Page Contains    Database Health    timeout=${TIMEOUT}

Verify Database Health Elements
    Element Should Be Visible With Healing    
    ...    css:[data-testid="health-status"]
    ...    xpath://div[contains(@class, "stMetric")]//label[contains(text(), "Health Status")]
    Element Should Be Visible With Healing    
    ...    css:[data-testid="performance-metrics"]
    ...    xpath://div[contains(@class, "stPlotlyChart")]

Check Database Metrics
    Element Should Be Visible With Healing    
    ...    css:[data-testid="connection-pool"]
    ...    xpath://div[contains(@class, "stMetric")]//label[contains(text(), "Connection Pool")]
    Element Should Be Visible With Healing    
    ...    css:[data-testid="query-performance"]
    ...    xpath://div[contains(@class, "stMetric")]//label[contains(text(), "Query Performance")]

Create Test Dataset If Not Exists
    Create Directory    ${TEST_DATA_DIR}
    ${file_exists}=    Run Keyword And Return Status    File Should Exist    ${TEST_CSV_FILE}
    IF    not ${file_exists}
        Create Test CSV File
    END

Create Test CSV File
    ${content}=    Catenate    SEPARATOR=\n
    ...    id,name,value,timestamp
    ...    1,Test A,10.5,2025-01-01
    ...    2,Test B,15.2,2025-01-02
    ...    3,Test C,8.7,2025-01-03
    Create File    ${TEST_CSV_FILE}    ${content}
