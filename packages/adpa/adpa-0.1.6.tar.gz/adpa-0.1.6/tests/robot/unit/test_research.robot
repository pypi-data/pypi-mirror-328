*** Settings ***
Documentation     Unit tests for Research functionality
Resource          ../resources/common.robot
Library           ../../adpa/research/search.py
Library           Collections

*** Variables ***
${QUERY}          artificial intelligence
${MAX_RESULTS}    5

*** Test Cases ***
Test Search Functionality
    [Documentation]    Test basic search functionality
    ${results}=    Perform Search    ${QUERY}    ${MAX_RESULTS}
    Should Not Be Empty    ${results}
    Length Should Be    ${results}    ${MAX_RESULTS}

Test Result Format
    [Documentation]    Test search result format
    ${results}=    Perform Search    ${QUERY}    1
    Validate Result Format    ${results}[0]

Test Multiple Sources
    [Documentation]    Test searching from multiple sources
    ${results}=    Search Multiple Sources    ${QUERY}    ${MAX_RESULTS}
    FOR    ${result}    IN    @{results}
        Should Have Source    ${result}
    END

Test Error Handling
    [Documentation]    Test search error handling
    Run Keyword And Expect Error    *    Perform Search    ${EMPTY}    ${MAX_RESULTS}

*** Keywords ***
Perform Search
    [Arguments]    ${query}    ${max_results}
    ${results}=    Search Topic    ${query}    max_results=${max_results}
    RETURN    ${results}

Search Multiple Sources
    [Arguments]    ${query}    ${max_results}
    ${results}=    Search Topic    
    ...    ${query}    
    ...    max_results=${max_results}    
    ...    sources=["web", "arxiv", "news"]
    RETURN    ${results}

Validate Result Format
    [Arguments]    ${result}
    Dictionary Should Contain Key    ${result}    title
    Dictionary Should Contain Key    ${result}    content
    Dictionary Should Contain Key    ${result}    url
    Dictionary Should Contain Key    ${result}    source

Should Have Source
    [Arguments]    ${result}
    Dictionary Should Contain Key    ${result}    source
    Should Not Be Empty    ${result}[source]
