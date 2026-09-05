#Name: Jenil Makwana
#Enrollment: 92600565009

#Q.5 Python program to find fibonacci series

n=int(input("Enter the number: "))

a=0
b=1
for i in range (n):
    a,b=b,a+b
    print(a)