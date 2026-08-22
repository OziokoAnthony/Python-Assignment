# 8-12. Sandwiches
# Question

# Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich being ordered. Call the function three times, using a different number of arguments each time.


def make_sandwich(*items):
    print("\nSandwich order:")

    for item in items:
        print(f"- {item}")


make_sandwich("cheese")

make_sandwich("cheese", "chicken", "lettuce")

make_sandwich("beef", "cheese", "tomato", "onion", "mayonnaise")


# 8-13. User Profile
# Question

# Start with a copy of user_profile.py. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.


def build_profile(first, last, **user_info):
    user_info["first"] = first
    user_info["last"] = last

    return user_info


profile = build_profile(
    "Anthony",
    "Ozioko",
    age=34,
    profession="Software Developer",
    country="Nigeria"
)

print(profile)


# 8-14. Cars
# Question

# Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or optional feature. Print the dictionary that’s returned.


def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }

    car.update(car_info)

    return car


car = make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)

print(car)
