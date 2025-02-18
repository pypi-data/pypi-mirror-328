import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Team Management - ADPA Framework",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Team Management")

# Main Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Teams Overview",
    "Team Configuration",
    "Role Management",
    "Performance"
])

with tab1:
    st.header("Teams Overview")
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Teams", "5", "↑ 1")
    with col2:
        st.metric("Total Agents", "24", "↑ 3")
    with col3:
        st.metric("Tasks/Hour", "156", "↑ 12")
    with col4:
        st.metric("Success Rate", "98.5%", "↑ 0.5%")
    
    # Teams List
    st.subheader("Active Teams")
    teams_data = {
        'Research Team': {
            'members': 5,
            'agents': 8,
            'tasks': 45,
            'success': 98.5
        },
        'Development Team': {
            'members': 4,
            'agents': 6,
            'tasks': 38,
            'success': 97.8
        },
        'Support Team': {
            'members': 3,
            'agents': 4,
            'tasks': 42,
            'success': 99.1
        },
        'QA Team': {
            'members': 3,
            'agents': 3,
            'tasks': 31,
            'success': 98.7
        },
        'Content Team': {
            'members': 2,
            'agents': 3,
            'tasks': 28,
            'success': 98.2
        }
    }
    
    for team, details in teams_data.items():
        with st.expander(team, expanded=True):
            col1, col2, col3, col4, col5 = st.columns([2,1,1,1,1])
            with col1:
                st.write(f"**{team}**")
            with col2:
                st.write(f"Members: {details['members']}")
            with col3:
                st.write(f"Agents: {details['agents']}")
            with col4:
                st.write(f"Tasks: {details['tasks']}")
            with col5:
                st.write(f"Success: {details['success']}%")

with tab2:
    st.header("Team Configuration")
    
    # Team Actions
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Configure Teams")
    with col2:
        st.button("➕ Create Team", type="primary")
    
    # Team Configuration
    for team in teams_data.keys():
        with st.expander(f"{team} Configuration"):
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Team Name", value=team, key=f"name_{team}")
                st.text_area("Description", value="Team description...", key=f"desc_{team}")
                st.multiselect(
                    "Team Members",
                    ["John Doe", "Jane Smith", "Bob Wilson", "Alice Brown"],
                    key=f"members_{team}"
                )
            with col2:
                st.multiselect(
                    "Assigned Agents",
                    ["Research Agent", "Development Agent", "Support Agent"],
                    key=f"agents_{team}"
                )
                st.multiselect(
                    "Available Tools",
                    ["File Operations", "Data Processing", "API Integration"],
                    key=f"tools_{team}"
                )
                st.selectbox(
                    "Team Status",
                    ["Active", "Inactive", "Maintenance"],
                    key=f"status_{team}"
                )
            
            # Team Settings
            st.write("**Team Settings**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.number_input(
                    "Max Concurrent Tasks",
                    1, 100, 20,
                    key=f"tasks_{team}"
                )
            with col2:
                st.number_input(
                    "Task Timeout (min)",
                    1, 60, 15,
                    key=f"timeout_{team}"
                )
            with col3:
                st.number_input(
                    "Max Retries",
                    0, 10, 3,
                    key=f"retries_{team}"
                )
            
            # Save Actions
            col1, col2, col3 = st.columns(3)
            with col1:
                st.button("Save Changes", key=f"save_{team}")
            with col2:
                st.button("Reset", key=f"reset_{team}")
            with col3:
                st.button("Delete Team", key=f"delete_{team}")

