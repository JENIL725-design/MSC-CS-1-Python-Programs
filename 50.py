# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.50 Python Program to demonstrate Classes and Objects
print("Name: Jenil N Makwana \nEnrollment: 92600565009\n")

# Defining the class
class Student:
    def __init__(self, name, enrollment):
        self.name = name
        self.enrollment = enrollment

    def display_info(self):
        print("--- Student Record ---")
        print(f"Name: {self.name}")
        print(f"Enrollment Number: {self.enrollment}")

# Creating an object of the Student class using your details
student1 = Student("Jenil N Makwana", "92600565009")

# Calling the method to display the data
student1.display_info()