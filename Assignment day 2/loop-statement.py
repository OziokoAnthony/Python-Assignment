# PIZZA TOPPINGS

from json.encoder import INFINITY
print("--- Exercise 7-4: Pizza Toppings ---")

prompt = "\nEnter a pizza topping (or type 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza!")


#  MOVIE TICKETS

print("\n--- Movie Tickets ---")

age_prompt = "\nEnter your age to see ticket price (or type 'quit' to exit): "

while True:
    user_input = input(age_prompt)
    if user_input.lower() == 'quit':
        break
    
    age = int(user_input)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")


# THREE EXITS (Using Pizza Loop)

print("\n- Three Exits ---")

# Version 1: Conditional test directly in the while statement
print("\n[Version 1: Conditional test in while statement]")
user_topping = ""
while user_topping.lower() != 'quit':
    user_topping = input("Enter topping (type 'quit' to exit): ")
    if user_topping.lower() != 'quit':
        print(f"Adding {user_topping} to your pizza.")

# Version 2: Active flag variable (Boolean flag)
print("\n[Version 2: Active variable flag]")
active = True
while active:
    user_topping = input("Enter topping (type 'quit' to exit): ")
    if user_topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {user_topping} to your pizza.")

# Version 3: Using a break statement
print("\n[Version 3: Using break statement]")
while True:
    user_topping = input("Enter topping (type 'quit' to exit): ")
    if user_topping.lower() == 'quit':
        break
    print(f"Adding {user_topping} to your pizza.")



# #  INFINITY (Uncomment to test)

# print("\n--- Infinity ---")
# while True:
#     print("This loop runs forever! Press CTRL+C to stop it.")
