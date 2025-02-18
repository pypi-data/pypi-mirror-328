*** Settings ***
Documentation     Test suite for AI integration features
Resource          ../../resources/common.robot
Resource          ../../resources/variables.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment
Test Setup       Start Streamlit App
Test Teardown    Stop Streamlit App

*** Test Cases ***
Test Query Generation
    [Documentation]    Test AI-powered SQL query generation
    [Tags]    ai    nlp
    Given Open Browser To Streamlit
    When Input Text    id=nlquery    Show all users who registered last month
    And Click Button    Generate SQL
    Then Page Should Contain    SELECT *
    And Page Should Contain    FROM users
    And Page Should Contain    WHERE
    [Teardown]    Close Browser

Test Query Explanation
    [Documentation]    Test AI explanation of SQL queries
    [Tags]    ai    nlp
    Given Open Browser To Streamlit
    When Input Text    id=sqlquery    SELECT * FROM users WHERE created_at >= NOW() - INTERVAL '1 month'
    And Click Button    Explain Query
    Then Page Should Contain    This query retrieves all users
    And Page Should Contain    registered in the last month
    [Teardown]    Close Browser

Test Query Optimization
    [Documentation]    Test AI-powered query optimization
    [Tags]    ai    performance
    Given Open Browser To Streamlit
    When Input Text    id=sqlquery    SELECT * FROM users u JOIN orders o ON u.id = o.user_id WHERE u.country = 'US'
    And Click Button    Optimize Query
    Then Page Should Contain    Optimized Query
    And Page Should Contain    CREATE INDEX
    [Teardown]    Close Browser

Test Error Explanation
    [Documentation]    Test AI explanation of database errors
    [Tags]    ai    error-handling
    Given Open Browser To Streamlit
    When Input Text    id=sqlquery    SELECT * FROM non_existent_table
    And Click Button    Execute Query
    Then Page Should Contain    Error Explanation
    And Page Should Contain    The table 'non_existent_table' does not exist
    [Teardown]    Close Browser
