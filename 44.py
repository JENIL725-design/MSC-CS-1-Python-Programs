import whois
domain = input("Enter Domain Name: ")
result = whois.whois(domain)
print("\nDomain Name:", domain)
print("Creation Date:", result.creation_date)
