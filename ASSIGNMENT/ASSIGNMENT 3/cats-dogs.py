# 10-8. Cats and Dogs
# Question

# Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print their contents. Use a try -except block to catch FileNotFoundError, and print a friendly message if a file is missing.



from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for filename in files:
    path = Path(filename)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")

    else:
        print(f"\nContents of {filename}:")
        print(contents)



from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for filename in files:
    path = Path(filename)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        pass

    else:
        print(f"\nContents of {filename}:")
        print(contents)