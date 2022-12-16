from rich import print
import re
from collections import defaultdict, deque
import bisect
import statistics

TOTAL_MINUTES = 30
rate_pattern = re.compile(r"rate=(\d+);")
valve_pattern = re.compile(r"Valve ([A-Z]{2})")
next_valves_pattern = re.compile(r"valves?\s{1}(.*)$")
graph = defaultdict(list)
valves = {}
with open("sample.txt")  as f:
    for line in f:
        valve = valve_pattern.search(line).group(1)
        rate = int(rate_pattern.search(line).group(1))
        next_valves = next_valves_pattern.search(line).group(1).split(", ")
        valves[valve] = rate
        for n_valve in next_valves:
            graph[valve].append(n_valve)

start = 'AA'
Q = deque([start]) 
ms = 0
opened = set()
visited = set()
pressures = []
while ms!= 30:
    ms += 1
    if Q:
        valve = Q.pop()
    print(ms,valve)
    rt = TOTAL_MINUTES - ms
    if len(opened) != 0:
        print(f"{sum(valves[vo] for vo in opened)},{rt=}")
        bisect.insort(pressures,sum(valves[vo]*rt for vo in opened))
    if valve not in opened:
        if valves[valve] > statistics.mean(valves.values()):
            opened.add(valve)
            continue
    nvl = deque(graph[valve])
    if len(nvl) == 1:
        nv = nvl.popleft()
        Q.append(nv)
        continue
    while nvl:
        nv = nvl.popleft()
        if nv not in visited:
            print(nv)
            visited.add(nv)
            Q.append(nv)
            break
