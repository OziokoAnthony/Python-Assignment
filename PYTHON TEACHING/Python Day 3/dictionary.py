
    # Dictionaries
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

# std = ['Alice', 20, 'A']

# student = {"name": "Alice", "age": 20, "grade": "A", "hobbies": ["reading", "swimming", "coding"]}

# print(student["name"])
# print(student["age"])

inventory = {}
# print(inventory)
# print(type(inventory))
# print(len(inventory))


# dict() constructor
# list()

# person = dict(name="Amara", age=30, city = "Lagos" )

t = ("age", "20", "name", "amara")
# print(person)

# Accessing values


# print(profile["courses"])
# print(profile["citizenship"])
# print(profile["age"])

# .get() method

# print(profile.get('grade'))
# print(profile.get('courses'))
# print(profile.get('citizenship'))
# print(profile.get('age'))

# Checking if a key exists
# print("name" in profile)
# print("age" in profile)

# profile = {
#     "name": "Rita",
#     "citizenship": ["Nigerian", "Canadian", "Indian"],
#     "courses": ["Mth101", "Bio101", "Chm101"],
#     "grade": "A",
# }
# Modifying Dictionaries
# # Adding a new key value pair
# profile["courses"].append("Gst101")
# profile["courses"].insert(1, "Phy101")

# profile["age"] = 30

person = {"name": "Rita", "age": 30, "country": "Nigeria"}
# .pop()
# print(person.pop("state", "None"))

# .popitem()
# print(person.popitem())


# Removing item
# del
# del person["age"]
del person
# del deletes by reference and deletes totally.

# print(person)

# clear()
# person = {"name": "Rita", "age": 30, "country": "Nigeria"}
# print(person.clear())
# print(person)

# updating with another dict

student = {
    "name": "Rita",
    "citizenship": ["Nigerian", "Canadian", "Indian"],
    "courses": ["Mth101", "Bio101", "Chm101"],
    "grade": "A",
    "state": "Enugu",
    "age": 30,
    "gpa": 3.9,
}

bio = {"state": "Enugu", "age": 30, "gpa": 3.9}

# student.update(bio)
# student["bio"] = {}
# print(student)

ENUM = {
    "UNDER-REVIEW": "under-review",
    "APPROVED": "approved",
    "REJECTED": "rejected",
}

property = {
    "name": "Eccima building",
    "amenties": ["toilets", "power", "good road"],
    "location": "All saints roundout",
    "price": 130_000_000,
    "status": ENUM["APPROVED"],
}

# update
property.update(
    {
        "location": "Shoprite roundout",
        "price": 150_000_000,
    }
)

# print(property)

# dict.keys()
get_all_key = property.keys()
# print(get_all_key)

# dict.values()
get_all_values = property.values()
# print(get_all_values)

# dict.items()
get_all_items = property.items()
# print(get_all_items)


# for i in property.items():
#     print(i)

# t = ('name', 'Eccima building')
# # print(t[1])


product_prices = {"Laptop": 999.99, "Mouse": 25.50, "Keyboad": 49.00, "Monitor": 299.00}
total = 0

# print("------ Invoice -------")
# for product, price in product_prices.items():
#     print(f"{product}\t\t $\t{price}")
#     total += price

# print("-" * 22)
# print(f"{'TOTAL':<12} ${total:>8.2f}")


school = {
    "student_1": {"name": "Amara", "age": 20, "grade": "A"},
    "student_2": {"name": "Rita", "age": 22, "grade": "B"},
    "student_3": {"name": "Charles", "age": 21, "grade": "C"},
}

# Get alice's grade
# print(school.get("student_1").get("grade"))
# print(school.get("student_3").update({"grade": "F"}))
school["student_3"]["grade"] = "A"
# print(school)

# Nested looping
# for student_id, info in school.items():
#     print(f'\n {student_id}:')
# for field, value in info.items():
#         print(f' {field}: {value}')

# Dictionary Comprehensions

# squares = {}
# for n in range(1, 6):
#     squares[n] = n**2

# output = [1, 4, 9, 16, 25]
# squares = [n**2 for n in range(1,6)]

# {key_expression: value_expression for var in iterable}

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares = {n**2: n for n in range(1, 6)}
# print(squares)

# swap keys and values  {1: 'a', 2: 'b', 3: 'c'}
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
# print(inverted)

score = {"Rita": 88, "Amara": 45, "James": 72, "Ifeanyi": 39, "Lilian": 95}

# Only keep students who passed (score >= 50)
# Output = {"Rita": 88, "James": 72, "Lilian":95}

passed = {key: value for key, value in score.items() if value >= 50}
# print(passed)

# Price discount
# Apply a 10% discount to all products in the price dictionary
import math


price = {"Laptop": 999.99, "Mouse": 25.50, "Keyboard": 49.00, "Monitor": 299.00}

discounted = {key: math.ceil(value * 0.9) for key, value in price.items()}
# print(discounted)