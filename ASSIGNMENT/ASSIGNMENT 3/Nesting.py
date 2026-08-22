# 6-7. People
# Question

# Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.


person_1 = {
    "first_name": "Anthony",
    "last_name": "Ozioko",
    "age": 34,
    "city": "Enugu"
}

person_2 = {
    "first_name": "Abigail",
    "last_name": "James",
    "age": 20,
    "city": "Lagos"
}

person_3 = {
    "first_name": "David",
    "last_name": "Okafor",
    "age": 25,
    "city": "Abuja"
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()


# 6-8. Pets
# Question

# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and print everything you know about each pet.


pet_1 = {
    "animal": "dog",
    "owner": "Anthony"
}

pet_2 = {
    "animal": "cat",
    "owner": "Abigail"
}

pet_3 = {
    "animal": "parrot",
    "owner": "David"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()


# 6-9. Favorite Places
# Question

# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    "Anthony": ["Enugu", "Abuja", "Lagos"],
    "Abigail": ["London", "Paris"],
    "David": ["Dubai", "New York", "Toronto"]
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")

    for place in places:
        print(f"- {place}")

    print()


# 6-10. Favorite Numbers
# Question

# Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.


favorite_numbers = {
    "Anthony": [7, 10, 21],
    "Abigail": [3, 8],
    "Augustine": [5, 15, 20],
    "James": [2, 12],
    "David": [4, 9, 18]
}

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")

    for number in numbers:
        print(number)

    print()


# 6-11. Cities
# Question

# Make a dictionary called cities. Use the names of three cities as keys. Create a dictionary of information about each city and include the country, approximate population, and one fact about that city. Print the name of each city and all the information stored about it.


cities = {
    "enugu": {
        "country": "Nigeria",
        "population": 722664,
        "fact": "Enugu is known as the Coal City."
    },

    "london": {
        "country": "United Kingdom",
        "population": 8982000,
        "fact": "London is the capital of the United Kingdom."
    },

    "paris": {
        "country": "France",
        "population": 2102650,
        "fact": "Paris is home to the Eiffel Tower."
    }
}

for city, information in cities.items():
    print(f"City: {city.title()}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
    print()


# 6-12. Extensions
# Question

# Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.


cities = {
    "enugu": {
        "country": "Nigeria",
        "population": 722664,
        "fact": "Enugu is known as the Coal City.",
        "language": "English",
        "famous_for": "Coal"
    },

    "london": {
        "country": "United Kingdom",
        "population": 8982000,
        "fact": "London is the capital of the United Kingdom.",
        "language": "English",
        "famous_for": "Big Ben"
    },

    "paris": {
        "country": "France",
        "population": 2102650,
        "fact": "Paris is home to the Eiffel Tower.",
        "language": "French",
        "famous_for": "Eiffel Tower"
    }
}

for city, information in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
    print(f"Language: {information['language']}")
    print(f"Famous for: {information['famous_for']}")
