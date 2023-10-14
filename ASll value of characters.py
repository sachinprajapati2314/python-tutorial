# enter input
char = str(input('enter the (only)string = '))

for x in char:
    print(f"The ASll value of '{x}' = {ord(x)}")

print("\n")

# all alphabets with their ascii value
a = 64
i = 0

while(i <= 25):
    a = a + 1
    print(f"{chr(a)} = {a}")
    i += 1

print("\n")

b = 96
i = 0

while(i <= 25):
    b = b + 1
    print(f"{chr(b)} = {b}")
    i += 1