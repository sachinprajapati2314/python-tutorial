num = int(input("enter the number = "))

if num == 1:
      print("1 is \"Not prime number\"")

elif num == 0:
     print("Zero is neither prime nor composite")

for i in range(2,num+1):
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)
