#  largest find among three numbers using conditional operator 

a = int(input("enter the first number = "))
b = int(input("enter the second number = "))
c = int(input("enter the third number = "))

if (a >= b) and (a >= c):
    print(a, "is the largest number ")
elif(b >= a) and (b >= c):
     print(b, "is the largest number ")
else:
     print(c, "is the largest number ")
    