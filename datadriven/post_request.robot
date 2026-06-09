*** Settings ***
Library    RequestsLibrary
Library    Collections
Test Template   User validates the response status code and message with different sets of data


*** Variables ***
${base_url}     http://localhost:8080/
${relative_url}     app/videogames
${response}


*** Test Cases ***                  id      name        releaseDate                     reviewScore         category        rating      expected_response_code          Content-Type

Valid Test case_data                95      Gname1      2021-12-09T12:35:02.038Z        61                  Action1         9           200                             application/json
Invalid Release Date format         91      zname1      $%^&&**********&^*^**^**        67                  Action2         9           400                             application/json
Invalid Review Score                92      Revie       2021-12-09T12:35:02.038Z        $%^^                ""              ""          400                             application/json
Invalid Blank id                    ""      ""          ""                              ""                  ""              ""          400                             application/json
Invalid string value for id         string  Fight       ""                              ""                  ""              ""          400                             application/json
Blank data with valid id            96       ""         ""                              ""                  ""              ''          200                             application/json


*** Keywords ***

User validates the response status code and message with different sets of data
    [Arguments]     ${id}       ${name}     ${releaseDate}      ${reviewScore}      ${category}     ${rating}       ${expected_response_code}   ${header_type}
    user creates session with the base url
    user posts requests with relative url       ${id}       ${name}     ${releaseDate}      ${reviewScore}      ${category}     ${rating}       ${header_type}
    user validates the response status code     ${expected_response_code}

user creates session with the base url
    create session    mysession    ${base_url}      verify=true
user posts requests with relative url
    [Arguments]     ${id}       ${name}     ${releaseDate}      ${reviewScore}      ${category}     ${rating}       ${header_type}
    ${body}=    create dictionary   id=${id}     name=${name}   releaseDate=${releaseDate}    reviewScore=${reviewScore}      category=${category}       rating=${rating}
    ${header}=      create dictionary    Content-Type=${header_type}
    ${Aresponse}=    post request    mysession   ${relative_url}    data=${body}    headers=${header}
    set global variable    ${response}     ${Aresponse}

user validates the response status code
    [Arguments]     ${expected_response_code}
    log to console    ${response.status_code}
    log to console    ${response.content}
    ${Actual_response_code}     convert to string    ${response.status_code}
    should be equal     ${Actual_response_code}      ${expected_response_code}



