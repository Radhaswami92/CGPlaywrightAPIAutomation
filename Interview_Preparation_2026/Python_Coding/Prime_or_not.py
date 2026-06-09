a = [1,2,4,5,6,7,8,9,10]
primenos=[]
for ele in a:
    if ele == 1:
        primenos.append(ele)
        continue
    count = 0
    for i in range(1, ele+1):
        if ele % i == 0:
            count +=1
    if count ==2:
        primenos.append(ele)

print(f"The prime nos are: {primenos}")
