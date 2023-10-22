a = input("enter hexadecimal number = ")

# convert hexadecimal to decimal
deciaml = int(a,16)

# convert decimal to binary
b_y = bin(deciaml)

# str pos.
binary = str(b_y[2:])

print("binary number = ",binary)