# Exercise 25 — Validate a Password Strength
# Objective: Check if a password meets security criteria.
# 
# Question:
# Ensure the password has at least 8 characters, including a number and special character.

password = input("Enter a password: ")

has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if len(password) >= 8 and has_number and has_special:
    print("Password is strong.")
else:
    print("Password is not strong enough.")
