# find out sum of digit of given number 
# first use function 

def digit_sum(num):
    sum = 0
    for x in str(num):
        sum += int(x)
    return sum

# input number 
num = input("enter the number = ")
digit_num = digit_sum(num)
print(digit_num)