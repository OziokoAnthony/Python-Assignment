# Exercise 16 — Check if a Number is Even or Odd
# Objective: Learn how to use the if-else statement in Python.
# 
# Question:
# Write a program that asks the user for a number, checks if it is even or odd, and prints the result.
# 
# Expected output:
# Enter a number: 7
# 7 is an odd number.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
