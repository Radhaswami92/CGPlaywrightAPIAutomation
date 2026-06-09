stra = "aaaabbcccddfg"
new_str =""

for ele in stra:
    if ele not in new_str:
        if stra.count(ele) == 1:
            new_str += ele
        else:
            new_str = new_str + f"{ele}{stra.count(ele)}"
print(new_str)