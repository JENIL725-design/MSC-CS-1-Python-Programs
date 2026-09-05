#Name: Jenil Makwana
#Enrollment: 92600565009

#Q.15 Python Program to demonstrate the use of various arguments which can be passed to functions

print("Name: Jenil Makwana \n Enrollment: 92600565009")

def student(name, age=21):
    print("Student Name is: ", name)
    print("Student Age is: ", age)

print("Using positional arguments:")
student("Jenil", 22)

print("Using keyword arguments:")
student(age=22, name="Rahul")

print("Using default arguments:")
student("Karan")