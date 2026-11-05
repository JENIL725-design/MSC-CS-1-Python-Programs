# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.35 Python Program to demonstrate the use of DataFrames
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import pandas as pd

data = {
    "Name": ["Jenil", "Rahul", "Priya"],
    "Age": [21, 21, 23],
    "City": ["Ahmedabad", "Rajkot", "Surat"]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

print("\nDataFrame Information:")
print(df.info())

print("\nFirst Two Records:")
print(df.head(2))