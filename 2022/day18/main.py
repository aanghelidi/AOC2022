from typing import Generator
from operator import itemgetter
from collections import deque

cubes = set()
with open("input.txt") as f:
    for line in f:
        x, y, z = [int(n) for n in line.split(",")]
        cubes.add((x, y, z))


def adj_cubes_faces(
    x: int, y: int, z: int
) -> Generator[tuple[int, int, int], None, None]:
    yield x + 1, y, z
    yield x - 1, y, z
    yield x, y + 1, z
    yield x, y - 1, z
    yield x, y, z + 1
    yield x, y, z - 1


def surface_area(coords: set[tuple[int, int, int]]) -> int:
    res = 0
    for x, y, z in coords:
        for ax, ay, az in adj_cubes_faces(x, y, z):
            if (ax, ay, az) not in coords:
                res += 1
    return res


print(f"Part 1: {surface_area(cubes)}")

min_x, min_y, min_z = [min(cubes, key=itemgetter(i))[i] for i in range(3)]
max_x, max_y, max_z = [max(cubes, key=itemgetter(i))[i] for i in range(3)]
all_cubes = {
    (x, y, z)
    for x in range(min_x - 1, max_x + 2)
    for y in range(min_y - 1, max_y + 2)
    for z in range(min_z - 1, max_z + 2)
}
remaining_cubes = all_cubes - cubes
Q = deque([list(remaining_cubes)[0]])
while Q:
    cube = Q.popleft()
    if cube not in remaining_cubes:
        continue
    remaining_cubes.remove(cube)
    for acube in adj_cubes_faces(*cube):
        Q.append(acube)

print(f"Part 2: {surface_area(cubes)-surface_area(remaining_cubes)}")
