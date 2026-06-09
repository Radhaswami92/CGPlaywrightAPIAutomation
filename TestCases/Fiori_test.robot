*** Settings ***
Library    SeleniumLibrary




*** Variables ***
${url}      https://ui5.sap.com/1.54.3/test-resources/sap/tnt/demokit/toolpageapp/webapp/index.html
${browser}      chrome



*** Test Cases ***

Run Test for Fiori Application
    Given user opens browser and hit the fiori URL
    And user clicks on settings in the home page
    When user edit all the shop owner details
    Then user saves the details successfully


*** Keywords ***
user opens browser and hit the fiori URL
    open browser    ${url}      ${browser}
    maximize browser window
    sleep   3

User clicks on Settings in the home page
    click element    xpath://li[@id='__item1-__list0-1']

User edit all the shop owner details
           #css:div.sapTntToolPageMainContentWrapper
    clear element text    xpath://div[@id='toolpageapp---detailSettings--firstNameInput']
    input text    xpath://div[@id='toolpageapp---detailSettings--firstNameInput']       Peter
    input text    xpath://input[@id='toolpageapp---detailSettings--lastNameInput-inner']    Parker
    input text    xpath://input[@id='toolpageapp---detailSettings--addressStreetInput-inner']       Park Street
    input text    xpath://input[@id='toolpageapp---detailSettings--addressTownInput-inner']     783324 New California
    input text    xpath://input[@id='toolpageapp---detailSettings--addressCountryInput-inner']      United Kingdom
    input text    xpath://input[@id='toolpageapp---detailSettings--phoneNumberInput-inner']     +91 9654729888
    input text    xpath://input[@id='toolpageapp---detailSettings--faxNumberInput-inner']       +89 8928929892
    input text    xpath://input[@id='toolpageapp---detailSettings--emailInput-inner']       jeet.zaper@gmail.com

User saves the details successfully
    click element    xpath://span[@id='toolpageapp---detailSettings--save-content']
    wait until page contains    Save was pressed
    close browser