with tab3:
    st.header("Role Management")
    
    # Role Categories
    roles = {
        "Team Lead": {
            "permissions": [
                "Manage Team",
                "Assign Tasks",
                "View Analytics",
                "Configure Agents"
            ],
            "members": ["John Doe", "Alice Brown"]
        },
        "Agent Manager": {
            "permissions": [
                "Configure Agents",
                "Monitor Performance",
                "Handle Errors"
            ],
            "members": ["Bob Wilson"]
        },
        "Tool Manager": {
            "permissions": [
                "Configure Tools",
                "Monitor Usage",
                "Update Settings"
            ],
            "members": ["Jane Smith"]
        },
        "Member": {
            "permissions": [
                "View Dashboard",
                "Execute Tasks",
                "View Reports"
            ],
            "members": ["Tom Brown", "Sarah Wilson"]
        }
    }
    
    for role, details in roles.items():
        with st.expander(role):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Role Configuration**")
                st.text_input("Role Name", value=role, key=f"role_{role}")
                st.multiselect(
                    "Permissions",
                    [
                        "Manage Team",
                        "Assign Tasks",
                        "View Analytics",
                        "Configure Agents",
                        "Monitor Performance",
                        "Handle Errors",
                        "Configure Tools",
                        "Monitor Usage",
                        "Update Settings",
                        "View Dashboard",
                        "Execute Tasks",
                        "View Reports"
                    ],
                    default=details["permissions"],
                    key=f"perm_{role}"
                )
            with col2:
                st.write("**Assigned Members**")
                st.multiselect(
                    "Members",
                    ["John Doe", "Jane Smith", "Bob Wilson", "Alice Brown", "Tom Brown", "Sarah Wilson"],
                    default=details["members"],
                    key=f"members_role_{role}"
                )
            
            col1, col2 = st.columns(2)
            with col1:
                st.button("Save Role", key=f"save_role_{role}")
            with col2:
                st.button("Delete Role", key=f"delete_role_{role}")

with tab4:
    st.header("Performance Analytics")
    
    # Time Range Selection
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Team Performance")
    with col2:
        timeframe = st.selectbox(
            "Timeframe",
            ["Last Hour", "Last 24 Hours", "Last 7 Days", "Last 30 Days"]
        )
    
    # Performance Charts
    col1, col2 = st.columns(2)
    
    # Task Completion Rate
    with col1:
        times = [datetime.now() - timedelta(hours=i) for i in range(24)]
        completion_data = {
            'Research Team': [45 + (i % 10) for i in range(24)],
            'Development Team': [38 + (i % 8) for i in range(24)],
            'Support Team': [42 + (i % 12) for i in range(24)]
        }
        
        fig = go.Figure()
        for team, data in completion_data.items():
            fig.add_trace(go.Scatter(
                x=times,
                y=data,
                mode='lines',
                name=team
            ))
        fig.update_layout(title="Tasks Completed by Team")
        st.plotly_chart(fig)
    
    # Success Rate
    with col2:
        success_data = {
            'Research Team': [98 + (i % 3) for i in range(24)],
            'Development Team': [97 + (i % 4) for i in range(24)],
            'Support Team': [99 + (i % 2) for i in range(24)]
        }
        
        fig = go.Figure()
        for team, data in success_data.items():
            fig.add_trace(go.Scatter(
                x=times,
                y=data,
                mode='lines',
                name=team
            ))
        fig.update_layout(title="Success Rate by Team")
        st.plotly_chart(fig)
    
    # Team Workload Distribution
    st.subheader("Workload Distribution")
    workload_data = pd.DataFrame({
        'Team': list(teams_data.keys()),
        'Tasks': [d['tasks'] for d in teams_data.values()],
        'Members': [d['members'] for d in teams_data.values()],
        'Agents': [d['agents'] for d in teams_data.values()],
        'Success': [d['success'] for d in teams_data.values()]
    })
    
    fig = px.sunburst(
        workload_data,
        path=['Team'],
        values='Tasks',
        color='Success',
        title="Team Workload Distribution"
    )
    st.plotly_chart(fig)

# Sidebar
with st.sidebar:
    st.header("Quick Actions")
    
    # Team Actions
    st.subheader("Teams")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Start All")
    with col2:
        st.button("Stop All")
    
    # Task Management
    st.subheader("Tasks")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Assign")
    with col2:
        st.button("Review")
    
    # Monitoring
    st.subheader("Monitoring")
    st.toggle("Auto Refresh", value=True)
    st.number_input("Refresh Interval (s)", 1, 3600, 60)
    
    # Documentation
    st.subheader("Help")
    st.markdown("[Team Setup Guide](https://docs.adpa.dev/teams)")
    st.markdown("[Role Management](https://docs.adpa.dev/roles)")
    st.markdown("[Best Practices](https://docs.adpa.dev/best-practices)")
