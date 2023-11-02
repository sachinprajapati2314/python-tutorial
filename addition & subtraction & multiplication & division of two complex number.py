c1 = int(input("enter a1 = "))
c2 = int(input("enter a2 = "))
c3 = int(input("\nenter b1 = "))
c4 = int(input("enter b2 = "))

a = complex(c1, c2)
b = complex(c3, c4)

# Operators
opr = input("enter operator = ")

if opr == "+":
    add = a+b   # addition of two complex number
    print("addition of complex number = ",add)

elif opr == "-":
    sub = a-b  # subtraction of two complex number
    print("subtraction of complex number = ",sub)

elif opr == "*":
    mul = a*b  # multiplication of two complex number
    print("multiplication of complex number = ",mul)

elif opr == "/":
    div = a/b   # division two complex number
    print("division of complex number = ",div)