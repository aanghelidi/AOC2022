from typing import Iterator

NEIGHBOURS_DELTAS = [complex(-1,0), complex(1,0), complex(0,-1),complex(0,1)]
ans = 0
M = {} 
with open("sample.txt")  as f:
    for y,line in enumerate(f):
        line = line.strip()
        for x,value in enumerate(line):
            M[complex(x,y)] = int(value)

max_x = max(x.real for x in M.keys())
max_y = max(x.imag for x in M.keys())
num_out = 4* max_x
num_in = 0
edges = {0,max_x,max_y}

def get_trees_between_edges(pos: complex) -> Iterator[complex]:
    for n_del in NEIGHBOURS_DELTAS:
        n_pos = pos +n_del
        while n_pos in M:
            yield n_pos
            n_pos += n_del

for pos in M:
    if pos.real in edges or pos.imag in edges:
        continue
    num_in += check_is_visible(pos)

print(num_in+num_out)

