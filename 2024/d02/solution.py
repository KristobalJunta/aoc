import fileinput


def get_input():
    return list(
        list(map(int, x))
        for x in map(
            str.split,
            filter(None, (s.removesuffix("\n") for s in fileinput.input())),
        )
    )


def part1(data):
    def is_safe(report):
        diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
        return all(abs(x) < 4 for x in diffs) and (
            all(x > 0 for x in diffs) or all(x < 0 for x in diffs)
        )

    safety_checks = [is_safe(r) for r in data]

    return sum(safety_checks)


def part2(data):
    pass


if __name__ == "__main__":
    indata = get_input()

    print(part1(indata))
    print(part2(indata))
