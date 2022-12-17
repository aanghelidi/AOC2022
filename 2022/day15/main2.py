import re

numbers = lambda x: [int(m) for m in re.findall(r'-?\d+', x)]
manhattan = lambda x,y : abs(x[0]-y[0]) + abs(x[1]-y[1])
sensors , positive_slope_lines, negative_slope_lines = [] , [], []
with open("input.txt")  as f:
    for line in f:
        x_s,y_s,x_b,y_b = numbers(line)
        sensor, beacon = (x_s,y_s), (x_b,y_b)
        sensors.append(sensor)
        d = manhattan(sensor,beacon)
        negative_slope_lines += [x_s + y_s - d, x_s + y_s + d]
        positive_slope_lines += [x_s - y_s - d, x_s - y_s + d]

pd = nd = -1
N = len(positive_slope_lines)
for i in range(N):
    for j in range(i + 1, N):
        ps, ns = positive_slope_lines[i], positive_slope_lines[j]
        if abs(ps - ns) == 2:
            pd = min(ps, ns) + 1
        ps, ns = negative_slope_lines[i], negative_slope_lines[j]
        if abs(ps - ns) == 2:
            nd = min(ps, ns) + 1
x, y = (pd + nd) // 2, (nd - pd) // 2
print(f"Part 2: {x * 4000000 + y}")
