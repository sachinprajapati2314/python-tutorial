a = int(input("enter the first number of A.P series = "))
n = int(input("enter the total number in A.P series = "))
d = int(input("enter the difference of A.P series = "))

sum = (n * (2*a + (n-1) * d)) // 2
tn = a + (n-1) * d

for i in range(a, tn, d):
    print(i,end="+")

print(tn,"=",sum)