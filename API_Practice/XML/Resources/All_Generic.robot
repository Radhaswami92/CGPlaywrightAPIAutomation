*** Settings ***
Library    Collections
Library    RequestsLibrary


*** Variables ***
${base_url}     http://localhost:8080

*** Keywords ***
Create session for base url
    create session    mysession     ${base_url}     verify=true