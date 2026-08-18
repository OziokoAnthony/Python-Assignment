# Exercise 29 — Check How a String Starts or Ends
# Objective: Practice using startswith() and endswith() together with conditionals.
# 
# Question:
# Ask the user for a filename, such as "report.pdf". Check whether it starts with "report" and ends with ".pdf". Print whether it is a valid report PDF.
# 
# Expected output:
# Enter a filename: report.pdf
# This is a valid report PDF file.

filename = input("Enter a filename: ").strip()

if filename.startswith("report") and filename.endswith(".pdf"):
    print("This is a valid report PDF file.")
else:
    print("This is not a valid report PDF file.")
