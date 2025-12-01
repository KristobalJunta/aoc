import fileinput


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    data = [tuple(x.strip().split() for x in s.split("|")) for s in data]
    return data


def part1(data):
    return sum(len(d) in (2, 3, 4, 7) for _, output in data for d in output)


def part2(data):
    res = 0

    # logic is weird, see notes.txt

    for signals, output in data:
        signals = [frozenset(x) for x in signals]
        output = [frozenset(x) for x in output]

        signals_by_len = {len(s): s for s in signals}

        digit_signal = {
            1: signals_by_len[2],
            4: signals_by_len[4],
            7: signals_by_len[3],
            8: signals_by_len[7],
        }

        # remove known digits
        for v in digit_signal.values():
            signals.remove(v)

        # find C segment
        c_seg = [
            seg
            for seg in "abcdefg"
            if sum(seg not in signal for signal in signals) == 2
            and seg in digit_signal[7]
        ].pop()

        digit_signal[5] = [s for s in signals if len(s) == 5 and c_seg not in s].pop()
        digit_signal[6] = [s for s in signals if len(s) == 6 and c_seg not in s].pop()

        # remove known digits again
        signals.remove(digit_signal[5])
        signals.remove(digit_signal[6])

        for signal in signals:
            if len(signal) == 5 and signal > digit_signal[1]:
                digit_signal[3] = signal
            elif len(signal) == 6:
                if signal > digit_signal[4]:
                    digit_signal[9] = signal
                else:
                    digit_signal[0] = signal

        digit_signal[2] = [s for s in signals if s not in digit_signal.values()].pop()
        signal_digit = {v: k for k, v in digit_signal.items()}

        # from pprint import pprint
        # pprint({k: "".join(v) for k, v in digit_signal.items()})

        locres = int("".join(str(signal_digit[s]) for s in output))
        res += locres

    return res


if __name__ == "__main__":
    indata = get_input()
    print(part1(indata))
    print(part2(indata))


### NOTES

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg


digit | # segs | seg ids
1     | 2      | cf
7     | 3      | acf
4     | 4      | bcdf
8     | 7      | abcdefg
2     | 5      | acdeg
3     | 5      | acdfg
5     | 5      | abdfg
6     | 6      | abdefg
0     | 6      | abcefg
9     | 6      | abcdfg


Deriving digits from signal observation

first we get digits that have unique segments count
- 1 has 2 segs
- 7 has 3 segs
- 4 has 4 segs
- 8 has 7 segs

digits 5 and 6 can be derived as they have 1 common segment missing
segment C is not in 5 and 6, but is in all other digits
- 5 has 5 segs and does not include C seg
- 6 has 6 segs and does not include C seg

some digits can then be derived based on the ones we already got
with some help of set algebra:
- 3 has 5 segs and is superset of 1
- 9 has 6 segs and is superset of 4
- 0 has 6 segs and is not a superset of 4

after all this, digit 2 is the last one left
"""
