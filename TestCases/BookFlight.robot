*** Settings ***
Documentation    How to book a  flight
Library    SeleniumLibrary

*** Variables ***

${browser}      chrome
${url}      https://www.phptravels.net/flights
${Destination_From}     xpath:(//input[@placeholder='Flying From'])[1]
${Element_ToDestination}    xpath:(//input[@placeholder='To Destination'])[1]
${DestinationLocation}      Banak
${ToDestination}         Goa
${DateElement}      id:departure
${Month Text}   February 2022
${NextButton}       xpath://div[2]/div[1]/table/thead/tr[1]/th[3]/i
${monthElement}     (//div[@class='datepicker dropdown-menu']/div[1][@class='datepicker-days']/table[1]/thead[1]/tr[1]/th[2])[1]

*** Test Cases ***

Select Radio Button
    open browser    ${url}    ${browser}
    set browser implicit wait    10s
    maximize browser window
    Accept Cookies
    sleep    3
    Select Round Trip
    scroll page
    Select From Destination
    Select To Destination
    Select Departure Date
    wait until


*** Keywords ***

Select Round Trip
    click element     xpath://label[@for='one-way']

Select From Destination
    input text      ${Destination_From}     banga
    @{ListAutosearchelemenst}   get webelements    xpath://div/div/div[1]/strong
    FOR     ${element}  IN      @{ListAutosearchelemenst}
            ${Text}=    get text    ${element}
            scroll element into view    ${element}
            run keyword if    '${Text}' == '${DestinationLocation}'      click element    ${element}
            exit for loop if    '${Text}' == '${DestinationLocation}'
    END

Select To Destination
    input text      ${Element_ToDestination}  Go
    @{ListWebElements}      get webelements     xpath://div/div/div[1]/strong
    FOR     ${element}  IN      @{ListWebElements}
            ${GrabTxt}  get text    ${element}
            scroll element into view    ${element}
            run keyword if    '${GrabTxt}' == '${ToDestination}'      click element    ${element}
            exit for loop if       '${GrabTxt}' == '${ToDestination}'
    END

Accept Cookies
    click button    xpath://*[contains(text(),'Got It')]

scroll page
    execute javascript    window.scrollTo(0,200)

Select Departure Date
    click element       ${DateElement}
    sleep    5

    FOR     ${i}    IN RANGE        12

        ${MonthDisplayed}   get text    ${monthElement}
        log to console    ${MonthDisplayed}
        run keyword if    '${MonthDisplayed}' != '${Month Text}'     click element       xpath:(//*[@class='icon mdi mdi-long-arrow-right'])[1]
        exit for loop if   '${MonthDisplayed}' == '${Month Text}'
    END










