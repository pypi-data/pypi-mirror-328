# DBPA Robot Framework Test Suite Documentation
Version: 0.0.2

## Overview
This document describes the Robot Framework test suite for the Database Personal Assistant (DBPA) package. The test suite provides comprehensive testing coverage for database operations, installation verification, and functional testing.

## Test Suite Structure
```
tests/robot/
├── resources/
│   ├── common.robot       # Common keywords and variables
│   ├── variables.robot    # Global test variables
│   └── keywords/
│       ├── database_keywords.robot    # Database-specific keywords
│       └── installation_keywords.robot # Installation-specific keywords
├── tests/
│   ├── functional/
│   │   └── database_operations.robot  # Database operation tests
│   └── installation/
│       └── installation_tests.robot   # Package installation tests
└── results/              # Test execution results
```

## Test Categories

### 1. Installation Tests
Located in `tests/installation/installation_tests.robot`

- Package installation verification
- Module import testing
- Version checking
- Dependency verification
- CLI functionality testing

Tags: `installation`, `smoke`, `critical`

### 2. Database Operations Tests
Located in `tests/functional/database_operations.robot`

#### 2.1 Basic Operations
- Natural language query execution
- Table creation and verification
- Data insertion and retrieval
- Complex join operations

Tags: `database`, `functional`, `smoke`

#### 2.2 Data Manipulation
- Data updates
- Data deletion
- Transaction management
- Error handling

Tags: `dml`, `data`, `transaction`

#### 2.3 Schema Operations
- Schema creation
- Table management
- Column modifications

Tags: `ddl`, `schema`

## Test Environment Setup

### Prerequisites
- Python 3.11.9 or higher
- PostgreSQL database
- Robot Framework and required libraries

### Environment Variables
```
DB_HOST=cat670aihdrkt1.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com
DB_PORT=5432
DB_NAME=d21q7sr3ble3eq
DB_USER=u3b39k1h1djh6v
```

### Required Python Packages
```
robotframework>=6.1.1
robotframework-databaselibrary>=1.4.0
robotframework-seleniumlibrary>=6.1.3
psycopg2-binary>=2.9.9
```

## Running Tests

### Running All Tests
```bash
robot --outputdir results tests/robot/tests/
```

### Running Specific Test Categories
```bash
# Run installation tests
robot --outputdir results tests/robot/tests/installation/

# Run database tests
robot --outputdir results tests/robot/tests/functional/database_operations.robot

# Run smoke tests only
robot --outputdir results --include smoke tests/robot/tests/
```

### Test Tags
- `smoke`: Basic functionality tests
- `critical`: Essential functionality
- `high`: High-priority tests
- `medium`: Medium-priority tests
- `database`: Database-related tests
- `functional`: Functional tests
- `installation`: Installation tests
- `ddl`: Data Definition Language tests
- `dml`: Data Manipulation Language tests
- `nlp`: Natural Language Processing tests
- `error`: Error handling tests
- `transaction`: Transaction management tests

## Test Reports
Test results are generated in the `results` directory:
- `report.html`: Detailed test execution report
- `log.html`: Test execution log with debug information
- `output.xml`: Raw test output data

## Version History

### 0.0.2 (2025-02-17)
- Added comprehensive database operation tests
- Implemented transaction testing
- Added error handling scenarios
- Enhanced test organization and documentation
- Added support for complex queries and joins

### 0.0.1 (Initial Release)
- Basic installation tests
- Simple database operations
- Package verification tests

## Best Practices

### 1. Test Organization
- Use BDD-style test cases (Given-When-Then)
- Group related tests using tags
- Maintain clear test documentation
- Follow single responsibility principle

### 2. Database Testing
- Use isolated test schemas
- Clean up test data after execution
- Verify both success and error cases
- Test transaction boundaries

### 3. Code Quality
- Follow Robot Framework style guide
- Use descriptive test and keyword names
- Maintain test independence
- Implement proper setup and teardown

## Troubleshooting

### Common Issues
1. Database Connection Failures
   - Verify environment variables
   - Check database credentials
   - Ensure network connectivity

2. Test Setup Issues
   - Verify Python version
   - Check required packages
   - Ensure proper permissions

3. Test Execution Errors
   - Review test logs
   - Check database state
   - Verify test dependencies

## Contributing
1. Follow the established test structure
2. Add appropriate tags to new tests
3. Update documentation for new features
4. Maintain backward compatibility
5. Add test cases for bug fixes

## Future Enhancements
1. Add performance testing
2. Implement parallel test execution
3. Add more complex database scenarios
4. Enhance error handling coverage
5. Add security testing scenarios
