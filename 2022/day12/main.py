import heapq

with open("input.txt") as f:
    data = f.read().strip().splitlines()

H, W, grid, key_positions = len(data), len(data[0]), [], {}
for i in range(H):
    row = [0] * W
    for j in range(W):
        if (value := data[i][j]) in ["S", "E"]:
            row[j] = 0 if value == "S" else 25
            key_positions[value] = (i, j)
        else:
            row[j] = ord(value) - ord("a")
    grid.append(row)


def n4(i, j):
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni = i + dr
        nj = j + dc
        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] <= grid[i][j] + 1:
            yield ni, nj


visited, start = set(), key_positions["S"]
pq = [(0, start)]
while pq:
    steps, (i, j) = heapq.heappop(pq)
    if (i, j) in visited:
        continue
    visited.add((i, j))
    if (i, j) == key_positions["E"]:
        print(f"Part 1: {steps}")
        break
    for ni, nj in n4(i, j):
        heapq.heappush(pq, (steps + 1, (ni, nj)))

all_a_pos = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 0]

# Brute force
all_steps = []
for a_start in all_a_pos:
    visited, start = set(), a_start
    pq = [(0, start)]
    while pq:
        steps, (i, j) = heapq.heappop(pq)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if (i, j) == key_positions["E"]:
            all_steps.append(steps)
            break
        for ni, nj in n4(i, j):
            heapq.heappush(pq, (steps + 1, (ni, nj)))

print(f"Part 2: {min(all_steps)}")
