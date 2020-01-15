*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.

Library     SeleniumLibrary


*** Variables ***
${SERVER}         www.hepsiburada.com
${BROWSER}        Chrome
${DELAY}          0.5
${VALID USER}     demo
${VALID PASSWORD}    mode
${LOGIN URL}      https://${SERVER}/uyelik/giris?ReturnUrl=%2f
${WELCOME URL}    https://${SERVER}/
${ERROR URL}      https://${SERVER}/error.html

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Open Browser To Welcome Page
    Open Browser    ${WELCOME URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    #Login Page Should Be Open

Close Browser
    Terminate all processes
    Close all browsers

Login Page Should Be Open
    Title Should Be    Üye Giriş Sayfası – Hepsiburada.com

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Welcome Page Should Be Open
    Location Should Be    ${WELCOME URL}
    Title Should Be    Welcome Page
