import networkx as nx
from functools import cache

g = nx.DiGraph()
with open('inputs/11.txt') as in_f:
    for line in in_f:
        src = line.split(':')[0]
        for n in line.split(':')[1].split():
            g.add_edge(src, n)

silver = 0
for _ in nx.all_simple_paths(g, source='you', target='out'):
    silver += 1

@cache
def count(src, tgt):
    if src == tgt:
        return 1

    c = 0
    for n in g.successors(src):
        c += count(n, tgt)

    return c

svr_fft = count('svr', 'fft')
fft_dac = count('fft', 'dac')
dac_out = count('dac', 'out')

print(silver)
print(svr_fft * fft_dac * dac_out)
