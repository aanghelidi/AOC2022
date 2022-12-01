with open("input.txt") as f:
    data = f.read()

cals = [sum(int(c) for c in cal) for cal in [s.split() for s in data.split("\n\n")]]
print(f"Part 1: {max(cals)}")
cals.sort(reverse=True)
print(f"Part 2: {sum(cals[0:3])}")
