def main() -> None:
    with open("06/input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    sop = get_marker(data, 4)
    som = get_marker(data, 14)

    print(f"Part One: {sop}")
    print(f"Part Two: {som}")


def get_marker(data: str, cnt_distinct: int) -> int:
    marker: list[str] = []
    cnt = 1

    for char in data:
        marker.append(char)
        if len(set(marker)) == cnt_distinct:
            return cnt
        if len(marker) >= cnt_distinct:
            marker.pop(0)
        cnt += 1
    return 0


if __name__ == "__main__":
    main()
