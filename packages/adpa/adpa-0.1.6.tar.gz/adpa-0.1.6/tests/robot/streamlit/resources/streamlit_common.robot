*** Settings ***
Documentation     Common keywords for Streamlit page testing
Library           SeleniumLibrary
Library           Process

*** Variables ***
${STREAMLIT_PORT}    8501
${DEFAULT_TIMEOUT}   10s

*** Keywords ***
Wait For Streamlit Element
    [Arguments]    ${locator}    ${timeout}=${DEFAULT_TIMEOUT}
    Wait Until Element Is Visible    ${locator}    ${timeout}
    Wait Until Element Is Enabled    ${locator}    ${timeout}

Click Streamlit Element
    [Arguments]    ${locator}    ${timeout}=${DEFAULT_TIMEOUT}
    Wait For Streamlit Element    ${locator}    ${timeout}
    Click Element    ${locator}

Input Streamlit Text
    [Arguments]    ${locator}    ${text}    ${timeout}=${DEFAULT_TIMEOUT}
    Wait For Streamlit Element    ${locator}    ${timeout}
    Input Text    ${locator}    ${text}

Select Streamlit Option
    [Arguments]    ${dropdown_locator}    ${option_text}    ${timeout}=${DEFAULT_TIMEOUT}
    Click Streamlit Element    ${dropdown_locator}    ${timeout}
    ${option_locator}=    Set Variable    xpath://div[contains(text(), '${option_text}')]
    Click Streamlit Element    ${option_locator}    ${timeout}

Verify Streamlit Page Loaded
    [Arguments]    ${page_title}    ${timeout}=${DEFAULT_TIMEOUT}
    Wait Until Element Is Visible    xpath://h1[contains(text(), '${page_title}')]    ${timeout}
    Wait Until Page Contains Element    css:div[data-testid="stVerticalBlock"]

Wait For Streamlit Spinner
    Wait Until Element Is Not Visible    css:div[data-testid="stSpinner"]    ${DEFAULT_TIMEOUT}

Verify No Streamlit Errors
    Page Should Not Contain Element    css:div[data-testid="stException"]
    Page Should Not Contain Element    css:div[data-baseweb="notification"] div[role="alert"]

Take Screenshot On Failure
    [Arguments]    ${test_name}
    Run Keyword If Test Failed    Capture Page Screenshot    ${test_name}_failure.png

Start Streamlit Server
    [Arguments]    ${script_path}    ${port}=${STREAMLIT_PORT}
    ${handle}=    Start Process    streamlit    run    ${script_path}    --server.port    ${port}
    Set Suite Variable    ${STREAMLIT_HANDLE}    ${handle}
    Sleep    5s    # Wait for server to start

Stop Streamlit Server
    Terminate Process    ${STREAMLIT_HANDLE}
    Sleep    2s    # Wait for cleanup
