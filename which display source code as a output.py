source_code = """Hii sir
how are you 
how can hlep you """

print("source code :")
print(source_code)

f = open("source code.txt","w")
f.write(source_code)
f.close()

file_name = "source code.txt"

print(f"\n-> source code has been saved to {file_name}")