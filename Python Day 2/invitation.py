# guest = ("Darlington", "James", "Precious")
# print(f"Dear {guest[0]}, you are cordially invited to my birthday party.")
# print(f"Dear {guest[1]}, you are cordially invited to my birthday party.")
# print(f"Dear {guest[2]}, you are cordially invited to my birthday party.")

guest = ["Darlington", "James", "Precious"]

for i in guest:
    print(f"Dear {i}, you are cordially invited to my birthday party.")

popped_guest = guest.pop(2)

insert_guest = input("Name: ")
guest.append(insert_guest)


print(f"Dear {guest[0]}, you are cordially invited to my birthday party.")
print(f"Dear {guest[1]}, you are cordially invited to my birthday party.")
print(f"Dear {guest[2]}, you are cordially invited to my birthday party.")


guest.insert(0, "Amara")
print(f"Dear {guest[0]}, you are cordially invited to my birthday party.")

guest.append("Chisom")
print(f"Dear {guest[3]}, you are cordially invited to my birthday party.")




guests = ["Darlington", "James", "Chisom", "Dennis", "Precious", "David"]

print("I can invite only two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

for guest in guests:
    print(f"{guest}, you are still invited to dinner.")

del guests[0]
del guests[0]

print(guests)
