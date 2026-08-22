# 8-6. City Names
# Question

# Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


place_1 = city_country("santiago", "chile")
place_2 = city_country("london", "england")
place_3 = city_country("abuja", "nigeria")

print(place_1)
print(place_2)
print(place_3)


# 8-7. Album
# Question

# Write a function called make_album() that builds a dictionary describing a music album. The function should take an artist name and an album title, and return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value. Use None to add an optional parameter that allows you to store the number of songs on an album.


def make_album(artist, title, number_of_songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if number_of_songs:
        album["number_of_songs"] = number_of_songs

    return album


album_1 = make_album("Burna Boy", "Twice As Tall")
album_2 = make_album("Davido", "Timeless")
album_3 = make_album("Wizkid", "Made in Lagos")

print(album_1)
print(album_2)
print(album_3)

album_4 = make_album("Burna Boy", "Love, Damini", 19)

print(album_4)


# 8-8. User Albums
# Question

# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.


def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }

    return album


while True:
    print("\nEnter album information.")
    print("Enter 'q' at any time to quit.")

    artist = input("Artist: ")

    if artist == "q":
        break

    title = input("Album title: ")

    if title == "q":
        break

    album = make_album(artist, title)

    print(album)
