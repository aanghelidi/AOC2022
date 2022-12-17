import re

numbers = lambda x: [int(m) for m in re.findall(r'-?\d+', x)]
manhattan = lambda x,y : abs(x[0]-y[0]) + abs(x[1]-y[1])
distances, seen = {}, set() 

with open("input.txt")  as f:
    for line in f:
        x_s,y_s,x_b,y_b = numbers(line)
        sensor, beacon = (x_s,y_s), (x_b,y_b)
        distances[sensor] = (beacon, manhattan(sensor,beacon))

find_y = 2_000_000
for sensor, (beacon, distance) in distances.items():
    x,y = sensor[0], sensor[1]
    cost_to_reach_y = abs(find_y - y)
    if cost_to_reach_y > distance:
        continue
    remaining_moves = distance - cost_to_reach_y
    no_beacon_x = set(range(x-remaining_moves,x+remaining_moves+1))
    if beacon[1] == find_y:
        no_beacon_x.remove(beacon[0])
    seen |= no_beacon_x
print(f"Part 1: {len(seen)}")
