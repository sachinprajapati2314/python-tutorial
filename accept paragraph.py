user_in = input("enter the paragraph = \n")
print("""enter choice = 
1) count 
2) capitalize
3) find""")
choice = input("enter (1, 2, 3, none) = ")

if choice == "1":
    u = input("count sen. = ")
    a = user_in.count(u)
    print(a)

elif choice == "2":
    b = user_in.capitalize()
    print(b)

elif choice == "3":
    s = input("find sen. = ")
    c = user_in.find(s)
    print(c)

else:
    print("you entered = \n",user_in)