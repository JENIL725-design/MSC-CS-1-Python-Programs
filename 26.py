# Name: Jenil N Makwana
# Enrollment: 92600565017
# Q.26 Python Program to use try-except-finally block
print("Name: Jenil N Makwana \nEnrollment: 92600565017")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
finally:
    print("This block is always executed.")