*** Settings ***
Documentation     Technical tests for database operations
Resource          ../../resources/database.resource
Library           DatabaseLibrary
Library           OperatingSystem
Library           Collections

Suite Setup       Connect To Database
Suite Teardown    Disconnect From Database

*** Variables ***
${TEST_TABLE}     test_table
${BACKUP_TABLE}   test_table_backup

*** Test Cases ***
Test Connection Pool Configuration
    [Documentation]    Test database connection pool settings
    [Tags]    technical    connection    pool
    ${pool_size}=    Query    SHOW max_connections
    Should Be True    ${pool_size[0][0]} > 0
    ${active_connections}=    Query    SELECT count(*) FROM pg_stat_activity
    Should Be True    ${active_connections[0][0]} <= ${pool_size[0][0]}

Test Table Indexing Performance
    [Documentation]    Test index creation and query performance
    [Tags]    technical    performance    index
    Create Test Table    ${TEST_TABLE}
    # Create index
    Execute SQL String    CREATE INDEX idx_${TEST_TABLE}_name ON ${TEST_TABLE}(name)
    # Test query performance
    ${result}=    Query    EXPLAIN ANALYZE SELECT * FROM ${TEST_TABLE} WHERE name = 'test'
    Should Contain    ${result[0][0]}    Index Scan
    [Teardown]    Drop Test Table    ${TEST_TABLE}

Test Transaction Rollback
    [Documentation]    Test transaction rollback functionality
    [Tags]    technical    transaction
    Create Test Table    ${TEST_TABLE}
    Start Transaction
    Insert Test Data    ${TEST_TABLE}    test_name    100
    Rollback Transaction
    ${count}=    Get Row Count    ${TEST_TABLE}
    Should Be Equal As Integers    ${count}    0
    [Teardown]    Drop Test Table    ${TEST_TABLE}

Test Vacuum Analysis
    [Documentation]    Test vacuum analyze performance
    [Tags]    technical    maintenance
    Create Test Table    ${TEST_TABLE}
    FOR    ${i}    IN RANGE    100
        Insert Test Data    ${TEST_TABLE}    name_${i}    ${i}
    END
    Execute SQL String    VACUUM ANALYZE ${TEST_TABLE}
    ${stats}=    Query    
    ...    SELECT last_vacuum, last_analyze 
    ...    FROM pg_stat_user_tables 
    ...    WHERE relname = '${TEST_TABLE}'
    Should Not Be Empty    ${stats[0][0]}
    [Teardown]    Drop Test Table    ${TEST_TABLE}

Test Concurrent Access
    [Documentation]    Test concurrent database access
    [Tags]    technical    concurrency
    Create Test Table    ${TEST_TABLE}
    # Simulate concurrent access
    FOR    ${i}    IN RANGE    5
        Start Transaction
        Insert Test Data    ${TEST_TABLE}    concurrent_${i}    ${i}
        Commit Transaction
    END
    ${count}=    Get Row Count    ${TEST_TABLE}
    Should Be Equal As Integers    ${count}    5
    [Teardown]    Drop Test Table    ${TEST_TABLE}

Test Error Handling
    [Documentation]    Test database error handling
    [Tags]    technical    error
    Create Test Table    ${TEST_TABLE}
    Run Keyword And Expect Error    *duplicate key*    
    ...    Execute SQL String    
    ...    INSERT INTO ${TEST_TABLE} (id, name, value) 
    ...    VALUES (1, 'test', 100), (1, 'test2', 200)
    [Teardown]    Drop Test Table    ${TEST_TABLE}

Test Large Dataset Performance
    [Documentation]    Test performance with large datasets
    [Tags]    technical    performance    large-data
    Create Test Table    ${TEST_TABLE}
    # Insert large dataset
    FOR    ${i}    IN RANGE    1000
        Insert Test Data    ${TEST_TABLE}    bulk_${i}    ${i}
    END
    # Test batch operations
    ${start_time}=    Get Time    epoch
    Execute SQL String    UPDATE ${TEST_TABLE} SET value = value + 1
    ${end_time}=    Get Time    epoch
    ${duration}=    Evaluate    ${end_time} - ${start_time}
    Should Be True    ${duration} < 5    # Should complete within 5 seconds
    [Teardown]    Drop Test Table    ${TEST_TABLE}
