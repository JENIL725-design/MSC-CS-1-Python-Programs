#Name: Jenil Makwana
#Enrollment: 92600565009

# Q.23 Python Program to handle division by zero using try and except

print("Name: Jenil Makwana \n Enrollment: 92600565009")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")