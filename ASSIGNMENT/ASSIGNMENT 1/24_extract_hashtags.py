# Exercise 24 — Extract Hashtags from a Social Media Post
# Objective: Identify and extract all hashtags from a post.
# 
# Question:
# Extract all hashtags from:
# "Loving #Python and #Coding at #LkhibraAcademy"
# 
# Expected output:
# Hashtags: ['#Python', '#Coding', '#LkhibraAcademy']

post = "Loving #Python and #Coding at #LkhibraAcademy"

hashtags = [word for word in post.split() if word.startswith("#")]

print(f"Hashtags: {hashtags}")
