*** Settings ***
Documentation     Integration test suite for LLM functionality
Resource          keywords/llm_keywords.robot
Resource          keywords/validation_keywords.robot
Resource          keywords/integration_keywords.robot

Suite Setup       Initialize Integration Test Environment
Suite Teardown    Cleanup Integration Test Environment

*** Test Cases ***
Test Multi-Provider Chain
    [Documentation]    Test chaining multiple LLM providers
    [Tags]    integration    chain
    ${prompt}=    Get Test Prompt    chain    simple
    ${result}=    Execute Provider Chain    ${prompt}
    Validate Chain Result    ${result}
    Verify Provider Order    ${result}

Test Fallback Chain
    [Documentation]    Test fallback between providers
    [Tags]    integration    fallback
    ${prompt}=    Get Test Prompt    chain    fallback
    Simulate Primary Provider Failure
    ${result}=    Execute Fallback Chain    ${prompt}
    Verify Fallback Execution    ${result}
    Reset Provider Status

Test Load Balancing
    [Documentation]    Test load balancing across providers
    [Tags]    integration    load_balance
    ${requests}=    Generate Test Requests    100
    ${results}=    Execute Load Balanced Requests    ${requests}
    Verify Load Distribution    ${results}
    Validate Response Times    ${results}

Test Provider Switching
    [Documentation]    Test dynamic provider switching
    [Tags]    integration    switch
    ${conditions}=    Get Switch Conditions
    FOR    ${condition}    IN    @{conditions}
        ${result}=    Test Provider Switch    ${condition}
        Verify Provider Selection    ${result}    ${condition}
    END

Test Cross-Provider Consistency
    [Documentation]    Test response consistency across providers
    [Tags]    integration    consistency
    ${prompt}=    Get Test Prompt    consistency    check
    ${results}=    Get All Provider Responses    ${prompt}
    Verify Response Consistency    ${results}
    Measure Response Variance    ${results}

Test Provider Capabilities
    [Documentation]    Test provider-specific capabilities
    [Tags]    integration    capabilities
    ${capabilities}=    Get Provider Capabilities
    FOR    ${provider}    IN    @{capabilities}
        Verify Provider Features    ${provider}
        Test Provider Limits    ${provider}
    END

Test Error Propagation
    [Documentation]    Test error handling across providers
    [Tags]    integration    errors
    ${error_cases}=    Get Error Test Cases
    FOR    ${case}    IN    @{error_cases}
        ${result}=    Test Error Handling    ${case}
        Verify Error Propagation    ${result}
    END

Test Provider Metrics
    [Documentation]    Test metric collection across providers
    [Tags]    integration    metrics
    Start Metric Collection
    ${workload}=    Execute Test Workload
    ${metrics}=    Collect Provider Metrics
    Validate Metric Accuracy    ${metrics}
    Compare Provider Performance    ${metrics}

Test Token Management
    [Documentation]    Test token management across providers
    [Tags]    integration    tokens
    ${scenarios}=    Get Token Test Scenarios
    FOR    ${scenario}    IN    @{scenarios}
        ${usage}=    Measure Token Usage    ${scenario}
        Verify Token Accounting    ${usage}
    END

Test Provider Cost Optimization
    [Documentation]    Test cost optimization strategies
    [Tags]    integration    cost
    ${budget}=    Set Test Budget
    ${requests}=    Generate Cost Test Requests
    ${results}=    Execute Cost Optimized Requests    ${requests}    ${budget}
    Verify Cost Efficiency    ${results}    ${budget}

Test Cache Synchronization
    [Documentation]    Test cache sync across providers
    [Tags]    integration    cache
    ${data}=    Generate Cache Test Data
    Populate Provider Caches    ${data}
    Verify Cache Consistency
    Test Cache Invalidation
    Verify Cache Updates

Test Request Routing
    [Documentation]    Test intelligent request routing
    [Tags]    integration    routing
    ${requests}=    Generate Mixed Requests
    ${routes}=    Calculate Optimal Routes    ${requests}
    ${results}=    Execute Routed Requests    ${requests}    ${routes}
    Verify Routing Efficiency    ${results}

Test Provider Analytics
    [Documentation]    Test analytics across providers
    [Tags]    integration    analytics
    Start Analytics Collection
    ${workload}=    Execute Analytics Workload
    ${data}=    Collect Provider Analytics
    Validate Analytics Data    ${data}
    Generate Analytics Report    ${data}

Test Provider Monitoring
    [Documentation]    Test monitoring integration
    [Tags]    integration    monitoring
    Enable Provider Monitoring
    ${scenarios}=    Get Monitoring Scenarios
    FOR    ${scenario}    IN    @{scenarios}
        ${metrics}=    Execute Monitored Scenario    ${scenario}
        Verify Monitoring Accuracy    ${metrics}
    END

Test Cross-Provider Security
    [Documentation]    Test security across providers
    [Tags]    integration    security
    ${tests}=    Get Security Test Suite
    FOR    ${test}    IN    @{tests}
        ${result}=    Execute Security Test    ${test}
        Verify Security Compliance    ${result}
    END
