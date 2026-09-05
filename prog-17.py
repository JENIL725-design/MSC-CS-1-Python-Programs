#Name: Jenil Makwana
#Enrollment: 92600565009

#Q.17 Python Program to demonstrate the concept of inner class

print("Name: Jenil Makwana \n Enrollment: 92600565009")

class Student:
    def display(self):
        print("This is the Student class")

    class Address:
        def display_address(self):
            print("City: Rajkot")
            print("Country: India")

student1 = Student()
student1.display()

address1 = student1.Address()
address1.display_address()