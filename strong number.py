num = int(input("enter the number = "))
my_sum = 0
temp = num
while(num):
   i=1
   fact=1
   remainder = num%1
   while(i<=remainder):
      fact=fact*i
      i=i+1
   my_sum = my_sum+fact
   num= num//10
if(my_sum == temp):
   print("The number is a strong number")
else:
   print("The number is not a strong number")