import streamlit as st
from config.models import (
    CoreSettings, SecuritySettings, SystemConfig,
    Environment, LogLevel, AuthMethod
)
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
import json

st.set_page_config(
    page_title="ADPA Framework",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'core_settings' not in st.session_state:
    st.session_state.core_settings = CoreSettings(
        environment=Environment.DEV,
        max_concurrent_ops=100,
        log_level=LogLevel.INFO,
        debug_mode=False,
        perf_monitoring=True,
        auto_scaling=True
    )

if 'security_settings' not in st.session_state:
    st.session_state.security_settings = SecuritySettings(
        admin_username="admin",
        admin_password="admin123",
        auth_method=AuthMethod.JWT,
        session_timeout=60,
        enable_2fa=False,
        ip_whitelist=False
    )

# Core Management Functions
def save_settings():
    settings_path = os.path.join("config", "settings.json")
    os.makedirs("config", exist_ok=True)
    
    settings = {
        "core": st.session_state.core_settings.dict(),
        "security": st.session_state.security_settings.dict()
    }
    
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=4)
    st.success("Settings saved successfully!")

def load_settings():
    settings_path = os.path.join("config", "settings.json")
    if os.path.exists(settings_path):
        with open(settings_path, "r") as f:
            settings = json.load(f)
            st.session_state.core_settings = CoreSettings(**settings["core"])
            st.session_state.security_settings = SecuritySettings(**settings["security"])
        st.success("Settings loaded successfully!")
    else:
        st.warning("No saved settings found. Using defaults.")

def restart_services():
    st.session_state.restart_requested = True
    st.success("Services restart initiated!")

def clear_cache():
    # Store current settings
    core_settings = st.session_state.core_settings
    security_settings = st.session_state.security_settings
    
    # Clear session state
    st.session_state.clear()
    
    # Restore settings
    st.session_state.core_settings = core_settings
    st.session_state.security_settings = security_settings
    
    st.success("Cache cleared successfully!")

# Main Layout
st.title("🤖 ADPA Framework")

# Core Management Buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("💾 Save Settings", use_container_width=True):
        save_settings()
with col2:
    if st.button("📂 Load Settings", use_container_width=True):
        load_settings()
with col3:
    if st.button("🔄 Restart Services", use_container_width=True):
        restart_services()
with col4:
    if st.button("🧹 Clear Cache", use_container_width=True):
        clear_cache()

# Main Tabs
tab1, tab2, tab3 = st.tabs([
    "System Overview",
    "Core Settings",
    "Security Settings"
])

with tab1:
    st.header("System Overview")
    
    # System Status
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("System Health", "98%", "↑ 2%")
    with col2:
        st.metric("Active Components", "12/12", "")
    with col3:
        st.metric("Response Time", "0.8s", "↓ 0.1s")
    with col4:
        st.metric("Error Rate", "0.2%", "↓ 0.1%")
    
    # System Metrics
    col1, col2 = st.columns(2)
    
    with col1:
        # Response Time Graph
        times = [datetime.now() - timedelta(minutes=i) for i in range(30)]
        response_times = [0.8 + (i % 5) * 0.1 for i in range(30)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=times,
            y=response_times,
            mode='lines',
            name='Response Time'
        ))
        fig.update_layout(title="System Response Time (Last 30 Minutes)")
        st.plotly_chart(fig)
    
    with col2:
        # Error Rate Graph
        error_rates = [0.2 + (i % 3) * 0.1 for i in range(30)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=times,
            y=error_rates,
            mode='lines',
            name='Error Rate'
        ))
        fig.update_layout(title="System Error Rate (Last 30 Minutes)")
        st.plotly_chart(fig)

with tab2:
    st.header("Core Settings")
    
    # Manual form creation for core settings
    st.selectbox("Environment", 
                 options=[e.value for e in Environment],
                 index=list(Environment).index(st.session_state.core_settings.environment),
                 key="core_environment")
    
    st.number_input("Max Concurrent Operations",
                    min_value=1,
                    max_value=1000,
                    value=st.session_state.core_settings.max_concurrent_ops,
                    key="core_max_ops")
    
    st.selectbox("Log Level",
                 options=[l.value for l in LogLevel],
                 index=list(LogLevel).index(st.session_state.core_settings.log_level),
                 key="core_log_level")
    
    st.toggle("Debug Mode",
              value=st.session_state.core_settings.debug_mode,
              key="core_debug")
    
    st.toggle("Performance Monitoring",
              value=st.session_state.core_settings.perf_monitoring,
              key="core_perf")
    
    st.toggle("Auto-scaling",
              value=st.session_state.core_settings.auto_scaling,
              key="core_scaling")
    
    if st.button("Update Core Settings"):
        st.session_state.core_settings = CoreSettings(
            environment=Environment(st.session_state.core_environment),
            max_concurrent_ops=st.session_state.core_max_ops,
            log_level=LogLevel(st.session_state.core_log_level),
            debug_mode=st.session_state.core_debug,
            perf_monitoring=st.session_state.core_perf,
            auto_scaling=st.session_state.core_scaling
        )
        st.success("Core settings updated successfully!")

with tab3:
    st.header("Security Settings")
    
    # Manual form creation for security settings
    st.text_input("Admin Username",
                  value=st.session_state.security_settings.admin_username,
                  key="sec_username")
    
    st.text_input("Admin Password",
                  value=st.session_state.security_settings.admin_password,
                  type="password",
                  key="sec_password")
    
    st.selectbox("Authentication Method",
                 options=[a.value for a in AuthMethod],
                 index=list(AuthMethod).index(st.session_state.security_settings.auth_method),
                 key="sec_auth")
    
    st.number_input("Session Timeout (minutes)",
                    min_value=5,
                    max_value=1440,
                    value=st.session_state.security_settings.session_timeout,
                    key="sec_timeout")
    
    st.toggle("Enable 2FA",
              value=st.session_state.security_settings.enable_2fa,
              key="sec_2fa")
    
    st.toggle("IP Whitelisting",
              value=st.session_state.security_settings.ip_whitelist,
              key="sec_whitelist")
    
    if st.button("Update Security Settings"):
        st.session_state.security_settings = SecuritySettings(
            admin_username=st.session_state.sec_username,
            admin_password=st.session_state.sec_password,
            auth_method=AuthMethod(st.session_state.sec_auth),
            session_timeout=st.session_state.sec_timeout,
            enable_2fa=st.session_state.sec_2fa,
            ip_whitelist=st.session_state.sec_whitelist
        )
        st.success("Security settings updated successfully!")

# Sidebar
with st.sidebar:
    st.header("Quick Navigation")
    
    st.subheader("Management")
    st.markdown("- [Agent Management](/Agent_Management)")
    st.markdown("- [Team Management](/Team_Management)")
    st.markdown("- [Knowledge Management](/Knowledge_Management)")
    st.markdown("- [LLM Management](/LLM_Management)")
    
    st.subheader("Configuration")
    st.markdown("- [Core Settings](#core-settings)")
    st.markdown("- [Security Settings](#security-settings)")
    
    st.subheader("Documentation")
    st.markdown("[Framework Documentation](https://docs.adpa.dev)")
    st.markdown("[API Reference](https://docs.adpa.dev/api)")
    st.markdown("[Best Practices](https://docs.adpa.dev/best-practices)")
    
    # Environment Info
    st.subheader("Environment")
    st.info(f"Mode: {st.session_state.core_settings.environment}")
    st.info(f"Debug: {'Enabled' if st.session_state.core_settings.debug_mode else 'Disabled'}")
