import math

def gcd(num1,num2):

    gcd_num = math.gcd(num1,num2)
    return gcd_num

num1 = int(input("enter the first number = "))
num2 = int(input("enter the second number = "))
print("G.C.D number by using recursion =",gcd(num1,num2))