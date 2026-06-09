
noslist= []
for i in range(0,5):
    nos = input("please enter nos: ")
    noslist.append(nos)
max = noslist[0]
for i in range(1, len(noslist)):
    if max > noslist[i]:
        max = noslist[i]
print(max)
