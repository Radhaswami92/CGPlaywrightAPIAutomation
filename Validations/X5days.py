import datetime
#a = datetime.datetime.fromtimestamp(1347517370).strftime('%Y-%m-%d %H:%M:%S')
#print(a)
a = '2012-12-31 11:52:50'
b = a.split(' ')
print(b[0])
print(b[1])
#c=b[0]+'T'+b[1]
#print(c)
d=b[0].split('-')
print(d[2])
nd= int(d[2])
nm=int(d[1])
ny=int(d[0])
j=1
x = 6
for i in range(1, x):
    if int(nd) < 31:
        if i == x:
            break
        j = i
        while j <= i and int(nd) < 31:
            nd = int(nd) + 1
            j = j + 1
            x = x-1
        if nd < 10:
            nd = "{}{}".format('0', nd)

    elif int(nm) == 12 and int(nd) == 31:
        if i == x:
            break
        nm = "{}{}".format('0',1)
        nd = "{}{}".format('0',1)
        ny = ny + 1
        x = x - 1

    elif int(nm) < 12 and int(nd) == 31:
        if i == x:
            break
        nd = "{}{}".format('0', 1)
        nm = int(nm) + 1
        x = x-1
if type(nm) is str:
    if len(nm) < 2:
        if int(nm) < 10:
            nm = "{}{}".format('0', nm)
elif type(nm) is int:
    if int(nm) < 10:
        nm = "{}{}".format('0', nm)

print(nm)
print(nd)
print(ny)
Final_Dformat= str(ny) + '-' + str(nm) + '-' + str(nd) + 'T' + str(b[1])
print(Final_Dformat)
