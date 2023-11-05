a = int(input("enter the number of elements (1 to 10) = "))
l = []

print("enter only (11 - 99)")
for i in range(1,a+1):
    a = input(f"enter number {i} = ")
    l.append(a)

print(l)
pos = int(input("enter the element position = "))
ele = input("enter the desired element = ")

l.insert(pos,ele)

print("after insert desired position in arr =",l)