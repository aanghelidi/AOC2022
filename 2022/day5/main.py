import re
from collections import deque

with open("input.txt") as f:
    stacks, procedures = f.read().split("\n\n")

r = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
stacks = stacks.splitlines()


def parse_stacks(stacks: str) -> dict[int, deque]:
    n = len(stacks)
    m = len(stacks[0])
    j = 0
    ds = {}
    while j != m:
        elements = []
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                s_id = stacks[i][j]
                continue
            if stacks[i][j] != " ":
                elements.append(stacks[i][j])
        if s_id != " ":
            ds[int(s_id)] = deque(elements)
        j += 1
    return ds


ds = parse_stacks(stacks)


def move(n_el: int, from_s: Stack, to_s: Stack) -> None:
    i = 0
    Q = deque()
    while i != n_el:
        # part 1
        # el = from_s.pop()
        # to_s.append(el)
        el = from_s.pop()
        Q.append(el)
        i += 1
    # part 2
    while Q:
        el = Q.pop()
        to_s.append(el)


for p in procedures.splitlines():
    m = r.search(p)
    a, b, c = [int(m) for m in m.groups()]
    move(a, ds[b], ds[c])

ans = ""
for k in ds:
    ans += ds[k][-1]
print(ans)
