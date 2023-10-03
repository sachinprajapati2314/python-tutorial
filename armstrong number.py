# Python program to check if the number is an Armstrong number or not

num = int(input("enter the number = "))
order = len(str(num))
copy_n = num
sum = 0

while(num > 0):
    digit = num%10
    sum += digit ** order
    num = num // 10 
if (sum == copy_n):
    print("armstrong number ")
else:
    print("not armstrong number ")