import fileinput
import math


def get_input():
    data = [s.removesuffix('\n') for s in fileinput.input()]
    data = list(filter(None, data))
    return data


def part1(data):
    maxcubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    valid_ids = []

    for line in data:
        game, draws = line.split(':')
        _, game_id = game.split()
        game_valid = True

        for draw in draws.strip().split(';'):
            for cube in draw.strip().split(','):
                num, color = cube.strip().split()

                if int(num) > maxcubes[color.strip()]:
                    game_valid = False

        if game_valid:
            valid_ids.append(int(game_id))

    return sum(valid_ids)


def part2(data):
    results = []

    for line in data:
        _, draws = line.split(':')
        maxpercolor = dict()

        for draw in draws.strip().split(';'):
            for cube in draw.strip().split(','):
                num, color = cube.strip().split()
                maxpercolor[color] = max(maxpercolor.get(color, 0), int(num))

        results.append(math.prod(maxpercolor.values()))

    return sum(results)


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
