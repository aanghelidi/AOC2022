X, cycle, pixel_position, d, = 1, 1, 0, {1: 1}
signal_strength = lambda x: d[x] * x
crt_rows = {i: [*"." * 40] for i in range(6)}

def draw_pixel(X: int, pixel_position: int) -> None:
    if (pixel_drawn := pixel_position % 40) in (X - 1, X, X + 1):
        crt_rows[int(pixel_position / 40)][pixel_drawn] = "#"

with open("input.txt") as f:
    draw_pixel(X, pixel_position)
    for line in f:
        line = line.strip().split()
        match line:
            case ["noop"]:
                cycle += 1
                pixel_position += 1
                draw_pixel(X, pixel_position)
                d[cycle] = X
            case ["addx", strength]:
                inner_cycle = 1
                while inner_cycle != 2:
                    inner_cycle += 1
                    cycle += 1
                    pixel_position += 1
                    draw_pixel(X, pixel_position)
                    d[cycle] = X
                X += int(strength)
                cycle += 1
                pixel_position += 1
                draw_pixel(X, pixel_position)
                d[cycle] = X

print(f"Part 1: {sum(signal_strength(c) for c in range(20,221,40))}")
print("Part 2:")
for k, v in crt_rows.items():
    print("".join(v))
