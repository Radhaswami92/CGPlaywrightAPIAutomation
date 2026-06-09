a = [3,1,6,2,100,9,101,2,4,5,6]
max = a[0]
for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]
print(max)

