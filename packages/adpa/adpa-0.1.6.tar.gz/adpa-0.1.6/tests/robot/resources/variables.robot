*** Variables ***
# Application Settings
${BASE_URL}         http://localhost:8501
${BROWSER}          chrome
${SELENIUM_SPEED}    0.1

# Database Configuration
${DB_HOST}         localhost
${DB_PORT}         5432
${DB_USER}         adpa_test
${DB_PASSWORD}     test_password
${DATABASE_NAME}   adpa_test

# Test Data
@{SAMPLE_QUERIES}    Show me all employees    List departments with more than 5 employees
...                  What is the average salary    Who reports to John Smith
@{EXPECTED_TABLES}    employees    departments    salaries    reporting_structure

# Timeouts
${TIMEOUT_SHORT}    5s
${TIMEOUT_MEDIUM}   10s
${TIMEOUT_LONG}    30s

# UI Elements
${QUERY_INPUT}     id=query-input
${SUBMIT_BUTTON}   id=submit-query
${SQL_OUTPUT}      id=sql-output
${RESULTS_TABLE}   id=results-table
${ERROR_MESSAGE}   id=error-message
${HISTORY_LIST}    id=history-list
${SAVE_BUTTON}     id=save-query
${CLEAR_BUTTON}    id=clear-history
