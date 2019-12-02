def intprog(memory, noun, verb):
    memory[1:3] = [noun, verb]
    ptr = 0

    while True:
        opcode = memory[ptr]

        if opcode == 99:
            break

        pos_a, pos_b, pos_r = memory[ptr + 1:ptr + 4]

        if opcode == 1:
            memory[pos_r] = memory[pos_a] + memory[pos_b]
        if opcode == 2:
            memory[pos_r] = memory[pos_a] * memory[pos_b]

        ptr += 4

    return memory[0]
