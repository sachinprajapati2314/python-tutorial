a = int(input("enter the number of elements (1 to 10) = "))
l = []

print("enter only (11 - 99)")
for i in range(1,a+1):
    a = input(f"enter number {i} = ")
    l.append(a)

l.sort()
print("largest element of arr =",l[-2])