a = int(input("enter the number of elements (1 to 10) = "))
l = []

print("enter only (11 - 99)")
for i in range(0,a):
    a = input(f"enter number {i} = ")
    l.append(a)

print("arr =",l)
r = int(input("enter delete desired position(start- 0) = "))

l.remove(l[r])
print("after delete desired position in arr =",l)