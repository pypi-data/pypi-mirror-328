*** Settings ***
Documentation     Technical tests for team management functionality
Resource          ../../resources/team.resource
Library           Collections
Library           OperatingSystem

*** Variables ***
${TEAM_NAME}      test_team
${MEMBER_COUNT}   5

*** Test Cases ***
Test Team Creation
    [Documentation]    Test team creation and initialization
    [Tags]    technical    creation
    ${team}=    Create Team    ${TEAM_NAME}
    Should Not Be Empty    ${team.id}
    Should Be Equal    ${team.name}    ${TEAM_NAME}
    Should Be Empty    ${team.members}

Test Member Management
    [Documentation]    Test team member operations
    [Tags]    technical    members
    ${team}=    Create Team    ${TEAM_NAME}
    FOR    ${i}    IN RANGE    ${MEMBER_COUNT}
        Add Team Member    ${team}    member_${i}    role_${i}
    END
    ${members}=    Get Team Members    ${team}
    Length Should Be    ${members}    ${MEMBER_COUNT}

Test Role Management
    [Documentation]    Test team role assignments
    [Tags]    technical    roles
    ${team}=    Create Team    ${TEAM_NAME}
    Add Team Member    ${team}    leader    team_leader
    Add Team Member    ${team}    researcher    researcher
    ${leader_perms}=    Get Member Permissions    ${team}    leader
    ${researcher_perms}=    Get Member Permissions    ${team}    researcher
    Should Be True    ${leader_perms} > ${researcher_perms}

Test Permission Management
    [Documentation]    Test permission system
    [Tags]    technical    permissions
    ${team}=    Create Team    ${TEAM_NAME}
    Add Team Member    ${team}    user1    researcher
    ${perms}=    Create List    read    write
    Set Member Permissions    ${team}    user1    ${perms}
    ${current_perms}=    Get Member Permissions    ${team}    user1
    Lists Should Be Equal    ${perms}    ${current_perms}

Test Resource Allocation
    [Documentation]    Test team resource management
    [Tags]    technical    resources
    ${team}=    Create Team    ${TEAM_NAME}
    ${resources}=    Create Dictionary    
    ...    compute=10    
    ...    storage=1000
    Allocate Team Resources    ${team}    ${resources}
    ${usage}=    Get Resource Usage    ${team}
    Dictionaries Should Be Equal    ${resources}    ${usage}

Test Team Communication
    [Documentation]    Test team communication channels
    [Tags]    technical    communication
    ${team}=    Create Team    ${TEAM_NAME}
    Create Communication Channel    ${team}    general
    Send Team Message    ${team}    general    test_message
    ${messages}=    Get Channel Messages    ${team}    general
    Should Not Be Empty    ${messages}

Test Access Control
    [Documentation]    Test team access control
    [Tags]    technical    security
    ${team}=    Create Team    ${TEAM_NAME}
    Add Team Member    ${team}    user1    researcher
    ${resource}=    Create Team Resource    ${team}    test_data
    Set Resource Access    ${team}    ${resource}    user1    read
    ${access}=    Check Resource Access    ${team}    ${resource}    user1
    Should Be Equal    ${access}    read

Test Team Metrics
    [Documentation]    Test team performance metrics
    [Tags]    technical    metrics
    ${team}=    Create Team    ${TEAM_NAME}
    Start Team Monitoring    ${team}
    Run Team Activities    ${team}
    ${metrics}=    Get Team Metrics    ${team}
    Verify Team Metrics    ${metrics}

Test Concurrent Operations
    [Documentation]    Test concurrent team operations
    [Tags]    technical    concurrency
    ${team}=    Create Team    ${TEAM_NAME}
    ${operations}=    Create Concurrent Operations    ${team}
    Run Concurrent Team Operations    ${operations}
    Verify Operation Results    ${operations}

Test Team State Management
    [Documentation]    Test team state transitions
    [Tags]    technical    state
    ${team}=    Create Team    ${TEAM_NAME}
    Set Team State    ${team}    active
    ${state}=    Get Team State    ${team}
    Should Be Equal    ${state}    active
    Set Team State    ${team}    archived
    ${state}=    Get Team State    ${team}
    Should Be Equal    ${state}    archived
