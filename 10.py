from queue import Queue
import z3

def parse_machine(s):
    toks = s.split()
    goal = tuple([x == '#' for x in toks[0][1:-1]])
    buttons = []
    for tok in toks[1:-1]:
        buttons.append(tuple([int(x) for x in tok[1:-1].split(',')]))
    joltages = tuple([int(x) for x in toks[-1][1:-1].split(',')])

    return (goal, buttons, joltages)

machines = []
with open('inputs/10.txt') as in_f:
    for line in in_f:
        machines.append(parse_machine(line))

silver = 0
gold = 0
for goal, buttons, joltages in machines:
    # Silver
    cache = set()
    q = Queue()
    q.put((tuple([False for _ in goal]), None, 0))
    while q:
        curr_state, prev, steps = q.get()

        if curr_state in cache:
            continue

        if curr_state == goal:
            silver += steps
            break

        cache.add(curr_state)
        for b in buttons:
            if b == prev:
                continue

            new_state = tuple([not x if i in b else x for i, x in enumerate(curr_state)])
            q.put((new_state, b, steps + 1))

    # Gold
    s = z3.Optimize()
    ps = [z3.Int(f'p{i}') for i, _ in enumerate(buttons)]

    for p in ps:
        s.add(p >= 0)

    for i, joltage in enumerate(joltages):
        indices = [j for j in range(len(buttons)) if i in buttons[j] ]
        s.add(z3.Sum([ps[j] for j in indices]) == joltage)

    all_presses = z3.Sum(ps)
    s.minimize(all_presses)

    if s.check() == z3.sat:
        m = s.model()
        sol = [m[p].as_long() for p in ps]
        gold += sum(sol)

print(silver)
print(gold)
