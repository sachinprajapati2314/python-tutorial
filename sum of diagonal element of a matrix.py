a = [[1,8,6],
     [5,6,3],
     [7,4,6]]

a1 = (a[0][0])
a2 = (a[1][1])
a3 = (a[2][2])

b1 = (a[0][2])
b2 = (a[1][1])
b3 = (a[2][0])

sum = a1+a2+a3
sum2 = b1+b2+b3

print("Principal Diagonal = ",sum)
print("Secondary Diagonal = ",sum2)