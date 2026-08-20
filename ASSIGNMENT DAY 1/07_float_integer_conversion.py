# Exercise 7 — Convert Float to Integer and Vice Versa
# Objective: Learn how to convert between float and integer values.
# 
# Question:
# Convert a float 9.75 into an integer. Convert an integer 50 into a float. Print both values along with their data types.
# 
# Expected output:
# Float to Int: 9, Type: <class 'int'>
# Int to Float: 50.0, Type: <class 'float'>

price = 9.75
count = 50

price_as_int = int(price)
count_as_float = float(count)

print(f"Float to Int: {price_as_int}, Type: {type(price_as_int)}")
print(f"Int to Float: {count_as_float}, Type: {type(count_as_float)}")
