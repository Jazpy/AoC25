import bisect

nums = []
with open('inputs/06.txt') as in_f:
    for line in in_f:
        if line[0] == '+' or line[0] == '*':
            ops = line.split()
        else:
            nums.append(line.split())

def opper(n, x, o):
    if o == '+':
        return n + x
    else:
        return n * x

silver = 0
for i in range(len(ops)):
    curr_result = 0 if ops[i] == '+' else 1
    for r in nums:
        curr_result = opper(curr_result, int(r[i]), ops[i])
    silver += curr_result

gold = 0

print(silver)
print(gold)
