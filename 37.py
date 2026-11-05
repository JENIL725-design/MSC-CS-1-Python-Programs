# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.37 Python Program to create Pie Chart
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "PHP"]
marks = [85, 75, 65, 55]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Subject Marks Distribution")
plt.show()