# in the first way
a = str( input("enter string = ") )

s = []

for i in a:
    if i in "aeiouAEIOU":
      s.extend(i)
s = ' '.join(s)

print("consonants = ",str(s))

# in the second way
st = input("enter string = ")
k = str("")

for j in st:
  if j in "aeiouAEIOU":
     l=k.removeprefix()
print(str(l))