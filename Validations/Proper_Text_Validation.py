import cerberus
from cerberus import Validator
import functools

Expected_column_List_Master = [['TAG', 'TEXT', 'DATE'], ['TAG', 'MODIFICATION FLAG', 'CURRENCY CODE', 'CURRENCY NAME', 'FRACTIONAL DIGIT', 'COUNTRY CODE', 'COUNTRY NAME'], ['TAG', 'MODIFICATION FLAG', 'COUNTRY CODE', 'COUNTRY NAME'], ['TAG', 'MODIFICATION FLAG', 'COUNTRY CODE', 'COUNTRY NAME', 'DATE', 'HOLYDAY TYPE', 'SPECIAL HOLIDAY INFO'], ['TAG', 'MODIFICATION FLAG', 'SERVICE CODE', 'DATE', 'HOLYDAY TYPE', 'SPECIAL HOLIDAY INFO']]

fl = []
for line in open('CCH_20201205.TXT','r'):
    line = line.rstrip()
    fields = line.split('\t')
    fl.append(fields)

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

List_of_dict = []
Master_li_o_li=[]

for column in columnList:
    Actual_index = None
    temp_list=[]
    temp_list.clear()
    loc = len(column)
    print(loc)

    for z in range(0, len(fl)):
        #loc = len(column)
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
        temp_list.append(d)
    Master_li_o_li.append(temp_list)
print(Master_li_o_li)
schema_column0 = {
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


schema_column1 = {
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

schema_column2 = {
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

schema_column4 = {
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

# --BELOW CODE validate the individual list against individual schema
for j in range(0, len(Master_li_o_li)):
    v = Validator(vars()["{}{}".format("schema_column", j)])
    for idx, record in enumerate(Master_li_o_li[j]):
        if v.validate(record):
            print("valid")
        else:
            print(v.errors)
