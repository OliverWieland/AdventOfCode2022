Section = list[int]
Section_Pair = list[Section]


def main() -> None:
    containing_sections: list[Section_Pair] = []
    overlapping_sections: list[Section_Pair] = []

    with open("04/input.txt", "r", encoding="utf-8") as f:
        while True:
            data = f.readline().rstrip()

            if not data:
                break

            section_ranges = data.split(",")
            section1 = [int(s) for s in section_ranges[0].split("-")]
            section2 = [int(s) for s in section_ranges[1].split("-")]
            sections = [section1, section2]

            if is_containing(sections):
                containing_sections.append(sections)
            if is_overlapping(sections):
                overlapping_sections.append(sections)

    # for i in containing_sections:
    #     print(i)
    #     print(draw(i[0]))
    #     print(draw(i[1]))
    #     print()
    print(f"Part One: {len(containing_sections)}")

    # for i in overlapping_sections:
    #     print(i)
    #     print(draw(i[0]))
    #     print(draw(i[1]))
    #     print()
    print(f"Part Two: {len(overlapping_sections)}")


def draw(section: Section) -> str:
    section_string = " " * section[0] + "." * (section[1] - section[0] + 1)

    return section_string


def is_overlapping(sections: Section_Pair) -> bool:
    if sections[0][1] < sections[1][0]:
        return False
    if sections[0][0] > sections[1][1]:
        return False
    return True


def is_containing(sections: Section_Pair) -> bool:
    if (sections[0][0] <= sections[1][0]) and (sections[0][1] >= sections[1][1]):
        return True
    if (sections[0][0] >= sections[1][0]) and (sections[0][1] <= sections[1][1]):
        return True
    return False


if __name__ == "__main__":
    main()
