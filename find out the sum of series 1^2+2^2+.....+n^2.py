n = int(input("enter n = "))

sum = (n * (n+1) * (2 * n+1)) // 6

for i in range(1,n+1):
    print(i,end="^2 + ")

print(".... = ",sum)