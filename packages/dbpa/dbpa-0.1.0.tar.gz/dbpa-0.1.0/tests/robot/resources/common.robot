*** Settings ***
Documentation     Common resources and variables for DBPA tests
Library          OperatingSystem
Library          Process
Library          RequestsLibrary
Library          DatabaseLibrary
Library          SeleniumLibrary

*** Variables ***
${TEMP_DIR}      ${CURDIR}${/}..${/}..${/}temp
${VENV_DIR}      ${TEMP_DIR}${/}venv
${PACKAGE_DIR}   ${CURDIR}${/}..${/}..${/}..
${PYTHON_CMD}    python

*** Keywords ***
Setup Test Environment
    Create Directory    ${TEMP_DIR}
    ${result}=    Run Process    ${PYTHON_CMD}    -m    venv    ${VENV_DIR}
    Should Be Equal As Integers    ${result.rc}    0
    ${pip}=    Set Variable    ${VENV_DIR}${/}Scripts${/}pip
    ${result}=    Run Process    ${pip}    install    -e    ${PACKAGE_DIR}    shell=True
    Should Be Equal As Integers    ${result.rc}    0
    Set Suite Variable    ${PIP_CMD}    ${pip}

Teardown Test Environment
    Remove Directory    ${TEMP_DIR}    recursive=True

Install Package Dependencies
    [Arguments]    ${requirements_file}
    ${result}=    Run Process    ${PIP_CMD}    install    -r    ${requirements_file}    shell=True
    Should Be Equal As Integers    ${result.rc}    0

Verify Package Installation
    ${result}=    Run Process    ${PYTHON_CMD}    -c    import dbpa    shell=True
    Should Be Equal As Integers    ${result.rc}    0

Start Streamlit App
    ${result}=    Start Process    streamlit    run    ${PACKAGE_DIR}${/}src${/}dbpa${/}streamlit${/}app.py    shell=True
    Sleep    5s    # Wait for app to start
    Set Suite Variable    ${STREAMLIT_PROCESS}    ${result}

Stop Streamlit App
    Terminate Process    ${STREAMLIT_PROCESS}

Open Browser To Streamlit
    Open Browser    http://localhost:8501    chrome
    Maximize Browser Window
    Set Selenium Speed    0.5s

Close Browser Session
    Close Browser
