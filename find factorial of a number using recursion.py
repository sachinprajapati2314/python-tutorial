import math

def recursion(num):
    if num == "0":
        print("1")
    else:
        fac = math.factorial(num)
    
    return fac

n = int(input("enter the number = "))
print("factorial number by using recursion = ",recursion(n))