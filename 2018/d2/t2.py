from difflib import ndiff

with open('input.txt') as infile:
    ids = infile.readlines()
    ids = list(map(lambda s: s.strip(), ids))

    for item in ids:
        ids.remove(item)

        for other in ids:
            diffs = list(ndiff(item, other))
            diffcount = len(list(filter(lambda s: s[0] == '-', diffs)))
            if diffcount < 2:
                for i, s in enumerate(diffs):
                    if s[0] == '-':
                        print(item[:i] + item[i + 1:])
                        exit()
