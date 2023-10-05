# given number and name is palindrome number or not

# function use for number
def number(num):
    # int to str convert 
    str_num = str(num)

    # uses slicing
    reverse_num = str_num[::-1]

    # str to int convert 
    palindrome_num = int(reverse_num)

    # condition 
    if palindrome_num == num:
        print("is palindrome number ")
    else:
        print("is not palindrome number\n ")
    return

# function use for name
def name(name):

    # uses slicing
    reverse_name = name[::-1]

    # condition 
    if reverse_name == name :
        print("is palindrome name ")
    else:
        print("is not palindrome name ")
    return

number_input =int(input('enter the number  = '))
p_number = number(number_input)
print(p_number)

name_input = input("enter the name = ")
p_name = name(name_input)
print(p_name)