*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://www.bluesky.as/
${browser}  chrome
${HeaderMenus}      xpath://ul[@id='menu-top-header-menu']/li/a
${BusinessMenu}     Business



*** Test Cases ***
Validate the Header menu
    open browser   ${url}   ${browser}
    maximize browser window
    Validation of Business Menu
    close browser

*** Keywords ***
Validation of Business Menu
    @{ListWebElements}  get webelements    xpath://ul[@id='menu-top-header-menu']/li/a
    FOR     ${element}    IN    @{ListWebElements}
            ${Text}=   Get Text    ${element}
            Run Keyword If    '${Text}' == '${BusinessMenu}'    log to console      Business Menu is successfully validated
    END
