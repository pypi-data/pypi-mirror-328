*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/database.resource

Suite Setup       Run Keywords    Connect To Database    Open ADPA
Suite Teardown    Run Keywords    Close ADPA    Disconnect From Database
Test Setup       Clean Database
Test Teardown    Seed Test Data

*** Test Cases ***
Home Page Should Load
    Wait For Elements State    h1:text("ADPA")    visible
    Get Text    h1:text("ADPA")    ==    ADPA

Navigation Menu Should Work
    ${pages}=    Create List    Team Management    Research    Settings
    FOR    ${page}    IN    @{pages}
        Navigate To Page    ${page}
        Wait For Elements State    h1:text("${page}")    visible
    END

System Health Should Be Displayed
    Wait For Elements State    [data-testid="system-health"]    visible
    ${status}=    Get Text    [data-testid="health-status"]
    Should Be Equal    ${status}    healthy
