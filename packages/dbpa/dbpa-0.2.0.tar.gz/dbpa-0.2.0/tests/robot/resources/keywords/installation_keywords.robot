*** Settings ***
Documentation     Keywords for package installation testing
Resource          ../common.robot
Resource          ../variables.robot

*** Keywords ***
Package Should Be Importable
    [Documentation]    Verify that the DBPA package can be imported
    ${result}=    Run Process    ${VENV_PYTHON}    -c    import dbpa
    Should Be Equal As Integers    ${result.rc}    0
    Log    Successfully imported dbpa package

Create Test Virtual Environment
    [Documentation]    Create a fresh virtual environment for testing
    [Arguments]    ${venv_dir}
    Create Directory    ${venv_dir}
    ${result}=    Run Process    python    -m    venv    ${venv_dir}
    Should Be Equal As Integers    ${result.rc}    0
    [Return]    ${venv_dir}

Install Package In Environment
    [Documentation]    Install DBPA package in the specified environment
    [Arguments]    ${venv_dir}    ${package_dir}
    ${pip}=    Set Variable    ${venv_dir}${/}Scripts${/}pip
    ${result}=    Run Process    ${pip}    install    -e    ${package_dir}
    Should Be Equal As Integers    ${result.rc}    0
    [Return]    ${result.stdout}

Verify Package Version Format
    [Documentation]    Verify that package version follows semantic versioning
    [Arguments]    ${version}
    Should Match Regexp    ${version}    ^\\d+\\.\\d+\\.\\d+
    Log    Valid package version: ${version}

Check Required Dependencies
    [Documentation]    Verify that required dependencies are installed
    [Arguments]    ${pip_freeze_output}    @{required_packages}
    FOR    ${package}    IN    @{required_packages}
        Should Contain    ${pip_freeze_output}    ${package}
        Log    Found required package: ${package}
    END
