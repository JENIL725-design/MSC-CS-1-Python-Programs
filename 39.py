# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.39 Python Program to create Bar Graph
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "PHP"]
marks = [85, 75, 65, 55]

plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()