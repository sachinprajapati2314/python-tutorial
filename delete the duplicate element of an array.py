a = int(input("enter the number of elements (1 to 10) = "))
l = []

print("enter only (11 - 99)")
for i in range(1,a+1):
    a = input(f"enter number {i} = ")
    l.append(a)

l.sort()
print("before delete duplicate =",l)
# convert list to set
st = set(l)

# convert set to list
lst = list(st)
print("after delete duplicate =",lst)