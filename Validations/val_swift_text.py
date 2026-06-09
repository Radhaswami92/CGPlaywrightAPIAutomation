import pandas as pd
from cerberus import Validator
#import cerberus
import struct
import sys
fl = []
expected_list_1 = ['TAG', 'MODIFICATION FLAG', 'CURRENCY CODE', 'CURRENCY NAME', 'FRACTIONAL DIGIT', 'COUNTRY CODE', 'COUNTRY NAME']
expected_list_2 = ['TAG', 'MODIFICATION FLAG', 'CURRENCY CODE', 'CURRENCY NAME', 'FRACTIONAL DIGIT', 'COUNTRY CODE', 'COUNTRY NAME']
expected_list_3 = ['TAG', 'MODIFICATION FLAG', 'CURRENCY CODE', 'CURRENCY NAME', 'FRACTIONAL DIGIT', 'COUNTRY CODE', 'COUNTRY NAME']

for line in open('CCH_20201205.TXT','r'):
    line = line.rstrip()
    fields = line.split('\t')
    #print(fields)
    fl.append(fields)
print(fl[2])
#print(fl[1][4])
print(len(fl))

columnList=[]
cindexlist=[]
for iline in fl:
    if iline.__contains__('TAG'):
        indf = fl.index(iline)
        cindexlist.append(indf)
        columnList.append(iline)
print(columnList)
print(cindexlist)

# FinalList = []
# for eachlis in fl:
#     len_of_eachlis = len(eachlis)
#     while (len_of_eachlis < 7):
#         eachlis.append('NA')
#         len_of_eachlis = len_of_eachlis + 1
#     FinalList.append(eachlis)
# print(FinalList)

# Actual_column =[]  ##It contains the header column
# Actual_column_index = None
# for individual_list in fl:
#     if (individual_list == expected_list_1):
#         Actual_column = individual_list
#         Actual_column_index = fl.index(individual_list)
# print(Actual_column)
# print(len(Actual_column))
# print(Actual_column_index)
# Starting_index = Actual_column_index + 1


# List_of_dict = []
# for i in range(Starting_index, len(fl)):
#     dix = {}
#     for rang in range(0, len(Actual_column)):
#         dix[Actual_column[rang]] = fl[i][rang]
#     List_of_dict.append(dix)
#     print(dix)
# print(List_of_dict)


List_of_dict = []
for column in columnList:
    Actual_index = None

    for z in range(0, len(fl)):
        loc = len(column)
        if fl[z] == column:
            Actual_index = z
            break
    for i in range(Actual_index+1, len(fl)):
        if fl[i][0] == 'TAG':
            break
        Length_o = len(fl[i])
        while (Length_o<loc):
            fl[i].append("NA")
            Length_o =Length_o + 1
        d = {}
        for rang in range(0, len(column)):
            d[column[rang]] = fl[i][rang]
        List_of_dict.append(d)
        #print(d)
print(List_of_dict)
print(List_of_dict[241])
print(List_of_dict[242])
print(List_of_dict[243])
print(List_of_dict[0])
print(List_of_dict[-1])




# schema = {
#      'Sl_No.': {
#         'type': 'integer',
#         'regex': '[0-9]'
#      },
#      'Employee_Name':{
#          'type': 'string',
#          'regex': '[A-Z][a-z]*\s[A-Z][a-z]*'
#      },
#      'Employee_ID': {
#          'type': 'string',
#          'regex': '((EMP)[0-9]{4})'
#      },
#      'Bank_Account_No': {
#          'type': 'string',
#          'regex': '[0-9]'
#      },
#      'Bank_IFSC_Code': {
#          'type' : 'string',
#          'regex': '[A-Z]*[0-9]*'
#      },
#      'Salary_Amount': {
#          'type': 'float',
#          'regex': '[0-9]'
#      },
#  }
#
# v = Validator(schema)
# print(v.validate({'Salary_Amount': 'a'}))
#
# for idx, record in enumerate(List_of_dict):
#     if v.validate(record):
#         print("valid")
#     else:
#         print(v.errors)