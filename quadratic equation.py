import math

x = float(input("enter x = "))
y = float(input("enter y = "))
z = float(input("enter z = "))


d = ( y * y - 4 * x * z)

if (d > 0):
    root_1 =(-y + math.sqrt(d) ) // (2 * x)
    root_2 =(-y + math.sqrt(d) ) // (2 * x)
    print(f"value of root 1 = {root_1} and root 2 = {root_2}")

elif (d == 0):
    root_1 = root_2 = -y / 2*x
    print(f"value of root 1 = {root_1} and root 2 = {root_2}")

else:
    real = -y / (2 * x)
    img = math.sqrt(-d) / (2 * x)
    print(f"value of root 1 = {real}-{img} and root 2 = {real}+{img}")