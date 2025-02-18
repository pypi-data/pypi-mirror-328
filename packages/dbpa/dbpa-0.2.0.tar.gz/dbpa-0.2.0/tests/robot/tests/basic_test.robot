*** Settings ***
Documentation     Basic test to verify Robot Framework setup

*** Test Cases ***
Basic Test
    [Documentation]    Simple test to verify Robot Framework is working
    Log    Hello, Robot Framework!
    Should Be Equal    ${1}    ${1}
