
# HELLO ADMIN & NO USERS
print("--Greetings ---")

# Step 1: Initialize list with usernames
usernames = ['admin', 'jaden', 'sarah', 'alex', 'emma']

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Step 2:
print("\nTesting empty list scenario:")
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")


#CHECKING USERNAMES
print("\n--- Exercise 5-10: Checking Usernames ---")

current_users = ['john', 'sarah', 'Alex', 'emma', 'chris']
new_users = ['mario', 'SARAH', 'lisa', 'JOHN', 'david']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. You will need to enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")


#ORDINAL NUMBERS
print("\nOrdinal Numbers ---")

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        suffix = "st"
    elif number == 2:
        suffix = "nd"
    elif number == 3:
        suffix = "rd"
    else:
        suffix = "th"
    
    print(f"{number}{suffix}")
