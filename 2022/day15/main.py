import re
import math

numbers = lambda x: [int(m) for m in re.findall(r'\d+', x)]
manhattan = lambda x,y : abs(x.real-y.real) + abs(x.imag-y.imag)
ans = 0
grid = {} 
distances = {}
with open("input.txt")  as f:
    for line in f:
        x_s,y_s,x_b,y_b = numbers(line)
        sensor, beacon = complex(x_s,y_s), complex(x_b,y_b)
        grid[sensor] = complex(beacon) 
        distances[sensor] = int(manhattan(sensor,beacon))

def check_dist(pos: complex,distances: dict) -> bool: 
    for s_pos, distance in distances.items():
        md = manhattan(pos,s_pos)
        if md <= distance:
            return True
    return False

sy = set()
beacons = set(grid.values())
y = int(2e6)
for x in range(-int(1e7),int(1e7)):
    if check_dist(complex(x,y),distances) and complex(x,y) not in beacons:
        ans += 1
print(ans)


