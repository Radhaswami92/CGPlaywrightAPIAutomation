import pandas as pd
from cerberus import Validator
#import cerberus
import struct
import sys
import re
fl = []
expected_list = ['Sl_No.', 'Employee_Name', 'Employee_ID', 'Bank_Account_No', 'Bank_IFSC_Code', 'Salary_Amount']
for line in open('demo.txt','r'):
    #fields = line.split()
    valuez = re.split(r'\t+', line.rstrip('\t'))
    #r = re.compile(r'([^\t]*)\t*')
   # valuez = r.findall(line)[:-1]
    print(valuez)
    fl.append(valuez)
print(fl)
print(fl[1])
print(len(fl))

FinalList=[]
for eachlis in fl:
    eachlis = list(filter(None, eachlis))
    FinalList.append(eachlis)
print(FinalList)

Actual_column =[]  ##It contains the header column

#Actual_column_index = None
for individual_list in fl:
    individual_list = list(filter(None, individual_list))
    l = individual_list[-1].rstrip('\n')
    individual_list[-1] = l
    print(individual_list)
    if (individual_list == expected_list):
        Actual_column = individual_list
#print(Actual_column_index)
print(Actual_column)
print(len(Actual_column))
List_of_dict = []
for i in range(1, len(FinalList)):
    dix = {}
    for rang in range(0, len(Actual_column)):
        dix[Actual_column[rang]] = FinalList[i][rang]
    List_of_dict.append(dix)
print(List_of_dict)

schema = {
     'Sl_No.': {
        'type': 'integer',
        'regex': '[0-9]'
     },
     'Employee_Name':{
         'type': 'string',
         'regex': '[A-Z][a-z]*\s[A-Z][a-z]*'
     },
     'Employee_ID': {
         'type': 'string',
         'regex': '((EMP)[0-9]{4})'
     },
     'Bank_Account_No': {
         'type': 'string',
         'regex': '[0-9]'
     },
     'Bank_IFSC_Code': {
         'type' : 'string',
         'regex': '[A-Z]*[0-9]*'
     },
     'Salary_Amount': {
         'type': 'float',
         'regex': '[0-9]'
     },
 }

v = Validator(schema)
print(v.validate({'Salary_Amount': 'a'}))

for idx, record in enumerate(List_of_dict):
    if v.validate(record):
        print("valid")
    else:
        print(v.errors)