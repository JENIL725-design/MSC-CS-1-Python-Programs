#Name: Jenil Makwana
#Enrollment: 92600565009

# Q.21 Python Program to show single inheritance using classes Animal and Dog

print("Name: Jenil Makwana \n Enrollment: 92600565009")

class Animal:
    def eat(self):
        print("Animal can eat")


class Dog(Animal):
    def bark(self):
        print("Dog can bark")


dog = Dog()
dog.eat()
dog.bark()