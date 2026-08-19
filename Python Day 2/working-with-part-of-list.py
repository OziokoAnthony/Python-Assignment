cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[3:6])

print("The last three items in the list are:")
print(cubes[-3:])



pizzas = ["pepperoni", "chicken", "hawaiian"]

friend_pizzas = pizzas[:]

pizzas.append("beef")

friend_pizzas.append("vegetable")

print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)


friend_pizzas = pizzas[:]



foods = ["pizza", "falafel", "carrot cake"]

for food in foods:
    print(food)

print()

foods = ["pizza", "falafel", "carrot cake"]

for food in foods:
    print(food)





my_foods = ["pizza", "falafel", "carrot cake"]

friend_foods = my_foods[:]

my_foods.append("ice cream")
friend_foods.append("cannoli")

print("My favorite foods are:")

for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")

for food in friend_foods:
    print(food)
