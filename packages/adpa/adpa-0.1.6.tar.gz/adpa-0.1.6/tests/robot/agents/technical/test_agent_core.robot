*** Settings ***
Documentation     Technical tests for core agent functionality
Resource          ../../resources/agent.resource
Library           OperatingSystem
Library           Collections

*** Variables ***
${AGENT_NAME}     test_agent
${MEMORY_SIZE}    1000

*** Test Cases ***
Test Agent Initialization
    [Documentation]    Test agent initialization and configuration
    [Tags]    technical    initialization
    ${agent}=    Create Agent    ${AGENT_NAME}
    Should Not Be Empty    ${agent.id}
    Should Be Equal    ${agent.name}    ${AGENT_NAME}

Test Memory Management
    [Documentation]    Test agent memory operations
    [Tags]    technical    memory    performance
    ${agent}=    Create Agent    ${AGENT_NAME}
    FOR    ${i}    IN RANGE    ${MEMORY_SIZE}
        Add Memory Entry    ${agent}    memory_${i}    data_${i}
    END
    ${memory_size}=    Get Memory Size    ${agent}
    Should Be Equal As Integers    ${memory_size}    ${MEMORY_SIZE}

Test Agent State Management
    [Documentation]    Test agent state transitions
    [Tags]    technical    state
    ${agent}=    Create Agent    ${AGENT_NAME}
    Start Agent    ${agent}
    Should Be Equal    ${agent.state}    RUNNING
    Pause Agent    ${agent}
    Should Be Equal    ${agent.state}    PAUSED
    Resume Agent    ${agent}
    Should Be Equal    ${agent.state}    RUNNING
    Stop Agent    ${agent}
    Should Be Equal    ${agent.state}    STOPPED

Test Concurrent Operations
    [Documentation]    Test concurrent agent operations
    [Tags]    technical    concurrency
    ${agents}=    Create List
    FOR    ${i}    IN RANGE    5
        ${agent}=    Create Agent    agent_${i}
        Append To List    ${agents}    ${agent}
    END
    Run Parallel Operations    ${agents}
    Verify Agent States    ${agents}

Test Resource Management
    [Documentation]    Test agent resource usage
    [Tags]    technical    resources
    ${agent}=    Create Agent    ${AGENT_NAME}
    Start Resource Monitoring    ${agent}
    Run Heavy Operation    ${agent}
    ${usage}=    Get Resource Usage    ${agent}
    Should Be True    ${usage.cpu} < 80
    Should Be True    ${usage.memory} < 500

Test Error Recovery
    [Documentation]    Test agent error handling and recovery
    [Tags]    technical    error    recovery
    ${agent}=    Create Agent    ${AGENT_NAME}
    Inject Error    ${agent}
    Verify Error Handling    ${agent}
    Verify Agent Recovery    ${agent}

Test Performance Metrics
    [Documentation]    Test agent performance monitoring
    [Tags]    technical    performance    metrics
    ${agent}=    Create Agent    ${AGENT_NAME}
    Start Performance Monitoring    ${agent}
    Run Benchmark Operations    ${agent}
    ${metrics}=    Get Performance Metrics    ${agent}
    Verify Performance Thresholds    ${metrics}

Test Configuration Management
    [Documentation]    Test agent configuration handling
    [Tags]    technical    configuration
    ${agent}=    Create Agent    ${AGENT_NAME}
    ${config}=    Create Dictionary    
    ...    memory_limit=1000    
    ...    timeout=30    
    ...    retry_count=3
    Update Agent Configuration    ${agent}    ${config}
    ${current_config}=    Get Agent Configuration    ${agent}
    Dictionaries Should Be Equal    ${config}    ${current_config}
