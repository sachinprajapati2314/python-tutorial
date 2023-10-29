import shutil
f = open("my txt",'w')
f.write("hii sir How are you\n")
f.write("hii sachin how can help you ?")
f.close()

f1 = open("myfile txt","w")
f1.close

shutil.copyfile("my txt","myfile txt")

f1 = open("myfile txt","r")
print(f1.read())