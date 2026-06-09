*** Settings ***
Resource    ..${/}include_all.robot

*** Variables ***

*** Keywords ***
With Rest, get all Product names from the dashboard
    [Return]        ${Product_Index}
    ${response}=    post on session      ${SESSION_ALIAS}        ${Get_Product_Alias_ecom}   headers=${Next_Request_Headers}
    ${length}=  get length      ${response.json()["data"]}
    set test variable   ${ProductDetailsDictionary}     ${response.json()}[data]
    ${Products}=    create list
    ${Product_Index}=    create dictionary
    FOR     ${i}    IN RANGE    0   ${length}
        Append to List      ${Products}     ${response.json()}[data][${i}][productName]
        set to dictionary   ${Product_Index}   ${response.json()}[data][${i}][productName]        ${i}
    END
    Log to console      ...Products displayed in the Dashboard Page are : ${Products}

I add products the product:${Product} to the cart
    ${Product_index_dict}=       With Rest, get all Product names from the dashboard
    ${Product_idx}=     get from dictionary      ${Product_index_dict}      ${Product}
    ${body}=    create dictionary       _id=${cart_default_id}      product=${ProductDetailsDictionary}[${Product_idx}]
    ${resposne}=    post on session     ${SESSION_ALIAS}        ${Add_Product_to_cart_alias_ecom}       json=${body}    headers=${Next_Request_Headers}
    set test variable   ${response}    ${resposne}
#    ${product_order_dict}=      create dictionary   country=${EMPTY}
#    @{order_checkout_list}=     create list

    #{"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"},{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}


Response should be success with the message
    [Arguments]     ${EXPECTED_MESSAGE}=${EMPTY}
    should be equal    ${response.json()}[message]    ${EXPECTED_MESSAGE}
    ${code}=    convert to string       ${response.status_code}
    should be equal     ${code}     200




