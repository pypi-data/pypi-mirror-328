*** Settings ***
Documentation     Test suite for Database Agent functionality
Resource          ../resources/common.resource
Resource          ../resources/database.resource
Library           DatabaseLibrary
Library           OperatingSystem
Library           Collections

Suite Setup       Connect To Database
Suite Teardown    Disconnect From Database

*** Variables ***
${TEST_TABLE}     test_table
${BACKUP_TABLE}   test_table_backup

*** Keywords ***
Connect To Database
    Connect To Database    psycopg2    
    ...    database=${DATABASE NAME}    
    ...    user=${DATABASE USER}    
    ...    password=${DATABASE PASSWORD}    
    ...    host=${DATABASE HOST}    
    ...    port=${DATABASE PORT}

Create Test Table
    [Arguments]    ${table_name}
    Execute SQL String    
    ...    CREATE TABLE IF NOT EXISTS ${table_name} (
    ...    id SERIAL PRIMARY KEY,
    ...    name VARCHAR(100),
    ...    value INTEGER
    ...    )

Drop Test Table
    [Arguments]    ${table_name}
    Execute SQL String    DROP TABLE IF EXISTS ${table_name}

Insert Test Data
    [Arguments]    ${table_name}    ${name}    ${value}
    Execute SQL String    
    ...    INSERT INTO ${table_name} (name, value) 
    ...    VALUES ('${name}', ${value})

Backup Table
    [Arguments]    ${table_name}    ${backup_table}
    Execute SQL String    
    ...    CREATE TABLE ${backup_table} AS 
    ...    SELECT * FROM ${table_name}

Restore Table
    [Arguments]    ${backup_table}    ${table_name}
    Execute SQL String    
    ...    TRUNCATE TABLE ${table_name};
    ...    INSERT INTO ${table_name} SELECT * FROM ${backup_table}

Optimize Table
    [Arguments]    ${table_name}
    Execute SQL String    VACUUM ANALYZE ${table_name}
    Execute SQL String    REINDEX TABLE ${table_name}

Get Table Size
    [Arguments]    ${table_name}
    ${result}=    Query    SELECT pg_total_relation_size('${table_name}')
    [Return]    ${result[0]}

Verify Table Structure
    [Arguments]    ${table_name}
    ${columns}=    Query    
    ...    SELECT column_name, data_type 
    ...    FROM information_schema.columns 
    ...    WHERE table_name = '${table_name}'
    ...    ORDER BY ordinal_position
    [Return]    ${columns}

Get Row Count
    [Arguments]    ${table_name}
    ${result}=    Query    SELECT COUNT(*) FROM ${table_name}
    [Return]    ${result[0][0]}

*** Test Cases ***
Test Database Connection
    [Documentation]    Test database connection and basic query
    [Tags]    database    smoke
    ${result}=    Query    SELECT 1
    Should Be Equal As Integers    ${result[0][0]}    1

Test Create And Drop Table
    [Documentation]    Test creating and dropping tables
    [Tags]    database    tables
    Create Test Table    ${TEST_TABLE}
    Table Must Exist    ${TEST_TABLE}
    Drop Test Table    ${TEST_TABLE}
    Table Must Not Exist    ${TEST_TABLE}

Test Insert And Query Data
    [Documentation]    Test inserting and querying data
    [Tags]    database    data
    Create Test Table    ${TEST_TABLE}
    Insert Test Data    ${TEST_TABLE}    test_name    100
    ${result}=    Query    SELECT * FROM ${TEST_TABLE} WHERE name = 'test_name'
    Should Be Equal As Strings    ${result[0][1]}    test_name
    Should Be Equal As Integers    ${result[0][2]}    100
    [Teardown]    Drop Test Table    ${TEST_TABLE}

Test Backup And Restore
    [Documentation]    Test backing up and restoring tables
    [Tags]    database    backup
    Create Test Table    ${TEST_TABLE}
    Insert Test Data    ${TEST_TABLE}    original    100
    Backup Table    ${TEST_TABLE}    ${BACKUP_TABLE}
    Execute SQL String    UPDATE ${TEST_TABLE} SET value = 200 WHERE name = 'original'
    Restore Table    ${BACKUP_TABLE}    ${TEST_TABLE}
    ${result}=    Query    SELECT value FROM ${TEST_TABLE} WHERE name = 'original'
    Should Be Equal As Integers    ${result[0][0]}    100
    [Teardown]    Run Keywords
    ...    Drop Test Table    ${TEST_TABLE}    AND
    ...    Drop Test Table    ${BACKUP_TABLE}

Test Table Information
    [Documentation]    Test retrieving table information
    [Tags]    database    metadata
    Create Test Table    ${TEST_TABLE}
    ${columns}=    Verify Table Structure    ${TEST_TABLE}
    Length Should Be    ${columns}    3    # id, name, value
    # Verify column types
    Should Be Equal As Strings    ${columns[0][0]}    id
    Should Be Equal As Strings    ${columns[1][0]}    name
    Should Be Equal As Strings    ${columns[2][0]}    value
    [Teardown]    Drop Test Table    ${TEST_TABLE}

Test Database Optimization
    [Documentation]    Test database optimization commands
    [Tags]    database    maintenance
    Create Test Table    ${TEST_TABLE}
    Optimize Table    ${TEST_TABLE}
    ${size_info}=    Get Table Size    ${TEST_TABLE}
    Should Not Be Empty    ${size_info}[0]    # total_size
    [Teardown]    Drop Test Table    ${TEST_TABLE}

Test Multiple Operations
    [Documentation]    Test multiple database operations in sequence
    [Tags]    database    integration
    # Create and populate table
    Create Test Table    ${TEST_TABLE}
    Insert Test Data    ${TEST_TABLE}    record1    100
    Insert Test Data    ${TEST_TABLE}    record2    200
    
    # Verify initial state
    ${count}=    Get Row Count    ${TEST_TABLE}
    Should Be Equal As Integers    ${count}    2
    
    # Backup and modify
    Backup Table    ${TEST_TABLE}    ${BACKUP_TABLE}
    Execute SQL String    DELETE FROM ${TEST_TABLE} WHERE name = 'record1'
    
    # Verify modification
    ${count}=    Get Row Count    ${TEST_TABLE}
    Should Be Equal As Integers    ${count}    1
    
    # Restore and verify
    Restore Table    ${BACKUP_TABLE}    ${TEST_TABLE}
    ${count}=    Get Row Count    ${TEST_TABLE}
    Should Be Equal As Integers    ${count}    2
    
    [Teardown]    Run Keywords
    ...    Drop Test Table    ${TEST_TABLE}    AND
    ...    Drop Test Table    ${BACKUP_TABLE}
