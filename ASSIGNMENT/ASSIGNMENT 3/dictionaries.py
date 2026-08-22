#  6-1. Person
# Question

# Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.



person = {
    "first_name": "Anthony",
    "last_name": "Ozioko",
    "age": 34,
    "city": "Enugu"
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])


# 6-2. Favorite Numbers
# Question

# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number.


favorite_numbers = {
    "Anthony": 7,
    "Abigail": 10,
    "Augustine": 21,
    "James": 15,
    "David": 3
}

print("Anthony's favorite number is", favorite_numbers["Anthony"])
print("Abigail's favorite number is", favorite_numbers["Abigail"])
print("Augustine's favorite number is", favorite_numbers["Augustine"])
print("James's favorite number is", favorite_numbers["James"])
print("David's favorite number is", favorite_numbers["David"])


# 6-3. Glossary
# Question

# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values. Print each word and its meaning as neatly formatted output.


glossary = {
    "variable": "A name that refers to a value.",
    "string": "A series of characters.",
    "list": "A collection of items stored in one variable.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A reusable block of code that performs a task."
}

print("Variable:", glossary["variable"])
print("\nString:", glossary["string"])
print("\nList:", glossary["list"])
print("\nDictionary:", glossary["dictionary"])
print("\nFunction:", glossary["function"])
