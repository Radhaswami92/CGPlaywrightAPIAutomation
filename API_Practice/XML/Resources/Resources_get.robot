*** Settings ***
Library    XML
#Library    OS
Library    Collections
Library    RequestsLibrary
Library    API_Practice/main.py


*** Variables ***
${base_url}     http://localhost:8080
${Relative_url}     /app/videogames
${Api_response}
${Expected_response_code}   200
${xml_path}     C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/API_Practice/XML/get_res.xml
${xsd_path}     C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/API_Practice/XML/schema.xsd


*** Keywords ***
Get the complete list of all video games
    ${response}=     get request      mysession        ${Relative_url}
    set global variable   ${Api_response}       ${response}
User prints the status code into the console
    log to console    ${Api_response.status_code}
User prints the content into the console
    log to console    ${Api_response.content}
    save xml  ${Api_response.content}       C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/API_Practice/XML/get_res.xml       encoding=UTF-8
User validates the reponse code returned
    ${Response_code_returned}   convert to string    ${Api_response.status_code}
    should be equal     ${Response_code_returned}       ${Expected_response_code}
    main.validate xml response
#User validates the xml schema









