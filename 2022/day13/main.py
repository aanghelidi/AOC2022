import ast

with open("sample.txt") as f:
    pairs = [p.splitlines() for p in f.read().strip().split("\n\n")]


def compare_order(e1: int | list, e2: int | list) -> int:
    if isinstance(e1, int) and isinstance(e2, int):
        if e1 < e2:
            return -1
        else:
            return 0 if e1 == e2 else 1
    if isinstance(e1, list) and isinstance(e2, list):
        min_side = 0
        while min_side < len(e1) and min_side < len(e2):
            c = compare_order(e1[min_side], e2[min_side])
            if c in (-1, 1):
                return c
            min_side += 1
        if min_side == len(e1) and min_side < len(e2):
            return -1
        else:
            return 1 if min_side == len(e2) and min_side < len(e1) else 0
    if isinstance(e1, int) and isinstance(e2, list):
        return compare_order([e1], e2)
    else:
        return compare_order(e1, [e2])


ans = 0
for i, pair in enumerate(pairs, start=1):
    left, right = ast.literal_eval(pair[0]), ast.literal_eval(pair[1])
    ans += (compare_order(left, right) == -1) * i

print(f"Part 1: {ans}")
