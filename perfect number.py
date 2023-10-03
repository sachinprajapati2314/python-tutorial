# check given number is perfect number or not (if sum of its factors is equals to no)

num = int(input("enter the number = "))
s = 0

for i in range (1,num):
    if num%i == 0:
        s = s+i
if s == num:
    print('the entered number is perfect number ')
else:
    print('the entered number is not perfect number')