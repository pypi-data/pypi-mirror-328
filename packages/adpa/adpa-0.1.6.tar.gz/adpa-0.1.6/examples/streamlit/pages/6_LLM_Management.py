import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
import json
import os
from config.models import LLMProvider, CircuitBreaker, RetryPolicy, FailoverConfig

st.set_page_config(
    page_title="LLM Management",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state for LLM providers
if 'llm_providers' not in st.session_state:
    st.session_state.llm_providers = {
        "gpt-4": {
            "name": "gpt-4",
            "api_key": "sk-...",
            "base_url": "https://api.openai.com/v1",
            "organization_id": "org-...",
            "circuit_breaker": {
                "enabled": True,
                "failure_threshold": 5,
                "recovery_timeout": 60
            },
            "retry_policy": {
                "max_retries": 3,
                "backoff_factor": 1.5,
                "retry_delay": 1
            },
            "failover": {
                "enabled": True,
                "backup_providers": ["claude-2"],
                "failover_timeout": 30
            }
        },
        "claude-2": {
            "name": "claude-2",
            "api_key": "sk-...",
            "base_url": "https://api.anthropic.com/v1",
            "organization_id": None,
            "circuit_breaker": {
                "enabled": True,
                "failure_threshold": 3,
                "recovery_timeout": 30
            },
            "retry_policy": {
                "max_retries": 2,
                "backoff_factor": 2.0,
                "retry_delay": 2
            },
            "failover": {
                "enabled": True,
                "backup_providers": ["gpt-4"],
                "failover_timeout": 20
            }
        }
    }

# Add dark mode support
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

def save_llm_settings():
    settings_path = os.path.join("config", "llm_settings.json")
    os.makedirs("config", exist_ok=True)
    with open(settings_path, "w") as f:
        json.dump(st.session_state.llm_providers, f, indent=4)
    st.success("LLM settings saved successfully!")

def load_llm_settings():
    settings_path = os.path.join("config", "llm_settings.json")
    if os.path.exists(settings_path):
        with open(settings_path, "r") as f:
            st.session_state.llm_providers = json.load(f)
        st.success("LLM settings loaded successfully!")
    else:
        st.warning("No saved LLM settings found.")

# Main Layout
st.title("🤖 LLM Management")

# Core Management Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("💾 Save Settings", use_container_width=True):
        save_llm_settings()
with col2:
    if st.button("📂 Load Settings", use_container_width=True):
        load_llm_settings()

# Overview Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Active Models", "12", "↑ 2")
with col2:
    st.metric("Total Providers", "4", "↑ 1")
with col3:
    st.metric("Avg Response Time", "0.8s", "↓ 0.1s")
with col4:
    st.metric("Success Rate", "99.8%", "↑ 0.2%")

# Performance Graphs
col1, col2 = st.columns(2)

with col1:
    # Response Time Graph
    times = [datetime.now() - timedelta(minutes=i) for i in range(30)]
    response_times = {
        "gpt-4": [0.8 + (i % 5) * 0.1 for i in range(30)],
        "claude-2": [0.7 + (i % 4) * 0.15 for i in range(30)]
    }
    
    fig = go.Figure()
    for model, times_data in response_times.items():
        fig.add_trace(go.Scatter(
            x=times,
            y=times_data,
            mode='lines',
            name=model
        ))
    fig.update_layout(
        title="Response Time by Model (Last 30 Minutes)",
        xaxis_title="Time",
        yaxis_title="Response Time (s)"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Success Rate Graph
    success_rates = {
        "gpt-4": [99.8 - (i % 3) * 0.1 for i in range(30)],
        "claude-2": [99.9 - (i % 4) * 0.15 for i in range(30)]
    }
    
    fig = go.Figure()
    for model, rates in success_rates.items():
        fig.add_trace(go.Scatter(
            x=times,
            y=rates,
            mode='lines',
            name=model
        ))
    fig.update_layout(
        title="Success Rate by Model (Last 30 Minutes)",
        xaxis_title="Time",
        yaxis_title="Success Rate (%)"
    )
    st.plotly_chart(fig, use_container_width=True)

# Model Management
st.header("Model Management")

# Add New Model
with st.expander("➕ Add New Model"):
    new_model_name = st.text_input("Model Name", key="new_model_name")
    new_api_key = st.text_input("API Key", type="password", key="new_api_key")
    new_base_url = st.text_input("Base URL", key="new_base_url")
    new_org_id = st.text_input("Organization ID (Optional)", key="new_org_id")
    
    if st.button("Add Model"):
        if new_model_name and new_api_key and new_base_url:
            st.session_state.llm_providers[new_model_name] = {
                "name": new_model_name,
                "api_key": new_api_key,
                "base_url": new_base_url,
                "organization_id": new_org_id if new_org_id else None,
                "circuit_breaker": {
                    "enabled": True,
                    "failure_threshold": 5,
                    "recovery_timeout": 60
                },
                "retry_policy": {
                    "max_retries": 3,
                    "backoff_factor": 1.5,
                    "retry_delay": 1
                },
                "failover": {
                    "enabled": True,
                    "backup_providers": [],
                    "failover_timeout": 30
                }
            }
            st.success(f"Model {new_model_name} added successfully!")
        else:
            st.error("Please fill in all required fields.")

# Existing Models
for model_id, provider in st.session_state.llm_providers.items():
    with st.expander(f"⚙️ {model_id}"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Basic Configuration")
            name = st.text_input("Model Name", value=provider["name"], key=f"name_{model_id}_basic")
            api_key = st.text_input("API Key", value=provider["api_key"], type="password", key=f"api_{model_id}_basic")
            base_url = st.text_input("Base URL", value=provider["base_url"], key=f"url_{model_id}_basic")
            org_id = st.text_input("Organization ID", value=provider["organization_id"], key=f"org_{model_id}_basic")
        
        with col2:
            st.subheader("Advanced Configuration")
            
            # Circuit Breaker
            st.markdown("**Circuit Breaker**")
            cb_enabled = st.toggle("Enabled", value=provider["circuit_breaker"]["enabled"], key=f"cb_enabled_{model_id}")
            cb_threshold = st.number_input("Failure Threshold", 
                                         value=provider["circuit_breaker"]["failure_threshold"],
                                         min_value=1,
                                         max_value=100,
                                         key=f"cb_threshold_{model_id}")
            cb_timeout = st.number_input("Recovery Timeout (s)",
                                       value=provider["circuit_breaker"]["recovery_timeout"],
                                       min_value=1,
                                       max_value=3600,
                                       key=f"cb_timeout_{model_id}")
            
            # Retry Policy
            st.markdown("**Retry Policy**")
            retry_max = st.number_input("Max Retries",
                                      value=provider["retry_policy"]["max_retries"],
                                      min_value=0,
                                      max_value=10,
                                      key=f"retry_max_{model_id}")
            retry_factor = st.number_input("Backoff Factor",
                                         value=provider["retry_policy"]["backoff_factor"],
                                         min_value=1.0,
                                         max_value=10.0,
                                         key=f"retry_factor_{model_id}")
            retry_delay = st.number_input("Initial Delay (s)",
                                        value=provider["retry_policy"]["retry_delay"],
                                        min_value=1,
                                        max_value=60,
                                        key=f"retry_delay_{model_id}")
            
            # Failover Configuration
            st.markdown("**Failover Configuration**")
            failover_enabled = st.toggle("Enabled", value=provider["failover"]["enabled"], key=f"failover_enabled_{model_id}")
            other_models = [m for m in st.session_state.llm_providers.keys() if m != model_id]
            backup_providers = st.multiselect("Backup Providers",
                                            options=other_models,
                                            default=provider["failover"]["backup_providers"],
                                            key=f"backup_providers_{model_id}")
            failover_timeout = st.number_input("Failover Timeout (s)",
                                             value=provider["failover"]["failover_timeout"],
                                             min_value=1,
                                             max_value=300,
                                             key=f"failover_timeout_{model_id}")
        
        # Update Button
        if st.button("Update Model", key=f"update_{model_id}"):
            st.session_state.llm_providers[model_id] = {
                "name": name,
                "api_key": api_key,
                "base_url": base_url,
                "organization_id": org_id,
                "circuit_breaker": {
                    "enabled": cb_enabled,
                    "failure_threshold": cb_threshold,
                    "recovery_timeout": cb_timeout
                },
                "retry_policy": {
                    "max_retries": retry_max,
                    "backoff_factor": retry_factor,
                    "retry_delay": retry_delay
                },
                "failover": {
                    "enabled": failover_enabled,
                    "backup_providers": backup_providers,
                    "failover_timeout": failover_timeout
                }
            }
            st.success(f"Model {name} updated successfully!")
        
        # Delete Button
        if st.button("Delete Model", key=f"delete_{model_id}"):
            del st.session_state.llm_providers[model_id]
            st.warning(f"Model {model_id} deleted successfully!")
            st.rerun()

# Sidebar
with st.sidebar:
    st.header("Quick Links")
    st.markdown("- [Add New Model](#add-new-model)")
    st.markdown("- [Model Management](#model-management)")
    
    # Theme Toggle
    if st.toggle("🌙 Dark Mode", value=st.session_state.theme == 'dark', key="theme_toggle"):
        st.session_state.theme = 'dark'
    else:
        st.session_state.theme = 'light'

    # Documentation & Help
    with st.expander("📚 Documentation"):
        st.markdown("""
        ### Quick Start
        1. Add your LLM provider
        2. Configure API keys
        3. Set up failover rules
        
        ### Tutorials
        - [Basic Setup](https://docs.adpa.dev/tutorials/basic-setup)
        - [Advanced Configuration](https://docs.adpa.dev/tutorials/advanced-config)
        - [Security Best Practices](https://docs.adpa.dev/tutorials/security)
        """)
    
    with st.expander("❓ Help"):
        st.markdown("""
        ### Common Issues
        - API key not working? Check the provider status
        - High latency? Adjust the circuit breaker settings
        - Errors? View the logs for details
        
        ### Support
        - [Report an Issue](https://github.com/your-repo/issues)
        - [Documentation](https://docs.adpa.dev)
        - [Community Forum](https://community.adpa.dev)
        """)

    # Batch Operations
    with st.expander("🔄 Batch Operations"):
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Enable All Models"):
                for model_id in st.session_state.llm_providers:
                    st.session_state.llm_providers[model_id]["circuit_breaker"]["enabled"] = True
                st.success("All models enabled!")
        
        with col2:
            if st.button("Disable All Models"):
                for model_id in st.session_state.llm_providers:
                    st.session_state.llm_providers[model_id]["circuit_breaker"]["enabled"] = False
                st.success("All models disabled!")
        
        with col3:
            if st.button("Reset All Settings"):
                for model_id in st.session_state.llm_providers:
                    st.session_state.llm_providers[model_id]["circuit_breaker"] = {
                        "enabled": True,
                        "failure_threshold": 5,
                        "recovery_timeout": 60
                    }
                st.success("All settings reset to defaults!")

    # Knowledge Management
    with st.expander("📚 Knowledge Management"):
        st.subheader("Document Context")
        col1, col2 = st.columns(2)
        
        with col1:
            st.number_input("Max Context Length", 
                           value=4096,
                           min_value=512,
                           max_value=128000,
                           step=512,
                           key="context_length")
            
            st.multiselect("Supported Document Types",
                          ["PDF", "TXT", "DOCX", "MD", "CODE"],
                          default=["PDF", "TXT"],
                          key="doc_types")
        
        with col2:
            st.selectbox("Embedding Model",
                        ["text-embedding-3-small", "text-embedding-3-large"],
                        key="embedding_model")
            
            st.number_input("Chunk Size",
                           value=512,
                           min_value=128,
                           max_value=2048,
                           step=128,
                           key="chunk_size")

    # Cost Optimization
    with st.expander("💰 Cost Optimization"):
        st.subheader("Cost Management")
        col1, col2 = st.columns(2)
        
        with col1:
            st.number_input("Monthly Budget ($)",
                           value=100,
                           min_value=0,
                           max_value=10000,
                           step=50,
                           key="monthly_budget")
            
            st.number_input("Alert Threshold (%)",
                           value=80,
                           min_value=50,
                           max_value=100,
                           step=5,
                           key="alert_threshold")
        
        with col2:
            st.multiselect("Cost Optimization Rules",
                          ["Use Cheaper Models First",
                           "Automatic Scaling",
                           "Cache Responses",
                           "Token Optimization"],
                          default=["Use Cheaper Models First"],
                          key="cost_rules")
            
            st.toggle("Enable Cost Alerts",
                     value=True,
                     key="cost_alerts")

    # Security Settings
    with st.expander("🔒 Security Settings"):
        st.subheader("Security Configuration")
        col1, col2 = st.columns(2)
        
        with col1:
            st.toggle("Enable API Key Encryption",
                     value=True,
                     key="api_encryption")
            
            st.toggle("Enable Request Logging",
                     value=True,
                     key="request_logging")
            
            st.number_input("Session Timeout (minutes)",
                           value=60,
                           min_value=5,
                           max_value=1440,
                           step=5,
                           key="session_timeout")
        
        with col2:
            st.text_area("IP Whitelist",
                        placeholder="Enter IPs, one per line",
                        key="ip_whitelist")
            
            st.number_input("Rate Limit (requests/minute)",
                           value=60,
                           min_value=1,
                           max_value=1000,
                           step=10,
                           key="rate_limit")

    # Keyboard Shortcuts
    with st.expander("⌨️ Keyboard Shortcuts"):
        st.markdown("""
        ### Available Shortcuts
        - `Ctrl + S`: Save Settings
        - `Ctrl + L`: Load Settings
        - `Ctrl + R`: Refresh Page
        - `Ctrl + D`: Toggle Dark Mode
        - `Ctrl + H`: Show Help
        - `Esc`: Close Popups
        """)

    st.header("Statistics")
    st.info(f"Total Models: {len(st.session_state.llm_providers)}")
    st.info(f"Active Models: {len([p for p in st.session_state.llm_providers.values() if p['circuit_breaker']['enabled']])}")
