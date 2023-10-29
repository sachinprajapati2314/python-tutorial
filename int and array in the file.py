# genrate 1-10 number in file
for i in range(1,11):
    f = open("my txt",'w')
    f.write(str(i))
    f.close()

    f = open("my txt","r")
    print(f.read())

# array in file 
a = [1,2,3,4]
b = ["hii","hello","bro"]

f = open("my txt",'w')
f.write(str(a))
f.write(str(b))
f.close()

f = open("my txt","r")
print("\narry in file = ",f.read())