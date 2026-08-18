# Exercise 19 — Grade Classifier
# Objective: Practice chaining multiple conditions with if-elif-else.
# 
# Question:
# Ask the user for a numeric test score (0–100). Assign a letter grade using:
# 90+ → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# below 60 → F
# 
# Print the score and corresponding grade.
# 
# Expected output:
# Enter your score: 84
# Score: 84 -> Grade: B

score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")
