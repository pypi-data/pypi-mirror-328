*** Settings ***
Documentation     Keywords for Agent testing
Resource         ../resources/common.robot
Library          ../libraries/AgentManager.py
Library          ../libraries/SecurityValidator.py
Library          ../libraries/MetricsCollector.py

*** Keywords ***
Initialize Agent Suite
    [Documentation]    Initialize the test suite
    Initialize Agent Manager
    Load Security Configurations
    Start Metrics Collection
    Initialize Test Environment

Cleanup Agent Suite
    [Documentation]    Clean up after test suite
    Stop All Agents
    Clear Agent States
    Stop Metrics Collection
    Reset Test Environment

Reset Agent Environment
    [Documentation]    Reset environment before each test
    Clear Agent Cache
    Reset Agent States
    Initialize Clean Environment

Agent Configuration Is Loaded
    [Documentation]    Load agent configuration
    ${config}=    Load Configuration File    ${CONFIG_FILE}
    Set Test Variable    ${AGENT_CONFIG}    ${config}
    Validate Configuration Structure

Agent "${name}" Is Started
    [Documentation]    Start a new agent
    ${agent}=    Start Agent    ${name}    ${AGENT_CONFIG}
    Set Test Variable    ${CURRENT_AGENT}    ${agent}
    Wait Until Agent Ready    ${name}

Agent Should Be Running
    [Documentation]    Verify agent is running
    ${status}=    Get Agent Status    ${CURRENT_AGENT}
    Should Be Equal As Strings    ${status}    RUNNING

Agent "${name}" Is Stopped
    [Documentation]    Stop an agent
    Stop Agent    ${name}
    Wait Until Agent Stopped    ${name}

Agent Should Be Stopped
    [Documentation]    Verify agent is stopped
    ${status}=    Get Agent Status    ${CURRENT_AGENT}
    Should Be Equal As Strings    ${status}    STOPPED

No Resource Leaks Should Be Present
    [Documentation]    Check for resource leaks
    ${leaks}=    Check Resource Leaks
    Should Be Empty    ${leaks}

Start Agent
    [Documentation]    Start agent with name
    [Arguments]    ${name}
    ${agent}=    Start Agent    ${name}    ${AGENT_CONFIG}
    Wait Until Agent Ready    ${name}

All Agents Should Be Running
    [Documentation]    Verify all agents are running
    ${agents}=    Get All Agents
    FOR    ${agent}    IN    @{agents}
        ${status}=    Get Agent Status    ${agent}
        Should Be Equal As Strings    ${status}    RUNNING
    END

Verify Agent Communication
    [Documentation]    Test agent communication
    ${success}=    Test Agent Communication
    Should Be True    ${success}

Stop Agent
    [Documentation]    Stop agent with name
    [Arguments]    ${name}
    Stop Agent    ${name}
    Wait Until Agent Stopped    ${name}

All Agents Should Be Stopped
    [Documentation]    Verify all agents are stopped
    ${agents}=    Get All Agents
    FOR    ${agent}    IN    @{agents}
        ${status}=    Get Agent Status    ${agent}
        Should Be Equal As Strings    ${status}    STOPPED
    END

Monitoring Is Enabled
    [Documentation]    Enable monitoring
    Enable Agent Monitoring
    Initialize Metrics Collection
    Set Monitoring Thresholds

Agent Health Check Should Pass
    [Documentation]    Verify agent health
    ${health}=    Check Agent Health    ${CURRENT_AGENT}
    Should Be True    ${health.is_healthy}

Resource Usage Should Be Within Limits
    [Documentation]    Check resource usage
    ${usage}=    Get Resource Usage    ${CURRENT_AGENT}
    Verify Resource Limits    ${usage}

No Critical Alerts Should Be Present
    [Documentation]    Check for critical alerts
    ${alerts}=    Get Critical Alerts
    Should Be Empty    ${alerts}

Simulate Agent Failure
    [Documentation]    Simulate agent failure
    Trigger Agent Failure    ${CURRENT_AGENT}

