import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Security Dashboard - ADPA Framework",
    page_icon="🔒",
    layout="wide"
)

st.title("🔒 Security Dashboard")

# Security Overview
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Security Score", "92/100", "↑ 3")
with col2:
    st.metric("Active Threats", "0", "↓ 2")
with col3:
    st.metric("Failed Attempts", "12", "↓ 5")
with col4:
    st.metric("Avg Response", "1.2s", "↓ 0.3s")

# Main Content
tab1, tab2, tab3 = st.tabs([
    "Security Monitoring",
    "Access Control",
    "Audit Logs"
])

with tab1:
    st.header("Security Monitoring")
    
    # Threat Detection
    st.subheader("Threat Detection")
    
    # Sample threat data
    threat_data = {
        'Category': [
            'Prompt Injection',
            'Data Leakage',
            'Rate Limiting',
            'Authentication',
            'API Abuse'
        ],
        'Attempts': [45, 32, 78, 23, 56],
        'Blocked': [45, 30, 78, 23, 54],
        'Success Rate': [100, 93.8, 100, 100, 96.4]
    }
    df_threats = pd.DataFrame(threat_data)
    
    # Create threat visualization
    fig = go.Figure(data=[
        go.Bar(name='Attempts', x=df_threats['Category'], y=df_threats['Attempts']),
        go.Bar(name='Blocked', x=df_threats['Category'], y=df_threats['Blocked'])
    ])
    fig.update_layout(
        title="Security Incidents by Category",
        barmode='group'
    )
    st.plotly_chart(fig)
    
    # Real-time Monitoring
    st.subheader("Real-time Monitoring")
    
    # Sample monitoring data
    timestamps = [datetime.now() - timedelta(minutes=i) for i in range(60)]
    requests = [100 + i % 20 for i in range(60)]
    blocked = [2 + i % 3 for i in range(60)]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=timestamps,
        y=requests,
        mode='lines',
        name='Total Requests'
    ))
    fig.add_trace(go.Scatter(
        x=timestamps,
        y=blocked,
        mode='lines',
        name='Blocked Requests'
    ))
    fig.update_layout(title="Request Monitoring")
    st.plotly_chart(fig)

with tab2:
    st.header("Access Control")
    
    # API Key Management
    st.subheader("API Key Management")
    api_keys = {
        'Key ID': ['key_1', 'key_2', 'key_3', 'key_4'],
        'Owner': ['John Doe', 'Jane Smith', 'Bob Wilson', 'Alice Brown'],
        'Status': ['Active', 'Active', 'Revoked', 'Active'],
        'Created': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-01-15'],
        'Last Used': ['2024-01-16', '2024-01-16', '2024-01-12', '2024-01-16']
    }
    df_keys = pd.DataFrame(api_keys)
    
    for idx, row in df_keys.iterrows():
        col1, col2, col3, col4, col5 = st.columns([2,2,1,2,2])
        with col1:
            st.write(f"**{row['Key ID']}**")
        with col2:
            st.write(row['Owner'])
        with col3:
            status_color = "🟢" if row['Status'] == 'Active' else "🔴"
            st.write(f"{status_color} {row['Status']}")
        with col4:
            st.write(f"Created: {row['Created']}")
        with col5:
            st.write(f"Last Used: {row['Last Used']}")
    
    # Rate Limiting
    st.subheader("Rate Limiting")
    rate_limits = {
        'Tier': ['Free', 'Basic', 'Pro', 'Enterprise'],
        'RPM': [60, 300, 1500, 5000],
        'TPM': [40000, 200000, 1000000, 'Unlimited'],
        'Current Usage': [45, 280, 1200, 3500]
    }
    df_limits = pd.DataFrame(rate_limits)
    
    for idx, row in df_limits.iterrows():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(f"**{row['Tier']}**")
        with col2:
            st.write(f"RPM: {row['RPM']}")
        with col3:
            st.write(f"TPM: {row['TPM']}")
        with col4:
            usage_pct = (row['Current Usage'] / row['RPM'] * 100) if isinstance(row['RPM'], (int, float)) else 0
            st.progress(min(usage_pct / 100, 1.0))

with tab3:
    st.header("Audit Logs")
    
    # Audit Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        event_type = st.selectbox(
            "Event Type",
            ["All", "Authentication", "API Call", "Rate Limit", "Error"]
        )
    with col2:
        severity = st.selectbox(
            "Severity",
            ["All", "Low", "Medium", "High", "Critical"]
        )
    with col3:
        timeframe = st.selectbox(
            "Timeframe",
            ["Last Hour", "Last 24 Hours", "Last 7 Days", "Last 30 Days"]
        )
    
    # Sample audit logs
    audit_logs = {
        'Timestamp': [datetime.now() - timedelta(minutes=i) for i in range(10)],
        'Event': [
            "Failed authentication attempt",
            "Rate limit exceeded",
            "API key created",
            "Prompt injection blocked",
            "Data access attempt",
            "API key revoked",
            "New IP address detected",
            "Successful authentication",
            "Configuration changed",
            "Security alert triggered"
        ],
        'Severity': [
            "High", "Medium", "Low", "High",
            "Medium", "Medium", "Low", "Low",
            "Medium", "High"
        ],
        'Details': [
            "IP: 192.168.1.100",
            "User: john_doe",
            "Admin action",
            "Pattern detected",
            "Unauthorized access",
            "Admin action",
            "IP: 192.168.1.101",
            "User: jane_smith",
            "Rate limits updated",
            "Multiple failures"
        ]
    }
    df_logs = pd.DataFrame(audit_logs)
    
    # Display logs
    for idx, row in df_logs.iterrows():
        col1, col2, col3 = st.columns([1,2,4])
        with col1:
            st.write(row['Timestamp'].strftime('%H:%M:%S'))
        with col2:
            severity_color = {
                "Low": "🟢",
                "Medium": "🟡",
                "High": "🔴",
                "Critical": "⚫"
            }
            st.write(f"{severity_color[row['Severity']]} {row['Event']}")
        with col3:
            st.write(f"_{row['Details']}_")

# Sidebar
with st.sidebar:
    st.header("Security Controls")
    
    # Security Settings
    st.subheader("Security Settings")
    st.toggle("Enable Rate Limiting", value=True)
    st.toggle("Prompt Injection Protection", value=True)
    st.toggle("Data Leak Prevention", value=True)
    st.toggle("IP Filtering", value=True)
    
    # Alert Configuration
    st.subheader("Alert Configuration")
    alert_channels = st.multiselect(
        "Alert Channels",
        ["Email", "Slack", "SMS", "Webhook"],
        ["Email", "Slack"]
    )
    
    # Alert Thresholds
    st.subheader("Alert Thresholds")
    st.slider("Failed Attempts", 1, 20, 5)
    st.slider("Rate Limit %", 1, 100, 80)
    
    # Actions
    st.subheader("Quick Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Reset Keys"):
            st.warning("Are you sure?")
    with col2:
        if st.button("Block All"):
            st.error("Emergency block!")
