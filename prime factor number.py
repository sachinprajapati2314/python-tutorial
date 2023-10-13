n = int(input("enter the number = "))

for i in range(1,n+1):
    if n%i == 0:
        flage = 0
        for j in range(2,i):
            if i%j == 0:
                flage = 1
        if flage == 0:
            print(i, end=" ")