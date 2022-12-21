from operator import add,sub,floordiv,mul,eq
from functools import lru_cache

math_operations = dict(zip('+-/*=',(add,sub,floordiv,mul,eq)))
registry = {}
with open("input.txt")  as f:
    for line in f:
        line = line.strip().split()
        match line:
            case [name,number]:
                name= name.rstrip(":")
                number= int(number)
                registry[name] = number
            case [name,arg1,op,arg2]:
                name= name.rstrip(":")
                registry[name] = (math_operations[op],arg1,arg2)

@lru_cache
def yell(name: str) -> int:
    yell_value = registry[name]
    # base case
    if isinstance(yell_value,int):
        return yell_value
    else:
        # We know its an op
        op,arg1,arg2 = yell_value
        return op(yell(arg1),yell(arg2))

print(f"Part 1: {yell('root')}")

@lru_cache
def yell2(name: str, humn_value: int) -> int:
    yell_value = registry[name]
    # base cases
    if name == "humn":
        return humn_value
    if isinstance(yell_value,int):
        return yell_value
    else:
        # We know its an op
        op,arg1,arg2 = yell_value
        return op(yell2(arg1,humn_value),yell2(arg2,humn_value))

lo = 0
hi = 1e9
while lo < hi:
    mid = (lo+hi)//2
    n1 = yell2(registry['root'][1],mid)
    n2 = yell2(registry['root'][2],mid)
    score = n1 - n2
    if score < 0:
        lo = mid
    elif score == 0:
        print(f"Part 2: {mid}")
        break
    else:
        hi = mid
