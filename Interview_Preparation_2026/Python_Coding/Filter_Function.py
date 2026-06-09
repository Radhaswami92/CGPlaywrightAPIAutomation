#Filter the even nos out of a list
numbers = [1,2,3,4,5,6,7,8,9,10]
a =lambda x : x % 2 == 0

c = filter(a,numbers)
print(list(c))
