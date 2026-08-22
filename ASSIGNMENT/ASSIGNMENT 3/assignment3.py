# 10-10. Common Words
# Question

# Find a few texts from Project Gutenberg and write a program that reads the files and determines how many times the word the appears in each text. Try counting the, with a space in the string, and see how much lower your count is .




from pathlib import Path

path = Path("sample.txt")

contents = path.read_text()

the_count = contents.lower().count("the")
the_space_count = contents.lower().count("the ")

print(f"The word 'the' appears about {the_count} times.")
print(f"The phrase 'the ' appears about {the_space_count} times.")
