n = int(input("enter n = "))

sum = pow(((n * (n+1)) // 2),2)

for i in range(1,n+1):
    print(i,end="^3 + ")

print(".... = ",sum)