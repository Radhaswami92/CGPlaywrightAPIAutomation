*** Settings ***
Library    RequestsLibrary
Library    Collections


*** Variables ***
&{sasa} =   {}


*** Test Cases ***
sample
    log to console   "hello"
    &{sasa}['a']=   2
    &{sasa}['b']=   1
    &{sasa}['c']=   3
    log to console   ${sasa}





