# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.30 Python Program to demonstrate the use of regular expression
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import re
text = "My enrollment number is 92600565009."
pattern = r"\d+"
result = re.findall(pattern, text)
print("Numbers found in the text:", result)