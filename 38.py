# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.38 Python Program to create Histogram
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import matplotlib.pyplot as plt

marks = [45, 55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()