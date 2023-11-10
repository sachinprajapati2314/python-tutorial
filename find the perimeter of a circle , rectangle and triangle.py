import math

# circle 
print("perimeter of circle :")
d = int(input("enter the diameter of circle = "))

p = math.pi * d * 2
print("perimeter of circle =",p)

# rectangle 
print("\nperimeter of rectangle :")
l = int(input("enter the Length of rectangle = "))
w = int(input("enter the width of rectangle = "))

p = (l + w) * 2
print("perimeter of rectangle =",p)

# triangle 
print("\nperimeter of triangle :")
a = int(input("enter the a = "))
b = int(input("enter the b = "))
c = int(input("enter the c = "))

p = a + b + c
print("perimeter of triangle =",p)