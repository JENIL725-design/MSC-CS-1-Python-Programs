# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.34 Python Program to delete records from MySQL table
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

# Re-inserting the record so we have something to delete
mycursor.execute("""
INSERT INTO students VALUES (1, 'Jenil', 21)
ON DUPLICATE KEY UPDATE name='Jenil', age=21
""")
mydb.commit()

# Deleting the record we just inserted
sql = "DELETE FROM students WHERE id = %s"
value = (1,)
mycursor.execute(sql, value)
mydb.commit()

print("Record deleted successfully")

mycursor.execute("SELECT * FROM students")
records = mycursor.fetchall()

print("Remaining Student Records:")
for row in records:
    print(row)

mydb.close()