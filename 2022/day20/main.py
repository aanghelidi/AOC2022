from collections import deque

with open("input.txt") as f:
    data = [int(line) for line in f.read().splitlines()]

N = len(data)
numbers = deque(data)
indexes = deque(i for i in range(N))
for i, num in enumerate(data):
    current_index = indexes.index(i)
    del numbers[current_index]
    del indexes[current_index]
    numbers.rotate(-num)
    indexes.rotate(-num)
    numbers.insert(current_index, num)
    indexes.insert(current_index, i)

print(f"Part 1: {sum(numbers[(numbers.index(0)+i)%N] for i in range(1000,3001,1000))}")


# Part 2
DECRYPTION_KEY = 811589153
data = [DECRYPTION_KEY * d for d in data]
numbers = deque(data)
indexes = deque(i for i in range(N))
c = 0
while c != 10:
    for i, num in enumerate(data):
        current_index = indexes.index(i)
        del numbers[current_index]
        del indexes[current_index]
        numbers.rotate(-num)
        indexes.rotate(-num)
        numbers.insert(current_index, num)
        indexes.insert(current_index, i)
    c += 1

print(f"Part 2: {sum(numbers[(numbers.index(0)+i)%N] for i in range(1000,3001,1000))}")
