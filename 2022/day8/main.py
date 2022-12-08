import math
NEIGHBOURS_DELTAS = [complex(-1, 0), complex(1, 0), complex(0, -1), complex(0, 1)]
M = {}
with open("input.txt") as f:
    for y, line in enumerate(f):
        line = line.strip()
        for x, value in enumerate(line):
            M[complex(x, y)] = int(value)

max_x, max_y = max(x.real for x in M.keys()), max(x.imag for x in M.keys())
num_in, num_out, edges = 0, 2 * (max_x + max_y), {0, max_x, max_y}


def check_is_visible(pos: complex) -> tuple[bool, int]:
    is_visible = True
    n_dir_blocked = 0
    viewing_distances = []
    for n_del in NEIGHBOURS_DELTAS:
        trees_seen = 0
        n_pos = pos + n_del
        while n_pos in M:
            trees_seen += 1
            if M[n_pos] >= M[pos]:
                n_dir_blocked += 1
                break
            n_pos += n_del
        viewing_distances.append(trees_seen)
    if n_dir_blocked == 4:
        is_visible = False
    return is_visible, math.prod(viewing_distances)


scenic_scores = []
for pos in M:
    if pos.real in edges or pos.imag in edges:
        continue
    n, sc = check_is_visible(pos)
    num_in += n
    scenic_scores.append(sc)

print(f"Part 1: {num_in+num_out}")
print(f"Part 2: {max(scenic_scores)}")
