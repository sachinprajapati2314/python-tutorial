x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[9,8,7],
     [1,2,3],
     [4,5,6]]

temp = 0

print("x = ")
for row1 in x:
    print(row1)

print("\ny = ")
for row2 in y:
    print(row2)

print("\n")
for i in range(len(x)):
    for j in range(len(x[0])):
        temp=x
        x=y
        y=temp

print("transpose x = ")
for x in x:
    print(x)
print("\ntranspose y = ")
for y in y:
    print(y)
