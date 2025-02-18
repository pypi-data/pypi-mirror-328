*** Settings ***
Documentation    Data Management GUI Tests with self-healing mechanisms
Resource    ../resources/gui_locators.resource
Resource    ../resources/common.resource

Test Setup    Begin Web Test
Test Teardown    End Web Test

*** Test Cases ***
User Can Upload Single Dataset
    [Documentation]    Verify single dataset upload functionality
    [Tags]    gui    data    upload    single
    Go To Data Management
    Select Upload Dataset Tab
    Upload Single Dataset
    Verify Dataset Preview
    Verify Basic Statistics
    Verify Upload Success Message

User Can Upload Multiple Datasets
    [Documentation]    Verify multiple dataset upload functionality
    [Tags]    gui    data    upload    multiple
    Go To Data Management
    Select Upload Dataset Tab
    Upload Multiple Datasets
    Verify All Datasets Uploaded
    Verify Dataset List Updated

User Can View Dataset Details
    [Documentation]    Verify dataset details view
    [Tags]    gui    data    view    details
    Go To Data Management
    Select View Datasets Tab
    Select First Dataset
    Verify Dataset Details
    Verify Column Information
    Verify Data Statistics

User Can Filter Dataset
    [Documentation]    Verify dataset filtering
    [Tags]    gui    data    view    filter
    Go To Data Management
    Select View Datasets Tab
    Select First Dataset
    Apply Column Filter
    Verify Filtered Results
    Clear Filter
    Verify Original Data

User Can Sort Dataset
    [Documentation]    Verify dataset sorting
    [Tags]    gui    data    view    sort
    Go To Data Management
    Select View Datasets Tab
    Select First Dataset
    Sort By Column
    Verify Sort Order
    Reverse Sort Order
    Verify Reversed Order

User Can Export Dataset
    [Documentation]    Verify dataset export functionality
    [Tags]    gui    data    export
    Go To Data Management
    Select View Datasets Tab
    Select First Dataset
    Export As CSV
    Verify CSV Export
    Export As Excel
    Verify Excel Export
    Export As JSON
    Verify JSON Export

User Can Visualize Dataset
    [Documentation]    Verify dataset visualization
    [Tags]    gui    data    visualize
    Go To Data Management
    Select View Datasets Tab
    Select First Dataset
    Create Histogram
    Verify Histogram
    Create Scatter Plot
    Verify Scatter Plot
    Create Box Plot
    Verify Box Plot

User Can Edit Dataset Metadata
    [Documentation]    Verify dataset metadata editing
    [Tags]    gui    data    metadata
    Go To Data Management
    Select View Datasets Tab
    Select First Dataset
    Edit Dataset Name
    Edit Dataset Description
    Verify Metadata Updates

User Can Delete Dataset
    [Documentation]    Verify dataset deletion
    [Tags]    gui    data    delete
    Go To Data Management
    Select View Datasets Tab
    Select First Dataset
    Delete Dataset
    Verify Deletion Confirmation
    Confirm Deletion
    Verify Dataset Removed

Data Management Should Handle Errors
    [Documentation]    Verify error handling
    [Tags]    gui    data    errors
    Go To Data Management
    Select Upload Dataset Tab
    Upload Invalid File
    Verify Error Message
    Upload Empty File
    Verify Empty File Error
    Upload Large File
    Verify Size Limit Error

*** Keywords ***
Upload Single Dataset
    ${file_path}=    Create Test CSV File    single_test
    Choose File    css:[data-testid="file-uploader"]    ${file_path}
    Input Dataset Information    Single Test    Test dataset for single upload
    Click Process Dataset

Upload Multiple Datasets
    @{datasets}=    Create List    test1    test2    test3
    FOR    ${dataset}    IN    @{datasets}
        ${file_path}=    Create Test CSV File    ${dataset}
        Choose File    css:[data-testid="file-uploader"]    ${file_path}
        Input Dataset Information    ${dataset}    Test dataset ${dataset}
        Click Process Dataset
        Wait Until Success Message Disappears
    END

Input Dataset Information
    [Arguments]    ${name}    ${description}
    ${name_input_locators}=    Get Dynamic Input Locator    Dataset Name
    Wait For And Input Text    css:[data-testid="dataset-name"]    ${name_input_locators}    ${name}
    ${desc_input_locators}=    Get Dynamic Input Locator    Description
    Wait For And Input Text    css:[data-testid="dataset-desc"]    ${desc_input_locators}    ${description}

Click Process Dataset
    ${process_btn_locators}=    Get Dynamic Button Locator    Process Dataset
    Wait For And Click Element    css:[data-testid="process-dataset"]    ${process_btn_locators}

Verify Dataset Preview
    Wait Until Element Is Visible    css:[data-testid="data-preview"]
    ${preview_rows}=    Get Element Count    css:[data-testid="preview-row"]
    Should Be True    ${preview_rows} > 0

Apply Column Filter
    ${filter_input_locators}=    Get Dynamic Input Locator    Filter
    Wait For And Input Text    css:[data-testid="column-filter"]    ${filter_input_locators}    test
    Press Keys    None    ENTER

Sort By Column
    ${sort_btn_locators}=    Create List
    ...    css:[data-testid="sort-button"]
    ...    xpath://th[contains(@class, "sortable")]
    Wait For And Click Element    css:[data-testid="sort-button"]    ${sort_btn_locators}

Create Histogram
    ${viz_select_locators}=    Create List
    ...    css:[data-testid="viz-type-select"]
    ...    xpath://select[contains(@class, "visualization-type")]
    Wait For And Click Element    css:[data-testid="viz-type-select"]    ${viz_select_locators}
    Select From List By Label    css:[data-testid="viz-type-select"]    Histogram
    ${column_select_locators}=    Create List
    ...    css:[data-testid="column-select"]
    ...    xpath://select[contains(@class, "column-selector")]
    Wait For And Click Element    css:[data-testid="column-select"]    ${column_select_locators}
    Select First Numeric Column

Select First Numeric Column
    @{numeric_columns}=    Get WebElements    css:[data-testid="numeric-column-option"]
    Click Element    ${numeric_columns}[0]

Verify Histogram
    Element Should Be Visible With Healing    
    ...    css:[data-testid="histogram-plot"]
    ...    xpath://div[contains(@class, "stPlotlyChart")]

Create Test CSV File
    [Arguments]    ${name}
    ${file_path}=    Set Variable    ${TEST_DATA_DIR}/${name}.csv
    ${content}=    Catenate    SEPARATOR=\n
    ...    id,name,value,category,timestamp
    ...    1,Test A,10.5,Cat1,2025-01-01
    ...    2,Test B,15.2,Cat2,2025-01-02
    ...    3,Test C,8.7,Cat1,2025-01-03
    ...    4,Test D,12.3,Cat2,2025-01-04
    ...    5,Test E,9.8,Cat1,2025-01-05
    Create File    ${file_path}    ${content}
    RETURN    ${file_path}

Wait Until Success Message Disappears
    Wait Until Element Is Not Visible    css:.stSuccess    timeout=10s
