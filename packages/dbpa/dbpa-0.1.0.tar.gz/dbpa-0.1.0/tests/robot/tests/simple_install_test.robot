*** Settings ***
Documentation     Simple installation test for DBPA package
Library          OperatingSystem
Library          Process

*** Test Cases ***
Test Package Import
    [Documentation]    Verify that DBPA package can be imported
    Log    Starting package import test
    Log    Current directory: ${CURDIR}
    ${status}    ${output}=    Run And Return Rc And Output    python -c "import dbpa"
    Log    Command status: ${status}
    Log    Command output: ${output}
    Should Be Equal As Integers    ${status}    0
    
Test Python Environment
    [Documentation]    Verify Python environment
    Log    Checking Python environment
    ${status}    ${output}=    Run And Return Rc And Output    python --version
    Log    Python version: ${output}
    Should Be Equal As Integers    ${status}    0
    
    ${status}    ${output}=    Run And Return Rc And Output    pip list
    Log    Installed packages: ${output}
    Should Be Equal As Integers    ${status}    0
