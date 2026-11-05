# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.28 Python Program to demonstrate the use of file handling
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

file = open("student.txt", "w")
file.write("Name: Jenil N Makwana\n")
file.write("Enrollment: 92600565009\n")
file.close()

file = open("student.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()