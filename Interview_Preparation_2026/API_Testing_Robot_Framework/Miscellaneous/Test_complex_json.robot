*** Settings ***

Library    JSONLibrary


*** Test Cases ***

Validate a Json file with multiple robot keywords
    ${JSON_FILE_obj}=       load json from file       Interview_Preparation_2026/API_Testing_Robot_Framework/Resources/Libraries/complex.json
    ${name}=    get value from json     ${JSON_FILE_obj}    $.stakeholders[0].contact.email
    log to console    ${name}
    #${name}     convert to string       ${name}[0]
    should be equal as strings    ${name}[0]    sarah.c@company.com
    ${action}=  get value from json    ${JSON_FILE_obj}     $.milestones.phase_1.tasks[0].history[1].action
    should be equal as strings    ${action}[0]      finished


Validate Json part 2
    ${Json_file_obj}=   load Json from file    Interview_Preparation_2026/API_Testing_Robot_Framework/Resources/Libraries/complex.json
    ${xx}=  Get Value From Json    ${Json_file_obj}     $.milestones.phase_1.tasks[1].dependencies[0]

    should be equal as strings  ${xx}[0]    TSK-101
    ${booleaz}=     Get value from json     ${Json_file_obj}    $.milestones.tasks[1].completed
    ${booleaz}=     convert to boolean      ${booleaz}
    should not be true      ${booleaz}





