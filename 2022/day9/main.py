from dataclasses import dataclass, field
from typing import Self
from rich import print

#code does not follow the rules described in the problem statement for updating the position of the tail. 
#Do not handle the case where the head is two steps directly up, down, left, or right from the tail.

DIRECTIONS = {
    "L": complex(-1, 0),
    "DUL": complex(-1, 1),
    "DDL": complex(-1, -1),
    "R": complex(1, 0),
    "DUR": complex(1, 1),
    "DDR": complex(1, -1),
    "D": complex(0, -1),
    "U": complex(0, 1),
}

DIAG_DIST = {
    complex(1, 2): "DUR",
    complex(-2, 1): "DUL",
    complex(-2, -1): "DDL",
    complex(2, -1): "DDR",
}


@dataclass
class Knot:
    position: complex
    name: str
    visited: set[complex] = field(init=False)

    def __post_init__(self) -> None:
        self.visited = {self.position}

    def move(self, d: str) -> None:
        self.position += DIRECTIONS[d]
        self.visited.add(self.position)

    def norm(self, other: Self) -> float:
        return abs(self.position - other.position)


s = complex(0, 0)
head, tail = Knot(position=s, name="head"), Knot(position=s, name="tail")
with open("sample.txt") as f:
    for i, line in enumerate(f):
        instruction = line.strip().split()
        match instruction:
            case ["R", step]:
                step = int(step)
                for i in range(step):
                    if (dist := head.position - tail.position) in DIAG_DIST:
                        #  tail += (head - tail) / abs(head - tail)
                        tail.move(DIAG_DIST[dist])
                    head.move("R")
                    if head.norm(tail) > 1:
                        if (
                            head.position.real == tail.position.real
                            or head.position.imag == tail.position.imag
                        ):
                            # head - tail
                            tail.move("R")
            case ["L", step]:
                step = int(step)
                for i in range(step):
                    if (dist := head.position - tail.position) in DIAG_DIST:
                        tail.move(DIAG_DIST[dist])
                    head.move("L")
                    if head.norm(tail) > 1:
                        if (
                            head.position.real == tail.position.real
                            or head.position.imag == tail.position.imag
                        ):
                            tail.move("L")
            case ["U", step]:
                step = int(step)
                for i in range(step):
                    if (dist := head.position - tail.position) in DIAG_DIST:
                        tail.move(DIAG_DIST[dist])
                    head.move("U")
                    if head.norm(tail) > 1:
                        if (
                            head.position.real == tail.position.real
                            or head.position.imag == tail.position.imag
                        ):
                            tail.move("U")
            case ["D", step]:
                step = int(step)
                for i in range(step):
                    if (dist := head.position - tail.position) in DIAG_DIST:
                        tail.move(DIAG_DIST[dist])
                    head.move("D")
                    if head.norm(tail) > 1:
                        if (
                            head.position.real == tail.position.real
                            or head.position.imag == tail.position.imag
                        ):
                            tail.move("D")

print(f"Part 1: {len(tail.visited)}")

