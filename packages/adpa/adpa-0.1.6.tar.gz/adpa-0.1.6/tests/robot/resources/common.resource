*** Settings ***
Documentation     Common resources for all test suites
Resource          test_init.resource

*** Keywords ***
Test Setup
    Setup Test Environment
    Start Browser Session

Test Teardown
    Take Error Screenshot
    End Browser Session
    Cleanup Test Environment

Mobile Test Setup
    Setup Test Environment
    Start Mobile Browser Session

# Common verification keywords
Verify Element Text
    [Arguments]    ${selector}    ${expected_text}    ${timeout}=${TIMEOUT}
    Wait For Elements State    ${selector}    visible    timeout=${timeout}
    Get Text    ${selector}    ==    ${expected_text}

Verify Element Count
    [Arguments]    ${selector}    ${expected_count}    ${timeout}=${TIMEOUT}
    Wait For Elements State    ${selector}    visible    timeout=${timeout}
    ${elements}=    Get Elements    ${selector}
    Length Should Be    ${elements}    ${expected_count}

Verify Element Exists
    [Arguments]    ${selector}    ${timeout}=${TIMEOUT}
    Wait For Elements State    ${selector}    visible    timeout=${timeout}

Verify Element Not Exists
    [Arguments]    ${selector}    ${timeout}=${TIMEOUT}
    Wait For Elements State    ${selector}    detached    timeout=${timeout}

# Common interaction keywords
Click Element
    [Arguments]    ${selector}    ${timeout}=${TIMEOUT}
    Wait For Elements State    ${selector}    visible    timeout=${timeout}
    Click    ${selector}

Type Text
    [Arguments]    ${selector}    ${text}    ${timeout}=${TIMEOUT}
    Wait For Elements State    ${selector}    visible    timeout=${timeout}
    Fill Text    ${selector}    ${text}

Select Option
    [Arguments]    ${selector}    ${option}    ${timeout}=${TIMEOUT}
    Wait For Elements State    ${selector}    visible    timeout=${timeout}
    Select Options By    ${selector}    text    ${option}

Upload File
    [Arguments]    ${selector}    ${file_path}    ${timeout}=${TIMEOUT}
    Wait For Elements State    ${selector}    visible    timeout=${timeout}
    Upload File By Selector    ${selector}    ${file_path}

# Common navigation keywords
Navigate To
    [Arguments]    ${path}
    Go To    ${BASE_URL}${path}
    Wait For Page Load

# Common test data management
Create Test Data
    [Arguments]    ${data_type}    ${count}=1
    ${data}=    Create List
    FOR    ${index}    IN RANGE    ${count}
        ${item}=    Generate ${data_type} Data    ${index}
        Append To List    ${data}    ${item}
    END
    [Return]    ${data}

Generate Project Data
    [Arguments]    ${index}
    ${project}=    Create Dictionary
    ${project.name}=    Set Variable    Test Project ${index}
    ${project.description}=    Set Variable    Test project description ${index}
    ${project.created_at}=    Get Current Date    result_format=%Y-%m-%d
    [Return]    ${project}

Generate Dataset Data
    [Arguments]    ${index}
    ${dataset}=    Create Dictionary
    ${dataset.name}=    Set Variable    Test Dataset ${index}
    ${dataset.type}=    Set Variable    CSV
    ${dataset.size}=    Set Variable    1024
    ${dataset.created_at}=    Get Current Date    result_format=%Y-%m-%d
    [Return]    ${dataset}

Generate Activity Data
    [Arguments]    ${index}
    ${activity}=    Create Dictionary
    ${activity.type}=    Set Variable    Test Activity ${index}
    ${activity.description}=    Set Variable    Test activity description ${index}
    ${activity.timestamp}=    Get Current Date    result_format=%Y-%m-%d %H:%M:%S
    [Return]    ${activity}
