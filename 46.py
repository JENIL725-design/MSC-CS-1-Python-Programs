# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.46 Python Program to generate hash of a string
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import hashlib

text = "Cybersecurity"
print(f"Original Text: {text}\n")

# MD5 Hash
md5_hash = hashlib.md5(text.encode()).hexdigest()
print(f"MD5 Hash: {md5_hash}")

# SHA-256 Hash
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print(f"SHA-256 Hash: {sha256_hash}")