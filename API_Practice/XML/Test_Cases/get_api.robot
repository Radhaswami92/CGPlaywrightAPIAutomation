*** Settings ***
Resource    ../Resources/All_Generic.robot
Resource    ../Resources/Resources_get.robot
Library    API_Practice/main.py
Test Setup  Create session for base url

*** Test Cases ***
User succesfully fetches the list of all the videogames
    Given get the complete list of all video games
    When user prints the status code into the console
    And user prints the content into the console
    Then user validates the reponse code returned

