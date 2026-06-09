li_1 = ["apple", 2, "apple", 1, 3, 4, 2,3,3]
li_2 = ["apple", 2, "pray", 3, 5, 8]
common_ele =[]
for item_1 in li_1:
    for item_2 in li_2:
        if item_1 == item_2:
            if item_1 not in common_ele:
                common_ele.append(item_1)
print(common_ele)


lis_1 = ["apple", 2, "apple", 1, 3, 4, 2,3,3]
lis_2 = ["apple", 2, "pray", 3, 5, 8]
common_ele =[]
for item_1 in lis_1:
    if item_1 in lis_2:
        if item_1 not in common_ele:
            common_ele.append(item_1)
print(common_ele)





