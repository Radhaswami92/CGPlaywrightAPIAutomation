*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary
Library    Process
Library    .${/}Libraries${/}Test_python_extension.py

#BUS_KEYWORD_FILES
Resource        .${/}READ_API_KEYWORDS${/}BUS_READ_ECOMMERCE_1.robot
Resource        .${/}REST_BUS_GENERIC.robot

*** Variables ***
&{LOGIN_API_PAYLOAD_ECOM}      userEmail=jeet.zaper@gmail.com      userPassword=Radhaswami@103
${Base_Url_Ecommerce}     https://rahulshettyacademy.com
${Base_Url_Event_Management}     https://api.eventhub.rahulshettyacademy.com
${Relative_Url_Ecommerce}     /api/ecom/auth/login
${Relative_Url_Event_Management}     /api/auth/login
&{Headers_Ecom}     Content-Type=application/json      Accept=application/json
${Get_Product_Alias_ecom}    /api/ecom/product/get-all-products
${Add_Product_to_cart_alias_ecom}    /api/ecom/user/add-to-cart
${cart_default_id}      69a82b65415d779f9b575789
#{"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"},{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}