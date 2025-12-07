from functools import cache

with open('inputs/07.txt') as in_f:
    mat = in_f.readlines()
for row in mat:
    for i, c in enumerate(row):
        if c == 'S':
            start = (0, i)


def get_sides(m, y, x):
    ret = []
    if x != 0:
        ret.append((y, x - 1))
    if x < len(m[0]) - 1:
        ret.append((y, x + 1))
    return ret


hit = set()

@cache
def get_possibilities(n):
    y, x = n

    if y >= len(mat):
        return 1

    if mat[y][x] == '^':
        hit.add((y, x))
        return get_possibilities((y, x - 1)) + get_possibilities((y, x + 1))

    return get_possibilities((y + 1, x))

gold = get_possibilities(start)
print(len(hit))
print(gold)
