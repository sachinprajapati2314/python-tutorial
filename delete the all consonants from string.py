a = str( input("enter string = ") )

s = []

for i in a:
    if i in "aeiouAEIOU":
      s.extend(i)
s = ' '.join(s)

print("consonants = ",str(s))