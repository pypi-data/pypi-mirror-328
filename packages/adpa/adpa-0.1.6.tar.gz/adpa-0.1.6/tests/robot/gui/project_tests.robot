*** Settings ***
Documentation    Project Management GUI Tests with self-healing mechanisms
Resource    ../resources/gui_locators.resource
Resource    ../resources/common.resource

Test Setup    Begin Web Test
Test Teardown    End Web Test

*** Test Cases ***
User Can Create New Project
    [Documentation]    Verify project creation functionality
    [Tags]    gui    project    create
    Go To Dashboard
    Click New Project
    Fill Project Details    Test Project    A test project description
    Submit Project Form
    Verify Project Created
    Verify Project Dashboard

User Can Edit Project Details
    [Documentation]    Verify project editing functionality
    [Tags]    gui    project    edit
    Create Test Project
    Go To Project Settings
    Edit Project Name    Updated Project Name
    Edit Project Description    Updated project description
    Save Project Changes
    Verify Project Updates

User Can Archive Project
    [Documentation]    Verify project archiving
    [Tags]    gui    project    archive
    Create Test Project
    Go To Project Settings
    Archive Project
    Verify Archive Confirmation
    Confirm Archive
    Verify Project Archived
    Access Archived Projects
    Verify Project In Archives

User Can Restore Archived Project
    [Documentation]    Verify project restoration
    [Tags]    gui    project    restore
    Create And Archive Test Project
    Access Archived Projects
    Restore Project
    Verify Project Restored
    Verify Project Active

User Can Delete Project
    [Documentation]    Verify project deletion
    [Tags]    gui    project    delete
    Create Test Project
    Go To Project Settings
    Delete Project
    Verify Delete Confirmation
    Confirm Delete
    Verify Project Deleted

User Can Manage Project Team
    [Documentation]    Verify team management
    [Tags]    gui    project    team
    Create Test Project
    Go To Project Settings
    Add Team Member    test.user@example.com    Editor
    Verify Team Member Added
    Change Member Role    test.user@example.com    Viewer
    Verify Role Updated
    Remove Team Member    test.user@example.com
    Verify Team Member Removed

User Can Set Project Preferences
    [Documentation]    Verify project preferences
    [Tags]    gui    project    preferences
    Create Test Project
    Go To Project Settings
    Set Default View    Research
    Set Auto Save    True
    Set Notification Level    High
    Save Preferences
    Verify Preferences Saved

Project Dashboard Shows Correct Metrics
    [Documentation]    Verify project metrics
    [Tags]    gui    project    metrics
    Create Test Project With Data
    Go To Project Dashboard
    Verify Task Metrics
    Verify Progress Metrics
    Verify Timeline
    Verify Recent Activities

Project Supports Multiple Languages
    [Documentation]    Verify project internationalization
    [Tags]    gui    project    i18n
    Create Test Project
    Change Project Language    Deutsch
    Verify German Interface
    Change Project Language    Español
    Verify Spanish Interface
    Reset Language

Project Handles Concurrent Access
    [Documentation]    Verify concurrent access handling
    [Tags]    gui    project    concurrent
    Create Test Project
    Open Project In New Session
    Make Concurrent Changes
    Verify Conflict Resolution
    Verify Changes Merged

*** Keywords ***
Click New Project
    ${new_project_btn_locators}=    Get Dynamic Button Locator    New Project
    Wait For And Click Element    css:[data-testid="new-project-btn"]    ${new_project_btn_locators}

Fill Project Details
    [Arguments]    ${name}    ${description}
    ${name_input_locators}=    Get Dynamic Input Locator    Project Name
    ${desc_input_locators}=    Get Dynamic Input Locator    Project Description
    Wait For And Input Text    css:[data-testid="project-name"]    ${name_input_locators}    ${name}
    Wait For And Input Text    css:[data-testid="project-desc"]    ${desc_input_locators}    ${description}

Submit Project Form
    ${submit_btn_locators}=    Get Dynamic Button Locator    Create Project
    Wait For And Click Element    css:[data-testid="create-project"]    ${submit_btn_locators}

Verify Project Created
    Wait Until Page Contains    Project created successfully    timeout=${TIMEOUT}
    Element Should Be Visible With Healing    
    ...    css:[data-testid="project-header"]
    ...    xpath://div[contains(@class, "project-title")]

Go To Project Settings
    ${settings_btn_locators}=    Get Dynamic Button Locator    Project Settings
    Wait For And Click Element    css:[data-testid="project-settings"]    ${settings_btn_locators}

Edit Project Name
    [Arguments]    ${new_name}
    ${name_input_locators}=    Get Dynamic Input Locator    Project Name
    Wait For And Input Text    css:[data-testid="project-name"]    ${name_input_locators}    ${new_name}

Archive Project
    ${archive_btn_locators}=    Get Dynamic Button Locator    Archive Project
    Wait For And Click Element    css:[data-testid="archive-project"]    ${archive_btn_locators}

Create And Archive Test Project
    Create Test Project
    Go To Project Settings
    Archive Project
    Verify Archive Confirmation
    Confirm Archive

Open Project In New Session
    ${session_id}=    Get Random String
    New Browser    browser=${BROWSER}    headless=${HEADLESS}
    New Context    viewport={'width': 1920, 'height': 1080}
    New Page    ${BASE_URL}
    Set Suite Variable    ${CONCURRENT_SESSION}    ${session_id}

Make Concurrent Changes
    ${name_input_locators}=    Get Dynamic Input Locator    Project Name
    Wait For And Input Text    css:[data-testid="project-name"]    ${name_input_locators}    Concurrent Edit
    Save Project Changes
    Switch Browser    1
    Edit Project Name    Another Edit
    Save Project Changes

Verify Conflict Resolution
    Element Should Be Visible With Healing    
    ...    css:[data-testid="conflict-dialog"]
    ...    xpath://div[contains(@class, "conflict-resolution")]
    Element Should Contain    css:[data-testid="conflict-message"]    Conflict detected

Create Test Project With Data
    Create Test Project
    Upload Sample Dataset
    Create Sample Tasks
    Generate Sample Timeline

Upload Sample Dataset
    ${file_path}=    Create Test CSV File    project_data
    Choose File    css:[data-testid="file-uploader"]    ${file_path}

Create Sample Tasks
    FOR    ${index}    IN RANGE    5
        Add Task    Task ${index}    Task description ${index}
        Set Task Status    Task ${index}    ${index % 3}
    END

Generate Sample Timeline
    ${timeline_data}=    Generate Test Data    rows=10
    Add Timeline Events    ${timeline_data}

Add Timeline Events
    [Arguments]    ${events}
    FOR    ${event}    IN    @{events}
        Add Event    ${event.name}    ${event.timestamp}
    END
