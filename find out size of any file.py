f = open("my txt",'w')
f.write("hiii sir")
f.close()

f = open("my txt")
f_1 = f.read()

# bytes 
print(bytes(f_1,'utf-8'))