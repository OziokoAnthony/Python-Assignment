# Exercise 2 — Swap Two Variables Without a Third Variable
# Objective: Swap two values without using a temporary variable.
# 
# Question:
# Swap the values of students_morning = 15 and students_evening = 25 without using an extra variable.
# 
# Expected output:
# Before Swap: Morning Batch = 15, Evening Batch = 25
# After Swap: Morning Batch = 25, Evening Batch = 15

students_morning = 15
students_evening = 25

print(f"Before Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")

students_morning, students_evening = students_evening, students_morning

print(f"After Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")
