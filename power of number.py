# find out power of number. 

num = int(input("enter the number = "))
power = int(input("enter the number power = "))
i = 0
result = 1

while power != 0:
    result *= num
    power -= 1
    
print(result)