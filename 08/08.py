Wood = list[str]


def main() -> None:
    with open("08/input.txt", "r", encoding="utf-8") as f:
        trees: Wood = [line.strip() for line in f.readlines()]

    height = len(trees)
    width = len(trees[0])

    visible_trees = [[False] * width for _ in range(height)]
    visible_trees[0] = [True for _ in range(width)]
    visible_trees[-1] = [True for _ in range(width)]
    for i in range(height):
        visible_trees[i][0] = True
        visible_trees[i][-1] = True

    # view from the left
    for row in range(1, height - 1):
        max_tree_height: int = int(trees[row][0])
        for col in range(1, width - 1):
            tree_height = int(trees[row][col])
            if tree_height > max_tree_height:
                visible_trees[row][col] = True
                max_tree_height = tree_height

    # view from the right
    for row in range(1, height - 1):
        max_tree_height: int = int(trees[row][-1])
        for col in range(width - 1, 1, -1):
            tree_height = int(trees[row][col])
            if tree_height > max_tree_height:
                visible_trees[row][col] = True
                max_tree_height = tree_height

    # view from the top
    for col in range(1, width - 1):
        max_tree_height: int = int(trees[0][col])
        for row in range(1, height - 1):
            tree_height = int(trees[row][col])
            if tree_height > max_tree_height:
                visible_trees[row][col] = True
                max_tree_height = tree_height

    # view from the bottom
    for col in range(1, width - 1):
        max_tree_height: int = int(trees[-1][col])
        for row in range(height - 1, 1, -1):
            tree_height = int(trees[row][col])
            if tree_height > max_tree_height:
                visible_trees[row][col] = True
                max_tree_height = tree_height

    count_visible = 0
    for row in visible_trees:
        count_visible += row.count(True)

    print(f"Part One: {count_visible}")

    max_score = 0
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            score = get_scenic_score(trees, row, col)
            if score > max_score:
                max_score = score

    print(f"Part Two: {max_score}")


def get_scenic_score(trees: Wood, row: int, col: int) -> int:
    height = len(trees)
    width = len(trees[0])

    own_height = int(trees[row][col])

    if row == 0 or col == 0:
        return 0

    # view to the left
    left_view = 0
    for c in range(col - 1, -1, -1):
        tree = trees[row][c]
        left_view += 1
        if int(tree) >= own_height:
            break

    # view to the right
    right_view = 0
    for c in range(col + 1, width):
        tree = trees[row][c]
        right_view += 1
        if int(tree) >= own_height:
            break

    # view to the top
    top_view = 0
    for r in range(row - 1, -1, -1):
        tree = trees[r][col]
        top_view += 1
        if int(tree) >= own_height:
            break

    # view to the bottom
    bottom_view = 0
    for r in range(row + 1, height):
        tree = trees[r][col]
        bottom_view += 1
        if int(tree) >= own_height:
            break

    return left_view * right_view * top_view * bottom_view


if __name__ == "__main__":
    main()
