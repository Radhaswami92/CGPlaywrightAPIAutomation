import datetime
a = datetime.datetime.fromtimestamp(1347517370).strftime('%Y-%m-%d %H:%M:%S')
print(a)
#a = '2012-11-31 11:52:50'
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
for i in range(1,2):
    if int(d[2]) < 31:
        nm = str(d[1])
        nd = nd + i
    elif nm == 12 and nd == 31:
        nm = "{}{}".format('0',1)
        nd = "{}{}".format('0',1)
        ny = ny + i
    elif nm < 12 and nd == 31:
        nm = nm + i
        nd = "{}{}".format('0', 1)

print(nm)
print(nd)
print(ny)
Final_Dformat= str(ny) + '-' + str(nm) + '-' + str(nd) + 'T' + str(b[1])
print(Final_Dformat)
