import time
import os 

f = ("my txt")

a = os.path.getctime(f)
b = os.path.getmtime(f)

cre_t = time.ctime(a)
mod_t = time.ctime(b)

print(f"created at = {cre_t}")
print(f"last modification = {mod_t}")