*** Settings ***
Suite Setup     Create my session for API Ecommerce
Resource    ..${/}..${/}Resources${/}include_all.robot

*** Test Cases ***

#Get me all the products in the Dashboard and validate the product names
#    With Rest, get all Product names from the dashboard
#    log to console    ${Products}

Validate that I am able to add ZARA COAT 3 to the cart successfully
    I add products the product:ZARA COAT 3 to the cart
    Response should be success with the message      Product Added To Cart

Validate that I am able to add iphone 13 pro to the cart successfully
    I add products the product:iphone 13 pro to the cart
    Response should be success with the message      Product Added To Cart

