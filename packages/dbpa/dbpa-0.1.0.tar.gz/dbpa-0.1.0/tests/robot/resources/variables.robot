*** Variables ***
# Database Configuration
${DB_HOST}         cat670aihdrkt1.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com
${DB_PORT}         5432
${DB_NAME}         d21q7sr3ble3eq
${DB_USER}         u3b39k1h1djh6v
${DB_PASS}         pe905cee8d4566aa6576b85ec9683f0e6cc79234cbd344f2d7277a5b8024c4116

# API Configuration
${API_BASE_URL}    http://localhost:8501
${API_TIMEOUT}     10

# Browser Configuration
${BROWSER}         chrome
${DELAY}           0.5

# Test Data
${TEST_QUERY}      Show me all tables in the database
${TEST_TABLE}      users
${TEST_COLUMN}     username

# Expected Results
${EXPECTED_TITLE}    DBPA - Database Personal Assistant
${SUCCESS_MESSAGE}   Query executed successfully
