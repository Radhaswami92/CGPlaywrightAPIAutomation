import pandas as pd
import csv
import re
from cerberus import Validator

df = pd.read_csv('Book2.csv')
print(df.head())
print(df.head(1))

df_dict = df.to_dict(orient='records')
print(df_dict)

schema = {
     'Sl No.': {
        'type': 'integer',
        'regex': '[0-9]'
     },
     'Employee Name':{
         'type': 'string',
         'regex': '[A-Z][a-z]*\s[A-Z][a-z]*'
     },
     'Employee ID': {
         'type': 'string',
         'regex': '((EMP)[0-9]{4})'
     },
     'Bank Account No': {
         'type': 'float',
         'regex': '[0-9]'
     },
     'Bank IFSC Code': {
         'type' : 'string',
         'regex': '[A-Z]*[0-9]*'
     },
     'Salary Amount': {
         'type': 'float',
         'regex': '[0-9]'
     },
 }

v = Validator(schema)
print(v.validate({'Sl No.': 'a'}))

for idx, record in enumerate(df_dict):
    if v.validate(record):
        print("valid")
    else:
        print(v.errors)

