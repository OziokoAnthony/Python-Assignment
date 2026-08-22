# Setup data for testing
car = 'Honda'                   #I change the car variable to 'Honda' to match the first test case
bike = 'Yamaha'
age = 25
score = 85
colors = ['red', 'blue', 'green']

#STANDARD EQUALITY & INEQUALITY (1-4)
print("1. Is car == 'Honda'? I predict True.")
print(car == 'Honda')

print("\n2. Is car == 'audi'? I predict False.")
print(car == 'audi')

print("\n3. Is bike != 'Honda'? I predict True.")
print(bike != 'Honda')

print("\n4. Is bike == 'yamaha'? I predict False (due to capital Y).")
print(bike == 'yamaha')

#LOWER() METHOD TESTS (5-6)
print("\n5. Is bike.lower() == 'yamaha'? I predict True.")
print(bike.lower() == 'yamaha')

print("\n6. Is car.lower() == 'HONDA'? I predict False.")
print(car.lower() == 'HONDA')

#NUMERICAL TESTS (7-12)
print("\n7. Is age == 25? I predict True.")
print(age == 25)

print("\n8. Is age != 25? I predict False.")
print(age != 25)

print("\n9. Is score > 80? I predict True.")
print(score > 80)

print("\n10. Is score < 50? I predict False.")
print(score < 50)

print("\n11. Is age >= 25? I predict True.")
print(age >= 25)

print("\n12. Is score <= 70? I predict False.")
print(score <= 70)

#AND / OR KEYWORD TESTS (13-16)
print("\n13. Is age > 20 and score > 80? I predict True.")
print(age > 20 and score > 80)

print("\n14. Is age > 30 and score > 80? I predict False.")
print(age > 30 and score > 80)

print("\n15. Is age > 30 or score > 80? I predict True.")
print(age > 30 or score > 80)

print("\n16. Is age > 30 or score < 50? I predict False.")
print(age > 30 or score < 50)

#LIST MEMBERSHIP TESTS (17-20)
print("\n17. Is 'blue' in colors? I predict True.")
print('blue' in colors)

print("\n18. Is 'yellow' in colors? I predict False.")
print('yellow' in colors)

print("\n19. Is 'yellow' not in colors? I predict True.")
print('yellow' not in colors)

print("\n20. Is 'red' not in colors? I predict False.")
print('red' not in colors)
