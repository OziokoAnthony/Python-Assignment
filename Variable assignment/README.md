# Python Exercises Solutions

FIRST PYTHON CLASS AND TOPIC THOUGHT
01-05  Basic Syntax & Variables
06-10  Data Types & Conversions
11-15  Operators & Expressions
16-19  Conditionals
20-29  String Operations & Formatting
30     Palindrome Checker Mini Project


ASSIGNMENT
# Python Exercises Assignment
### Topics covered: Basic Syntax & Variables · Data Types & Conversions · Operators & Expressions · Conditionals · String Operations
*(Loops, functions, data structures, and file I/O are not required for this assignment.)*

*Adapted from: 100 Python Exercises with Solutions — Lkhibra Academy*
*Original exercise numbers are noted in parentheses for reference.*

---

## Part A — Basic Syntax & Variables

### Exercise 1 — Declare and Print Variables
**Objective:** Understand how to declare and print variables in Python.

**Task:**
- Declare variables for an instructor's name, the number of students in a Python class, and the course name.
- Print them using a formatted string.

**Expected Output Example:**
```
The instructor is Alex, there are 30 students in the Python class!
```

---

### Exercise 2 — Swap Two Variables Without a Third Variable
**Objective:** Swap two values without using a temporary variable.

**Task:**
- Swap the values of `students_morning = 15` and `students_evening = 25` without using an extra variable.

**Expected Output:**
```
Before Swap: Morning Batch = 15, Evening Batch = 25
After Swap: Morning Batch = 25, Evening Batch = 15
```

---

### Exercise 3 — Assign Multiple Variables in One Line
**Objective:** Learn how to assign multiple variables in one line.

**Task:**
- Assign values to three variables representing the number of Python, Java, and AI students in a single line.

**Expected Output:**
```
Python = 25, Java = 18, AI = 12
```

---

### Exercise 4 — Check the Type of a Variable
**Objective:** Learn how to check variable types using `type()`.

**Task:**
- Declare different types of variables: an integer (age), a float (course rating), and a string (course name).
- Use `type()` to check their data types.

**Expected Output:**
```
21 is of type <class 'int'>
4.9 is of type <class 'float'>
Python Programming is of type <class 'str'>
```

---

### Exercise 5 — Concatenating Strings
**Objective:** Learn how to concatenate (combine) multiple strings in Python.

**Task:**
- Declare three separate string variables: instructor, academy name, and slogan.
- Concatenate them to form a full sentence.
- Print the combined string.

**Expected Output:**
```
The instructor at Lkhibra Academy says: "Learning Python is fun!"
```

---

## Part B — Data Types & Conversions

### Exercise 6 — Convert String to Integer and Vice Versa
**Objective:** Learn how to convert between string and integer data types.

**Task:**
- Convert the string `"100"` into an integer.
- Convert the integer `42` into a string.
- Print both values along with their data types.

**Expected Output:**
```
Integer value: 100, Type: <class 'int'>
String value: 42, Type: <class 'str'>
```

---

### Exercise 7 — Convert Float to Integer and Vice Versa
**Objective:** Learn how to convert between float and integer values.

**Task:**
- Convert a float `9.75` into an integer.
- Convert an integer `50` into a float.
- Print both values along with their data types.

**Expected Output:**
```
Float to Int: 9, Type: <class 'int'>
Int to Float: 50.0, Type: <class 'float'>
```

---

### Exercise 8 — Convert a Boolean to an Integer
**Objective:** Learn how Boolean values convert to integers.

**Task:**
- Convert the Boolean values `True` and `False` into integers.
- Print their numerical values.

**Expected Output:**
```
True as an integer: 1
False as an integer: 0
```

---

### Exercise 9 — Convert List to a String and Back
**Objective:** Learn how to convert between lists and strings.

**Task:**
- Convert a list of words into a single string.
- Convert the string back into a list.

**Expected Output:**
```
List to String: Python, is, amazing
String to List: ['Python', 'is', 'amazing']
```

---

### Exercise 10 — Convert Dictionary Keys and Values to Lists
**Objective:** Learn how to extract dictionary keys and values as lists.

**Task:**
- Convert dictionary keys into a list.
- Convert dictionary values into a list.

**Expected Output:**
```
Keys: ['name', 'age', 'language']
Values: ['Lkhibra Academy', 5, 'Python']
```

---

## Part C — Operators & Expressions

### Exercise 11 — Perform Arithmetic Operations
**Objective:** Learn how to use arithmetic operators in Python.

**Task:**
- Perform addition, subtraction, multiplication, division, and modulus operations.
- Print the results.

**Expected Output:**
```
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.5
Modulus: 0
```

---

### Exercise 12 — Use Comparison Operators
**Objective:** Understand comparison operators in Python.

**Task:**
- Compare two numbers using comparison operators.
- Print the results.

**Expected Output:**
```
10 > 5: True
10 < 5: False
10 == 10: True
10 != 5: True
10 >= 5: True
10 <= 5: False
```

---

### Exercise 13 — Use Logical Operators
**Objective:** Learn how logical operators work in Python.

**Task:**
- Use `and`, `or`, and `not` to evaluate logical expressions.

**Expected Output:**
```
True and False: False
True or False: True
Not True: False
```

---

### Exercise 14 — Use Assignment Operators
**Objective:** Learn how assignment operators modify variables.

