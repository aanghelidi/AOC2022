from collections import defaultdict, deque
import re

ans, d = 0, defaultdict(int)
numbers = lambda x: [int(m) for m in re.findall(r"\d+", x)]

with open("input.txt") as f:
    term_out = [cmd.strip().split() for cmd in f.read().strip().split("$") if cmd != ""]

stack = deque()
for cmd in term_out:
    match cmd:
        case ["cd", ".."]:
            stack.pop()
            previous_dir = stack[-1]
        case ["cd", dest]:
            stack.append(dest)
        case ["ls", *rest]:
            if cmd == cached_cmd:
                continue
            s_sizes = sum(numbers("".join(rest)))
            p = ""
            for node in stack:
                p += node
                d[p] += s_sizes
    cached_cmd = cmd

print(f"Part 1: {sum(v for v in d.values() if v <= 100000)}")
print(f"Part 2: {min(v for v in d.values() if 70000000 - d['/'] +v > 30000000)}")
