# DELI & NO PASTRAMI

print("--Deli Order Queue ---")

# Initial orders containing at least three pastrami sandwiches
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'roast beef', 'pastrami', 'club']
finished_sandwiches = []

# Alert the user that pastrami is out of stock
print("Sorry, the deli has completely run out of pastrami today!\n")

# Use a while loop to remove all instances of 'pastrami' from the queue
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process the remaining orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print final confirmation summary
print("\nAll orders complete. The following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")


#  DREAM VACATION POLL

print("\n--Dream Vacation Poll ---")

responses = {}
polling_active = True

while polling_active:
    # Get the user's name and their response
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, where would you go? ")
    
    # Store the response in our dictionary matrix
    responses[name] = location
    
    # Check if anyone else wants to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Show results breakdown
print("\n--- Poll Results ---")
for name, location in responses.items():
    print(f"{name.title()} wants to visit {location.title()}.")