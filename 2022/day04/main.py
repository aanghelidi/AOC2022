import re

ans, ans2 = 0, 0
r = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")


def is_contains(a, b, c, d):
    if a >= c and b <= d or c >= a and d <= b:
        return True
    else:
        return False


def is_contains2(a, b, c, d):
    if c >= a and c <= b:
        return True
    elif a >= c and a <= d:
        return True
    elif b == c or b == d:
        return True
    else:
        return False


with open("input.txt") as f:
    for line in f:
        line = line.strip()
        m = r.search(line)
        a, b, c, d = [int(m) for m in m.groups()]
        ans += is_contains(a, b, c, d)
        ans2 += is_contains2(a, b, c, d)

print(f"Part 1: {ans}")
print(f"Part 2: {ans2}")
