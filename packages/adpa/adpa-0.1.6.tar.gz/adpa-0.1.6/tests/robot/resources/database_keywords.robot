*** Settings ***
Documentation    Keywords for database component testing
Library          SeleniumLibrary
Library          RequestsLibrary
Library          DatabaseLibrary
Library          OperatingSystem
Library          Collections

*** Variables ***
${HEALTH_CHECK_ENDPOINT}    http://localhost:8501/api/health
${DB_MONITOR_ENDPOINT}      http://localhost:8501/api/monitor
${BACKUP_DIR}              ${CURDIR}/../../backups
${LOG_DIR}                 ${CURDIR}/../../logs
${MAX_RETRIES}            3
${RETRY_DELAY}            5s

*** Keywords ***
Start Application
    [Documentation]    Start the Streamlit application and setup test environment
    Create Session    streamlit    ${APP_URL}
    Set Selenium Speed    0.5s
    Open Browser    ${APP_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://div[contains(@class, 'stTabs')]    timeout=20s
    Create Directory    ${BACKUP_DIR}
    Create Directory    ${LOG_DIR}

Stop Application
    [Documentation]    Clean up test environment
    Close All Browsers
    Delete All Sessions
    Cleanup Test Data

Cleanup Test Data
    [Documentation]    Remove test data and temporary files
    Remove Files    ${BACKUP_DIR}/test_*
    Empty Directory    ${LOG_DIR}

Wait For Database Recovery
    [Documentation]    Wait for database to recover with exponential backoff
    [Arguments]    ${max_attempts}=5    ${initial_delay}=1
    FOR    ${attempt}    IN RANGE    1    ${max_attempts + 1}
        ${status}=    Run Keyword And Return Status    Test Database Connection
        Return From Keyword If    ${status}
        ${delay}=    Evaluate    ${initial_delay} * (2 ** (${attempt} - 1))
        Sleep    ${delay}s
    END
    Fail    Database did not recover after ${max_attempts} attempts

Monitor Database Health
    [Documentation]    Monitor database health metrics
    ${response}=    GET On Session    streamlit    ${HEALTH_CHECK_ENDPOINT}
    Should Be Equal As Strings    ${response.status_code}    200
    ${health}=    Set Variable    ${response.json()}
    Should Be True    ${health['score']} >= 0
    Should Be True    ${health['score']} <= 100
    [Return]    ${health}

Check Resource Usage
    [Documentation]    Check resource usage metrics
    ${response}=    GET On Session    streamlit    ${DB_MONITOR_ENDPOINT}
    Should Be Equal As Strings    ${response.status_code}    200
    ${metrics}=    Set Variable    ${response.json()}
    FOR    ${metric}    IN    @{metrics}
        Should Be True    ${metric['value']} >= 0
        Should Be True    ${metric['value']} <= 100
    END
    [Return]    ${metrics}

Verify Database Backup
    [Documentation]    Verify database backup creation
    [Arguments]    ${backup_name}
    File Should Exist    ${BACKUP_DIR}/${backup_name}
    ${size}=    Get File Size    ${BACKUP_DIR}/${backup_name}
    Should Be True    ${size} > 0

Log Error
    [Documentation]    Log error with timestamp
    [Arguments]    ${error_message}
    ${timestamp}=    Get Current Date
    ${log_entry}=    Set Variable    [${timestamp}] ERROR: ${error_message}
    Append To File    ${LOG_DIR}/error.log    ${log_entry}\n

Attempt Recovery
    [Documentation]    Attempt to recover from database failure
    [Arguments]    ${error_type}
    ${recovery_script}=    Set Variable If
    ...    '${error_type}' == 'connection'    ${CURDIR}/scripts/recover_connection.sh
    ...    '${error_type}' == 'corruption'    ${CURDIR}/scripts/recover_data.sh
    ...    '${error_type}' == 'performance'    ${CURDIR}/scripts/optimize_db.sh
    ...    ${CURDIR}/scripts/general_recovery.sh
    
    ${result}=    Run Process    ${recovery_script}
    Run Keyword If    ${result.rc} != 0
    ...    Log Error    Recovery failed: ${result.stderr}
    [Return]    ${result.rc} == 0

Check System Resources
    [Documentation]    Check system resource availability
    ${cpu}=    Get CPU Usage
    ${memory}=    Get Memory Usage
    ${disk}=    Get Disk Usage
    
    Run Keyword If    ${cpu} > 90    Log Warning    High CPU usage: ${cpu}%
    Run Keyword If    ${memory} > 90    Log Warning    High memory usage: ${memory}%
    Run Keyword If    ${disk} > 90    Log Warning    High disk usage: ${disk}%
    
    [Return]    ${cpu} < 90 and ${memory} < 90 and ${disk} < 90

Get CPU Usage
    ${result}=    Run Process    wmic    cpu    get    loadpercentage
    ${lines}=    Split To Lines    ${result.stdout}
    ${usage}=    Set Variable    ${lines[1]}
    [Return]    ${usage}

Get Memory Usage
    ${result}=    Run Process    wmic    OS    get    FreePhysicalMemory,TotalVisibleMemorySize    /Value
    ${free}=    Get Line    ${result.stdout}    1
    ${total}=    Get Line    ${result.stdout}    2
    ${free_num}=    Convert To Number    ${free.split('=')[1]}
    ${total_num}=    Convert To Number    ${total.split('=')[1]}
    ${usage}=    Evaluate    (1 - ${free_num}/${total_num}) * 100
    [Return]    ${usage}

Get Disk Usage
    ${result}=    Run Process    wmic    logicaldisk    get    size,freespace,caption
    ${lines}=    Split To Lines    ${result.stdout}
    ${usage}=    Set Variable    0
    FOR    ${line}    IN    @{lines}
        Continue For Loop If    '${line.strip()}' == '' or '${line.strip()}' == '${lines[0]}'
        ${parts}=    Split String    ${line}
        ${free}=    Convert To Number    ${parts[1]}
        ${total}=    Convert To Number    ${parts[2]}
        ${disk_usage}=    Evaluate    (1 - ${free}/${total}) * 100
        ${usage}=    Set Variable If    ${disk_usage} > ${usage}    ${disk_usage}    ${usage}
    END
    [Return]    ${usage}
