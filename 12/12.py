import math


Position = tuple[int, int]


class Node:
    grid_width: int = 10000
    grid_height: int = 10000

    def __init__(self, pos: Position, height: int = 0):
        self._x: int = pos[0]
        self._y: int = pos[1]
        self.height: int = height

        self.g: float = 0
        self.h: float = 0
        self.neighbors: list[Position] = []
        self.prev_node: Node | None = None

        self.calc_neighbors()

    def initialize(self) -> None:
        self.g = 0
        self.h = 0
        # self.prev_node = None

    def calc_neighbors(self):
        self.neighbors.clear()
        if self.x > 0:
            self.neighbors.append((self.x - 1, self.y))
        if self.x < self.grid_width - 1:
            self.neighbors.append((self.x + 1, self.y))
        if self.y > 0:
            self.neighbors.append((self.x, self.y - 1))
        if self.y < self.grid_height - 1:
            self.neighbors.append((self.x, self.y + 1))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        return True

    def __sub__(self, other: "Node") -> float:
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def __hash__(self):
        return self.x * 256 + self.y

    @property
    def position(self) -> Position:
        return self._x, self._y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def set_x(self, value: int) -> None:
        self._x = value
        self.calc_neighbors

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def set_y(self, value: int) -> None:
        self._y = value
        self.calc_neighbors()

    @property
    def f(self) -> float:
        return self.g + self.h


Path = list[Node]
Grid = list[list[Node]]


class Pathfinder:
    def __init__(self, grid: Grid):
        self.grid = grid

        self.calculated_paths: list[Path] = []
        self.no_paths: set[Node] = set()

    def _node_of(self, pos: Position) -> Node:
        for row in self.grid:
            for node in row:
                if node.position == pos:
                    return node
        raise AttributeError(f"A node with position {pos} doesn't exist.")

    def init_nodes(self) -> None:
        for row in self.grid:
            for node in row:
                node.initialize()

    def find_calculated(self, node: Node) -> list[Node] | None:
        for path in self.calculated_paths:
            if node in path:
                idx = path.index(node) + 1
                return path[idx:]
        return None

    def process(self, start_pos: Position, end_pos: Position) -> Path | None:
        lowest_f_node: Node
        lowest_f: float
        path: Path = []
        open_set: set[Node] = set()
        closed_set: set[Node] = set()
        start: Node = self._node_of(start_pos)
        end: Node = self._node_of(end_pos)

        start.prev_node = None
        current = start

        self.init_nodes()

        open_set.add(current)

        while len(open_set):
            lowest_f_node = current
            lowest_f = 10000

            for node in open_set:
                if node.f < lowest_f:
                    lowest_f = node.f
                    lowest_f_node = node

            current = lowest_f_node
            if current in self.no_paths:
                break

            open_set.remove(current)
            closed_set.add(current)

            calced_path = self.find_calculated(current)

            if calced_path:
                node = current

                while node.prev_node:
                    path.insert(0, node)
                    node = node.prev_node
                path += calced_path

                self.calculated_paths.append(path)
                return path

            if current == end:
                node = current

                while node.prev_node:
                    path.insert(0, node)
                    node = node.prev_node

                self.calculated_paths.append(path)
                return path

            for neighbor in current.neighbors:
                node = self._node_of(neighbor)
                if node in closed_set:
                    continue
                if node.height - current.height > 1:
                    continue

                g = current.g + 1

                if node in open_set:
                    if g < node.g:
                        node.g = g
                        node.prev_node = current
                else:
                    node.g = g
                    open_set.add(node)
                    node.prev_node = current

                node.h = heuristic(node, end)

        node = current
        while node:
            self.no_paths.add(node)
            node = node.prev_node
        return None


def process(start: list[Position], end: Position, grid: list[list[Node]]) -> int:
    pathfinder = Pathfinder(grid)
    min_moves: int = 100000

    while start:
        s = start.pop(0)
        moves = pathfinder.process(s, end)
        if moves is None:
            continue

        print(f"Moves from Start {s}: {len(moves)}")
        length = len(moves)
        if length < min_moves:
            min_moves = length

        while moves[-1].height == 0:
            pos = moves[-1].position
            moves.pop()
            print(f"Moves from Start {pos}: {len(moves)}")
            start.remove(pos)
            min_moves -= 1

    return min_moves


def create_grid(lines: list[str]) -> tuple[Position, Position, list[list[Node]]]:
    grid: Grid = []
    start: Position = (0, 0)
    end: Position = (0, 0)
    start_found: bool = False
    end_found: bool = False

    for y, line in enumerate(lines):
        if not start_found:
            x = line.find("S")
            if x >= 0:
                start = (x, y)
                line = line.replace("S", "a")
                start_found = True
        if not end_found:
            x = line.find("E")
            if x >= 0:
                end = (x, y)
                line = line.replace("E", "z")
                end_found = True

        line = [ord(c) - ord("a") for c in line.strip()]

        grid_line: list[Node] = []
        for x, height in enumerate(line):
            grid_line.append(Node((x, y), height))

        grid.append(grid_line)
    return start, end, grid


def get_possible_starts(grid: Grid) -> list[Position]:
    positions: list[Position] = []

    for row in grid:
        for node in row:
            if node.height == 0:
                positions.append(node.position)
    return positions


def heuristic(a: Node, b: Node) -> float:
    height_diff = a.height - b.height
    if height_diff < 0:
        height_diff = 0
    return (b - a) * (height_diff + 1)


def main():
    start: Position
    end: Position
    grid: Grid

    with open("12/input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    Node.grid_height = len(lines)
    Node.grid_width = len(lines[0].strip())

    start, end, grid = create_grid(lines)
    result = process([start], end, grid)
    print(f"Part One: {result}")

    starts: list[Position] = get_possible_starts(grid)
    result = process(starts, end, grid)
    print(f"Part Two: {result}")


if __name__ == "__main__":
    main()