Recovery Process Should Start
    [Documentation]    Verify recovery process
    ${recovery}=    Get Recovery Status
    Should Be Equal As Strings    ${recovery.state}    ACTIVE

Agent Should Be Restarted
    [Documentation]    Verify agent restart
    Wait Until Agent Ready    ${CURRENT_AGENT}
    ${status}=    Get Agent Status    ${CURRENT_AGENT}
    Should Be Equal As Strings    ${status}    RUNNING

Failure Should Be Logged
    [Documentation]    Check failure logging
    ${logs}=    Get Failure Logs
    Should Not Be Empty    ${logs}

Alerts Should Be Generated
    [Documentation]    Verify alert generation
    ${alerts}=    Get Generated Alerts
    Should Not Be Empty    ${alerts}

Security Configuration Is Loaded
    [Documentation]    Load security config
    ${config}=    Load Security Configuration    ${SECURITY_FILE}
    Set Test Variable    ${SECURITY_CONFIG}    ${config}

Agent "${name}" Is Started With Security
    [Documentation]    Start agent with security
    ${agent}=    Start Secure Agent    ${name}    ${SECURITY_CONFIG}
    Set Test Variable    ${CURRENT_AGENT}    ${agent}

Authentication Should Be Required
    [Documentation]    Verify authentication
    ${auth}=    Check Authentication Required
    Should Be True    ${auth}

Communication Should Be Encrypted
    [Documentation]    Verify encryption
    ${encrypted}=    Check Communication Encryption
    Should Be True    ${encrypted}

Access Controls Should Be Enforced
    [Documentation]    Verify access controls
    ${controls}=    Check Access Controls
    Should Be True    ${controls}

Security Audit Log Should Be Updated
    [Documentation]    Check audit logging
    ${audit}=    Get Security Audit Log
    Should Not Be Empty    ${audit}

Multiple Agents Are Running
    [Documentation]    Setup multiple agents
    Start Multiple Test Agents
    Wait For All Agents Ready

Message Is Sent Between Agents
    [Documentation]    Send test message
    ${message}=    Create Test Message
    Send Message Between Agents    ${message}

Message Should Be Delivered
    [Documentation]    Verify message delivery
    ${delivered}=    Check Message Delivery
    Should Be True    ${delivered}

Message Processing Should Complete
    [Documentation]    Verify processing
    ${processed}=    Check Message Processing
    Should Be True    ${processed}

Response Should Be Received
    [Documentation]    Verify response
    ${response}=    Get Message Response
    Should Not Be Empty    ${response}

Message Log Should Be Updated
    [Documentation]    Check message logging
    ${log}=    Get Message Log
    Should Not Be Empty    ${log}

Resource Limits Are Configured
    [Documentation]    Configure resource limits
    Load Resource Limits
    Set Resource Thresholds

Resource Usage Should Be Monitored
    [Documentation]    Verify monitoring
    ${monitoring}=    Check Resource Monitoring
    Should Be True    ${monitoring}

Resource Limit Is Exceeded
    [Documentation]    Simulate resource limit
    Trigger Resource Limit Exceeded

Agent Should Be Throttled
    [Documentation]    Verify throttling
    ${throttled}=    Check Agent Throttling
    Should Be True    ${throttled}

Warning Should Be Generated
    [Documentation]    Check warning generation
    ${warnings}=    Get Generated Warnings
    Should Not Be Empty    ${warnings}

Multiple Agents With Different Priorities
    [Documentation]    Setup priority testing
    Start Priority Test Agents

High Load Is Generated
    [Documentation]    Generate test load
    Generate High Load

High Priority Agents Should Get Resources
    [Documentation]    Verify priority handling
    ${allocation}=    Check Resource Allocation
    Verify Priority Resource Assignment    ${allocation}

Low Priority Agents Should Be Throttled
    [Documentation]    Verify low priority throttling
    ${throttled}=    Check Low Priority Throttling
    Should Be True    ${throttled}

Priority Changes Should Be Reflected
    [Documentation]    Verify priority updates
    Change Agent Priorities
    ${updated}=    Check Priority Updates
    Should Be True    ${updated}
