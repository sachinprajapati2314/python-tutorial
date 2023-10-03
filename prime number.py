num = int(input("enter the number = "))

#Assume the number is prime until proven otherwise
s = True

if num == 1:
    print("1 is \"Not prime number\"")

elif num == 0:
    print("Zero is neither prime nor composite")

elif num > 1:
    for i in range (2, num):
        if num % i == 0:
            s = False
if s:
    print("is prime number")
else:
    print("is Not prime number")