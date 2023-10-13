import math

n = int(input("enter the n = "))
r = int(input("enter the r = "))

nCr = math.factorial(n) // (math.factorial(r) * (math.factorial(n-r)))
print(nCr)