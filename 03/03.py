def main() -> None:
    priority_sum: int = 0

    with open("03/input.txt", "r", encoding="utf-8") as f:
        while True:
            data = f.readline().rstrip()
            if not data:
                break

            length = len(data)
            compartment = [data[: int(length / 2)], data[int(length / 2) :]]

            for item in compartment[0]:
                if item in compartment[1]:
                    priority_sum += get_priority(item)
                    break

    print(f"Part One: {priority_sum}")

    priority_sum = 0

    with open("03/input.txt", "r", encoding="utf-8") as f:
        while True:
            rucksacks = []
            for _ in range(3):
                rucksacks.append(f.readline().rstrip())

            if not rucksacks[0]:
                break

            length = [len(x) for x in rucksacks]
            max_rucksack = rucksacks[length.index(max(length))]

            for item in max_rucksack:
                if is_common(item, rucksacks):
                    priority_sum += get_priority(item)
                    break

    print(f"Part Two: {priority_sum}")


def is_common(item: str, rucksacks: list[str]) -> bool:
    for r in rucksacks:
        if item not in r:
            return False
    return True


def get_priority(item: str) -> int:
    code = ord(item)

    if code < 97:
        return code - 65 + 27
    return code - 97 + 1


if __name__ == "__main__":
    main()
