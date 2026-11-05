# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.42 Python Program to accept domain name and display WHOIS information
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import whois

domain = input("Enter Domain Name: ")
result = whois.whois(domain)

print("\nWHOIS Information:")
print("Domain Name:", result.domain_name)
print("Registrar:", result.registrar)
print("Creation Date:", result.creation_date)
print("Expiration Date:", result.expiration_date)