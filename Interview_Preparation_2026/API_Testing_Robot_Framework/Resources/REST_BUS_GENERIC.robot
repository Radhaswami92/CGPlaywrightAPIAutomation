*** Settings ***

Resource    include_all.robot

*** Keywords ***

Create my session for API Ecommerce
    create session    my_session    ${Base_Url_Ecommerce}     verify=true    disable_warnings=1
    set suite variable    ${SESSION_ALIAS}  my_session
    ${response}=    post on session    ${SESSION_ALIAS}     ${Relative_Url_Ecommerce}       json=&{LOGIN_API_PAYLOAD_ECOM}      headers=${Headers_Ecom}
    set suite variable    ${SESSION_TOKEN}      ${response.json()["token"]}
    ${Next_Request_Headers}=        create dictionary    Authorization=${SESSION_TOKEN}     Accept=application/json
    set suite variable    ${Next_Request_Headers}       ${Next_Request_Headers}





API call to proact
    [Arguments]     ${method}=${methods}        ${endpoint}=${endpoint}     ${data}=${body}
    Create my session for API Ecommerce
    Run Keyword If  ${method}== "POST"
        ${response}=    post on session     ${SESSION_ALIAS}    ${endpoint}     json=${data}    headers=${Next_Request_Headers}

    set test variable   ${response}   ${response}


Perform API call to view create order
    [Arguments]     ${method}=POST      &{args}
    ${end_point}=   set variable    /api/ecom/order/create-order
    ${body}=    create dictonary    orders=&{args}
    API call to proact    method=${method}   endpoint =${end_point}     data=${body}

API Input list parameter being
    [Arguments]     ${object_name}      &{args}

    ${variable_exist}=      Run keyword and return status   Variable should exist   ${object_name_input`}
    ${list}=    create empty list
    if ${object_name}













