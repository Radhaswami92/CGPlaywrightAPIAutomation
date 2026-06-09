a = [3,1,6,2,100,9,101,2,4,5,6,1,9,9,9,9,9,1]

for i in range(0, len(a)):
    for j in range(len(a)-1, i,-1):
        if a[i] == a[j]:
            del a[i]

print(a)

b = [3,1,6,2,100,9,101,2,4,5,6,1,9,9,9,9,9,1]
new_list_duplicates = []
###################### FInd duplicated ele ##########
for i in range(0, len(b)):
    for j in range(i + 1, len(b)):
        if b[i] == b[j]:
            if b[i] not in new_list_duplicates:
                new_list_duplicates.append(b[i])

print(new_list_duplicates)

######################################
new_list_without_duplicates=[]
for ele in b:
    if ele not in new_list_without_duplicates:
        new_list_without_duplicates.append(ele)
print(new_list_without_duplicates)
