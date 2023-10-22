a = input("enter binary number = ")

# convert binary to decimal
d = int(a,2)

# convert deecimal to binary
h = hex(d)

# str 
hexa_d =str(h[2:])

print("hexadecimal number = ",hexa_d.upper())