#Name: Jenil Makwana
#Enrollment: 92600565009

#Q.20(b) Python Program to show method overriding using a parent class Animal and a child class Dog

print("Name: Jenil Makwana \n Enrollment: 92600565009")

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()