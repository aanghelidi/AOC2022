from collections import defaultdict, deque
import re

ans = 0
d = defaultdict(int)
current_dir = "/"
FS = defaultdict(list)
numbers = lambda x: [int(m) for m in re.findall(r"\d+", x)]

with open("sample.txt") as f:
    term_out = [cmd.strip().split() for cmd in f.read().strip().split("$") if cmd != ""]

for cmd in term_out:
    cached_dir = "/"
    match cmd:
        case ["cd", dest]:
            if dest == "..":
                current_dir = cached_dir
            else:
                FS[current_dir].append(dest)
                current_dir = dest
        case ["ls", *rest]:
            d[current_dir] = sum(numbers("".join(rest)))

FS["/"].remove("/")


def get_dir_size(k: str, d: dict, fs: dict) -> int:
    Q = deque([k])
    size = 0
    visited = set()
    while Q:
        cd = Q.pop()
        size += d[cd]
        if cd in fs:
            for sk in fs[cd]:
                if sk in visited:
                    continue
                Q.append(sk)
    return size


total_size = 0
for k in d:
    if (size := get_dir_size(k, d, FS)) <= 100000:
        total_size += size
print(total_size)
