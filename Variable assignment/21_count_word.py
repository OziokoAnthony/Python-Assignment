# Exercise 21 — Count the Occurrences of a Word in a Review
# Objective: Count how many times a specific word appears in customer reviews.
# 
# Question:
# Given a review, count how often the word "quality" appears.
# 
# Expected output:
# The word 'quality' appears 3 times.

review = input("Enter a review: ")

words = review.lower().split()
count = words.count("quality")

print(f"The word 'quality' appears {count} times.")
