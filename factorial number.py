import math

# number input 
num = int(input("enter the number = "))

# use condition
if (num == 0):
    print("1")
else:
   num1 = num * math.factorial(num - 1)
   print(num1)