from typing import Iterator
import re
from rich import print
import heapq
from dataclasses import dataclass,field

# ord(value) - ord('a')
#N8 = {
#    "L": complex(-1, 0),
#    "DUL": complex(-1, 1),
#    "DDL": complex(-1, -1),
#    "R": complex(1, 0),
#    "DUR": complex(1, 1),
#    "DDR": complex(1, -1),
#    "D": complex(0, -1),
#    "U": complex(0, 1),
#}
N4 = {
    "L": complex(-1, 0),
    "R": complex(1, 0),
    "D": complex(0, 1),
    "U": complex(0, -1),
}


def n4(pos: complex) -> Iterator[complex]:
    global grid
    for np in N4.values():
        np = pos + np
        if np in grid:
            yield np

@dataclass(order=True)
class Position:
    elevation: int
    position: complex=field(compare=False)

    def __post_init__(self) -> None:
        self.elevation *= -1

grid = {}
key_positions = {}
with open("sample.txt") as f:
    for y, line in enumerate(f):
        line = line.strip()
        for x, value in enumerate(line):
            if value == 'S' or value == 'E':
                key_positions[value] = complex(x,y)
                grid[complex(x, y)] = Position(ord(value),complex(x,y)) 
            else:
                grid[complex(x, y)] = Position(ord(value)-ord('a'),complex(x,y))

ans = 0
visited = set()
pq = []
heapq.heapify(pq)
heapq.heappush(pq,grid[key_positions['S']])
visited.add(key_positions['S'])

while pq:
    current_pos : Position = heapq.heappop(pq)
    tmp_np = []
    for np in n4(current_pos.position):
        if np == key_positions['E']:
            print(ans)
            raise SystemExit()
        if current_pos.position == key_positions['S']:
            current_pos.elevation = ord('a') - ord('a')
        if np not in visited:
            if grid[np].elevation >= current_pos.elevation - 1:
                tmp_np.append(grid[np])
                visited.add(np)
    breakpoint()
    for np in tmp_np:
        if np == (current_pos.position + N4["R"]) or np == (current_pos.position + N4["D"]):
            heapq.heappush(pq,np)
        else:
            heapq.heappush(pq,np)
    ans += 1



print(ans)
