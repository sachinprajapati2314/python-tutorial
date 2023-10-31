import os 

def check_permission(file_name):
    if os.access(file_name, os.R_OK):
        print(f"read permission is granted for file {file_name}")
    else:
        print(f"read permission is not granted for file {file_name}")
    if  os.access(file_name, os.W_OK):
        print(f"write permission is granted for file {file_name}")
    else:
        print(f"write permission is not granted for file {file_name}")
    if os.access(file_name, os.X_OK):
        print(f"execute permission is granted for file {file_name}")
    else:
        print(f"execute permission is not granted for file {file_name}")

file_name = ("mysp txt")
check_permission(file_name)