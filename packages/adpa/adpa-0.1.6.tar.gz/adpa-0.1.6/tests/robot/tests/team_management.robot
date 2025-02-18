*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/database.resource

Suite Setup       Run Keywords    Connect To Database    Open ADPA
Suite Teardown    Run Keywords    Close ADPA    Disconnect From Database
Test Setup       Clean Database
Test Teardown    Seed Test Data

*** Test Cases ***
Create New Team
    Navigate To Page    Team Management
    Click    button:text("Create Team")
    Fill Text    [data-testid="team-name"]    Test Team
    Fill Text    [data-testid="team-description"]    A test team
    Click    button:text("Save")
    Wait For Elements State    text="Team created successfully"    visible

Edit Team
    Navigate To Page    Team Management
    Click    [data-testid="edit-team-1"]
    Fill Text    [data-testid="team-name"]    Updated Team
    Click    button:text("Save")
    Wait For Elements State    text="Team updated successfully"    visible

Delete Team
    Navigate To Page    Team Management
    Click    [data-testid="delete-team-1"]
    Click    button:text("Confirm")
    Wait For Elements State    text="Team deleted successfully"    visible
