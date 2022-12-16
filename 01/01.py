from io import TextIOWrapper


def get_next_elf(f: TextIOWrapper) -> int:
    cnt = 0

    while True:
        data = f.readline().rstrip()

        if not data:
            return cnt
        cnt += int(data)


def main():
    elf: list[str] = []
    with open("01/input.txt", "r", encoding="utf-8") as f:
        while True:
            next_elf = get_next_elf(f)
            if not next_elf:
                break
            elf.append(next_elf)

    elf.sort()

    print(elf)

    print(f"max calories: {elf[-1]}")
    print(f"sum of top three: {sum(elf[-3:])}")


if __name__ == "__main__":
    main()
