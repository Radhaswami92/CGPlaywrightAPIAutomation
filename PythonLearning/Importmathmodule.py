import math

print(math.sqrt(1000))

print(math.factorial(5))

n = 5
k = 4

val = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
print(val)
from math import factorial   # to write it in a more optimized way we can import specific function as well

x = factorial(n) / (factorial(k) * factorial(n-k))
print(x)

from math import factorial as fac # this is also helpful to call  the predefined function by custom defined name

y = fac(n) / (fac(k) * fac(n-k))
print(y)

# Single slash represents the float result thats why the printed value is in decimal
# Double slash represents the integer result as it will round of the resuklt and display with out decimal. see the below code

yz = fac(n) // (fac(k) * fac(n-k))
print(yz)

# Below code is to know how many integers can be converted into string or calculate the no of characters by considering the value as string

j = 100
print(fac(j))
print(len(str(fac(j))))