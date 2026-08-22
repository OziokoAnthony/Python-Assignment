# Original menu setup
buffet_menu = ("Rice", "Chicken", "Salad", "Soup", "Ice Cream")

print("--- Original Buffet Menu ---")
for food in buffet_menu:
    print(f"- {food}")

# Testing tuple immutability (Python will crash here on purpose)
print("\nTrying to change Chicken to Pasta...")
try:
    buffet_menu[1] = "Pasta"
except TypeError as error:
    print(f"Change blocked by Python: {error}")

# Overwriting the tuple to update the menu items
buffet_menu = ("Rice", "Steak", "Salad", "Pasta", "Ice Cream")

print("\n--- Revised Buffet Menu ---")
for food in buffet_menu:
    print(f"- {food}")
