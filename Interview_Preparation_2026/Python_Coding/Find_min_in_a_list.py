a = [3,1,6,2,100,9,101,2,4,5,6]

min = a[0]

for i in range(0, len(a)):
    if a[i] < min:
        min = a[i]
print(min)