*** Settings ***
Documentation     Keywords for database operations testing
Library          DatabaseLibrary
Library          OperatingSystem
Library          Process
Resource         ../common.robot
Resource         ../variables.robot

*** Keywords ***
Connect To Test Database
    [Documentation]    Connect to the test database using environment variables
    Connect To Database    psycopg2    
    ...    ${DB_NAME}    
    ...    ${DB_USER}    
    ...    ${DB_PASS}    
    ...    ${DB_HOST}    
    ...    ${DB_PORT}
    Log    Connected to database: ${DB_NAME} at ${DB_HOST}

Create Test Schema
    [Documentation]    Create a test schema for database operations
    Execute SQL String    
    ...    CREATE SCHEMA IF NOT EXISTS test_schema;
    Set Search Path    test_schema
    Log    Created and set test schema: test_schema

Create Sample Tables
    [Documentation]    Create sample tables for testing
    Execute SQL String    
    ...    CREATE TABLE IF NOT EXISTS users (
    ...        id SERIAL PRIMARY KEY,
    ...        username VARCHAR(50) NOT NULL,
    ...        email VARCHAR(100) NOT NULL,
    ...        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ...    );
    
    Execute SQL String    
    ...    CREATE TABLE IF NOT EXISTS orders (
    ...        id SERIAL PRIMARY KEY,
    ...        user_id INTEGER REFERENCES users(id),
    ...        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ...        total_amount DECIMAL(10,2) NOT NULL
    ...    );
    Log    Created sample tables: users, orders

Insert Sample Data
    [Documentation]    Insert sample data into test tables
    Execute SQL String    
    ...    INSERT INTO users (username, email) VALUES 
    ...    ('testuser1', 'test1@example.com'),
    ...    ('testuser2', 'test2@example.com');
    
    Execute SQL String    
    ...    INSERT INTO orders (user_id, total_amount) VALUES 
    ...    (1, 100.50),
    ...    (1, 75.25),
    ...    (2, 200.00);
    Log    Inserted sample data into tables

Clean Test Schema
    [Documentation]    Clean up test schema and all its objects
    Execute SQL String    DROP SCHEMA IF EXISTS test_schema CASCADE;
    Log    Cleaned up test schema

Wait For Database Operation
    [Documentation]    Wait for database operation to complete with timeout
    [Arguments]    ${timeout}=5s
    Sleep    ${timeout}
    Log    Waited ${timeout} for database operation

Verify Table Exists
    [Documentation]    Verify that a table exists in the database
    [Arguments]    ${table_name}
    Table Must Exist    ${table_name}
    Log    Table exists: ${table_name}

Verify Record Count
    [Documentation]    Verify the number of records in a table
    [Arguments]    ${table_name}    ${expected_count}
    ${count}=    Row Count    SELECT * FROM ${table_name}
    Should Be Equal As Integers    ${count}    ${expected_count}
    Log    Table ${table_name} has ${count} records

Execute Natural Language Query
    [Documentation]    Execute a natural language query using DBPA
    [Arguments]    ${query}
    ${result}=    Run Process    
    ...    ${VENV_PYTHON}    -m    dbpa    query    ${query}
    Should Be Equal As Integers    ${result.rc}    0
    [Return]    ${result.stdout}
