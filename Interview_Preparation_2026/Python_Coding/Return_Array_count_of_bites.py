

n = 161
# x = 2
# bits =[]
# count = 1
# while x < n:
#     if x * 2 < n:
#         x = x * 2
#         count = count + 1
#         bits.append(x)
#     else:
#         break
li = []
while n != 0:
    c = n % 2
    li.append(c)
    n = n//2
li.reverse()
print(li)
s = [li.count(1)]

for i in range(0, len(li)):
    if li[i] == 1:
        s.append(i)
print(s)






