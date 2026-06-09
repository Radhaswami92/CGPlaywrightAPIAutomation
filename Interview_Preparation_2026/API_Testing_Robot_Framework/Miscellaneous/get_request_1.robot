*** Settings ***
Library     RequestsLibrary
Library     Collections
Library    JSONLibrary
Library    Process

*** Variables ***
&{API_PAYLOAD}      userEmail=jeet.zaper@gmail.com      userPassword=Radhaswami@103
@{list_data}        pencil      rubber      1       2
${Base_Url}     https://rahulshettyacademy.com
#${Base_Url}     https://api.eventhub.rahulshettyacademy.com
${Relative_Url}     /api/ecom/auth/login
#${Relative_Url}     /api/auth/login
*** Keywords ***


*** Test Cases ***

Test Login
    create session      my_session      ${base_url}     verify=true     disable_warnings=1
    ${body}=        create dictionary       userEmail=jeet.zaper@gmail.com      userPassword=Radhaswami@103
    #${body}=        create dictionary       email=student@example.com      password=secret123
    ${header}=      create dictionary        Content-Type=application/json      accept=application/json
    ${response}=        post on session    my_session       ${Relative_Url}     json=${body}        headers=${header}
    #{response}=    post on session    my_session    ${Relative_Url}    json=${body}    headers=${header}
    ${s}=       create dictionary    apple=fruit        papaya=vegetable
    ${e}=       create dictionary    banana=I eat        juice=I drink
    ${Li}=      create list    ${e}     ${response.json()}       ${s}
    ${d}=       create dictionary    data=${Li}
    #log to console    ${response.json()["token"]}
    ${repos}=   set variable    ${d}[data][1][message]
    log to console    ${repos}
    log to console    ${response.content}
    log to console    ${response.status_code}
    should be true    ${response.elapsed.total_seconds()} < 2.0

*** Keywords ***
