a = [3,1,6,2,100,9,101,2,4,5,6]
a.sort(reverse=True)
print(a[1])

b = [3,1,6,2,100,9,101,2,4,5,6]

max_1 = b[0]
max_2 = 0

for i in range(1, len(b)):
    if b[i] > max_1:
        max_2 = max_1
        max_1 = b[i]
print(max_2)
print(max_1)

