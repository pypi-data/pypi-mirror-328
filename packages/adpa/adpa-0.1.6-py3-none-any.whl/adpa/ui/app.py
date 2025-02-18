"""ADPA Framework Main Application."""
import streamlit as st
from typing import Dict, Any, Optional
import yaml
import os

from adpa.utils.logger import get_logger
from adpa.utils.config import load_config
from adpa.ui.pages import (
    teams,
    agents,
    knowledge_tools,
    llm_integration,
    database_storage,
    api_integration
)

# Setup logging
logger = get_logger(__name__)

# Configure Streamlit page
st.set_page_config(
    page_title="ADPA Framework",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application entry point."""
    # Load configuration
    config = load_config()
    
    # Header
    st.title("🧠 ADPA Framework")
    st.markdown("""
    ### Autonomous Data Processing Agents Framework
    
    Welcome to the ADPA Framework - your central hub for managing autonomous data processing agents.
    """)
    
    # Main dashboard
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Active Teams", len(config.get("teams", [])))
        
    with col2:
        st.metric("Active Agents", sum(len(team.get("agents", [])) for team in config.get("teams", [])))
        
    with col3:
        st.metric("Active LLMs", len(config.get("llms", [])))
    
    # Quick Actions
    st.subheader("Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("➕ New Team"):
            st.switch_page("pages/teams.py")
            
    with col2:
        if st.button("➕ New Agent"):
            st.switch_page("pages/agents.py")
            
    with col3:
        if st.button("🔍 Search Documents"):
            st.switch_page("pages/search.py")
            
    with col4:
        if st.button("⚙️ Settings"):
            st.switch_page("pages/settings.py")
    
    # System Status
    st.subheader("System Status")
    status_col1, status_col2 = st.columns(2)
    
    with status_col1:
        st.markdown("### Services")
        services = {
            "Elasticsearch": "http://localhost:9200",
            "Kibana": "http://localhost:5601",
            "Vector Store": "Active",
            "LLM Service": config.get("llm_service", {}).get("status", "Not Configured")
        }
        
        for service, status in services.items():
            st.write(f"- **{service}**: {status}")
    
    with status_col2:
        st.markdown("### Recent Activity")
        st.info("Activity log coming soon!")
    
    # Documentation
    st.sidebar.markdown("""
    ### Documentation
    - [User Guide](docs/user_guide)
    - [API Reference](docs/api)
    - [Configuration](docs/config)
    """)
    
    # Environment Info
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"""
    ### Environment
    - Version: {config.get('version', 'Unknown')}
    - Mode: {config.get('mode', 'Development')}
    """)

if __name__ == "__main__":
    main()
