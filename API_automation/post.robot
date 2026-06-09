*** Settings ***
Library     RequestsLibrary
Library    Collections

*** Variables ***

${Base_Url}     http://localhost:8080/
${Relative_url}     app/videogames
${Relative_url_get_videogame}   app/videogames/36
${response}
${expected_response_message}    Record Added Successfully
${Expected_response_code}   200
${response_get}
${response_put}
${Relative_url_put_videogame}   app/videogames/37
${response_delete}
${relative_Url_delete}      app/videogames/120



*** Test Cases ***
Test-C1:Add Video games post method
    Given user creates a session with the base url
    When User post request with relative URL
    Then user validates the status code
    And user successfully validates the response message

Test-C2:Validate the added video game
    Given user creates a session with the base url
    When user get request with id of the video game
    Then user prints logs into the console
    And user validates the get response code and validates the message as well

Test-C3:update the video game details
    Given user creates a session with the base url
    When user put request with relative url
    Then user sucessfully logs the reponse and content of the updation
    And user successfully validates the response code and content of the put request

Test-C4: Delete the video game request
    Given user creates a session with the base url
    When user does delete request with relative URL and information id
    Then user prints the log of deletion into the console
    And user validates the deletion response code and content


*** Keywords ***

User creates a session with the base URL
    create session    mysession     ${Base_Url}     verify=true

User post request with relative URL
    ${body}=     create dictionary   id=34     name=D_Dragon_part5   releaseDate=2021-12-09T12:35:02.038Z    reviewScore=64      category=Action_D5_Category     rating=9
    ${header}=   create dictionary    Content-Type=application/json
    ${Aresponse}   post request    mysession    ${Relative_url}    data=${body}    headers=${header}
    set global variable    ${response}     ${Aresponse}

user validates the status code

    log to console    ${response.status_code}
    log to console    ${response.content}
    log to console    ${response.headers}
    ${Actual_statuscode}    convert to string    ${response.status_code}
    should be equal    ${Actual_statuscode}     ${Expected_response_code}

User successfully validates the response message
    ${Actual_response_message}      convert to string    ${response.content}
    should contain    ${Actual_response_message}    ${expected_response_message}

User get request with id of the video game
    ${response}     get request    mysession    ${Relative_url_get_videogame}
    set global variable    ${response_get}      ${response}
user prints logs into the console
    log to console    ${response_get.status_code}
    log to console    ${response_get.content}
user validates the get response code and validates the message as well
    ${Actual_response_code}     convert to string    ${response_get.status_code}
    should be equal    ${Actual_response_code}      ${Expected_response_code}
    ${Actual_response_content}      convert to string     ${response_get.content}
    should contain    ${Actual_response_content}        FinalExecution

User put request with relative URL
    ${body}=     create dictionary   id=37     name=D_Dragon_Part2 second   releaseDate=2021-12-09T12:35:02.038Z    reviewScore=49      category=Action_D_Category     rating=6
    ${header}=   create dictionary    Content-Type=application/json
    ${Aresponse}   put request    mysession    ${Relative_url_put_videogame}    data=${body}    headers=${header}
    set global variable    ${response_put}     ${Aresponse}
user sucessfully logs the reponse and content of the updation
    log to console    ${response_put.status_code}
    log to console    ${response_put.content}
user successfully validates the response code and content of the put request
    ${Actual_response_code}     convert to string    ${response_put.status_code}
    should be equal    ${Actual_response_code}      ${Expected_response_code}
    ${Actual_response_content}      convert to string    ${response_put.content}
    should contain    ${Actual_response_content}        D_Dragon_Part2

user does delete request with relative URL and information id
    ${Aresponse}    delete request    mysession     ${relative_Url_delete}
    set global variable    ${response_delete}       ${Aresponse}
user prints the log of deletion into the console
    log to console    ${response_delete.status_code}
    log to console    ${response_delete.content}
User validates the deletion response code and content
    ${Actual_response_code}     convert to string    ${response_delete.status_code}
    should be equal    ${Actual_response_code}      ${Expected_response_code}
    ${Actual_response_message}      convert to string    ${response_delete.content}
    should contain    ${Actual_response_message}        Record Deleted Successfully




complete session
    create session    mysession     ${Base_Url}     verify=true
    ${body}=     create dictionary   id=36     name=FinalMission   releaseDate=2021-12-09T12:35:02.038Z    reviewScore=95      category=final     rating=6
    ${header}=   create dictionary    Content-Type=application/json
    ${response}=    post on session    mysession    ${Relative_url}    data=${body}    headers=${header}
    log to console    ${response.status_code}
    log to console    ${response.content}
    log to console    ${response.headers}
    log to console    ${response.curl}
    ${Actual_statuscode}    convert to string    ${response.status_code}
    should be equal    ${Actual_statuscode}     200


