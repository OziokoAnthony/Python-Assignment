# Exercise 17 — Find the Largest Number
# Objective: Learn how to compare values using if-elif-else.
# 
# Question:
# Take three numbers as input. Find and print the largest number.
# 
# Expected output:
# Enter three numbers: 5 12 9
# The largest number is 12.

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
third = float(input("Enter third number: "))

if first >= second and first >= third:
    largest = first
elif second >= first and second >= third:
    largest = second
else:
    largest = third

print(f"The largest number is {largest:g}.")
