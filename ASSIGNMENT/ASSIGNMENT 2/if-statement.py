
#  ALIEN COLORS #1

print("--- Exercise 5-3: Alien Colors #1 ---")

# The test
alien_color = 'green'
if alien_color == 'green':
    print("Version 1 (Passes): The player just earned 5 points.")

# Version that fails the test (produces no output)
alien_color = 'red'
if alien_color == 'green':
    print("Version 2 (Fails): The player just earned 5 points.")



#  ALIEN COLORS #2

print("\n--- Exercise 5-4: Alien Colors #2 ---")

# Version running the 'if' block
alien_color = 'green'
if alien_color == 'green':
    print("Version 1 (If): The player just earned 5 points for shooting the alien.")
else:
    print("Version 1 (Else): The player just earned 10 points.")

# Version running the 'else' block
alien_color = 'yellow'
if alien_color == 'green':
    print("Version 2 (If): The player just earned 5 points for shooting the alien.")
else:
    print("Version 2 (Else): The player just earned 10 points.")



# EXERCISE 5-5: ALIEN COLORS #3

print("\n--- Exercise 5-5: Alien Colors #3 ---")

# Version 1 (Green Alien)
alien_color = 'green'
if alien_color == 'green':
    print("Green Alien: The player earned 5 points.")
elif alien_color == 'yellow':
    print("Green Alien: The player earned 10 points.")
else:
    print("Green Alien: The player earned 15 points.")

# Version 2 (Yellow Alien)
alien_color = 'yellow'
if alien_color == 'green':
    print("Yellow Alien: The player earned 5 points.")
elif alien_color == 'yellow':
    print("Yellow Alien: The player earned 10 points.")
else:
    print("Yellow Alien: The player earned 15 points.")

# Version 3 (Red Alien)
alien_color = 'red'
if alien_color == 'green':
    print("Red Alien: The player earned 5 points.")
elif alien_color == 'yellow':
    print("Red Alien: The player earned 10 points.")
else:
    print("Red Alien: The player earned 15 points.")


#  STAGES OF LIFE

print("\n--- Exercise 5-6: Stages of Life ---")

# You can change this variable value to test different execution branches
age = 28

if age < 2:
    print(f"Age {age}: The person is a baby.")
elif age >= 2 and age < 4:
    print(f"Age {age}: The person is a toddler.")
elif age >= 4 and age < 13:
    print(f"Age {age}: The person is a kid.")
elif age >= 13 and age < 20:
    print(f"Age {age}: The person is a teenager.")
elif age >= 20 and age < 65:
    print(f"Age {age}: The person is an adult.")
else:
    print(f"Age {age}: The person is an elder.")
