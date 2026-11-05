# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.47 Python Program to display current working directory and list files
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import os

# Get current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}\n")

# List all files and directories in the current path
print("Contents of the directory:")
contents = os.listdir(cwd)

for item in contents:
    print("-", item)