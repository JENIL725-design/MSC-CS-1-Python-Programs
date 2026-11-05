# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.33 Python Program to update records in MySQL table
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

# Inserting initial record using your name
mycursor.execute("""
INSERT INTO students VALUES (1, 'Jenil', 21)
ON DUPLICATE KEY UPDATE name='Jenil', age=21
""")
mydb.commit()

# Updating the age
sql = "UPDATE students SET age = %s WHERE id = %s"
values = (22, 1)
mycursor.execute(sql, values)
mydb.commit()

print("Record updated successfully")

mycursor.execute("SELECT * FROM students")
records = mycursor.fetchall()

print("Updated Student Records:")
for row in records:
    print(row)

mydb.close()