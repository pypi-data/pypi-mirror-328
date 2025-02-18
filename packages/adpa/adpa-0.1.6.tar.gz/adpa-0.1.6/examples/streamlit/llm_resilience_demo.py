"""Streamlit demo for LLM resilience features."""
import streamlit as st
import asyncio
import random
import time
import os
from dotenv import load_dotenv
from adpa.llms.base import LLMConfig
from adpa.llms.openai.client import OpenAIProvider
from adpa.llms.gemini.client import GeminiProvider
from adpa.llms.groq.client import GroqProvider
from adpa.llms.resilience.failover import FailoverManager
from adpa.llms.errors.resilience import FailoverError, NetworkResilienceError, RateLimitError

# Load environment variables
load_dotenv()

# Initialize providers
def init_providers():
    """Initialize LLM providers."""
    providers = {}
    
    # OpenAI
    if os.getenv("OPENAI_API_KEY"):
        providers["openai"] = OpenAIProvider(LLMConfig(
            api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=1000,
            timeout=30.0
        ))
    
    # Gemini
    if os.getenv("GEMINI_API_KEY"):
        providers["gemini"] = GeminiProvider(LLMConfig(
            api_key=os.getenv("GEMINI_API_KEY"),
            model="gemini-pro",
            temperature=0.7,
            max_tokens=1000,
            timeout=30.0
        ))
    
    # Groq
    if os.getenv("GROQ_API_KEY"):
        providers["groq"] = GroqProvider(LLMConfig(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768",
            temperature=0.7,
            max_tokens=1000,
            timeout=30.0
        ))
    
    return providers

# Initialize providers
providers = init_providers()

# Sidebar configuration
st.sidebar.title("Configuration")

# Provider selection
available_providers = list(providers.keys())
if not available_providers:
    st.error("No providers configured. Please set API keys in .env file.")
    st.stop()

primary_provider = st.sidebar.selectbox(
    "Primary Provider",
    available_providers,
    index=0
)

secondary_providers = st.sidebar.multiselect(
    "Secondary Providers",
    [p for p in available_providers if p != primary_provider],
    default=[p for p in available_providers if p != primary_provider]
)

# Resilience settings
st.sidebar.subheader("Resilience Settings")
max_retries = st.sidebar.slider("Max Retries", 1, 10, 3)
timeout = st.sidebar.slider("Timeout (seconds)", 1, 60, 30)
failure_threshold = st.sidebar.slider("Failure Threshold", 1, 10, 3)

# Initialize managers
def init_managers():
    """Initialize failover manager."""
    failover_manager = FailoverManager(
        primary_provider=providers[primary_provider],
        secondary_providers=[providers[p] for p in secondary_providers],
        max_retries=max_retries
    )
    return failover_manager

failover_manager = init_managers()

# Main content
st.title("LLM Resilience Demo")
st.markdown("""
This demo shows how the ADPA framework handles LLM provider resilience:
- Provider Failover
- Error Handling
- Circuit Breaking
""")

# Create tabs
tab1, tab2, tab3 = st.tabs([
    "Provider Failover",
    "Circuit Breaking",
    "Error Simulation"
])

