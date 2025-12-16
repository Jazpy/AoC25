shape_sizes = {}
silver = 0
with open('inputs/12.txt') as in_f:
    for line in in_f:
        line = line.strip()

        if not line:
            continue

        if len(line) == 2:
            ctr = 0
            for _ in range(3):
                nl = next(in_f)
                ctr += nl.count('#')
            shape_sizes[int(line[0])] = ctr
        else:
            toks = line.split(':')
            area = int(toks[0].split('x')[0]) * int(toks[0].split('x')[1])

            used = 0
            for i, s in enumerate(toks[1].strip().split()):
                used += shape_sizes[i] * int(s)
            if used <= area:
                silver += 1

print(silver)
