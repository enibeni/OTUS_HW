*** Settings ***
Library  Selenium2Library
Library  Selenium2Library

*** Variables ***
${URL}          https://demo23.opencart.pro/admin
${BROWSER}      Chrome


*** Test Cases ***
The user can open AdminPanel by Chrome
        Open AdminPanel  Chrome  demo  demo
        Welcome Page Should Be Open
        Close test browser
The user can not open AdminPanel with wrong password
        Open AdminPanel  Chrome  demo  wrong
        AdminPanel Page Should Be Open
        Close test browser
The user can not open AdminPanel with wrong login
        Open AdminPanel  Chrome  wrong  wrong
        AdminPanel Page Should Be Open
        Close test browser


*** Keywords ***
Open AdminPanel
    [Arguments]      ${BROWSER1}    ${LOGIN}    ${PASSWORD}
    Open browser    ${URL}   ${BROWSER1}
    Input Text      id:input-username     ${LOGIN}
    Input Text      id:input-password     ${PASSWORD}
    Click Button    css:button[type='submit']


AdminPanel Page Should Be Open
    Title Should Be    Авторизация


Welcome Page Should Be Open
    Title Should Be    Панель состояния


Close test browser
    Close browser