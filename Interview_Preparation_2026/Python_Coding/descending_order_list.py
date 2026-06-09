a = [3,1,6,2,100,9,101,2,4,5,6]

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(a)