n = int(input("enter the n number = "))

sum = (n * (n+1)) // 2

for i in range(1,n+1):
    print(i,end=" + ")

print(".... = ",sum)