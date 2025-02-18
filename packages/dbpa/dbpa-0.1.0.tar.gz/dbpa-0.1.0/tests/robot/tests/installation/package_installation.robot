*** Settings ***
Documentation     Test suite for verifying DBPA package installation
Resource          ${CURDIR}/../../resources/common.robot
Suite Setup      Setup Test Environment
Suite Teardown   Teardown Test Environment

*** Test Cases ***
Test Package Installation In Fresh Environment
    [Documentation]    Verify that DBPA can be installed in a fresh virtual environment
    [Tags]    installation    smoke
    Given Setup Test Environment
    When Install Package Dependencies    ${PACKAGE_DIR}${/}requirements.txt
    Then Verify Package Installation

Test Package Import Functionality
    [Documentation]    Verify that all main DBPA modules can be imported
    [Tags]    installation    smoke
    ${result}=    Run Process    
    ...    ${PYTHON_CMD}    -c
    ...    from dbpa.core import ConfigLoader; from dbpa.database import DatabaseConnection; from dbpa.models import AppSettings    
    ...    shell=True
    Should Be Equal As Integers    ${result.rc}    0

Test CLI Command Availability
    [Documentation]    Verify that DBPA CLI commands are available
    [Tags]    installation    smoke
    ${result}=    Run Process    dbpa    --help    shell=True
    Should Be Equal As Integers    ${result.rc}    0
    Should Contain    ${result.stdout}    Usage: dbpa

Test Package Version
    [Documentation]    Verify that package version is accessible
    [Tags]    installation    smoke
    ${result}=    Run Process    
    ...    ${PYTHON_CMD}    -c    
    ...    import dbpa; print(dbpa.__version__)    
    ...    shell=True
    Should Be Equal As Integers    ${result.rc}    0
    Should Match Regexp    ${result.stdout}    \\d+\\.\\d+\\.\\d+
