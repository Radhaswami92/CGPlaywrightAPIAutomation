*** Settings ***
Library    JSONLibrary
Library    os
Library    collections

*** Test Cases ***

Test-Case1: Extraxting json key to get the value of it
    ${json_obj}     load json from file     C://Json_practise//Profile.json
    ${Phone_Number_value}       get value from json    ${json_obj}      $.PhoneNo[0].Mobile[0]
    log to console      ${Phone_Number_value[0]}
    should be equal     ${Phone_Number_value[0]}       9435029739
    ${street_value}     get value from json              ${json_obj}    $.Address.Street
    should be equal     ${street_value[0]}     R.K Mission Road

# validating value from the array below
Test-Case2: Extraxting json key to validate the value in array
    ${json_obj}     load json from file     C://Json_practise//Profile.json
    ${Get_my_hobbies}       get value from json    ${json_obj}      $.Hobbies
    should contain    ${Get_my_hobbies[0]}     PlayinGuitar     PlayingPiano    SingingSongs
    log to console    ${Get_my_hobbies[0]}


*** Keywords ***


