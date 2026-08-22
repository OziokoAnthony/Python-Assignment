# 10-6. Addition
# Question

# Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    result = first_number + second_number

    print(f"The answer is {result}.")

except ValueError:
    print("Please enter numbers only.")


# 10-7. Addition Calculator
# Question

# Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number

while True:
    print("\nEnter two numbers to add.")
    print("Enter 'q' to quit.")

    first_number = input("First number: ")

    if first_number == "q":
        break

    second_number = input("Second number: ")

    if second_number == "q":
        break

    try:
        first_number = int(first_number)
        second_number = int(second_number)

        result = first_number + second_number

    except ValueError:
        print("Please enter numbers only.")

    else:
        print(f"The answer is {result}.")
