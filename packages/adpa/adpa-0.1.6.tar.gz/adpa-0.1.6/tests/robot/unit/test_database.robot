*** Settings ***
Documentation     Unit tests for database functionality
Resource          ../resources/common.robot
Library           ../../adpa/database/database_utils.py
Library           Collections
Library           DatabaseLibrary

*** Variables ***
${DB_NAME}         ${POSTGRES_DATABASE}
${DB_USER}         ${POSTGRES_USER}
${DB_PASS}         ${POSTGRES_PASSWORD}
${DB_HOST}         ${POSTGRES_HOST}
${DB_PORT}         ${POSTGRES_PORT}

*** Test Cases ***
Test Database Connection
    [Documentation]    Test database connection
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    ${result}=    Query    SELECT 1
    Should Be Equal As Numbers    ${result[0][0]}    1
    Disconnect From Database

Test Create Tables
    [Documentation]    Test creating database tables
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    Create Required Tables
    Table Must Exist    agents_db.ag_agents
    Table Must Exist    agents_db.ag_conversations
    Table Must Exist    agents_db.ag_tools
    Disconnect From Database

Test Insert And Query Agent
    [Documentation]    Test inserting and querying agent data
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    ${agent_id}=    Insert Test Agent
    ${result}=    Query    SELECT name FROM agents_db.ag_agents WHERE id = ${agent_id}
    Should Be Equal    ${result[0][0]}    TestAgent
    Delete Test Agent    ${agent_id}
    Disconnect From Database

Test Update Agent
    [Documentation]    Test updating agent data
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    ${agent_id}=    Insert Test Agent
    Update Agent Configuration    ${agent_id}    temperature=0.8
    ${result}=    Query    SELECT configuration FROM agents_db.ag_agents WHERE id = ${agent_id}
    Should Be Equal    ${result[0][0]['temperature']}    0.8
    Delete Test Agent    ${agent_id}
    Disconnect From Database

*** Keywords ***
Create Required Tables
    Execute SQL String    CREATE SCHEMA IF NOT EXISTS agents_db;
    Execute SQL String    
    ...    CREATE TABLE IF NOT EXISTS agents_db.ag_agents (
    ...        id SERIAL PRIMARY KEY,
    ...        name TEXT NOT NULL,
    ...        configuration JSONB DEFAULT '{}'::jsonb,
    ...        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    ...        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    ...    )

Insert Test Agent
    Execute SQL String    
    ...    INSERT INTO agents_db.ag_agents (name, configuration) 
    ...    VALUES ('TestAgent', '{"temperature": 0.7}'::jsonb) 
    ...    RETURNING id
    ${result}=    Query    SELECT id FROM agents_db.ag_agents WHERE name = 'TestAgent'
    RETURN    ${result[0][0]}

Delete Test Agent
    [Arguments]    ${agent_id}
    Execute SQL String    DELETE FROM agents_db.ag_agents WHERE id = ${agent_id}

Update Agent Configuration
    [Arguments]    ${agent_id}    ${temperature}=0.7
    ${config}=    Create Dictionary    temperature=${temperature}
    Execute SQL String    
    ...    UPDATE agents_db.ag_agents 
    ...    SET configuration = '${config}'::jsonb 
    ...    WHERE id = ${agent_id}
