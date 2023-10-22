a = input("enter octal number = ")

# octal to decimal
d = int(a,8)

# decimal to binary
b = bin(d)

# str pos.
binary = str(b[2:])

print("binary number = ",binary)