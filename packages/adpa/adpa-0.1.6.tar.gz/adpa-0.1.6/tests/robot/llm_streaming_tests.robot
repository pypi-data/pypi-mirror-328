*** Settings ***
Documentation     Test suite for LLM streaming functionality
Resource          keywords/llm_keywords.robot
Resource          keywords/validation_keywords.robot
Resource          keywords/streaming_keywords.robot

Suite Setup       Initialize Test Environment
Suite Teardown    Cleanup Test Environment

*** Test Cases ***
Test OpenAI Streaming Generation
    [Documentation]    Test streaming text generation with OpenAI
    [Tags]    streaming    openai
    ${prompt}=    Get Test Prompt    openai    streaming
    ${stream}=    Start Stream Generation    openai    ${prompt}
    ${chunks}=    Collect Stream Chunks    ${stream}
    Validate Stream Result    ${chunks}

Test Gemini Streaming Generation
    [Documentation]    Test streaming text generation with Gemini
    [Tags]    streaming    gemini
    ${prompt}=    Get Test Prompt    gemini    streaming
    ${stream}=    Start Stream Generation    gemini    ${prompt}
    ${chunks}=    Collect Stream Chunks    ${stream}
    Validate Stream Result    ${chunks}

Test Stream Interruption
    [Documentation]    Test interrupting a streaming response
    [Tags]    streaming    interrupt
    ${prompt}=    Get Test Prompt    openai    long_streaming
    ${stream}=    Start Stream Generation    openai    ${prompt}
    Sleep    1s
    Interrupt Stream    ${stream}
    Verify Stream Interrupted    ${stream}

Test Stream Error Recovery
    [Documentation]    Test recovery from streaming errors
    [Tags]    streaming    error
    ${prompt}=    Get Test Prompt    openai    streaming
    Simulate Network Instability
    ${stream}=    Start Stream Generation With Retry    openai    ${prompt}
    ${chunks}=    Collect Stream Chunks    ${stream}
    Validate Stream Result    ${chunks}
    Reset Network

Test Parallel Streaming
    [Documentation]    Test multiple parallel streams
    [Tags]    streaming    parallel
    ${streams}=    Start Multiple Streams    3
    ${results}=    Wait For All Streams    ${streams}
    Validate Multiple Stream Results    ${results}

Test Stream Token Counting
    [Documentation]    Test token counting in streams
    [Tags]    streaming    tokens
    ${prompt}=    Get Test Prompt    openai    streaming
    ${stream}=    Start Stream Generation    openai    ${prompt}
    ${chunks}=    Collect Stream Chunks With Tokens    ${stream}
    Validate Stream Token Count    ${chunks}

Test Stream Format Consistency
    [Documentation]    Test consistency of streamed content format
    [Tags]    streaming    format
    ${prompt}=    Get Test Prompt    openai    streaming_format
    ${stream}=    Start Stream Generation    openai    ${prompt}
    ${chunks}=    Collect And Validate Format    ${stream}
    Verify Format Consistency    ${chunks}

Test Stream Performance
    [Documentation]    Test streaming performance metrics
    [Tags]    streaming    performance
    ${prompt}=    Get Test Prompt    openai    streaming
    ${metrics}=    Measure Stream Performance    openai    ${prompt}
    Validate Performance Metrics    ${metrics}

Test Stream Memory Usage
    [Documentation]    Test memory usage during streaming
    [Tags]    streaming    memory
    ${prompt}=    Get Test Prompt    openai    long_streaming
    ${usage}=    Monitor Memory During Stream    openai    ${prompt}
    Validate Memory Usage    ${usage}

Test Stream Cancellation Cleanup
    [Documentation]    Test resource cleanup after stream cancellation
    [Tags]    streaming    cleanup
    ${prompt}=    Get Test Prompt    openai    streaming
    ${stream}=    Start Stream Generation    openai    ${prompt}
    Cancel Stream    ${stream}
    Verify Resource Cleanup    ${stream}
