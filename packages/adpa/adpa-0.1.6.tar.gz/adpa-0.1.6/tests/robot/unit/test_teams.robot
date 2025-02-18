*** Settings ***
Documentation     Unit tests for Teams functionality
Resource          ../resources/common.robot
Library           ../../adpa/teams/team_utils.py
Library           Collections

*** Variables ***
${TEAM_NAME}      TestTeam
${TEAM_SIZE}      3
${MEMBER_NAME}    TestMember

*** Test Cases ***
Test Team Creation
    [Documentation]    Test creating a new team
    ${team}=    Create Test Team
    Should Not Be Empty    ${team}
    Should Be Equal    ${team.name}    ${TEAM_NAME}
    Should Be Equal As Numbers    ${team.size}    ${TEAM_SIZE}

Test Team Member Addition
    [Documentation]    Test adding team members
    ${team}=    Create Test Team
    ${member}=    Create Team Member    ${MEMBER_NAME}
    Add Member To Team    ${team}    ${member}
    ${members}=    Get Team Members    ${team}
    Should Contain    ${members}    ${member}

Test Team Member Removal
    [Documentation]    Test removing team members
    ${team}=    Create Test Team
    ${member}=    Create Team Member    ${MEMBER_NAME}
    Add Member To Team    ${team}    ${member}
    Remove Member From Team    ${team}    ${member}
    ${members}=    Get Team Members    ${team}
    Should Not Contain    ${members}    ${member}

Test Team Configuration
    [Documentation]    Test team configuration
    ${team}=    Create Test Team    CustomTeam    5
    Should Be Equal    ${team.name}    CustomTeam
    Should Be Equal As Numbers    ${team.size}    5

Test Team Role Assignment
    [Documentation]    Test role assignment
    ${team}=    Create Test Team
    ${member}=    Create Team Member    ${MEMBER_NAME}
    Add Member To Team    ${team}    ${member}
    Assign Role    ${team}    ${member}    leader
    ${role}=    Get Member Role    ${team}    ${member}
    Should Be Equal    ${role}    leader

*** Keywords ***
Create Test Team
    [Arguments]    ${name}=${TEAM_NAME}    ${size}=${TEAM_SIZE}
    ${team}=    Create Team Instance    
    ...    name=${name}    
    ...    size=${size}
    RETURN    ${team}

Create Team Member
    [Arguments]    ${name}
    ${member}=    Create Member Instance    ${name}
    RETURN    ${member}

Add Member To Team
    [Arguments]    ${team}    ${member}
    Add Team Member    ${team}    ${member}

Remove Member From Team
    [Arguments]    ${team}    ${member}
    Remove Team Member    ${team}    ${member}

Get Team Members
    [Arguments]    ${team}
    ${members}=    Get Members    ${team}
    RETURN    ${members}

Get Member Role
    [Arguments]    ${team}    ${member}
    ${role}=    Get Role    ${team}    ${member}
    RETURN    ${role}

Assign Role
    [Arguments]    ${team}    ${member}    ${role}
    Set Member Role    ${team}    ${member}    ${role}
