import random

a = int(input("enter the number only(4, 6, 8) = "))

b1 = random.randint(1,9)
b = b1

b2 = random.randint(1,9)
b_2 = (b2)

b3 = random.randint(1,9)
b_3 = (b3)

c1 = random.randint(65,90)
c = chr(c1)

c2 = random.randint(65,90)
c_2 = chr(c2)

d1 = random.randint(97,122)
d = chr(d1)

d2 = random.randint(97,122)
d_2 = chr(d2)

e1 = random.randint(35,45)
e = chr(e1)

if a == 4:
    print("4 digit password = ",b,c,d,e)

elif a == 6:
    print("6 digit password = ",b,b_2,c,c_2,d,e)

elif a == 8:
    print("8 dgit password = ",b,b_2,b_3,c,c_2,d,d_2,e,)

else:
    print("sorry i can't help")