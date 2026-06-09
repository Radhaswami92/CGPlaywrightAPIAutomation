*** Settings ***
Library    FakerLibrary     locale=en_US
Library     Dialogs





*** Variables ***



*** Test Cases ***
Test with Fake data generation

    Comment    Generate Address
    ${address}=    Address
    log to console    ${address}






*** Keywords ***

