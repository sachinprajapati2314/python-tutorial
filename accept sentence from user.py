user_in = input("enter the sentence = ")
choice = input("enter (upper & lower & none) = ")

# choice 
if choice == "upper":
    a = user_in.upper()
    print("upper sentence = ",a)

elif choice == "lower":
    b = user_in.lower()
    print("lower sentence = ",b)

else:
    print("you entered = ",user_in)