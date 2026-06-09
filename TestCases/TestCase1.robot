*** Settings ***
Documentation   This script will validate if we get an error message while trying to login using incorrect credentials
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://www.bluesky.as/my-account/
${EmailElement}     xpath:(//input[@name='xoo-el-username'])[1]
${PasswordElement}  xpath:(//input[@name='xoo-el-password'])[1]
${LoginButton}  xpath:(//button[@class='button btn xoo-el-action-btn xoo-el-login-btn'])[1]
${ExpectedLoginFailureText}   Incorrect Email or Username. Lost your password?
${response}

*** Test Cases ***

LoginTest
    open browser    ${url}  ${browser}
    #set selenium speed  3
    maximize browser window
    element should be visible    ${EmailElement}
    element should be visible    ${PasswordElement}
    element should be enabled    ${EmailElement}
    Provide Email and Password
    sleep    3
    Submit Credentials
    ${response}   get text    css:div.xoo-el-notice-error
    should be equal as strings    ${response}   ${ExpectedLoginFailureText}
    close browser


*** Keywords ***

Provide Email and Password
    input text    ${EmailElement}    jeet.zaper@gmail.com
    input text    ${PasswordElement}   password@1
Submit Credentials
    click element  ${LoginButton}
