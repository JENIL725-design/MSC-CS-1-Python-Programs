# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.32 Python Program to create table, insert and display records
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS assignment_db")
mycursor.execute("USE assignment_db")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

mycursor.execute("DELETE FROM students")

sql = "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)"
values = [
    (1, "Jenil", 21),
    (2, "Rahul", 21),
    (3, "Priya", 23)
]

mycursor.executemany(sql, values)
mydb.commit()

print("Records inserted successfully")

mycursor.execute("SELECT * FROM students")
records = mycursor.fetchall()

print("Student Records:")
for row in records:
    print(row)

mydb.close()