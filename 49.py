# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.49 Python Program to demonstrate File I/O operations
print("Name: Jenil N Makwana \nEnrollment: 92600565009\n")

filename = "sample.txt"

# Writing data to a file
with open(filename, "w") as file:
    file.write("Hello, this is a test file for Practical 49.\n")
    file.write("Cybersecurity is going to be awesome!")

print(f"Data successfully written to '{filename}'.")

# Reading data back from the file
print("\nReading data from the file:")
print("-" * 30)

with open(filename, "r") as file:
    content = file.read()
    print(content)
    
print("-" * 30)