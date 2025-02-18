"""LLM integration page for ADPA Framework."""
import streamlit as st
from typing import Dict, List, Optional
import yaml

from adpa.core.llm import LLMManager
from adpa.core.types import LLMConfig, ModelResponse
from adpa.utils.logger import get_logger
from adpa.utils.config import load_config
from adpa.database.models.llm import LLMModel
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

def render_llm_page():
    """Render the LLM integration page."""
    st.title("🤖 LLM Integration")
    
    # Initialize LLM manager
    llm_manager = LLMManager()
    
    # Sidebar
    st.sidebar.markdown("### LLM Actions")
    action = st.sidebar.selectbox(
        "Select Action",
        ["Test Models", "Configure Models", "View Usage"]
    )
    
    if action == "Test Models":
        test_models(llm_manager)
    elif action == "Configure Models":
        configure_models(llm_manager)
    else:
        view_usage(llm_manager)

def test_models(llm_manager: LLMManager):
    """Test LLM models."""
    st.subheader("Test Models")
    
    # Model selection
    col1, col2 = st.columns(2)
    
    with col1:
        model = st.selectbox(
            "Select Model",
            llm_manager.list_models()
        )
        max_tokens = st.number_input(
            "Max Tokens",
            min_value=1,
            max_value=4096,
            value=100
        )
    
    with col2:
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.7
        )
        top_p = st.slider(
            "Top P",
            min_value=0.0,
            max_value=1.0,
            value=1.0
        )
    
    # Input prompt
    prompt = st.text_area("Enter Prompt")
    
    if st.button("Generate"):
        if not prompt:
            st.warning("Please enter a prompt.")
            return
        
        try:
            config = LLMConfig(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p
            )
            
            with st.spinner("Generating response..."):
                response = llm_manager.generate(prompt, config)
            
            display_model_response(response)
            
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            st.error(f"Generation failed: {str(e)}")

def display_model_response(response: ModelResponse):
    """Display model response."""
    st.markdown("### Model Response")
    
    st.markdown("**Generated Text:**")
    st.markdown(response.text)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Tokens Used", response.usage.total_tokens)
    
    with col2:
        st.metric("Response Time", f"{response.time_ms}ms")
    
    with col3:
        st.metric("Cost", f"${response.cost:.4f}")

def configure_models(llm_manager: LLMManager):
    """Configure LLM models."""
    st.subheader("Configure Models")
    
    # Add new model
    st.markdown("### Add Model")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Model Name")
        provider = st.selectbox(
            "Provider",
            ["OpenAI", "Anthropic", "Cohere", "Custom"]
        )
    
    with col2:
        api_key = st.text_input("API Key", type="password")
        endpoint = st.text_input("API Endpoint (optional)")
    
    if st.button("Add Model"):
        try:
            llm_manager.add_model(
                name=name,
                provider=provider,
                api_key=api_key,
                endpoint=endpoint
            )
            st.success(f"Model '{name}' added successfully!")
            
        except Exception as e:
            logger.error(f"Failed to add model: {str(e)}")
            st.error(f"Failed to add model: {str(e)}")
    
    # List models
    st.markdown("### Configured Models")
    models = llm_manager.list_models()
    
    if not models:
        st.info("No models configured.")
        return
    
    for model in models:
        with st.expander(f"Model: {model.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Provider**: {model.provider}")
                st.markdown(f"**Status**: {model.status}")
                st.markdown(f"**Added**: {model.created_at}")
            
            with col2:
                st.markdown(f"**Usage**: {model.usage.total_tokens} tokens")
                st.markdown(f"**Cost**: ${model.usage.total_cost:.2f}")
                st.markdown(f"**Last Used**: {model.last_used}")
            
            if st.button(f"Remove {model.name}", key=model.name):
                try:
                    llm_manager.remove_model(model.name)
                    st.success(f"Model '{model.name}' removed successfully!")
                    st.rerun()
                    
                except Exception as e:
                    logger.error(f"Failed to remove model: {str(e)}")
                    st.error(f"Failed to remove model: {str(e)}")

def view_usage(llm_manager: LLMManager):
    """View LLM usage statistics."""
    st.subheader("Usage Statistics")
    
    # Date range selection
    col1, col2 = st.columns(2)
    
    with col1:
        start_date = st.date_input("Start Date")
    
    with col2:
        end_date = st.date_input("End Date")
    
    if st.button("View Usage"):
        try:
            usage = llm_manager.get_usage(start_date, end_date)
            
            # Overall metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Tokens", usage.total_tokens)
            
            with col2:
                st.metric("Total Cost", f"${usage.total_cost:.2f}")
            
            with col3:
                st.metric("Total Requests", usage.total_requests)
            
            # Usage by model
            st.markdown("### Usage by Model")
            for model, stats in usage.by_model.items():
                with st.expander(f"Model: {model}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("Tokens", stats.tokens)
                        st.metric("Cost", f"${stats.cost:.2f}")
                    
                    with col2:
                        st.metric("Requests", stats.requests)
                        st.metric("Avg Response Time", f"{stats.avg_time_ms}ms")
            
        except Exception as e:
            logger.error(f"Failed to get usage: {str(e)}")
            st.error(f"Failed to get usage: {str(e)}")

def main():
    """Main entry point for LLM integration page."""
    try:
        render_llm_page()
    except Exception as e:
        st.error(f"Failed to render LLM integration page: {str(e)}")
        logger.error(f"LLM integration page error: {str(e)}")

if __name__ == "__main__":
    main()
