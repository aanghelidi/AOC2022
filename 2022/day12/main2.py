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

def n1(i, j, part=1):
    global grid
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni = i + dr
        nj = j + dc
        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] <= grid[i][j] + 1:
            yield ni, nj

def Djikstra(start,target,neighbours):
    explored = set()
    # cost, pos here cost is only 1 for each move
    pq = [(0, start)]
    while pq:
        steps, (i,j) = heapq.heappop(pq)
        if (i,j) in explored:
            continue
        explored.add((i,j))
        if target((i,j)):
            return steps
        for ni, nj in neighbours(i,j):
            heapq.heappush(pq, (steps+1,(ni,nj)))

start = key_positions['S']
target = lambda x: x == key_positions['E']
print(f"Part 1: {Djikstra(start=start,target=target,neighbours=n1)}")

def n2(i, j):
    global grid
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni = i + dr
        nj = j + dc
        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] >= grid[i][j] - 1:
            yield ni, nj

start = key_positions['E']
target = lambda x: grid[x[0]][x[1]] == 0 
print(f"Part 2: {Djikstra(start=start,target=target,neighbours=n2)}")
