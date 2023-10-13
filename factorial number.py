import math

# number input 
num = int(input("enter the number = "))

# use condition
if (num == 0):
    print("1")
else:
   fact = math.factorial(num)
   print(fact)