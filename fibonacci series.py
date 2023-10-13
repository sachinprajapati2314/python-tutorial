# number input
num = int(input("enter the number = "))

n1 = 0
n2 = 1

# 0 and 1 print
print(n1)
print(n2)

# for loop 
for i in range(1, num-1):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
