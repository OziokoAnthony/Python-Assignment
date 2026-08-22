# 10-9. Silent Cats and Dogs
# Question

# Modify your except block in Exercise 10-7 to fail silently if either file is missing.



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
        print(contents)from pathlib import Path

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
