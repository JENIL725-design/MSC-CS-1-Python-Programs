# Name: Jenil N Makwana
# Enrollment: 92600565009
# Q.45 Python Program to perform DNS lookup
print("Name: Jenil N Makwana \nEnrollment: 92600565009")

import subprocess

domain = "google.com"
print(f"--- Running DNS lookup for {domain} ---")

try:
    # Using 'nslookup' since 'dig' is not native to Windows
    result = subprocess.run(["nslookup", domain], capture_output=True, text=True, check=True)
    
    print("\nDNS Records:")
    print(result.stdout)
        
except FileNotFoundError:
    print("\nError: The command is not installed on this system.")
except subprocess.CalledProcessError as e:
    print(f"\nCommand failed with error: {e}")