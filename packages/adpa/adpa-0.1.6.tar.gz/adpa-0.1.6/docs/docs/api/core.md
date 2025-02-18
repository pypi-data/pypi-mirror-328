# Core API Reference

## Text2SQL

### Text2SQL Class

::: adpa.text2sql.Text2SQL
    handler: python
    selection:
      members:
        - translate
        - validate_schema
        - optimize_query

### SchemaInfo Model

::: adpa.text2sql.models.SchemaInfo
    handler: python
    selection:
      members:
        - tables
        - columns
        - relationships

### SQLQuery Model

::: adpa.text2sql.models.SQLQuery
    handler: python
    selection:
      members:
        - sql
        - params
        - is_optimized

## Agents

### Agent Class

::: adpa.agents.Agent
    handler: python
    selection:
      members:
        - execute_task
        - can_use_tool
        - get_status
        - get_history

### AgentConfig Model

::: adpa.agents.models.AgentConfig
    handler: python
    selection:
      members:
        - name
        - type
        - team
        - description
        - tools
        - llm_config
        - max_concurrent_tasks
        - timeout

### Task Model

::: adpa.agents.models.Task
    handler: python
    selection:
      members:
        - id
        - type
        - description
        - priority
        - status

## Database

### Database Class

::: adpa.database.Database
    handler: python
    selection:
      members:
        - connect
        - execute
        - execute_many
        - begin_transaction
        - commit
        - rollback

### DatabaseConfig Model

::: adpa.database.models.DatabaseConfig
    handler: python
    selection:
      members:
        - host
        - port
        - user
        - password
        - database
        - uri

## Configuration

### Config Class

::: adpa.config.Config
    handler: python
    selection:
      members:
        - load
        - validate
        - get
        - set

### ConfigValidator

::: adpa.config.validator.ConfigValidator
    handler: python
    selection:
      members:
        - validate_api_keys
        - validate_database
        - validate_application
