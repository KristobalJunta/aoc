import re


def parse_line(line):
    groups = re.search('\[\d{4}-\d{2}-\d{2} (\d{2}):(\d{2})\]\s(\w+)\s(#\d+)?', line).groups()
    hour = int(groups[0])
    minute = int(groups[1])
    action = groups[2]
    guard = int(groups[3][1:]) if groups[3] else None
    return hour, minute, action, guard


with open('input.txt') as infile:
    lines = sorted(infile.readlines(), key=lambda s: s[1:17])

    guards = dict()

    cur_guard = -1
    timestamp = -1
    for line in lines:
        hour, minute, action, guard = parse_line(line)
        if action == 'Guard':
            if guard not in guards:
                guards[guard] = [0]*60
            cur_guard = guard
            timestamp = -1
        if action == 'falls':
            timestamp = minute
        if action == 'wakes':
            if timestamp != -1:
                guards[cur_guard][timestamp:minute] = [t + 1 for t in guards[cur_guard][timestamp:minute]]
                timestamp = -1
            else:
                raise Exception('invalid timestamp')

    for guard in guards:
        data = guards.get(guard)
        sleep_time = sum(data)
        print(str(guard).ljust(6), str(sleep_time).ljust(4), data, len(data))

    max_guard = -1
    max_minute = -1
    max_freq = -1

    for guard in guards:
        data = guards[guard]
        minute, freq = max(enumerate(data), key=lambda e: e[1])

        if freq >= max_freq:
            max_guard = guard
            max_minute = minute
            max_freq = freq

            print(guard, minute, freq)

    print(max_guard, max_minute)
    print(max_guard * max_minute)
