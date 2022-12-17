Directory = dict[str, object]


def main() -> None:
    root: Directory = {"parent": ""}
    current_node = root

    with open("07/input.txt", "r", encoding="utf-8") as f:
        commands = [command.strip().split(" ") for command in f.readlines()]

    for command in commands:
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "/":
                    current_node = root
                elif command[2] == "..":
                    current_node = current_node["parent"]
                else:
                    current_node.update({command[2]: {"parent": current_node}})
                    current_node = current_node[command[2]]
            continue
        if command[0] != "dir":
            current_node.update({command[1]: int(command[0])})

    node = root

    get_node_size(root)

    sum = sum_sizes(root, 100000)
    print(f"Part One: {sum}")

    FS_SIZE = 70000000
    SPACE_NEEDED_FOR_UPDATE = 30000000
    available_space = FS_SIZE - root["size"]
    space_to_clean = SPACE_NEEDED_FOR_UPDATE - available_space

    size = find_space_to_clean(root, space_to_clean)
    print(f"Part Two: {size}")


def find_space_to_clean(node: Directory, needed_space: int) -> int:
    space: int = node["size"]
    if space < needed_space:
        return space

    for key, value in node.items():
        if key == "parent":
            continue

        if isinstance(value, dict):
            s = find_space_to_clean(value, needed_space)
            if s < space and s >= needed_space:
                space = s
    return space


def sum_sizes(node: Directory, max_size: int) -> int:
    sum = 0
    for key, value in node.items():
        if key == "parent":
            continue

        if isinstance(value, dict):
            sum += sum_sizes(value, max_size)

    if node["size"] <= max_size:
        sum += node["size"]
    return sum


def get_node_size(node: Directory) -> int:
    size = 0

    for key, value in node.items():
        if key == "parent":
            continue

        if isinstance(value, int):
            size += value
        else:
            size += get_node_size(value)

    node["size"] = size
    return size


if __name__ == "__main__":
    main()
