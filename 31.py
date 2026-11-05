# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.31 Python Program to connect Python with MySQL database
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if mydb.is_connected():
    print("Database Connected Successfully")

mydb.close()