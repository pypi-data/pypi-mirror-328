*** Settings ***
Documentation    Common keywords for ADPA Framework testing

*** Variables ***
${SCORE_THRESHOLD}    0.6
${BATCH_SIZE}        5
${TIMEOUT}          30s

*** Keywords ***
Framework Should Be Initialized
    ${status}=    Initialize Framework
    Should Be True    ${status}

Verify Core Components
    Component Should Exist    attention
    Component Should Exist    desire
    Component Should Exist    position
    Component Should Exist    action

Component Should Exist
    [Arguments]    ${component}
    ${result}=    Get Framework Component    ${component}
    Should Not Be Equal    ${result}    ${None}

Verify Attention Score
    [Arguments]    ${result}
    Verify Score    attention    ${result}

Verify Desire Score
    [Arguments]    ${result}
    Verify Score    desire    ${result}

Verify Position Score
    [Arguments]    ${result}
    Verify Score    position    ${result}

Verify Action Score
    [Arguments]    ${result}
    Verify Score    action    ${result}

Verify Score
    [Arguments]    ${component}    ${result}
    ${score}=    Get From Dictionary    ${result}    ${component}_score
    Should Be True    ${score} >= ${SCORE_THRESHOLD}
    Should Be True    ${score} <= 1.0

Verify Recommendations
    [Arguments]    ${result}    ${component}
    ${recommendations}=    Get From Dictionary    ${result}    ${component}_recommendations
    Length Should Be    ${recommendations}    > 0
    FOR    ${recommendation}    IN    @{recommendations}
        Should Not Be Empty    ${recommendation}
    END

Create Test Items
    [Arguments]    ${count}=${BATCH_SIZE}
    ${items}=    Create Test Items    ${count}
    Length Should Be    ${items}    ${count}
    [Return]    ${items}

Process And Verify Items
    [Arguments]    ${items}
    ${results}=    Process Items    ${items}
    Verify Batch Results    ${results}
    Verify Processing Time
    [Return]    ${results}

Wait For Processing
    [Arguments]    ${timeout}=${TIMEOUT}
    Wait Until Keyword Succeeds    ${timeout}    1s    Processing Should Be Complete

Processing Should Be Complete
    ${status}=    Get Processing Status
    Should Be Equal    ${status}    complete
