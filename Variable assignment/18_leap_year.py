# Exercise 18 — Check if a Year is a Leap Year
# Objective: Use conditional logic to determine leap years.
# 
# Question:
# Ask the user for a year and check whether it is a leap year.
# 
# Expected output:
# Enter a year: 2024
# 2024 is a leap year.

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
