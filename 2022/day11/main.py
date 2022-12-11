from dataclasses import dataclass
import re
from typing import Literal, Self
from rich import print
from collections import deque, OrderedDict, defaultdict
import math

numbers = lambda x: [int(m) for m in re.findall(r"\d+", x)]


@dataclass
class Item:
    worry_level: int

    def stay_managable(self, lcm: int) -> Self:
        self.worry_level = self.worry_level % lcm
        return self


@dataclass
class Monkey:
    m_id: int
    items: deque[Item]
    op: str
    divisible_by: int
    m_true: int
    m_false: int

    def apply_op(self, item: Item) -> Item:
        parts = self.op.split()
        match parts:
            case [x, "+", y]:
                if y.isdigit():
                    item.worry_level += int(y)
                    return item
                else:
                    item.worry_level += item.worry_level
                    return item
            case [x, "*", y]:
                if y.isdigit():
                    item.worry_level *= int(y)
                    return item
                else:
                    item.worry_level *= item.worry_level
                    return item
            case _:
                raise ValueError("Unknown op")

    def get_bored(self, item: Item) -> int:
        item.worry_level = item.worry_level // 3
        return item

    def apply_test(self, item: Item) -> bool:
        return item.worry_level % self.divisible_by == 0

    def throw(self, item: Item, other: Self) -> None:
        other.items.append(item)


def parse_monkeys(monkeys: list[list[str]]) -> OrderedDict[int, Monkey]:
    monkey_registry = OrderedDict()
    for monkey in monkeys:
        for notes in monkey:
            notes = notes.strip()
            if notes.startswith("Monkey"):
                m_id = numbers(notes)[0]
            elif notes.startswith("Starting"):
                items = deque(Item(wl) for wl in numbers(notes))
            elif notes.startswith("Operation"):
                _, _, op = notes.partition(" = ")
            elif notes.startswith("Test"):
                divisible_by = numbers(notes)[0]
            elif notes.startswith("If true"):
                m_true = numbers(notes)[0]
            elif notes.startswith("If false"):
                m_false = numbers(notes)[0]
            else:
                pass
        m = Monkey(
            m_id=m_id,
            items=items,
            op=op,
            divisible_by=divisible_by,
            m_true=m_true,
            m_false=m_false,
        )
        monkey_registry[m_id] = m
    return monkey_registry


with open("input.txt") as f:
    monkeys = [m.splitlines() for m in f.read().split("\n\n")]

monkey_registry = parse_monkeys(monkeys)
n_round = 0
monkey_business = defaultdict(int)
lcm = math.lcm(*[m.divisible_by for m in monkey_registry.values()])
while n_round < 10000:
    for monkey in monkey_registry.values():
        while monkey.items:
            item = monkey.items.popleft()
            item = monkey.apply_op(item)
            # part 1
            # item = monkey.get_bored(item)
            # part 2
            item = item.stay_managable(lcm)
            if monkey.apply_test(item):
                monkey.throw(item, monkey_registry[monkey.m_true])
            else:
                monkey.throw(item, monkey_registry[monkey.m_false])
            monkey_business[monkey.m_id] += 1
    n_round += 1

print(f"Answer: {math.prod(sorted(monkey_business.values(),reverse=True)[0:2])}")
