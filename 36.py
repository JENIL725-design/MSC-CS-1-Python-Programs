# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.36 Python Program to demonstrate different ways of creating DataFrames
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import pandas as pd

# Method 1: Using Dictionary
data1 = {
    "Name": ["Jenil", "Rahul"],
    "Age": [21, 21]
}
df1 = pd.DataFrame(data1)
print("DataFrame using Dictionary:")
print(df1)

# Method 2: Using List
data2 = [
    ["Jenil", 21],
    ["Rahul", 21],
    ["Priya", 23]
]
df2 = pd.DataFrame(data2, columns=["Name", "Age"])
print("\nDataFrame using List:")
print(df2)

# Method 3: Using List of Dictionaries
data3 = [
    {"Name": "Jenil", "Age": 21},
    {"Name": "Rahul", "Age": 21}
]
df3 = pd.DataFrame(data3)
print("\nDataFrame using List of Dictionaries:")
print(df3)

# Method 4: Using Series
data4 = {
    "Name": pd.Series(["Jenil", "Rahul"]),
    "Age": pd.Series([21, 21])
}
df4 = pd.DataFrame(data4)
print("\nDataFrame using Series:")
print(df4)