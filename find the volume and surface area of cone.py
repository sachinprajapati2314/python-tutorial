import math
r = int(input("enter the r of cone = "))
h = int(input("enter the h of cone = "))

# surface
s = math.pi * r * (r + math.sqrt((r*r) + (h*h)))
print("surface area of cone =",s)

# volume
v = (1/3) * (math.pi * r * r * h)
print("volume area of cone =",v)