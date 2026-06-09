a = [22,1,1,1,1,3,45,0,55,4,4,46,7,8,78,8]
d = {}
for i in range(0, len(a)):
    count = 1
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            count +=1
    if a[i] not in d.keys():
        d[a[i]] = count
print(d)

for ele in a :
    print(f"The count of {ele} is :{a.count(ele)}")

