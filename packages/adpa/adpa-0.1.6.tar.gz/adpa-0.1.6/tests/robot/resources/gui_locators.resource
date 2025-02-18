*** Settings ***
Library    SeleniumLibrary
Library    String
Library    Collections

*** Variables ***
${BROWSER}    chrome
${BASE_URL}    http://localhost:8501
${TIMEOUT}    20s

# Dynamic locator strategies
${LOCATOR_PRIORITY}    css, xpath, id, name, class

*** Keywords ***
Find Element With Healing
    [Arguments]    ${primary_locator}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    ${found}=    Run Keyword And Return Status    
    ...    Wait Until Element Is Visible    ${primary_locator}    timeout=${timeout}
    
    IF    ${found}
        RETURN    ${primary_locator}
    ELSE IF    ${backup_locators} is not ${None}
        FOR    ${locator}    IN    @{backup_locators}
            ${status}=    Run Keyword And Return Status    
            ...    Wait Until Element Is Visible    ${locator}    timeout=${timeout}
            IF    ${status}
                Log    Self-healed: Using backup locator ${locator} instead of ${primary_locator}    level=WARN
                RETURN    ${locator}
            END
        END
    END
    Fail    No viable locator found for element (primary: ${primary_locator})

Get Dynamic Button Locator
    [Arguments]    ${button_text}
    ${locators}=    Create List
    ...    css:button >> text="${button_text}"
    ...    xpath://button[contains(text(), "${button_text}")]
    ...    xpath://div[contains(@class, "stButton")]//button[contains(text(), "${button_text}")]
    RETURN    ${locators}

Get Dynamic Input Locator
    [Arguments]    ${label_text}
    ${locators}=    Create List
    ...    css:[aria-label="${label_text}"]
    ...    xpath://input[@aria-label="${label_text}"]
    ...    xpath://div[contains(@class, "stTextInput")]//input
    RETURN    ${locators}

Get Dynamic Tab Locator
    [Arguments]    ${tab_text}
    ${locators}=    Create List
    ...    css:[data-baseweb="tab"] >> text="${tab_text}"
    ...    xpath://button[contains(@role, "tab") and contains(text(), "${tab_text}")]
    ...    xpath://div[contains(@class, "stTabs")]//button[contains(text(), "${tab_text}")]
    RETURN    ${locators}

Wait For And Click Element
    [Arguments]    ${primary_locator}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    ${locator}=    Find Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    Click Element    ${locator}

Wait For And Input Text
    [Arguments]    ${primary_locator}    ${text}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    ${locator}=    Find Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    Input Text    ${locator}    ${text}

Element Should Be Visible With Healing
    [Arguments]    ${primary_locator}    ${backup_locators}=${None}    ${timeout}=${TIMEOUT}
    ${locator}=    Find Element With Healing    ${primary_locator}    ${backup_locators}    ${timeout}
    Element Should Be Visible    ${locator}
