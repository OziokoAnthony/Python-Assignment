# 6-4. Glossary 2
# Question

# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary.


glossary = {
    "variable": "A name that refers to a value.",
    "string": "A series of characters.",
    "list": "A collection of items.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A reusable block of code.",
    "loop": "A way to repeat code.",
    "integer": "A whole number.",
    "float": "A number with a decimal point.",
    "tuple": "An immutable collection of values.",
    "boolean": "A value that is either True or False."
}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}")


# 6-5. Rivers
# Question

# Make a dictionary containing three major rivers and the country each river runs through. Use a loop to print a sentence about each river. Use a loop to print the name of each river included in the dictionary. Use a loop to print the name of each country included in the dictionary.


rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")

for river in rivers:
    print(river.title())

print("\nCountries:")

for country in rivers.values():
    print(country.title())


# 6-6. Polling
# Question

# Use the code in favorite_languages.py. Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not . Loop through the list. If they have already taken the poll, print a message thanking them. If they have not, print a message inviting them to take the poll.


favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

people_to_poll = [
    "jen",
    "sarah",
    "michael",
    "david",
    "edward",
    "phil"
]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll.")
    else:
        print(f"{person.title()}, please take our favorite languages poll.")
