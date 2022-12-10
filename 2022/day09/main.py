from dataclasses import dataclass, field
from typing import Iterator, Self
from itertools import pairwise

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


@dataclass
class Knot:
    position: complex
    visited: set[complex] = field(init=False)

    def __post_init__(self) -> None:
        self.visited = {self.position}

    def move(self, d: str) -> None:
        self.position += DIRECTIONS[d]
        self.visited.add(self.position)

    def get_n8_and_self(self) -> Iterator[complex]:
        yield self.position
        for nc in DIRECTIONS.values():
            yield self.position + nc

    def place_behind(self, d: str, other: Self) -> None:
        # Check if the head and tail are in the same row or column
        if (
            abs(self.position.real - other.position.real) <= 1
            and abs(self.position.imag - other.position.imag) <= 1
        ):
            self.move(d)
        else:
            diff = other.position - self.position
            closest_direction = min(DIRECTIONS.values(), key=lambda x: abs(x - diff))
            self.position += closest_direction
            self.visited.add(self.position)


with open("input.txt") as f:
    lines = f.read().splitlines()

s = complex(0, 0)
for part, length in zip((1, 2), (2, 10)):
    rope = [Knot(position=s) for _ in range(length)]
    for line in lines:
        instruction = line.strip().split()
        match instruction:
            case [d, step]:
                step = int(step)
                for _ in range(step):
                    rope[0].move(d)
                    for h, t in pairwise(rope):
                        if h.position not in t.get_n8_and_self():
                            t.place_behind(d, h)
            case _:
                raise ValueError("Invalid instruction")
    print(f"Part {part}: {len(rope[-1].visited)}")
