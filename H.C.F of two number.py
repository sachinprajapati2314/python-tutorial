a = int(input("enter the first number = "))
b = int(input("enter the second number = "))

i = 0
while(a != b):
    if a > b:
        a -= b
    else :
        b -= a
i += 1
print(a)