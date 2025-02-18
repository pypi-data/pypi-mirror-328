# ADPA Framework GUI Documentation

## Overview
The ADPA Framework GUI is built using Streamlit and provides a user-friendly interface for managing agents, teams, and projects. The application follows a modular architecture with separate pages for different functionalities.

## Pages

### 1. Home Page (`Home.py`)
The main landing page that provides:
- Overview of the ADPA Framework
- Quick navigation to different sections
- System status and configuration

### 2. Agents Page (`pages/2_Agents.py`)
Manages AI agents with the following features:
- View all agents with expandable details
- Create new agents with customizable:
  - Name and description
  - Agent type (task_manager, research_assistant, etc.)
  - Prompt templates with system and user prompts
  - Team assignments
- Edit existing agents
- Delete agents
- Team assignment management

### 3. Teams Page (`pages/1_Teams.py`)
Manages teams with the following features:
- View all teams with expandable details
- Create new teams with:
  - Name and description
  - Team type
  - Configuration settings
- Edit existing teams
- Delete teams
- Agent assignment management

## Components

### 1. Prompt Templates
The system uses a flexible prompt template system:
- Each agent type has default templates
- Templates include:
  - System prompts defining agent roles
  - User prompt templates for interactions
  - Variables for dynamic content
  - Metadata for additional configuration

### 2. Database Models
The application uses SQLAlchemy models:
- `Agent`: Represents AI agents with types and configurations
- `Team`: Represents teams that can contain multiple agents
- `Project`: Represents projects that organize teams and agents
- `TeamAssignment`: Manages many-to-many relationships between teams and agents

### 3. State Management
Uses Streamlit's session state for:
- Page navigation
- Form handling
- Edit/delete confirmations
- Temporary data storage

## Usage Guide

### Managing Agents

1. **Viewing Agents**
   - Navigate to the Agents page
   - Expand agent cards to view details
   - See team assignments and prompt templates

2. **Creating Agents**
   - Click "Create New Agent" in the sidebar
   - Fill in required information:
     - Name (required)
     - Description
     - Agent Type
     - Prompt Template
     - Team Assignments
   - Click "Create" to save

3. **Editing Agents**
   - Click the edit button on an agent card
   - Modify agent details
   - Update team assignments
   - Click "Update" to save changes

4. **Deleting Agents**
   - Click the delete button on an agent card
   - Confirm deletion
   - Agent and related assignments will be removed

### Managing Teams

1. **Viewing Teams**
   - Navigate to the Teams page
   - Expand team cards to view details
   - See agent assignments

2. **Creating Teams**
   - Click "Create Team" in the sidebar
   - Fill in required information:
     - Name (required)
     - Description
     - Team Type
   - Click "Create" to save

3. **Editing Teams**
   - Select a team to edit
   - Modify team details
   - Click "Update" to save changes

4. **Managing Team Members**
   - Expand a team card
   - View current team members
   - Add new agents using the dropdown
   - Remove agents using the remove button

## Development Guide

### Adding New Features

1. **New Agent Types**
   - Add type to `AgentType` enum in models
   - Add default prompt template in `PromptRegistry`
   - Update UI to support new type

2. **New Team Types**
   - Add type to `TeamType` enum in models
   - Update UI to support new type

3. **New Prompt Templates**
   - Add template to `PromptRegistry`
   - Include system and user prompts
   - Define required variables

### Best Practices

1. **Form Handling**
   - Use Streamlit forms for data input
   - Include proper validation
   - Show success/error messages
   - Handle state transitions

2. **State Management**
   - Initialize session state variables
   - Clear state when navigating
   - Handle form submissions properly

3. **Error Handling**
   - Validate user input
   - Handle database errors
   - Show user-friendly error messages

4. **Code Organization**
   - Follow modular design
   - Keep pages focused
   - Reuse common components

## Deployment

1. **Prerequisites**
   - Python 3.8+
   - PostgreSQL database
   - Required Python packages

2. **Environment Setup**
   - Set database connection string
   - Configure environment variables
   - Initialize database

3. **Running the App**
   ```bash
   streamlit run Home.py
   ```

4. **Accessing the App**
   - Local: http://localhost:8501
   - Network: Check console output

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
See LICENSE file in the root directory.
