*** Settings ***

Library    XML
Library     Collections


*** Test Cases ***

Validate a XML file with multiple robot keywords
    ${XML_file_obj}     parse xml       C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/Interview_Preparation_2026/API_Testing_Robot_Framework/Resources/Libraries/complex.xml
    ${text1}    xml.get element text    ${XML_file_obj}     .//customer/customerId
    log to console    ${text1}
    ${list_ele_customer}    xml.get child elements    ${XML_file_obj}     .//customer/personalDetails
#    log to console    ${list_ele_customer}
#    log to console    ${list_ele_customer}[0]
#    log to console    ${list_ele_customer}[1]
#    log to console    ${list_ele_customer}[2]
    ${count}=    get length    ${list_ele_customer}
    log to console    ${count}
    log to console    ${list_ele_customer}[0].tag
    log to console    ${list_ele_customer}[1].tag
    log to console    ${list_ele_customer}[2].tag
    ${string_ele_tag}       convert to string    ${list_ele_customer[2].tag}
    should be equal as strings    ${string_ele_tag}       email

    ${string_ele_text}       convert to string    ${list_ele_customer[2].text}
    should be equal as strings    ${string_ele_text}       jane.doe@example.com
    ${list_ele_customer}    convert to string    ${list_ele_customer}
    log to console    Printing list
    log to console    ${list_ele_customer}



    


