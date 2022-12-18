CRT_HEIGHT = 6
CRT_WIDTH = 40


class Crt:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.crt = [[" "] * width for _ in range(height)]
        self.next = 0

    def __str__(self):
        rows = ["".join(row) for row in self.crt]
        return "\n".join(row for row in rows)

    def set_pixel(self, pos: int) -> None:
        x: int = self.next % self.width
        y: int = self.next // self.width

        self.crt[y][x] = "#" if abs(x - pos) <= 1 else " "
        self.next += 1


def main() -> None:
    cycle: int = 0
    signal_strength: int = 0
    x: int = 1
    crt = Crt(width=CRT_WIDTH, height=CRT_HEIGHT)

    with open("10/input.txt", "r", encoding="utf-8") as f:
        commands = [cmd.strip().split(" ") for cmd in f.readlines()]

    for cmd in commands:
        match cmd[0]:
            case "noop":
                cycle += 1
                crt.set_pixel(x)
                signal_strength += check_signal_strength(cycle, x)
            case "addx":
                cycle += 1
                crt.set_pixel(x)
                signal_strength += check_signal_strength(cycle, x)
                cycle += 1
                crt.set_pixel(x)
                signal_strength += check_signal_strength(cycle, x)
                x += int(cmd[1])
            case _:
                raise ValueError("Invalid command")

    print(f"Part One: {signal_strength}")
    print("Part Two:")
    print(crt)


def check_signal_strength(cycle: int, x: int) -> int:
    if (cycle - 20) % 40 == 0:
        return cycle * x
    return 0


if __name__ == "__main__":
    main()
