#Name: Jenil Makwana
#Enrollment: 92600565009

#Q.13 Python Program to demonstrate the use of dictionary and various functions of it

print("Name: Jenil Makwana \n Enrollment: 92600565009")

student = {
    "Name": "Jenil",
    "Age": 22,
    "Course": "MSc Cybersecurity"
}

print("The dictionary is: ", student)

print("The keys are: ", student.keys())

print("The values are: ", student.values())

print("The items are: ", student.items())

student["City"] = "Rajkot"
print("After adding City: ", student)

student.pop("Age")
print("After removing Age: ", student)

print("The length of dictionary is: ", len(student))