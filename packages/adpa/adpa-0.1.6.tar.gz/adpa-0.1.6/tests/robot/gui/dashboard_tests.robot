*** Settings ***
Documentation     Dashboard GUI Tests
Resource          ../resources/common.resource

Suite Setup       Setup Test Environment
Suite Teardown    Cleanup Test Environment
Test Setup       Test Setup
Test Teardown    Test Teardown

*** Test Cases ***
Dashboard Should Display Project Overview
    [Documentation]    Verify dashboard shows correct project overview information
    [Tags]    gui    dashboard    overview
    Verify Element Text    [data-testid="active-projects"]    Active Projects: 0
    Verify Element Text    [data-testid="total-datasets"]    Total Datasets: 0

Dashboard Should Show Recent Activities
    [Documentation]    Verify recent activities are displayed correctly
    [Tags]    gui    dashboard    activities
    Verify Element Text    [data-testid="no-activities"]    No recent activities

Dashboard Should Display System Health
    [Documentation]    Verify system health indicators are shown
    [Tags]    gui    dashboard    health
    Verify Element Text    [data-testid="system-status"]    System Status: Healthy

Dashboard Should Allow Project Switching
    [Documentation]    Verify project switching functionality
    [Tags]    gui    dashboard    projects
    Click Element    [data-testid="project-selector"]
    Verify Element Text    [data-testid="no-projects"]    No projects available

Dashboard Should Show Resource Usage
    [Documentation]    Verify resource usage metrics
    [Tags]    gui    dashboard    resources
    Verify Element Exists    [data-testid="cpu-usage"]
    Verify Element Exists    [data-testid="memory-usage"]
    Verify Element Exists    [data-testid="storage-usage"]

Dashboard Should Support Quick Actions
    [Documentation]    Verify quick action buttons
    [Tags]    gui    dashboard    actions
    Click Element    [data-testid="quick-actions"]
    Verify Element Exists    [data-testid="new-project"]
    Verify Element Exists    [data-testid="upload-dataset"]
    Verify Element Exists    [data-testid="start-analysis"]

Dashboard Should Handle Empty States
    [Documentation]    Verify empty state handling
    [Tags]    gui    dashboard    empty
    Verify Element Text    [data-testid="empty-message"]    Welcome to ADPA!
    Verify Element Exists    [data-testid="get-started-button"]

Dashboard Should Be Responsive
    [Documentation]    Verify dashboard responsiveness
    [Tags]    gui    dashboard    responsive    mobile
    [Setup]    Mobile Test Setup
    Verify Element Exists    [data-testid="mobile-menu"]
    Click Element    [data-testid="mobile-menu"]
    Verify Element Exists    [data-testid="mobile-navigation"]
    [Teardown]    Test Teardown
