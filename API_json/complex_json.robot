*** Settings ***
Library    RequestsLibrary
Library    os
Library    JSONLibrary
Library    Collections

*** Variables ***
${Base_url}     https://api.covid19api.com/
${Relative_Url}     /summary

*** Test Cases ***
Covid Json data
    create session    mysession     ${Base_url}
    ${response}=    get request    mysession    ${Relative_Url}
    ${json_object}=     to json    ${response.content}

    ${Global_new_confirmed}=        get value from json   ${json_object}    $.Global.NewConfirmed
    ${string_new_confirmed_global}      convert to string    ${Global_new_confirmed[0]}
    should be equal    ${string_new_confirmed_global}      636712

    ${Afghanistant_total_confirmed}=    get value from json    ${json_object}       $.Countries[0].TotalConfirmed
    ${string_afg_totalconfirmed}=   convert to string    ${Afghanistant_total_confirmed[0]}
    should be equal    ${string_afg_totalconfirmed}     157858

    ${Aus_contry_name}=     get value from json    ${json_object}      $.Countries[8].Country
    should be equal    ${Aus_contry_name[0]}        Australia

    ${country_list}=    get value from json    ${json_object}       $.Countries
    ${Country_name_list}       create list     #created a blank list so that I can append value to the list when required


    FOR    ${i}    IN RANGE      50
        #@value creates a list with all the values in individual dixtionary of ${country_list[0][${i}]}
        @{values}=      get dictionary values      ${country_list[0][${i}]}
        # when ever the loop executes I anm appending to list varibale with individual list index[0] since for every
        append to list    ${Country_name_list}   ${values[0]}    # at 0th index i will get the coutry value

        FOR    ${element}   IN     @{values}
            run keyword if    "${element}" == "Australia"     log to console    Its matching
            exit for loop if  "${element}" == "Australia"
        END

        ${i}=    Evaluate    ${i} + 1
    END
    log to console    ${Country_name_list}
    list should contain value   ${Country_name_list}    Australia

*** Keywords ***
