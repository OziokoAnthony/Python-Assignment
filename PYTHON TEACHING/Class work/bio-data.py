

# write a program that takes a user's first name, last name, age, and city as input, and then prints a message that uses the receive inputs. 

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"Hello, {first_name} {last_name}! You are {age} years old and live in {city}.")


# Store an hourly rate and hours worked. print the daily total, formatted with a thousand separator.

hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter your hours worked: "))

daily_total = hourly_rate * hours_worked
print(f"Your daily total is: ${daily_total:,.2f}")
