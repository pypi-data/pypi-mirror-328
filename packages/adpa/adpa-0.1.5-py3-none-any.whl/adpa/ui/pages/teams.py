"""Teams management page for ADPA Framework."""
import streamlit as st
from typing import Dict, List, Optional
import yaml

from adpa.core.team import TeamManager
from adpa.core.types import Team, TeamConfig
from adpa.utils.logger import get_logger
from adpa.utils.config import load_config
from adpa.database.models.team import TeamModel
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

def render_team_page():
    """Render the teams management page."""
    st.title("👥 Teams Management")
    
    # Initialize team manager
    team_manager = TeamManager()
    
    # Sidebar
    st.sidebar.markdown("### Team Actions")
    action = st.sidebar.selectbox(
        "Select Action",
        ["View Teams", "Create Team", "Edit Team", "Delete Team"]
    )
    
    if action == "View Teams":
        display_teams(team_manager)
    elif action == "Create Team":
        create_team(team_manager)
    elif action == "Edit Team":
        edit_team(team_manager)
    else:
        delete_team(team_manager)

def display_teams(team_manager: TeamManager):
    """Display all teams."""
    teams = team_manager.list_teams()
    
    if not teams:
        st.info("No teams found. Create a new team to get started!")
        return
    
    for team in teams:
        with st.expander(f"Team: {team.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Description**: {team.description}")
                st.markdown(f"**Created**: {team.created_at}")
                st.markdown(f"**Status**: {team.status}")
            
            with col2:
                st.markdown(f"**Agents**: {len(team.agents)}")
                st.markdown(f"**Tasks**: {len(team.tasks)}")
                st.markdown(f"**Owner**: {team.owner}")

def create_team(team_manager: TeamManager):
    """Create a new team."""
    st.subheader("Create New Team")
    
    name = st.text_input("Team Name")
    description = st.text_area("Description")
    owner = st.text_input("Owner")
    
    col1, col2 = st.columns(2)
    
    with col1:
        max_agents = st.number_input("Max Agents", min_value=1, value=5)
        task_timeout = st.number_input("Task Timeout (seconds)", min_value=30, value=300)
    
    with col2:
        priority = st.selectbox("Priority", ["low", "medium", "high"])
        status = st.selectbox("Status", ["active", "inactive", "maintenance"])
    
    if st.button("Create Team"):
        try:
            config = TeamConfig(
                max_agents=max_agents,
                task_timeout=task_timeout,
                priority=priority
            )
            
            team = Team(
                name=name,
                description=description,
                owner=owner,
                config=config,
                status=status
            )
            
            team_manager.create_team(team)
            st.success(f"Team '{name}' created successfully!")
            
        except Exception as e:
            logger.error(f"Failed to create team: {str(e)}")
            st.error(f"Failed to create team: {str(e)}")

def edit_team(team_manager: TeamManager):
    """Edit an existing team."""
    teams = team_manager.list_teams()
    
    if not teams:
        st.info("No teams found to edit.")
        return
    
    selected = st.selectbox(
        "Select Team to Edit",
        [team.name for team in teams]
    )
    
    team = next(t for t in teams if t.name == selected)
    
    st.subheader(f"Edit Team: {team.name}")
    
    description = st.text_area("Description", value=team.description)
    owner = st.text_input("Owner", value=team.owner)
    
    col1, col2 = st.columns(2)
    
    with col1:
        max_agents = st.number_input(
            "Max Agents",
            min_value=1,
            value=team.config.max_agents
        )
        task_timeout = st.number_input(
            "Task Timeout (seconds)",
            min_value=30,
            value=team.config.task_timeout
        )
    
    with col2:
        priority = st.selectbox(
            "Priority",
            ["low", "medium", "high"],
            index=["low", "medium", "high"].index(team.config.priority)
        )
        status = st.selectbox(
            "Status",
            ["active", "inactive", "maintenance"],
            index=["active", "inactive", "maintenance"].index(team.status)
        )
    
    if st.button("Update Team"):
        try:
            config = TeamConfig(
                max_agents=max_agents,
                task_timeout=task_timeout,
                priority=priority
            )
            
            updated_team = Team(
                name=team.name,
                description=description,
                owner=owner,
                config=config,
                status=status
            )
            
            team_manager.update_team(updated_team)
            st.success(f"Team '{team.name}' updated successfully!")
            
        except Exception as e:
            logger.error(f"Failed to update team: {str(e)}")
            st.error(f"Failed to update team: {str(e)}")

def delete_team(team_manager: TeamManager):
    """Delete an existing team."""
    teams = team_manager.list_teams()
    
    if not teams:
        st.info("No teams found to delete.")
        return
    
    selected = st.selectbox(
        "Select Team to Delete",
        [team.name for team in teams]
    )
    
    if st.button("Delete Team", type="primary"):
        try:
            team_manager.delete_team(selected)
            st.success(f"Team '{selected}' deleted successfully!")
            
        except Exception as e:
            logger.error(f"Failed to delete team: {str(e)}")
            st.error(f"Failed to delete team: {str(e)}")

def main():
    """Main entry point for teams page."""
    try:
        render_team_page()
    except Exception as e:
        st.error(f"Failed to render teams page: {str(e)}")
        logger.error(f"Teams page error: {str(e)}")

if __name__ == "__main__":
    main()