# Provider Failover Demo
with tab1:
    st.header("Provider Failover Demo")
    
    # Input
    prompt = st.text_area(
        "Enter your prompt",
        value="What is the capital of France?",
        key="failover_prompt"
    )
    
    # Display current provider status
    st.sidebar.subheader("Provider Status")
    for provider in [primary_provider] + secondary_providers:
        status_color = "🟢" if provider not in failover_manager._failed_providers else "🔴"
        st.sidebar.text(f"{status_color} {provider}")
    
    # Failover simulation
    if st.button("Test Failover", key="failover_button"):
        progress = st.progress(0)
        status = st.empty()
        results = st.container()
        
        try:
            # Reset failed providers
            failover_manager.reset()
            available_providers = [primary_provider] + secondary_providers
            
            # Simulate request with failover
            for i in range(max_retries):
                progress.progress((i + 1) / max_retries)
                current_provider = failover_manager._current_provider
                
                # Update status
                status.info(f"Attempt {i+1}/{max_retries}: Trying provider '{current_provider}'")
                
                try:
                    # Real provider call
                    response = asyncio.run(current_provider.chat(
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7,
                        max_tokens=1000,
                        timeout=timeout
                    ))
                    
                    # Success case
                    status.success(
                        f"✅ Request succeeded with provider '{current_provider}' "
                        f"on attempt {i+1}/{max_retries}"
                    )
                    
                    # Show detailed results
                    with results:
                        st.json({
                            "success": True,
                            "provider": current_provider,
                            "prompt": prompt,
                            "response": response["text"],
                            "metadata": {
                                "total_attempts": i + 1,
                                "failed_providers": list(failover_manager._failed_providers),
                                "remaining_providers": list(
                                    set(available_providers) - failover_manager._failed_providers
                                ),
                                "retry_count": i,
                                "final_provider": current_provider,
                                "usage": response["usage"]
                            }
                        })
                    break
                    
                except (NetworkResilienceError, RateLimitError) as e:
                    # Handle provider failure
                    failover_manager._failed_providers.add(current_provider)
                    
                    # Update status
                    status.warning(
                        f"Provider '{current_provider}' failed: {str(e)}. "
                        f"({len(failover_manager._failed_providers)}/{len(available_providers)} providers failed)"
                    )
                    
                    # Try next provider
                    success = asyncio.run(failover_manager._select_next_provider())
                    if not success:
                        remaining = set(available_providers) - failover_manager._failed_providers
                        raise FailoverError(
                            message=f"All providers failed after {i+1} attempts",
                            failed_provider=current_provider,
                            failover_target=next(iter(remaining)) if remaining else None,
                            failure_reason=f"All {len(available_providers)} providers exhausted"
                        )
                    continue
                
        except FailoverError as e:
            # Show detailed error
            status.error(
                f"❌ Failover Error: {str(e)}\n\n"
                f"All {len(available_providers)} providers failed to respond"
            )
            
            # Show error details
            with results:
                st.json({
                    "success": False,
                    "error": str(e),
                    "details": {
                        "failed_provider": e.details["failed_provider"],
                        "failover_target": e.details["failover_target"],
                        "failure_reason": e.details["failure_reason"],
                        "failover_attempted": True,
                        "resilience_type": "failover"
                    },
                    "failed_providers": list(failover_manager._failed_providers),
                    "metadata": {
                        "total_attempts": i + 1,
                        "available_providers": available_providers,
                        "success_rate": 0,
                        "last_provider": current_provider
                    }
                })
        
        finally:
            # Reset for next attempt
            failover_manager.reset()
            
            # Update final provider status
            for provider in available_providers:
                status_color = "🟢" if provider not in failover_manager._failed_providers else "🔴"
                st.sidebar.text(f"{status_color} {provider}")

# Circuit Breaking Demo
with tab2:
    st.header("Circuit Breaking Demo")
    
    # Initialize circuit breaker
    breaker = failover_manager.circuit_breaker
    
    # Display current state
    st.metric(
        "Circuit State",
        breaker.state.value,
        delta=None,
        delta_color="normal"
    )
    
    # Circuit breaker simulation
    if st.button("Test Circuit Breaker", key="breaker_button"):
        progress = st.progress(0)
        status = st.empty()
        
        for i in range(10):  # 10 test requests
            progress.progress((i + 1) / 10)
            
            try:
                # Simulate operation
                async def operation(request):
                    if random.random() < 0.6:  # 60% failure rate
                        raise Exception("Simulated failure")
                    return {"status": "success"}
                
                # Execute with circuit breaker
                result = asyncio.run(
                    breaker.execute({"test": "request"}, operation)
                )
                
                status.success(f"Request {i+1} succeeded")
                time.sleep(0.5)
                
            except FailoverError as e:
                status.error(f"Request {i+1} failed: Circuit is {breaker.state.value}")
                time.sleep(0.5)
            
            # Update state metric
            st.metric(
                "Circuit State",
                breaker.state.value,
                delta=None,
                delta_color="normal"
            )
            
        # Show final stats
        st.json({
            "final_state": breaker.state.value,
            "failure_count": breaker.failure_count,
            "success_count": breaker.success_count
        })

# Error Simulation
with tab3:
    st.header("Error Simulation")
    
    # Error type selection
    error_type = st.selectbox(
        "Select Error Type",
        ["Network Error", "Rate Limit Error", "Resource Error"]
    )
    
    # Error simulation
    if st.button("Simulate Error", key="error_button"):
        status = st.empty()
        
        if error_type == "Network Error":
            error = NetworkResilienceError(
                message="Network connection failed",
                network_condition="high_latency",
                retry_count=2,
                latency=5000.0
            )
        elif error_type == "Rate Limit Error":
            error = RateLimitError(
                message="Rate limit exceeded",
                limit_type="requests_per_minute",
                current_rate=120.0,
                limit=100.0
            )
        else:
            error = ResourceExhaustionError(
                message="Memory limit exceeded",
                resource_type="memory",
                current_usage=95.0,
                threshold=90.0
            )
        
        # Display error details
        status.error(f"Error: {str(error)}")
        st.json(error.details)

# Footer
st.markdown("---")
st.markdown("""
### Resources
- [Documentation](https://github.com/yourusername/adpa-framework)
- [Source Code](https://github.com/yourusername/adpa-framework)
""")
