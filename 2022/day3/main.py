import string
from itertools import islice
from functools import reduce

ans, ans2 = 0, 0
p = dict(zip(string.ascii_letters, range(1, 53)))

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        n = len(line)
        n2 = n // 2
        first, second = set(islice(line, n2)), set(islice(line, n2, n))
        item_type = first & second
        priority = p[item_type.pop()]
        ans += priority

print(f"Part 1: {ans}")

with open("input.txt") as f:
    s_group = []
    for i, line in enumerate(f, start=1):
        line = line.strip()
        s_group.append(set(line))
        if i % 3 == 0:
            item_type = reduce(set.intersection, s_group)
            priority = p[item_type.pop()]
            ans2 += priority
            s_group.clear()

print(f"Part 2: {ans2}")
