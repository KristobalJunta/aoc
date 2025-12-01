import fileinput


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    return data


def parse_commands(data):
    commands = []
    for s in data:
        c, d = s.split()
        d = int(d)
        commands.append((c, d))
    return commands


def part1(data):
    x, y = 0, 0

    for command, dt in parse_commands(data):
        if command == "up":
            y -= dt
        elif command == "down":
            y += dt
        elif command == "forward":
            x += dt
        else:
            raise ValueError(command)

    return x * y


def part2(data):
    x, y, aim = 0, 0, 0

    for command, dt in parse_commands(data):
        if command == "up":
            aim -= dt
        elif command == "down":
            aim += dt
        elif command == "forward":
            x += dt
            y += aim * dt
        else:
            raise ValueError(command)

    return x * y


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
