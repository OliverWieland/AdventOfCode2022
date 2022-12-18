from operator import sub

Position = list[int]

ROPE_LENGTH_PART1 = 2
ROPE_LENGTH_PART2 = 10


def calc_rope_positions(rope_length: int) -> int:
    rope: list[Position] = [[0, 0] for _ in range(rope_length)]

    with open("09/input.txt", "r", encoding="utf-8") as f:
        commands = [cmd.strip().split(" ") for cmd in f.readlines()]

    tail_positions: set[tuple[int, int]] = set()

    for cmd in commands:
        cnt = int(cmd[1])
        match cmd[0]:
            case "L":
                for _ in range(cnt):
                    rope = move_left(rope)
                    tail_positions.add(tuple(rope[-1]))
            case "R":
                for _ in range(cnt):
                    rope = move_right(rope)
                    tail_positions.add(tuple(rope[-1]))
            case "U":
                for _ in range(cnt):
                    rope = move_up(rope)
                    tail_positions.add(tuple(rope[-1]))
            case "D":
                for _ in range(cnt):
                    rope = move_down(rope)
                    tail_positions.add(tuple(rope[-1]))
            case _:
                raise ValueError(f"Invalid command {cmd}")

    return len(tail_positions)


def move_left(rope: list[Position]) -> list[Position]:
    rope[0][0] -= 1
    for i in range(1, len(rope)):
        rope[i] = move_tail(rope[i - 1], rope[i])

    return rope


def move_right(rope: list[Position]) -> list[Position]:
    rope[0][0] += 1
    for i in range(1, len(rope)):
        rope[i] = move_tail(rope[i - 1], rope[i])

    return rope


def move_up(rope: list[Position]) -> list[Position]:
    rope[0][1] -= 1
    for i in range(1, len(rope)):
        rope[i] = move_tail(rope[i - 1], rope[i])

    return rope


def move_down(rope: list[Position]) -> list[Position]:
    rope[0][1] += 1
    for i in range(1, len(rope)):
        rope[i] = move_tail(rope[i - 1], rope[i])

    return rope


def move_tail(head: Position, tail: Position) -> Position:
    dist_vector = list(map(sub, head, tail))

    match dist_vector:
        case [0, 2]:
            tail[1] += 1
        case [1, 2] | [2, 1] | [2, 2]:
            tail[0] += 1
            tail[1] += 1
        case [2, 0]:
            tail[0] += 1
        case [2, -1]:
            tail[0] += 1
            tail[1] -= 1
        case [2, -1] | [1, -2] | [2, -2]:
            tail[0] += 1
            tail[1] -= 1
        case [0, -2]:
            tail[1] -= 1
        case [-1, -2] | [-2, -1] | [-2, -2]:
            tail[0] -= 1
            tail[1] -= 1
        case [-2, 0]:
            tail[0] -= 1
        case [-2, 1] | [-1, 2] | [-2, 2]:
            tail[0] -= 1
            tail[1] += 1
        case _:
            pass
    return tail


if __name__ == "__main__":
    print(f"Part One: {calc_rope_positions(ROPE_LENGTH_PART1)}")
    print(f"Part Two: {calc_rope_positions(ROPE_LENGTH_PART2)}")
