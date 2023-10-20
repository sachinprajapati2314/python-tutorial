a = int(input("enter decimal number = "))

# convert hexadecimal
d = hex(a)

# string position
f = str(d[2:])

# convert upper case
b = f.upper()

print("hexadecimal number = ",(b))