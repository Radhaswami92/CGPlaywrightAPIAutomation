*** Settings ***
Library     RequestsLibrary
Library     Collections
Library     RequestsLogger


*** Variables ***
${Base_Url}     http://localhost:8080
${Relative_URL}     app/videogames


*** Test Cases ***

Get Request Scenario
    Given user creates session with the base url
    When user creates get request with relative url
    Then user validates the response code successfully



*** Keywords ***
User creates session with the base url
    create session    mysession     ${Base_Url}     verify=true
User creates get request with relative URL
    ${response}=    get request    mysession    ${Relative_URL}
User validates the response code successfully
    ${response}=    get request    mysession    ${Relative_URL}
    ${Actual_status_code}       convert to string    ${response.status_code}
    should be equal    ${Actual_status_code}        200

