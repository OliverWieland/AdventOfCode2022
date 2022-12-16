from enum import Enum, auto
import re


class CRANE_TYPE(Enum):
    CrateMover_9000 = auto()
    CrateMover_9001 = auto()


Stack = list[str]


def main() -> None:
    with open("05/input.txt", "r", encoding="utf-8") as f:
        stacks = get_stacks(f)

        while True:
            operation = f.readline().rstrip()
            if not operation:
                break

            stacks = process_crane_operation(
                stacks, operation, CRANE_TYPE.CrateMover_9000
            )
    s = ""
    for stack in stacks:
        s += stack[0]
    print(f"Part One: {s}")

    with open("05/input.txt", "r", encoding="utf-8") as f:
        stacks = get_stacks(f)

        while True:
            operation = f.readline().rstrip()
            if not operation:
                break

            stacks = process_crane_operation(
                stacks, operation, CRANE_TYPE.CrateMover_9001
            )
    s = ""
    for stack in stacks:
        s += stack[0]
    print(f"Part Two: {s}")


def process_crane_operation(
    stacks: list[Stack], operation: str, crane_type: CRANE_TYPE
) -> list[Stack]:

    match = re.match(r"move (\d+) from (\d+) to (\d+)", operation)

    if not match:
        return stacks

    command = [int(s) for s in match.group(1, 2, 3)]

    if crane_type == CRANE_TYPE.CrateMover_9001:
        crates = stacks[command[1] - 1][: command[0]]
        crates.extend(stacks[command[2] - 1])
        stacks[command[2] - 1] = crates
        for i in range(command[0]):
            stacks[command[1] - 1].pop(0)
    elif crane_type == CRANE_TYPE.CrateMover_9000:
        for i in range(command[0]):
            crate = stacks[command[1] - 1].pop(0)
            stacks[command[2] - 1].insert(0, crate)

    return stacks


def get_stacks(f) -> list[Stack]:
    stacks: list[Stack] = [[], [], [], [], [], [], [], [], []]

    while True:
        data: str = f.readline().rstrip()

        if data.startswith(" "):
            f.readline()
            return stacks

        crates: str = data[1::4]
        for i, stack in enumerate(stacks):
            if crates[i] != " ":
                stack.append(crates[i])


if __name__ == "__main__":
    main()
