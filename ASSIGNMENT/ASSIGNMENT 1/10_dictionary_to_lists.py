# Exercise 10 — Convert Dictionary Keys and Values to Lists
# Objective: Learn how to extract dictionary keys and values as lists.
# 
# Question:
# Convert dictionary keys into a list. Convert dictionary values into a list.
# 
# Expected output:
# Keys: ['name', 'age', 'language']
# Values: ['Lkhibra Academy', 5, 'Python']

academy = {
    "name": "Lkhibra Academy",
    "age": 5,
    "language": "Python"
}

keys = list(academy.keys())
values = list(academy.values())

print(f"Keys: {keys}")
print(f"Values: {values}")
