def compute(data_stream: str, n_char: int) -> int:
    for i, _ in enumerate(data_stream, start=1):
        if i < n_char:
            continue
        if len(set(data_stream[i - n_char : i])) == n_char:
            return i

with open("input.txt") as f:
    data_stream = f.read()

for i, n_char in enumerate((4, 14), start=1):
    print(f"Part {i}: {compute(data_stream,n_char)}")
