# Exercise 9 — Convert List to a String and Back
# Objective: Learn how to convert between lists and strings.
# 
# Question:
# Convert a list of words into a single string. Convert the string back into a list.
# 
# Expected output:
# List to String: Python, is, amazing
# String to List: ['Python', 'is', 'amazing']

words = ["Python", "is", "amazing"]

text = ", ".join(words)
words_again = text.split(", ")

print(f"List to String: {text}")
print(f"String to List: {words_again}")