**Task:**
- Use different assignment operators to modify a variable.

**Expected Output:**
```
Initial Value: 10
After += : 15
After -= : 12
After *= : 24
After /= : 8.0
After %= : 0.0
```

---

### Exercise 15 — Use Bitwise Operators
**Objective:** Learn how to manipulate binary numbers using bitwise operators.

**Task:**
- Perform bitwise operations on integers.

**Expected Output:**
```
5 & 3 = 1
5 | 3 = 7
5 ^ 3 = 6
5 << 1 = 10
5 >> 1 = 2
```

---

## Part D — Conditionals

### Exercise 16 — Check if a Number is Even or Odd
**Objective:** Learn how to use the `if-else` statement in Python.

**Task:**
- Write a program that asks the user for a number.
- Check if the number is even or odd.
- Print the result.

**Expected Output:**
```
Enter a number: 7
7 is an odd number.
```

---

### Exercise 17 — Find the Largest Number
**Objective:** Learn how to compare values using `if-elif-else`.

**Task:**
- Take three numbers as input.
- Find and print the largest number.

**Expected Output:**
```
Enter three numbers: 5 12 9
The largest number is 12.
```

---

### Exercise 18 — Check if a Year is a Leap Year
**Objective:** Use conditional logic to determine leap years.

**Task:**
- Ask the user for a year.
- Check if it is a leap year.

**Expected Output:**
```
Enter a year: 2024
2024 is a leap year.
```

---

### Exercise 19 — Grade Classifier
**Objective:** Practice chaining multiple conditions with `if-elif-else`.

**Task:**
- Ask the user for a numeric test score (0–100).
- Assign a letter grade using the scale: 90+ → A, 80–89 → B, 70–79 → C, 60–69 → D, below 60 → F.
- Print the score and the corresponding grade.

**Expected Output:**
```
Enter your score: 84
Score: 84 -> Grade: B
```

---

## Part E — String Operations & Formatting

### Exercise 20 — Extract the Domain from an Email
**Objective:** Extract the domain name from an email address.

**Task:**
- Given an email address, extract and print the domain name.

**Expected Output:**
```
Domain: example.com
```

---

### Exercise 21 — Count the Occurrences of a Word in a Review
**Objective:** Count how many times a specific word appears in customer reviews.

**Task:**
- Given a review, count how often the word "quality" appears.

**Expected Output:**
```
The word 'quality' appears 3 times.
```

---

### Exercise 22 — Format an Invoice
**Objective:** Properly align items and prices in an invoice using string formatting.

**Task:**
- Format the invoice for items purchased and their prices.

**Expected Output:**
```
Item        Price
-------------------
Laptop      $1200.99
Mouse       $25.50
```

---

### Exercise 23 — Reverse Words in a Sentence
**Objective:** Reverse the order of words in a sentence while keeping their individual order intact.

**Task:**
- Reverse the words in the sentence: "Lkhibra Academy is great".

**Expected Output:**
```
great is Academy Lkhibra
```

---

### Exercise 24 — Extract Hashtags from a Social Media Post
**Objective:** Identify and extract all hashtags from a post.

**Task:**
- Extract all hashtags from: "Loving #Python and #Coding at #LkhibraAcademy"

**Expected Output:**
```
Hashtags: ['#Python', '#Coding', '#LkhibraAcademy']
```

---

### Exercise 25 — Validate a Password Strength
**Objective:** Check if a password meets security criteria.

**Task:**
- Ensure the password has at least 8 characters, including a number and special character.

---

### Exercise 26 — Remove Extra Spaces from a String
**Objective:** Clean up a messy text by removing unnecessary spaces.

**Task:**
- Remove excess spaces from: " Hello   World  !  "

**Expected Output:**
```
Hello World !
```

---

### Exercise 27 — Convert a String to Title Case
**Objective:** Convert a string so that each word starts with a capital letter.

**Task:**
- Convert "lkhibra academy python training" to title case.

**Expected Output:**
```
Lkhibra Academy Python Training
```

---

### Exercise 28 — Replace Words in a Text
**Objective:** Replace certain words in a text dynamically.

**Task:**
- Replace "Python" with "Java" in "I love Python programming".

**Expected Output:**
```
I love Java programming
```

---

### Exercise 29 — Check How a String Starts or Ends
**Objective:** Practice using `startswith()` and `endswith()` together with conditionals.

**Task:**
- Ask the user for a filename (e.g., "report.pdf").
- Check whether it starts with "report" and whether it ends with ".pdf".
- Print a message telling the user whether the file is a valid report PDF.

**Expected Output:**
```
Enter a filename: report.pdf
This is a valid report PDF file.
```

---

## Mini Project — Palindrome Checker

**Objective:** Combine variables, string operations, and conditionals into one small program.

**Task:**
- Ask the user to enter a word or phrase.
- Clean it up: remove spaces and convert it to lowercase (so "Race car" and "racecar" are treated the same).
- Check whether the cleaned text reads the same forwards and backwards.
- Print whether it is a palindrome or not.

**Expected Output:**
```
Enter a word or phrase: Racecar
Racecar is a palindrome!
```
```
Enter a word or phrase: Python
Python is not a palindrome.
```

**Hint:** You can reverse a string with slicing: `text[::-1]`. No loops or functions are required — a single `if-else` check is enough.

---

*End of Assignment. Good luck!*

