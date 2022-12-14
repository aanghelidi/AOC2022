import itertools
from collections import deque
from operator import attrgetter

START, rocks = complex(500, 0), set()

with open("input.txt") as f:
    paths = [p.split(" -> ") for p in f.read().strip().splitlines()]

for path in paths:
    for begin_position, end_position in itertools.pairwise(path):
        begin, end = complex(*[int(a) for a in begin_position.split(",")]), complex(*[int(a) for a in end_position.split(",")])
        direction = (end - begin) / abs(end - begin)
        line_set = set()
        line_set.add(begin)
        while begin != end:
            begin += direction
            line_set.add(begin)
        rocks |= line_set

bottom, min_x, max_x = max(rocks, key=attrgetter("imag")).imag, int(min(rocks, key=attrgetter("real")).real), int(max(rocks, key=attrgetter("real")).real)
for part in (1, 2):
    Q, n_units, rested = deque([START]), 0, set()
    if part == 2:
        rocks |= {complex(x, bottom + 2) for x in range(min_x - 111, max_x + 151)}
    while Q:
        position = Q.popleft()
        if position + 1j not in rested and position + 1j not in rocks:
            position += 1j
        elif position + -1 + 1j not in rested and position + -1 + 1j not in rocks:
            position += -1 + 1j
        elif position + 1 + 1j not in rested and position + 1 + 1j not in rocks:
            position += 1 + 1j
        else:
            rested.add(position)
        if part == 1 and position.imag > bottom:
            break
        if position in rested and position == START:
            n_units += 1
            break
        if position in rested:
            Q.append(START)
            n_units += 1
            rested.add(position)
        else:
            Q.append(position)
    print(f"Answer: {n_units}")
