*** Settings ***
Library    XML
Library    os
Library    Collections
Library    RequestsLibrary
Library    JSONLibrary


*** Variables ***
${base_url}     http://localhost:8080
${relative_url}     /app/videogames


*** Test Cases ***
TestCase1: Raw xml file
    ${xml_object}=      parse xml    C://Json_practise//videogames.xml
    #check the single element value
    ${Video_game_name}=    get element text    ${xml_object}       .//videoGame[18]/name
    log to console    ${Video_game_name}
    should be equal    ${Video_game_name}       D_Dragon_Part2 second

    #approach 2 Indirect process
    ${Video_game_element}=      get element    ${xml_object}        .//videoGame[18]/name
    should be equal    ${Video_game_element.text}       D_Dragon_Part2 second

    #approach 3
    element text should be    ${xml_object}     D_Dragon_Part2 second       .//videoGame[18]/name

TestCase 2: API request validation of xml
    create session    mysession     ${base_url}
    ${response}     get request    mysession        ${relative_url}
    #${json_object}          ${response.content}
    #log to console    ${json_object}
    log to console    ${response.status_code}
    #log to console    ${response.content}
    ${video_game_text}      get element text    ${response.content}     .//videoGame[18]/name
    should be equal    ${video_game_text}       D_Dragon_Part2 second

    #check number of elements
    ${element_count}        get element count    ${response.content}    .//videoGame
    log to console    ${element_count}
    should be equal as integers    ${element_count}     26

    # check validation attribute is present or not
    element attribute should be    ${response.content}      category    Action_D_Category      .//videoGame[18]

    #check validation of child elements
    ${child_elements}=      get child elements    ${response.content}       .//videoGame[18]
    should not be empty    ${child_elements}

    ${id}=      get element text    ${child_elements[0]}
    ${name}=    get element text    ${child_elements[1]}
    ${name2}=    get element text    ${child_elements[2]}
    log to console    ${name}
    log to console    ${id}
    log to console    ${name2}
    # you can perform should be equal validation for each index of the child elements


*** Keywords ***
