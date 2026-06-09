import cerberus
from cerberus import Validator
import functools

Expected_column_List_Master = [['TAG', 'TEXT', 'DATE'], ['TAG', 'MODIFICATION FLAG', 'CURRENCY CODE', 'CURRENCY NAME', 'FRACTIONAL DIGIT', 'COUNTRY CODE', 'COUNTRY NAME'], ['TAG', 'MODIFICATION FLAG', 'COUNTRY CODE', 'COUNTRY NAME'], ['TAG', 'MODIFICATION FLAG', 'COUNTRY CODE', 'COUNTRY NAME', 'DATE', 'HOLYDAY TYPE', 'SPECIAL HOLIDAY INFO'], ['TAG', 'MODIFICATION FLAG', 'SERVICE CODE', 'DATE', 'HOLYDAY TYPE', 'SPECIAL HOLIDAY INFO']]

fl = []
for line in open('CCH_20201205.TXT','r'):
    line = line.rstrip()
    fields = line.split('\t')
    fl.append(fields)

print(fl[2])
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

# Validation of expected column with the actual column list

if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, Expected_column_List_Master, columnList), True):
    print("The lists Expected column List and Actual column List are the same")
else:
    print("The lists Expected column List and Actual column List are not the same")

p_index = 1
List_of_dict = []
List_of_dict_column1 = []
List_of_dict_column2 = []
List_of_dict_column3 = []
List_of_dict_column4 = []
List_of_dict_column5 = []

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
        while Length_o < loc:
            fl[i].append("NA")
            Length_o = Length_o + 1
        d = {}
        for rang in range(0, len(column)):
            d[column[rang]] = fl[i][rang]
        List_of_dict.append(d)
        vars()["{}{}".format("List_of_dict_column", p_index)].append(d)
    p_index = p_index + 1

#print(Master_li_o_li[4])
#print(List_of_dict)
#print(List_of_dict_column1)
#print(List_of_dict_column2)
#print(List_of_dict_column3)
#print(List_of_dict_column4[52538])
#print(List_of_dict_column5)

schema_column1 = {
     'TAG': {
        'type': 'string',
        'regex': '[A-Z]*'
     },
     'TEXT': {
         'type': 'string',
         'regex': '[A-Z]*(\s)*[A-Z]*'
     },
     'DATE': {
         'type': 'string',
         'regex': '([0-9]{8})*'
     },
}


schema_column2 = {
     'TAG': {
        'type': 'string',
        'regex': '[A-Z]*'
     },
     'MODIFICATION FLAG': {
         'type': 'string',
         'regex': '[A-Z]*'
     },
     'CURRENCY CODE': {
         'type': 'string',
         'regex': '[A-Z]*'
     },
     'CURRENCY NAME': {
         'type': 'string',
         'regex': '[A-Z]*(\s)*[A-Z]*(\s)*[A-Z]*(\s)*[A-Z]*(\s)*[A-Z]*|(A-Z)*'
     },
     'FRACTIONAL DIGIT': {
         'type' : 'string',
         'regex': '[0-9]'
     },
     'COUNTRY CODE': {
         'type': 'string',
         'regex': '[A-Z]*|(NA)'
     },
     'COUNTRY NAME': {
         'type': 'string',
         'regex': '[A-Z]*(\s)*[A-Z]*|(NA)'
     },
 }

schema_column3 = {
     'TAG': {
        'type': 'string',
        'regex': '[A-Z]*'
     },
     'MODIFICATION FLAG': {
         'type': 'string',
         'regex': '[A-Z]*'
     },
     'COUNTRY CODE': {
         'type': 'string',
         'regex': '[A-Z]*|(NA)'
     },
     'COUNTRY NAME': {
         'type': 'string',
         'regex': '([A-Z]*(\s)*[A-Z]*)|(NA)'
     },
 }

schema_column4 = {
     'TAG': {
        'type': 'string',
        'regex': '[A-Z]*'
     },
     'MODIFICATION FLAG': {
         'type': 'string',
         'regex': '[A-Z]*'
     },
     'COUNTRY CODE': {
         'type': 'string',
         'regex': '[A-Z]*'
     },
     'COUNTRY NAME': {
         'type': 'string',
         'regex': '([A-Z]*(\s)*[A-Z]*)|(([A-Z]*)(,)(\s)*[A-Z]*)'
     },
     'DATE': {
         'type': 'string',
         'regex': '[0-9]{8}'
     },
     'HOLYDAY TYPE': {
         'type': 'string',
         'regex': '[A-Z]|(NA)'
     },
     'SPECIAL HOLIDAY INFO': {
         'type': 'string',
         'regex': '([A-Z]*(\s)*[A-Z]*)|(NA)'
     },
 }

schema_column5 = {
     'TAG': {
        'type': 'string',
        'regex': '[A-Z]*'
     },
     'MODIFICATION FLAG': {
         'type': 'string',
         'regex': '[A-Z]*'
     },
     'SERVICE CODE': {
         'type': 'string',
         'regex': '[A-Z]*'
     },
     'DATE': {
         'type': 'string',
         'regex': '[0-9]{8}'
     },
     'HOLYDAY TYPE': {
         'type': 'string',
         'regex': '[A-Z]|(NA)'
     },
     'SPECIAL HOLIDAY INFO': {
         'type': 'string',
         'regex': '([A-Z]*(\s)*[A-Z]*)|(NA)'
     },
 }

#Schema_Master_List = [schema_column0, schema_column1, schema_column2, schema_column3, schema_column4]


v = Validator(schema_column1)
#print(v.validate({'Salary_Amount': 'a'}))

for idx, record in enumerate(List_of_dict_column1):
    if v.validate(record):
        print("valid")
    else:
        print(v.errors)

x = Validator(schema_column2)
for idx, record in enumerate(List_of_dict_column2):
    if x.validate(record):
        print("valid")
    else:
        print("{}{}".format(idx, x.errors))

y = Validator(schema_column3)
for idx, record in enumerate(List_of_dict_column3):
    if y.validate(record):
        print("valid")
    else:
        print("{}{}".format(idx, y.errors))

z = Validator(schema_column4)
for idx, record in enumerate(List_of_dict_column4):
    if z.validate(record):
        print("valid")
    else:
        print("{}{}".format(idx, z.errors))

u = Validator(schema_column5)
for idx, record in enumerate(List_of_dict_column5):
    if u.validate(record):
        print("valid")
    else:
        print("{}{}".format(idx, u.errors))

