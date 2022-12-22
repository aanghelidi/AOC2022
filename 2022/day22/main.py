import re
from operator import attrgetter
from collections import UserDict
from typing import Self

NEIGHBOURS_DELTAS = dict(zip('LRUD',(complex(-1,0), complex(1,0), complex(0,-1),complex(0,1))))
NEIGHBOURS_DELTAS_R = dict(zip((complex(-1,0),complex(1,0),complex(0,-1),complex(0,1)),'LRUD'))
FACINGS = dict(zip('RDLU',range(4)))
numbers = re.compile(r'(\d+)')

class MapBoard(UserDict):
    @classmethod
    def from_list_of_str(cls, m: list[str]) -> Self:
        g = cls()
        for y,row in enumerate(m,start=1):
            for x,el in enumerate(row,start=1):
                g[complex(x,y)] = el 
        return g
    @property
    def max_width(self) -> float:
        return max(self.data,key=attrgetter('real')).real
    @property
    def max_height(self) -> float:
        return max(self.data,key=attrgetter('imag')).imag
    @property
    def min_width(self) -> float:
        return min(self.data,key=attrgetter('real')).real
    @property
    def min_height(self) -> float:
        return min(self.data,key=attrgetter('imag')).imag
    @property
    def leftmost_open(self) -> complex:
        min_height = self.min_height
        for i in range(1,int(self.max_width)+1):
            if not self.data[complex(i,min_height)].isspace():
                return complex(i,min_height)

    def minmaxlen_row(self, y: int) -> tuple[int,int,int]:
        min_line = 0
        for x in range(1,int(self.max_width)):
            if not self.data.get(complex(x,y),"x").isspace():
                min_line = x 
                break
        max_line = min_line
        for x in range(min_line,int(self.max_width)):
            if complex(x,y) in self.data:
                max_line+=1
        return min_line,max_line-1,max_line-min_line


def parse_path(p: str) -> list[str]:
    return [sb for sb in numbers.split(p) if sb]

def move(current_pos: complex, num: int, facing: str, m: MapBoard) -> complex:
    i = 0
    while i != num:
        current_pos += 1 * NEIGHBOURS_DELTAS[facing]
        i+=1
    return current_pos

def rotate(current_facing: str, instruction: str) -> str:
    # clockwise
    if instruction == "R":
        new_facing = NEIGHBOURS_DELTAS[current_facing] * complex(0,1) 
        return NEIGHBOURS_DELTAS_R[new_facing]
    # counter-clockwise
    elif instruction == "L":
        new_facing = NEIGHBOURS_DELTAS[current_facing] * complex(0,-1) 
        return NEIGHBOURS_DELTAS_R[new_facing]
    else:
        raise ValueError("Invalid instruction")

with open("sample.txt")  as f:
    data = f.read().split("\n\n")

map_of_board: MapBoard = MapBoard.from_list_of_str(data[0].splitlines())
path = parse_path(data[1])
last_facing = {} 
pos = map_of_board.leftmost_open
facing = 'R'
#for instruction in path:
#    if instruction.isdigit():
#        pos = move(pos,int(instruction),facing,map_of_board)
#    else:
#        facing = rotate(facing,instruction)
#
