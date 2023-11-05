import sys

# int
a = 5445
a1 = sys.getsizeof(a)
print("size of int =",a1)

# string
b = "sachin"
b1 = sys.getsizeof(b)
print("size of str =",b1)

# list
c = []
c1 = sys.getsizeof(c)
print("size of list =",c1) 

# set
d = {}
d1 = sys.getsizeof(d)
print("size of set =",d1)