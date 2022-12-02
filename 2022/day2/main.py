ans, ans2 = 0, 0
wr, lr = dict(zip("ABC", "YZX")), dict(zip("ABC", "CAB"))
scores = dict(zip("rps", range(1, 4)))
vr = dict(zip("ABCXYZ", ["r", "p", "s"] * 2))


def score2(c, s):
    if s == "X":
        return scores[vr[lr[c]]] + 0
    elif s == "Y":
        return scores[vr[c]] + 3
    else:
        return scores[vr[wr[c]]] + 6


def score(c, s):
    ws = 0
    if vr[c] == vr[s]:
        ws += 3
    elif wr[c] == s:
        ws += 6
    return ws + scores[vr[s]]


with open("input.txt") as f:
    for line in f:
        parts = line.split()
        c, s = parts[0], parts[1]
        ans += score(c, s)
        ans2 += score2(c, s)

print(f"Part 1: {ans}")
print(f"Part 2: {ans2}")
