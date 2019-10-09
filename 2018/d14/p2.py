def find_pattern(haystack, pattern):
    haystack = ''.join(map(str, haystack))
    try:
        return haystack.index(pattern)
    except ValueError:
        return -1


def solve(pattern):
    recipes = [3, 7]

    elf1 = 0
    elf2 = 1

    pat_len = 0

    while True:
        new_recipes = list(map(int, list(str(recipes[elf1] + recipes[elf2]))))
        recipes += new_recipes

        for recipe in new_recipes:
            if int(pattern[pat_len]) == recipe:
                pat_len += 1
            else:
                pat_len = 0

            if pat_len == len(pattern):
                return find_pattern(recipes, pattern)

        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)


assert solve('51589') == 9
assert solve('01245') == 5
assert solve('92510') == 18
assert solve('59414') == 2018
print(solve('293801'))
