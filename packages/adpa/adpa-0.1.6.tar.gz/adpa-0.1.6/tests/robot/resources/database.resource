# -*- coding: utf-8 -*-

*** Settings ***
Documentation     Database keywords and variables
Library           DatabaseLibrary
Variables         env.py

*** Variables ***
${DB_NAME}         adpa_test
${DB_USER}         adpa_test
${DB_PASSWORD}     test_password
${DB_HOST}         localhost
${DB_PORT}         5432

*** Keywords ***
Connect To Database
    [Documentation]    Connect to PostgreSQL database
    DatabaseLibrary.Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASSWORD}    ${DB_HOST}    ${DB_PORT}

Disconnect From Database
    [Documentation]    Disconnect from database
    DatabaseLibrary.Disconnect From Database

Clean Database
    [Documentation]    Clean test data from database
    Execute SQL String    DELETE FROM agent_memory WHERE 1=1;
    Execute SQL String    DELETE FROM agent_conversation WHERE 1=1;
    Execute SQL String    DELETE FROM agent WHERE 1=1;

Seed Test Data
    [Documentation]    Insert test data into database
    Execute SQL String    INSERT INTO users (username, email) VALUES ('test_user', 'test@example.com');
    Execute SQL String    INSERT INTO projects (name, user_id) VALUES ('test_project', (SELECT id FROM users WHERE username = 'test_user'));

Create Test Table
    [Documentation]    Create a test table for database operations
    [Arguments]    ${table_name}
    Execute SQL String    
    ...    CREATE TABLE IF NOT EXISTS ${table_name} (
    ...    id SERIAL PRIMARY KEY,
    ...    name VARCHAR(100),
    ...    value INTEGER
    ...    )

Drop Test Table
    [Documentation]    Drop a test table
    [Arguments]    ${table_name}
    Execute SQL String    DROP TABLE IF EXISTS ${table_name}

Insert Test Data
    [Documentation]    Insert test data into specified table
    [Arguments]    ${table_name}    ${name}    ${value}
    Execute SQL String    
    ...    INSERT INTO ${table_name} (name, value) 
    ...    VALUES ('${name}', ${value})

Backup Table
    [Documentation]    Create a backup of specified table
    [Arguments]    ${source_table}    ${backup_table}
    Execute SQL String    
    ...    CREATE TABLE ${backup_table} AS 
    ...    SELECT * FROM ${source_table}

Restore Table
    [Documentation]    Restore table from backup
    [Arguments]    ${backup_table}    ${target_table}
    Execute SQL String    
    ...    TRUNCATE TABLE ${target_table};
    ...    INSERT INTO ${target_table} 
    ...    SELECT * FROM ${backup_table}

Get Row Count
    [Documentation]    Get number of rows in specified table
    [Arguments]    ${table_name}
    ${result}=    Query    SELECT COUNT(*) FROM ${table_name}
    [Return]    ${result[0][0]}

Verify Table Structure
    [Documentation]    Verify the structure of specified table
    [Arguments]    ${table_name}
    ${columns}=    Query    
    ...    SELECT column_name, data_type 
    ...    FROM information_schema.columns 
    ...    WHERE table_name = '${table_name}'
    ...    ORDER BY ordinal_position
    [Return]    ${columns}

Optimize Table
    [Documentation]    Run optimization commands on specified table
    [Arguments]    ${table_name}
    Execute SQL String    VACUUM ANALYZE ${table_name}
    Execute SQL String    REINDEX TABLE ${table_name}

Get Table Size
    [Documentation]    Get size information for specified table
    [Arguments]    ${table_name}
    ${result}=    Query    
    ...    SELECT pg_size_pretty(pg_total_relation_size('${table_name}')) as total_size,
    ...           pg_size_pretty(pg_table_size('${table_name}')) as table_size,
    ...           pg_size_pretty(pg_indexes_size('${table_name}')) as index_size
    [Return]    ${result[0]}
