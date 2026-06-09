*** Settings ***
Library     XML


*** Test Cases ***

Load and print the value
    ${xml}=     parse xml    C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/Interview_Preparation_2026/API_Testing_Robot_Framework/Resources/Libraries/complex.xml
    ${value}=   get element text    ${xml}  .//order[@id='ORD-20260527-001']/orderSummary/totalAmount
    Log to console      ${value}
    should be equal as strings    ${value}    1418.97




