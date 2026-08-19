# What is an exception in Python?
# An exception in Python is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions. It is an error that occurs at runtime, which can be caused by various factors such as invalid input, file not found, division by zero, etc. When an exception occurs, Python stops executing the current block of code and looks for a way to handle the exception. If the exception is not handled, it will terminate the program and display an error message.


# diving by zero
# result = 10 / 0
# print(result)


name = "Ifeanyi"
# total = '5' + names
# print(total)

# Types of errors
# 1. Syntax error
# 2. Exception (Runtime Error)

# TypeError
# print("hello" + 5)

# ValueError
# print(int('abc'))

# KeyError
# d = {"name": "rita"}
# print(d["age"])

# indexError
# names = ["Kosy", "Liliam", "Loveth"]
# names[4]

# NameError
# name = "Ifeanyi"
# total = '5' + names
# print(total)

# try/except

# try:
#     # code that might cause error
#     name = "Ifeanyi"
#     total = "5" + names
#     print(total)
# except NameError as e:
#     print(e)
#     print("There was an error here")

# Code that runs if that error occurs


# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError, NameError  as e:
#         print(e, "Why you dey divide by zero nah")

# divide(10, 0)

# try:
#     age = int(input("Enter your age: "))
#     print(ages)
# except (NameError, ValueError) as error:
#     print(error)

# else and finally
# try:
#     # Code that might fail
# except ExceptionType:
#     # Do something if this error occur
# else:
#     # Run ONLY if No exception occurred
# finally:
#     # runs always - whether or not an exception occurred.
#  db.close()

# try:
#     number = int(input("Enter a number"))
#     result = 100 / number
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print(f"Result: {result}")
# finally:
#     print("Greetings from nigeria")


def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistically large")
    print(f"Age set to {age}")


try:
    set_age(180)
except ValueError as e:
    print(e)


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError(f"Cannot withdraw {amount}. Balance is only {balance}")
    return balance - amount

try:
    new_balance = withdraw(100, 250)
except ValueError as e:
    print(f'Transaction failed: {e}')

