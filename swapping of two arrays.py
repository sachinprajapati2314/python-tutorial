# 1 method
a = [1,2,3,4]
b = [5,6,7,8]

print("before swapping = ")
print(a)
print(b)

t = a
a = b
b = t

print("after swapping = ")
print(a)
print(b)

# 2 method
m = ["hii","how","hello"]
print("before swapping = ",m)

g = m[0]
h = m[1]
j = m[2]

t = g
g = h
h = j
j = t

p = [g,h,j]
print("after swapping = ",p)