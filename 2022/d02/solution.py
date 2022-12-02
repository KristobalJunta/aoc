import fileinput
import enum


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    return data


class Shape(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


CHAR_SHAPE = {
    'A': Shape.ROCK,
    'B': Shape.PAPER,
    'C': Shape.SCISSORS,
    'X': Shape.ROCK,
    'Y': Shape.PAPER,
    'Z': Shape.SCISSORS,
}


def game_score(elf, me):
    if elf == me:
        return 3
    else:
        if (
            elf == Shape.ROCK and me == Shape.PAPER
            or elf == Shape.PAPER and me == Shape.SCISSORS
            or elf == Shape.SCISSORS and me == Shape.ROCK
        ):
            return 6
        else:
            return 0


def part1(data):
    score = 0

    for line in data:
        a, b = line.split()
        elf = CHAR_SHAPE[a]
        me = CHAR_SHAPE[b]

        score += game_score(elf, me) + me.value

    return score


def part2(data):
    picks_win = {
        Shape.ROCK: Shape.PAPER,
        Shape.PAPER: Shape.SCISSORS,
        Shape.SCISSORS: Shape.ROCK,
    }
    picks_loose = {v: k for k, v in picks_win.items()}

    score = 0

    for line in data:
        shape, outcome = line.split()
        shape = CHAR_SHAPE[shape]

        if outcome == 'X':  # lose
            score += 0 + picks_loose[shape].value
        elif outcome == 'Y':  # draw
            score += 3 + shape.value
        else:  # Z means win, ага да конєшно
            score += 6 + picks_win[shape].value

    return score


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
