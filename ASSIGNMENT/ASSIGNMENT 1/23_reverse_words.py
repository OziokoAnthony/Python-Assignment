# Exercise 23 — Reverse Words in a Sentence
# Objective: Reverse the order of words in a sentence while keeping their individual order intact.
# 
# Question:
# Reverse the words in the sentence: "Lkhibra Academy is great".
# 
# Expected output:
# great is Academy Lkhibra

sentence = "Lkhibra Academy is great"

reversed_sentence = " ".join(sentence.split()[::-1])

print(reversed_sentence)
