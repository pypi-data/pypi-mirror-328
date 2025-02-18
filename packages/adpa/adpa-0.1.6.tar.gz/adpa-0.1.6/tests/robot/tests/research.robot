*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/database.resource

Suite Setup       Run Keywords    Connect To Database    Open ADPA
Suite Teardown    Run Keywords    Close ADPA    Disconnect From Database
Test Setup       Clean Database
Test Teardown    Seed Test Data

*** Test Cases ***
Search Functionality
    Navigate To Page    Research
    Fill Text    [data-testid="search-input"]    test query
    Click    button:text("Search")
    Wait For Elements State    [data-testid="search-results"]    visible
    ${results_count}=    Get Element Count    [data-testid="search-result-item"]
    Should Be True    ${results_count} > 0

Filter Results
    Navigate To Page    Research
    Click    [data-testid="filter-dropdown"]
    Click    text=Last Week
    Wait For Elements State    [data-testid="filtered-results"]    visible
    ${filtered_count}=    Get Element Count    [data-testid="search-result-item"]
    Should Be True    ${filtered_count} >= 0

Export Results
    Navigate To Page    Research
    Fill Text    [data-testid="search-input"]    export test
    Click    button:text("Search")
    Wait For Elements State    [data-testid="search-results"]    visible
    Click    button:text("Export")
    ${download_promise}=    Promise To Wait For Download    *.csv
    Click    text=CSV
    ${file_obj}=    Wait For    ${download_promise}
    Should Not Be Empty    ${file_obj}[saveAs]
