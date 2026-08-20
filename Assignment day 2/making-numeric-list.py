for number in range(1, 21):
    print(number)

    numbers = list(range(1, 1_000_001))

for number in numbers:
    print(number)


    numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))


odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

    multiples_of_three = list(range(3, 31, 3))

for number in multiples_of_three:
    print(number)


    cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

    cubes = [number ** 3 for number in range(1, 11)]

for cube in cubes:
    print(cube)