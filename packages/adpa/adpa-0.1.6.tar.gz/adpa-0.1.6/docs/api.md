# API Reference

!!! note "Version"
    Current version: 1.5.0

## Core Components

### Text2SQL

::: adpa.text2sql.core
    options:
        show_root_heading: true
        show_source: true

### Agent System

::: adpa.agent.core
    options:
        show_root_heading: true
        show_source: true

### Database Integration

::: adpa.database.core
    options:
        show_root_heading: true
        show_source: true

### LLM Integration

::: adpa.llm.core
    options:
        show_root_heading: true
        show_source: true

### Monitoring

::: adpa.monitoring.core
    options:
        show_root_heading: true
        show_source: true

## Models

### Configuration

::: adpa.models.config
    options:
        show_root_heading: true
        show_source: true

### Database Models

::: adpa.models.database
    options:
        show_root_heading: true
        show_source: true

### Agent Models

::: adpa.models.agent
    options:
        show_root_heading: true
        show_source: true

## Utilities

### Security

::: adpa.utils.security
    options:
        show_root_heading: true
        show_source: true

### Validation

::: adpa.utils.validation
    options:
        show_root_heading: true
        show_source: true

### Helpers

::: adpa.utils.helpers
    options:
        show_root_heading: true
        show_source: true

## Agents

### BaseAgent

::: adpa.agent.base.BaseAgent
    options:
        show_root_heading: true
        show_source: true

### ModeratorAgent

::: adpa.agent.moderator.ModeratorAgent
    options:
        show_root_heading: true
        show_source: true

### LifeCoachAgent

::: adpa.agent.life_coach.LifeCoachAgent
    options:
        show_root_heading: true
        show_source: true

### ITArchitectAgent

::: adpa.agent.it_architect.ITArchitectAgent
    options:
        show_root_heading: true
        show_source: true

### RouterAgent

::: adpa.agent.router.RouterAgent
    options:
        show_root_heading: true
        show_source: true

## Teams

### Team

::: adpa.team.Team
    options:
        show_root_heading: true
        show_source: true

## Toolbox

### Tool

::: adpa.toolbox.Tool
    options:
        show_root_heading: true
        show_source: true

### APITool

::: adpa.toolbox.APITool
    options:
        show_root_heading: true
        show_source: true

### LoggingTool

::: adpa.toolbox.LoggingTool
    options:
        show_root_heading: true
        show_source: true

### DataTransformTool

::: adpa.toolbox.DataTransformTool
    options:
        show_root_heading: true
        show_source: true

### ResearchEngine

::: adpa.research_engine.ResearchEngine
    options:
        show_root_heading: true
        show_source: true

## CLI Commands

### chat

```bash
python -m cli.main chat "Your message here"
```

### list-teams

```bash
python -m cli.main list-teams
```

### list-tools

```bash
python -m cli.main list-tools
```

## Configuration

### Environment Variables

Required in `.env`:
```
OPENAI_API_KEY=your-api-key-here
ENVIRONMENT=development
LOG_LEVEL=INFO
```

### Config File (config.ini)

```ini
[DEFAULT]
DEBUG=False
LOG_LEVEL=INFO

[OpenAI]
MODEL_NAME=gpt-4
TEMPERATURE=0.7
MAX_TOKENS=2000

[Agents]
MODERATOR_NAME=moderator
LIFE_COACH_NAME=life_coach
IT_ARCHITECT_NAME=it_architect
ROUTER_NAME=router

[Teams]
DEFAULT_TEAM_SIZE=2
COLLABORATION_TIMEOUT=300

[Logging]
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
LOG_FILE=chatbot.log
