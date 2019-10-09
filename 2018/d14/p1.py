def solve(iterations):
    recipes = [3, 7]

    elf1 = 0
    elf2 = 1

    while len(recipes) < iterations + 10:
        recipes += list(map(int, list(str(recipes[elf1] + recipes[elf2]))))

        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

    print(recipes)
    return ''.join(map(str, recipes[iterations:iterations+10]))


assert solve(9) == '5158916779'
assert solve(5) == '0124515891'
assert solve(18) == '9251071085'
assert solve(2018) == '5941429882'
print(solve(293801))
