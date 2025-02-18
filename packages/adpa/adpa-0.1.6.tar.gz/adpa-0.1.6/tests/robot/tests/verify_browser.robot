*** Settings ***
Library    Browser
Suite Setup    Start Streamlit App
Suite Teardown    Close All Processes

*** Variables ***
${TIMEOUT}    30s
${STREAMLIT_PORT}    8505
${STREAMLIT_URL}    http://localhost:${STREAMLIT_PORT}

*** Keywords ***
Start Streamlit App
    ${handle}=    Start Process    streamlit    run    streamlit_app/Home.py    --server.port\=${STREAMLIT_PORT}    --server.headless=true    shell=True
    Set Suite Variable    ${STREAMLIT_HANDLE}    ${handle}
    Sleep    5s    # Wait for Streamlit to start

Close All Processes
    Terminate Process    ${STREAMLIT_HANDLE}
    Close Browser    ALL

*** Test Cases ***
Browser Library Test
    New Browser    chromium    headless=False
    New Context    viewport={'width': 1920, 'height': 1080}
    New Page    ${STREAMLIT_URL}
    Get Title    ==    Home
    Take Screenshot    filename=home_page
    
    # Wait for Streamlit to load
    Wait For Elements State    [data-testid="stHeader"]    visible    timeout=${TIMEOUT}
    
    # Verify navigation menu exists
    Wait For Elements State    [data-testid="stSidebarNav"]    visible    timeout=${TIMEOUT}
    
    # Take final screenshot
    Take Screenshot    filename=loaded_page
