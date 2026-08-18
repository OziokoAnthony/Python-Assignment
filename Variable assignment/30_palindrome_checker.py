# Mini Project — Palindrome Checker
# Objective: Combine variables, string operations, and conditionals into one small program.
# 
# Question:
# Ask the user to enter a word or phrase. Clean it up by removing spaces and converting it to lowercase. Check whether the cleaned text reads the same forwards and backwards. Print whether it is a palindrome or not.
# 
# Hint:
# You can reverse a string with slicing: text[::-1]. No loops or functions are required.
# 
# Expected output:
# Enter a word or phrase: Racecar
# Racecar is a palindrome!
# 
# Enter a word or phrase: Python
# Python is not a palindrome.

text = input("Enter a word or phrase: ")

cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print(f"{text} is a palindrome!")
else:
    print(f"{text} is not a palindrome.")
