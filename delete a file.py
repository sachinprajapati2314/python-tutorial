import os
f = open("my txt",'w')
f.write("hii sir How are you\n")
f.write("hii sachin how can help you ?")
f.close()

f = open("my txt","r")
print(f.read())

# delete  file (print error) plese don't panic
os.remove("my txt")


