"""API integration page for ADPA Framework."""
import streamlit as st
from typing import Dict, List, Optional
import yaml

from adpa.core.api import APIManager
from adpa.core.types import APIConfig, Endpoint
from adpa.utils.logger import get_logger
from adpa.utils.config import load_config
from adpa.database.models.api import APIModel
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

def render_api_page():
    """Render the API integration page."""
    st.title("🔌 API Integration")
    
    # Initialize API manager
    api_manager = APIManager()
    
    # Sidebar
    st.sidebar.markdown("### API Actions")
    action = st.sidebar.selectbox(
        "Select Action",
        ["Test Endpoints", "Configure APIs", "View Logs"]
    )
    
    if action == "Test Endpoints":
        test_endpoints(api_manager)
    elif action == "Configure APIs":
        configure_apis(api_manager)
    else:
        view_logs(api_manager)

def test_endpoints(api_manager: APIManager):
    """Test API endpoints."""
    st.subheader("Test Endpoints")
    
    # API selection
    api = st.selectbox(
        "Select API",
        api_manager.list_apis()
    )
    
    try:
        endpoints = api_manager.list_endpoints(api)
        
        if not endpoints:
            st.info("No endpoints found for this API.")
            return
        
        # Endpoint testing
        for endpoint in endpoints:
            with st.expander(f"Endpoint: {endpoint.path}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Method**: {endpoint.method}")
                    st.markdown(f"**Description**: {endpoint.description}")
                    st.markdown(f"**Version**: {endpoint.version}")
                
                with col2:
                    st.markdown(f"**Auth Required**: {endpoint.auth_required}")
                    st.markdown(f"**Rate Limit**: {endpoint.rate_limit}/min")
                    st.markdown(f"**Status**: {endpoint.status}")
                
                # Parameters
                if endpoint.parameters:
                    st.markdown("### Parameters")
                    params = {}
                    
                    for param in endpoint.parameters:
                        if param.type == "string":
                            params[param.name] = st.text_input(
                                param.name,
                                key=f"{endpoint.path}_{param.name}"
                            )
                        elif param.type == "number":
                            params[param.name] = st.number_input(
                                param.name,
                                key=f"{endpoint.path}_{param.name}"
                            )
                        elif param.type == "boolean":
                            params[param.name] = st.checkbox(
                                param.name,
                                key=f"{endpoint.path}_{param.name}"
                            )
                
                # Headers
                if endpoint.headers:
                    st.markdown("### Headers")
                    headers = {}
                    
                    for header in endpoint.headers:
                        headers[header.name] = st.text_input(
                            header.name,
                            key=f"{endpoint.path}_{header.name}"
                        )
                
                # Test button
                if st.button("Test Endpoint", key=f"test_{endpoint.path}"):
                    try:
                        with st.spinner("Testing endpoint..."):
                            response = api_manager.test_endpoint(
                                api,
                                endpoint.path,
                                params=params,
                                headers=headers
                            )
                        
                        st.markdown("### Response")
                        st.json(response)
                        
                    except Exception as e:
                        logger.error(f"Endpoint test failed: {str(e)}")
                        st.error(f"Endpoint test failed: {str(e)}")
        
    except Exception as e:
        logger.error(f"Failed to list endpoints: {str(e)}")
        st.error(f"Failed to list endpoints: {str(e)}")

def configure_apis(api_manager: APIManager):
    """Configure API integrations."""
    st.subheader("Configure APIs")
    
    # Add new API
    st.markdown("### Add API")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("API Name")
        base_url = st.text_input("Base URL")
        version = st.text_input("Version")
    
    with col2:
        auth_type = st.selectbox(
            "Auth Type",
            ["none", "basic", "bearer", "oauth2"]
        )
        api_key = st.text_input("API Key", type="password")
        timeout = st.number_input("Timeout (seconds)", min_value=1, value=30)
    
    if st.button("Add API"):
        try:
            config = APIConfig(
                name=name,
                base_url=base_url,
                version=version,
                auth_type=auth_type,
                api_key=api_key,
                timeout=timeout
            )
            
            api_manager.add_api(config)
            st.success(f"API '{name}' added successfully!")
            
        except Exception as e:
            logger.error(f"Failed to add API: {str(e)}")
            st.error(f"Failed to add API: {str(e)}")
    
    # List APIs
    st.markdown("### Configured APIs")
    apis = api_manager.list_apis()
    
    if not apis:
        st.info("No APIs configured.")
        return
    
    for api in apis:
        with st.expander(f"API: {api.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Base URL**: {api.base_url}")
                st.markdown(f"**Version**: {api.version}")
                st.markdown(f"**Auth Type**: {api.auth_type}")
            
            with col2:
                st.markdown(f"**Status**: {api.status}")
                st.markdown(f"**Endpoints**: {len(api.endpoints)}")
                st.markdown(f"**Last Used**: {api.last_used}")
            
            # Test connection
            if st.button(f"Test {api.name}", key=f"test_{api.name}"):
                try:
                    api_manager.test_connection(api.name)
                    st.success("API connection test successful!")
                except Exception as e:
                    logger.error(f"API test failed: {str(e)}")
                    st.error(f"API test failed: {str(e)}")
            
            # Remove API
            if st.button(f"Remove {api.name}", key=f"remove_{api.name}"):
                try:
                    api_manager.remove_api(api.name)
                    st.success(f"API '{api.name}' removed successfully!")
                    st.rerun()
                except Exception as e:
                    logger.error(f"Failed to remove API: {str(e)}")
                    st.error(f"Failed to remove API: {str(e)}")

def view_logs(api_manager: APIManager):
    """View API integration logs."""
    st.subheader("API Logs")
    
    # Date range selection
    col1, col2 = st.columns(2)
    
    with col1:
        start_date = st.date_input("Start Date")
    
    with col2:
        end_date = st.date_input("End Date")
    
    # API selection
    api = st.selectbox(
        "Select API",
        ["All"] + api_manager.list_apis()
    )
    
    # Log level
    level = st.selectbox(
        "Log Level",
        ["All", "INFO", "WARNING", "ERROR"]
    )
    
    if st.button("View Logs"):
        try:
            logs = api_manager.get_logs(
                start_date=start_date,
                end_date=end_date,
                api=None if api == "All" else api,
                level=None if level == "All" else level
            )
            
            if not logs:
                st.info("No logs found for the selected criteria.")
                return
            
            for log in logs:
                with st.expander(
                    f"{log.timestamp} - {log.level} - {log.api}"
                ):
                    st.markdown(f"**Endpoint**: {log.endpoint}")
                    st.markdown(f"**Status**: {log.status}")
                    st.markdown(f"**Duration**: {log.duration_ms}ms")
                    
                    if log.request:
                        st.markdown("**Request:**")
                        st.json(log.request)
                    
                    if log.response:
                        st.markdown("**Response:**")
                        st.json(log.response)
                    
                    if log.error:
                        st.markdown("**Error:**")
                        st.error(log.error)
            
        except Exception as e:
            logger.error(f"Failed to get logs: {str(e)}")
            st.error(f"Failed to get logs: {str(e)}")

def main():
    """Main entry point for API integration page."""
    try:
        render_api_page()
    except Exception as e:
        st.error(f"Failed to render API integration page: {str(e)}")
        logger.error(f"API integration page error: {str(e)}")

if __name__ == "__main__":
    main()
