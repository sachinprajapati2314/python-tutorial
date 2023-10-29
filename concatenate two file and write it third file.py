# file no. one
f = open("my txt",'w')
f.write("hello ")
f.close()

f = open("my txt")
f_1 = f.read()

# file no. two
f1 = open("mysp txt",'w')
f1.write("sachin prajapati")
f1.close()

f1 = open("mysp txt")
f_2 = f1.read()

# make file no. third
f2 = open("my third txt","w")
f2.write(f_1+f_2)
f2.close()

f2 = open("my third txt","r")
print(f2.read())
