def recursion(num,power):
    i = 0
    result = 1

    while power != 0:
        result *= num
        power -= 1
    return result

num = int(input("enter the number = "))
power = int(input("enter the power = "))

print("power of number using recursion = ",recursion(num,power))