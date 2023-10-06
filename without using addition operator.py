num_1 = int(input("enter the first number = "))
num_2 = int(input("enter the second number = "))

while (num_2 != 0):
    temp = num_1 & num_2
    num_1 = num_1 ^ num_2
    num_2 = temp << 1

print(num_1)