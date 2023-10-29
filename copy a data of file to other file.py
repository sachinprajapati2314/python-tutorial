import shutil

#file no.1
f = open("my txt",'w')
f.write("hii sir How are you\n")
f.write("hii sachin how can help you ?")
f.close()

# file no.2
f1 = open("myfile txt","w")
f1.close

# copy file no.1 to file no.2
shutil.copyfile("my txt","myfile txt")

# read file no.2
f1 = open("myfile txt","r")
print(f1.read())