# Exercise 20 — Extract the Domain from an Email
# Objective: Extract the domain name from an email address.
# 
# Question:
# Given an email address, extract and print the domain name.
# 
# Expected output:
# Domain: example.com

email = input("Enter email address: ").strip()

if "@" in email:
    domain = email.split("@", 1)[1]
    print(f"Domain: {domain}")
else:
    print("Invalid email address.")
