import streamlit as st
import yaml
import json
from pathlib import Path

st.set_page_config(
    page_title="Configuration - ADPA Framework",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Configuration Manager")

# Configuration Overview
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Active Providers", "4", "↑ 1")
with col2:
    st.metric("Environment", "Production", None)
with col3:
    st.metric("Config Version", "1.1.0", None)
with col4:
    st.metric("Last Updated", "10 mins ago", None)

# Main Content
tab1, tab2, tab3, tab4 = st.tabs([
    "Global Settings",
    "Provider Config",
    "Environment Variables",
    "System Preferences"
])

with tab1:
    st.header("Global Settings")
    
    # System Settings
    st.subheader("System Settings")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Default Timeout (s)", 1, 300, 60)
        st.number_input("Max Retries", 0, 10, 3)
        st.number_input("Batch Size", 1, 1000, 100)
    with col2:
        st.selectbox(
            "Log Level",
            ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        )
        st.text_input("Log Directory", "./logs")
        st.checkbox("Enable Debug Mode", False)
    
    # Cache Settings
    st.subheader("Cache Settings")
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Enable Cache", True)
        st.number_input("Cache TTL (s)", 0, 86400, 3600)
    with col2:
        st.text_input("Cache Directory", "./cache")
        st.number_input("Max Cache Size (MB)", 1, 10000, 1000)

with tab2:
    st.header("Provider Configuration")
    
    # Provider Selection
    provider = st.selectbox(
        "Select Provider",
        ["OpenAI", "Google Gemini", "Groq", "Anthropic"]
    )
    
    # Provider Settings
    st.subheader(f"{provider} Settings")
    
    # API Configuration
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("API Key", type="password")
        st.text_input("Organization ID", type="password")
    with col2:
        st.text_input("Base URL")
        st.selectbox("API Version", ["v1", "v2"])
    
    # Model Configuration
    st.subheader("Model Configuration")
    models_config = {
        'OpenAI': {
            'Default Model': 'gpt-4',
            'Available Models': ['gpt-4', 'gpt-3.5-turbo'],
            'Max Tokens': 4096,
            'Temperature': 0.7
        },
        'Google Gemini': {
            'Default Model': 'gemini-pro',
            'Available Models': ['gemini-pro'],
            'Max Tokens': 8192,
            'Temperature': 0.8
        }
    }
    
    if provider in models_config:
        config = models_config[provider]
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Default Model", config['Available Models'])
            st.multiselect("Available Models", config['Available Models'],
                          default=config['Available Models'])
        with col2:
            st.number_input("Max Tokens", 1, 32768, config['Max Tokens'])
            st.slider("Temperature", 0.0, 1.0, config['Temperature'])

with tab3:
    st.header("Environment Variables")
    
    # Environment Selection
    env = st.selectbox(
        "Environment",
        ["Development", "Staging", "Production"]
    )
    
    # Environment Variables
    st.subheader(f"{env} Environment Variables")
    
    # Sample env vars
    env_vars = {
        'ADPA_ENV': env.upper(),
        'ADPA_DEBUG': 'true',
        'ADPA_LOG_LEVEL': 'INFO',
        'ADPA_CACHE_DIR': './cache',
        'ADPA_API_TIMEOUT': '60'
    }
    
    # Display and edit env vars
    new_vars = {}
    for key, value in env_vars.items():
        col1, col2, col3 = st.columns([2,3,1])
        with col1:
            st.text(key)
        with col2:
            new_vars[key] = st.text_input(f"Value for {key}", value, label_visibility="collapsed")
        with col3:
            if st.button("🗑️", key=f"delete_{key}"):
                st.write("Variable will be deleted")
    
    # Add new variable
    st.subheader("Add New Variable")
    col1, col2, col3 = st.columns([2,3,1])
    with col1:
        new_key = st.text_input("Variable Name")
    with col2:
        new_value = st.text_input("Variable Value")
    with col3:
        if st.button("Add"):
            st.success(f"Added {new_key}={new_value}")

with tab4:
    st.header("System Preferences")
    
    # Failover Settings
    st.subheader("Failover Settings")
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Enable Auto-Failover", True)
        st.number_input("Failover Threshold", 1, 10, 3)
    with col2:
        st.multiselect(
            "Backup Providers",
            ["OpenAI", "Google Gemini", "Groq", "Anthropic"],
            ["Google Gemini", "Groq"]
        )
        st.selectbox("Failover Strategy", ["Round Robin", "Priority Based"])
    
    # Performance Settings
    st.subheader("Performance Settings")
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Enable Performance Monitoring", True)
        st.number_input("Monitoring Interval (s)", 1, 3600, 60)
    with col2:
        st.number_input("Performance Alert Threshold (ms)", 100, 10000, 1000)
        st.selectbox("Performance Profile", ["Balanced", "High Performance", "Economy"])
    
    # Security Settings
    st.subheader("Security Settings")
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Enable Rate Limiting", True)
        st.number_input("Rate Limit (requests/min)", 1, 1000, 60)
    with col2:
        st.checkbox("Enable IP Filtering", False)
        st.text_area("Allowed IPs", "127.0.0.1\n192.168.1.0/24")

# Sidebar
with st.sidebar:
    st.header("Quick Actions")
    
    # Configuration File
    st.subheader("Configuration File")
    config_format = st.selectbox(
        "Format",
        ["YAML", "JSON"]
    )
    
    if st.button("Export Configuration"):
        st.success("Configuration exported!")
        
    if st.button("Import Configuration"):
        st.info("Select configuration file to import")
    
    # Backup & Restore
    st.subheader("Backup & Restore")
    if st.button("Create Backup"):
        st.success("Backup created!")
        
    if st.button("Restore Configuration"):
        st.warning("Select backup to restore")
    
    # Reset Options
    st.subheader("Reset Options")
    if st.button("Reset to Defaults"):
        st.error("Are you sure you want to reset?")
        
    # Documentation
    st.subheader("Documentation")
    st.markdown("[View Configuration Guide](https://docs.adpa.dev/config)")
    st.markdown("[View Best Practices](https://docs.adpa.dev/best-practices)")
