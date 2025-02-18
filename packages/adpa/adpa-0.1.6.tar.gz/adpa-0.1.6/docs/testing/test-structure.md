# ADPA Test Structure

## Overview

ADPA uses a hybrid testing approach across all test categories, combining technical Robot Framework tests with Gherkin-style workflow tests.

## Directory Structure

```
tests/
├── robot/                      # All Robot Framework tests
│   ├── agents/                # Agent-related tests
│   │   ├── technical/        # Technical implementation tests
│   │   │   ├── test_database_agent.robot
│   │   │   ├── test_research_agent.robot
│   │   │   └── test_team_agent.robot
│   │   └── workflows/        # Business workflow tests
│   │       ├── test_agent_collaboration.feature
│   │       ├── test_research_workflows.feature
│   │       └── test_team_management.feature
│   │
│   ├── database/             # Database tests
│   │   ├── technical/       # Database operations tests
│   │   │   └── test_database_operations.robot
│   │   └── workflows/       # Data management workflows
│   │       └── test_research_data_management.feature
│   │
│   ├── llm/                  # LLM integration tests
│   │   ├── technical/       # LLM implementation tests
│   │   │   ├── test_llm_integration.robot
│   │   │   └── test_prompt_engineering.robot
│   │   └── workflows/       # LLM usage workflows
│   │       ├── test_conversation_flows.feature
│   │       └── test_research_assistance.feature
│   │
│   ├── research/             # Research functionality tests
│   │   ├── technical/       # Research implementation tests
│   │   │   ├── test_analysis_methods.robot
│   │   │   └── test_data_processing.robot
│   │   └── workflows/       # Research workflows
│   │       ├── test_research_collaboration.feature
│   │       └── test_research_projects.feature
│   │
│   ├── cli/                  # CLI tests
│   │   ├── technical/       # CLI implementation tests
│   │   │   ├── test_cli_commands.robot
│   │   │   └── test_cli_options.robot
│   │   └── workflows/       # CLI usage workflows
│   │       ├── test_database_management.feature
│   │       └── test_research_commands.feature
│   │
│   ├── gui/                  # GUI tests
│   │   ├── technical/       # GUI implementation tests
│   │   │   ├── test_components.robot
│   │   │   └── test_layouts.robot
│   │   └── workflows/       # GUI usage workflows
│   │       ├── test_research_interface.feature
│   │       └── test_team_dashboard.feature
│   │
│   ├── integration/          # Integration tests
│   │   ├── technical/       # Technical integration tests
│   │   │   ├── test_api_integration.robot
│   │   │   └── test_service_integration.robot
│   │   └── workflows/       # End-to-end workflows
│   │       ├── test_research_lifecycle.feature
│   │       └── test_team_collaboration.feature
│   │
│   └── resources/            # Shared resources
│       ├── common.resource   # Common keywords
│       ├── database.resource # Database keywords
│       ├── research.resource # Research keywords
│       └── team.resource     # Team keywords

```

## Test Categories

### Technical Tests (.robot)
- Focus on implementation details
- Performance testing
- Error handling
- API testing
- Component testing
- Security testing

Example:
```robotframework
*** Test Cases ***
Test API Rate Limiting
    [Documentation]    Verify API rate limiting functionality
    [Tags]    technical    api    performance
    ${rate_limit}=    Get Rate Limit
    Make Multiple API Calls
    Verify Rate Limit Applied
```

### Workflow Tests (.feature)
- User scenarios
- Business processes
- Integration workflows
- End-to-end testing
- Acceptance criteria
- Collaboration scenarios

Example:
```gherkin
Scenario: Collaborative Research Project
    Given a research team "Climate Research" exists
    When researcher "John" creates a new project
    And researcher "Alice" joins the project
    Then both should have access to project resources
```

## Best Practices

### File Naming
- Technical tests: `test_<component>_<aspect>.robot`
- Workflow tests: `test_<workflow>_<type>.feature`

### Test Organization
1. **Technical Tests**
   - Group by component
   - Focus on specific functionality
   - Include performance metrics
   - Test edge cases

2. **Workflow Tests**
   - Group by business process
   - Focus on user interactions
   - Include acceptance criteria
   - Test common scenarios

### Tags
Use consistent tags across both types:
- Component: `database`, `research`, `team`, etc.
- Type: `technical`, `workflow`
- Aspect: `performance`, `security`, `usability`
- Priority: `critical`, `major`, `minor`

## Running Tests

### Individual Components
```bash
# Run technical database tests
robot tests/robot/database/technical/

# Run database workflows
robot tests/robot/database/workflows/
```

### Full Test Suite
```bash
# Run all tests
robot tests/robot/

# Run by tag
robot --include workflow tests/robot/
robot --include technical tests/robot/
```

### Specific Features
```bash
# Run specific workflow
robot tests/robot/research/workflows/test_research_collaboration.feature

# Run specific technical test
robot tests/robot/database/technical/test_database_operations.robot
```

## Test Development Workflow

1. **Start with Workflows**
   - Write business scenarios first
   - Define acceptance criteria
   - Create Gherkin feature files

2. **Add Technical Tests**
   - Implement technical requirements
   - Add performance tests
   - Include error cases

3. **Integration**
   - Combine workflow and technical tests
   - Verify end-to-end functionality
   - Ensure complete coverage

## Maintenance

1. **Regular Updates**
   - Keep both test types in sync
   - Update scenarios as requirements change
   - Maintain shared resources

2. **Review Process**
   - Technical review of .robot files
   - Business review of .feature files
   - Regular test coverage analysis

3. **Documentation**
   - Keep test documentation current
   - Document new scenarios
   - Update best practices
