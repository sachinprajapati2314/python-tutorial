import os

f = ("mysp txt")
d = "D:\\Users\\Username\\Documents\\mysp txt"

s = os.stat(f)
print("file size = ",s.st_size)

drive = os.path.splitdrive(d)
print("drive = ",d)
