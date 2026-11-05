# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.48 Python Program to demonstrate Exception Handling
print("Name: Jenil N Makwana \nEnrollment: 92600565009\n")

try:
    # Taking input from the user
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    
    # Attempting division
    result = num1 / num2
    print(f"Result of division: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero!")
    
except ValueError:
    print("Error: Please enter valid integer numbers only!")
    
finally:
    print("\nExecution of the try-except block is complete.")