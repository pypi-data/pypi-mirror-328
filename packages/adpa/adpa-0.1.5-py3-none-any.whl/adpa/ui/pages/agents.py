"""Agents management page for ADPA Framework."""
import streamlit as st
from typing import Dict, List, Optional
import yaml

from adpa.core.agent import AgentManager
from adpa.core.types import Agent, AgentConfig
from adpa.utils.logger import get_logger
from adpa.utils.config import load_config
from adpa.database.models.agent import AgentModel
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

def render_agent_page():
    """Render the agents management page."""
    st.title("🤖 Agents Management")
    
    # Initialize agent manager
    agent_manager = AgentManager()
    
    # Sidebar
    st.sidebar.markdown("### Agent Actions")
    action = st.sidebar.selectbox(
        "Select Action",
        ["View Agents", "Create Agent", "Edit Agent", "Delete Agent"]
    )
    
    if action == "View Agents":
        display_agents(agent_manager)
    elif action == "Create Agent":
        create_agent(agent_manager)
    elif action == "Edit Agent":
        edit_agent(agent_manager)
    else:
        delete_agent(agent_manager)

def display_agents(agent_manager: AgentManager):
    """Display all agents."""
    agents = agent_manager.list_agents()
    
    if not agents:
        st.info("No agents found. Create a new agent to get started!")
        return
    
    for agent in agents:
        with st.expander(f"Agent: {agent.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Description**: {agent.description}")
                st.markdown(f"**Created**: {agent.created_at}")
                st.markdown(f"**Status**: {agent.status}")
                st.markdown(f"**Team**: {agent.team}")
            
            with col2:
                st.markdown(f"**Type**: {agent.type}")
                st.markdown(f"**Model**: {agent.config.model}")
                st.markdown(f"**Tasks Completed**: {agent.stats.tasks_completed}")
                st.markdown(f"**Success Rate**: {agent.stats.success_rate:.2f}%")

def create_agent(agent_manager: AgentManager):
    """Create a new agent."""
    st.subheader("Create New Agent")
    
    name = st.text_input("Agent Name")
    description = st.text_area("Description")
    team = st.selectbox("Team", agent_manager.list_teams())
    
    col1, col2 = st.columns(2)
    
    with col1:
        agent_type = st.selectbox(
            "Agent Type",
            ["text", "code", "data", "task", "custom"]
        )
        model = st.selectbox(
            "Language Model",
            ["gpt-4", "gpt-3.5-turbo", "claude-2", "custom"]
        )
    
    with col2:
        max_tokens = st.number_input("Max Tokens", min_value=100, value=2000)
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
        status = st.selectbox("Status", ["active", "inactive", "training"])
    
    if st.button("Create Agent"):
        try:
            config = AgentConfig(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            agent = Agent(
                name=name,
                description=description,
                team=team,
                type=agent_type,
                config=config,
                status=status
            )
            
            agent_manager.create_agent(agent)
            st.success(f"Agent '{name}' created successfully!")
            
        except Exception as e:
            logger.error(f"Failed to create agent: {str(e)}")
            st.error(f"Failed to create agent: {str(e)}")

def edit_agent(agent_manager: AgentManager):
    """Edit an existing agent."""
    agents = agent_manager.list_agents()
    
    if not agents:
        st.info("No agents found to edit.")
        return
    
    selected = st.selectbox(
        "Select Agent to Edit",
        [agent.name for agent in agents]
    )
    
    agent = next(a for a in agents if a.name == selected)
    
    st.subheader(f"Edit Agent: {agent.name}")
    
    description = st.text_area("Description", value=agent.description)
    team = st.selectbox("Team", agent_manager.list_teams(), index=agent_manager.list_teams().index(agent.team))
    
    col1, col2 = st.columns(2)
    
    with col1:
        agent_type = st.selectbox(
            "Agent Type",
            ["text", "code", "data", "task", "custom"],
            index=["text", "code", "data", "task", "custom"].index(agent.type)
        )
        model = st.selectbox(
            "Language Model",
            ["gpt-4", "gpt-3.5-turbo", "claude-2", "custom"],
            index=["gpt-4", "gpt-3.5-turbo", "claude-2", "custom"].index(agent.config.model)
        )
    
    with col2:
        max_tokens = st.number_input(
            "Max Tokens",
            min_value=100,
            value=agent.config.max_tokens
        )
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=agent.config.temperature
        )
        status = st.selectbox(
            "Status",
            ["active", "inactive", "training"],
            index=["active", "inactive", "training"].index(agent.status)
        )
    
    if st.button("Update Agent"):
        try:
            config = AgentConfig(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            updated_agent = Agent(
                name=agent.name,
                description=description,
                team=team,
                type=agent_type,
                config=config,
                status=status
            )
            
            agent_manager.update_agent(updated_agent)
            st.success(f"Agent '{agent.name}' updated successfully!")
            
        except Exception as e:
            logger.error(f"Failed to update agent: {str(e)}")
            st.error(f"Failed to update agent: {str(e)}")

def delete_agent(agent_manager: AgentManager):
    """Delete an existing agent."""
    agents = agent_manager.list_agents()
    
    if not agents:
        st.info("No agents found to delete.")
        return
    
    selected = st.selectbox(
        "Select Agent to Delete",
        [agent.name for agent in agents]
    )
    
    if st.button("Delete Agent", type="primary"):
        try:
            agent_manager.delete_agent(selected)
            st.success(f"Agent '{selected}' deleted successfully!")
            
        except Exception as e:
            logger.error(f"Failed to delete agent: {str(e)}")
            st.error(f"Failed to delete agent: {str(e)}")

def main():
    """Main entry point for agents page."""
    try:
        render_agent_page()
    except Exception as e:
        st.error(f"Failed to render agents page: {str(e)}")
        logger.error(f"Agents page error: {str(e)}")

if __name__ == "__main__":
    main()
