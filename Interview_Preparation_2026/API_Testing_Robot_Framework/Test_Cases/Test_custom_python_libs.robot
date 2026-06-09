*** Settings ***
Resource    ..${/}Resources${/}include_all.robot
Resource    ..${/}Resources${/}Libraries${/}complex.json
Library    JSONLibrary


*** Test Cases ***

Validate a Json file with multiple robot keywords
    ${get_from_python_extension}=   print from python extension     HellofromRobot
    log to console      ${get_from_python_extension}