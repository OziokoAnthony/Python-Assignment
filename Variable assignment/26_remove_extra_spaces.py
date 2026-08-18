# Exercise 26 — Remove Extra Spaces from a String
# Objective: Clean up a messy text by removing unnecessary spaces.
# 
# Question:
# Remove excess spaces from:
# " Hello   World  !  "
# 
# Expected output:
# Hello World !

text = " Hello   World  !  "

clean_text = " ".join(text.split())

print(clean_text)
