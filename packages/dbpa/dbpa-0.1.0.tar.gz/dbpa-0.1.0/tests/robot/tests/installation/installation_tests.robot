*** Settings ***
Documentation     Test suite for verifying DBPA package installation and functionality
Resource          ${CURDIR}/../../resources/common.robot
Resource          ${CURDIR}/../../resources/variables.robot

Suite Setup       Setup Installation Test Environment
Suite Teardown    Teardown Installation Test Environment
Test Timeout      1 minute

Force Tags        installation
Default Tags      smoke    critical    stable

*** Variables ***
${TEST_VENV_DIR}    ${CURDIR}/../../temp/test_venv

*** Keywords ***
Setup Installation Test Environment
    Create Directory    ${CURDIR}/../../temp
    Remove Directory    ${TEST_VENV_DIR}    recursive=True
    Create Virtual Environment
    Install Package Dependencies

Create Virtual Environment
    ${result}=    Run Process    python    -m    venv    ${TEST_VENV_DIR}
    Should Be Equal As Integers    ${result.rc}    0
    Set Suite Variable    ${VENV_PYTHON}    ${TEST_VENV_DIR}${/}Scripts${/}python
    Set Suite Variable    ${VENV_PIP}    ${TEST_VENV_DIR}${/}Scripts${/}pip

Install Package Dependencies
    ${result}=    Run Process    ${VENV_PIP}    install    -e    ${CURDIR}/../../../..
    Should Be Equal As Integers    ${result.rc}    0
    Log    Package installation output: ${result.stdout}

Teardown Installation Test Environment
    Remove Directory    ${TEST_VENV_DIR}    recursive=True

*** Test Cases ***
Test Should Successfully Install Package In Fresh Environment
    [Documentation]    Verify that DBPA can be installed in a fresh virtual environment
    [Tags]    smoke    installation    critical
    Given Create Virtual Environment
    When Install Package Dependencies
    Then Package Should Be Importable

Test Should Import All Core Modules
    [Documentation]    Verify that all main DBPA modules can be imported
    [Tags]    smoke    installation    critical
    ${modules}=    Create List
    ...    dbpa.core
    ...    dbpa.database
    ...    dbpa.models
    ...    dbpa.utils
    FOR    ${module}    IN    @{modules}
        ${result}=    Run Process    ${VENV_PYTHON}    -c    import ${module}
        Should Be Equal As Integers    ${result.rc}    0
        Log    Successfully imported ${module}
    END

Test Should Access Package Version
    [Documentation]    Verify that package version is accessible and follows semver
    [Tags]    smoke    installation    medium
    ${result}=    Run Process    
    ...    ${VENV_PYTHON}    -c    
    ...    import dbpa; print(dbpa.__version__)
    Should Be Equal As Integers    ${result.rc}    0
    Should Match Regexp    ${result.stdout}    ^\\d+\\.\\d+\\.\\d+
    Log    Package version: ${result.stdout}

Test Should Have Required Dependencies Installed
    [Documentation]    Verify that all required dependencies are installed
    [Tags]    smoke    installation    high
    ${result}=    Run Process    ${VENV_PIP}    freeze
    Should Be Equal As Integers    ${result.rc}    0
    @{required_packages}=    Create List
    ...    streamlit
    ...    psycopg2-binary
    ...    langchain
    ...    openai
    ...    pydantic
    FOR    ${package}    IN    @{required_packages}
        Should Contain    ${result.stdout}    ${package}
        Log    Found required package: ${package}
    END

Test Should Execute CLI Command
    [Documentation]    Verify that DBPA CLI commands are available
    [Tags]    smoke    installation    high
    ${result}=    Run Process    ${VENV_PYTHON}    -m    dbpa    --help
    Should Be Equal As Integers    ${result.rc}    0
    Should Contain    ${result.stdout}    Usage: dbpa
    Log    CLI help output: ${result.stdout}
