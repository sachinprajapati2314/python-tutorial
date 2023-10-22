a = (input("enter binary number = "))

# convert binary to decimal
decimal = int(a,2)

# convert decimal to octal
o = oct(decimal)
octal = str(o[2:])
print("octal number = ",octal)