a = int(input("enter the number = "))
temp = 1

#use for loop
for i in range(1, a + 1):
    for j in range(1, i+1):
        print(temp,end=" ")
        temp = temp + 1
    print()
print("\n")

# use while loop
i = 1
while (i <= a):
    j = 1
    while(j <= i):
        print(temp,end=" ")
        temp = temp + 1
        j += 1
    i += 1
    print()
print("\n")

# reverse
temp = a * (a + 1) // 2

for i in range(a+1, 0, -1):
    for j in range(0,i-1):
        #print("*", end=" ")  print ( * )
        print(temp, end=" ")
        temp = temp -1
        -temp
    print()