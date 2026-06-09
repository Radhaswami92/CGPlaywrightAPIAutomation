li_1 = ["apple", 2, "apple", 1, 3, 4, 2,3,3]
li_2 = ["apple", 2, "pray", 3, 5, 8]

comon_ele =[]

for ele1 in li_1:
    if ele1 in li_2:
        if ele1 not in comon_ele:
            comon_ele.append(ele1)
print(comon_ele)
