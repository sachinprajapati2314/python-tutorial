# use function
def reverse_n(number):
    # int to str convert
    num_str = str(number)
    # reverse
    reverse_str = num_str[::-1]
    #str to int convert
    reverse_num = int(reverse_str)
    return reverse_num

# input 
num = int(input("enter the number = "))

reversed_num = reverse_n(num)
print("\noriginal number =", num)
print("reverse number =", reversed_num)