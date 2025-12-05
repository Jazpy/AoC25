import bisect

ranges = set()
ids = []
with open('inputs/05.txt') as in_f:
    range_flag = True
    for line in in_f:
        if not line.strip():
            range_flag = False
            continue

        if range_flag:
            toks = line.split('-')
            ranges.add((int(toks[0]), int(toks[1])))
        else:
            ids.append(int(line))
ranges = sorted(ranges)

coalesced = []
curr_range = list(ranges[0])
for r in ranges[1:]:
    if r[0] >= curr_range[0] and r[0] <= curr_range[1]:
        if r[1] > curr_range[1]:
            curr_range[1] = r[1]
    else:
        coalesced.append(curr_range)
        curr_range = list(r)
coalesced.append(curr_range)

silver, gold = 0, 0

for i in ids:
    for r in coalesced:
        if i >= r[0] and i <= r[1]:
            silver += 1
            break

for r in coalesced:
    gold += r[1] - r[0] + 1

print(silver)
print(gold)
