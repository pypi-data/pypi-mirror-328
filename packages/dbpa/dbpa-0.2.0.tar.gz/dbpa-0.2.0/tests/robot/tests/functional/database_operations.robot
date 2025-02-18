*** Settings ***
Documentation     Test suite for database operations using DBPA
Resource          ../../resources/common.robot
Resource          ../../resources/variables.robot
Resource          ../../resources/keywords/database_keywords.robot
Suite Setup       Setup Database Test Environment
Suite Teardown    Teardown Database Test Environment
Test Setup       Connect To Test Database
Test Teardown    Disconnect From Database
Force Tags       database    functional
Default Tags     smoke    critical    stable

*** Keywords ***
Setup Database Test Environment
    Setup Test Environment
    Create Test Schema
    Create Sample Tables
    Insert Sample Data

Create Test Schema
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    Execute SQL String    CREATE SCHEMA IF NOT EXISTS test_schema;
    Set Search Path    test_schema
    Disconnect From Database

Create Sample Tables
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    Execute SQL String    
    ...    CREATE TABLE IF NOT EXISTS users (
    ...        id SERIAL PRIMARY KEY,
    ...        username VARCHAR(50) NOT NULL UNIQUE,
    ...        email VARCHAR(100) NOT NULL UNIQUE,
    ...        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ...    )
    Execute SQL String    
    ...    CREATE TABLE IF NOT EXISTS orders (
    ...        id SERIAL PRIMARY KEY,
    ...        user_id INTEGER REFERENCES users(id),
    ...        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ...        total_amount DECIMAL(10,2) NOT NULL
    ...    )
    Disconnect From Database

Insert Sample Data
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    Execute SQL String    
    ...    INSERT INTO users (username, email) VALUES 
    ...    ('testuser1', 'test1@example.com'),
    ...    ('testuser2', 'test2@example.com')
    Execute SQL String    
    ...    INSERT INTO orders (user_id, total_amount) VALUES 
    ...    (1, 100.50),
    ...    (1, 75.25),
    ...    (2, 200.00)
    Disconnect From Database

Teardown Database Test Environment
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}    ${DB_PORT}
    Execute SQL String    DROP SCHEMA IF EXISTS test_schema CASCADE;
    Disconnect From Database
    Teardown Test Environment

*** Test Cases ***
Test Should Execute Simple Natural Language Query
    [Documentation]    Test executing a simple natural language query
    [Tags]    nlp    query    smoke
    Given Start Streamlit App
    When Execute Natural Language Query    Show all users
    Then Page Should Contain    testuser1
    And Page Should Contain    test1@example.com
    [Teardown]    Stop Streamlit App

Test Should Create New Table Using Natural Language
    [Documentation]    Test creating a new table using natural language
    [Tags]    ddl    schema    high
    ${query}=    Set Variable    Create a new table called customers with columns id (primary key), name (text), and email (text)
    When Execute Natural Language Query    ${query}
    Then Table Must Exist    customers
    And Check If Exists In Database    
    ...    SELECT column_name FROM information_schema.columns 
    ...    WHERE table_name = 'customers' AND column_name IN ('id', 'name', 'email')

Test Should Insert Data Using Natural Language
    [Documentation]    Test inserting data using natural language
    [Tags]    dml    data    high
    ${query}=    Set Variable    Insert into users a new user with username 'newuser' and email 'new@example.com'
    When Execute Natural Language Query    ${query}
    Then Check If Exists In Database    
    ...    SELECT * FROM users WHERE username = 'newuser' AND email = 'new@example.com'

Test Should Handle Complex Joins
    [Documentation]    Test handling complex join operations
    [Tags]    nlp    query    medium
    ${query}=    Set Variable    Show all users with their total order amounts
    When Execute Natural Language Query    ${query}
    Then Page Should Contain    testuser1
    And Page Should Contain    175.75    # Sum of testuser1's orders
    And Page Should Contain    testuser2
    And Page Should Contain    200.00    # testuser2's order amount

Test Should Handle Data Updates
    [Documentation]    Test updating existing data
    [Tags]    dml    data    high
    ${query}=    Set Variable    Update email to 'updated@example.com' for user with username 'testuser1'
    When Execute Natural Language Query    ${query}
    Then Check If Exists In Database    
    ...    SELECT * FROM users WHERE username = 'testuser1' AND email = 'updated@example.com'

Test Should Handle Data Deletion
    [Documentation]    Test deleting data
    [Tags]    dml    data    high
    ${query}=    Set Variable    Delete orders for user with username 'testuser1'
    When Execute Natural Language Query    ${query}
    ${count}=    Row Count    SELECT * FROM orders WHERE user_id = 1
    Should Be Equal As Integers    ${count}    0

Test Should Handle Error Cases
    [Documentation]    Test error handling for invalid queries
    [Tags]    error    negative    medium
    @{invalid_queries}=    Create List
    ...    Insert into nonexistent_table values (1, 'test')
    ...    Select from users where nonexistent_column = 'value'
    ...    Create table users (id int)    # Duplicate table
    FOR    ${query}    IN    @{invalid_queries}
        ${result}=    Execute Natural Language Query    ${query}
        Should Contain    ${result}    error
    END

Test Should Handle Complex Aggregations
    [Documentation]    Test handling complex aggregation queries
    [Tags]    nlp    query    medium
    ${query}=    Set Variable    Show total order amount per user with their email addresses
    When Execute Natural Language Query    ${query}
    Then Page Should Contain    test1@example.com
    And Page Should Contain    175.75    # Sum of testuser1's orders
    And Page Should Contain    test2@example.com
    And Page Should Contain    200.00    # testuser2's order amount

Test Should Support Transaction Rollback
    [Documentation]    Test transaction rollback functionality
    [Tags]    transaction    data    high
    Start Transaction
    Execute SQL String    DELETE FROM orders
    Row Count Is 0    SELECT * FROM orders
    Rollback Transaction
    Row Count Is Equal    SELECT * FROM orders    3    # Original number of orders
