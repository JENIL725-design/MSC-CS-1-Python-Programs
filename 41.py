# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.41 Python Program to perform WHOIS lookup
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import whois

domain = "google.com"
result = whois.whois(domain)

print("WHOIS Information:")
print(result)