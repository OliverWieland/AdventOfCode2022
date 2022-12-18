from typing import Callable


class Monkey:
    mod: int = 1
    boring_division: int = 1

    def __init__(self) -> None:
        self.items: list[int]
        self.operation: Callable[[int, int], int]
        self.operand: int
        self.test: int
        self.test_success: int
        self.test_fail: int
        self.inspection_count: int = 0

    def set_description(self, desc: str) -> None:
        if desc.startswith("Starting items"):
            self.items = [int(item) for item in desc[16:].split(",")]
        elif desc.startswith("Operation"):
            self.__set_operation(desc[21:])
        elif desc.startswith("Test"):
            self.test = int(desc[19:])
        elif desc.startswith("If true"):
            self.test_success = int(desc[-1])
        elif desc.startswith("If false"):
            self.test_fail = int(desc[-1])

    def append(self, item: int) -> None:
        self.items.append(item)

    def inspect(self) -> list[list[int]]:
        items: list[list[int]] = []
        while True:
            try:
                item: int = self.items.pop(0)
            except IndexError:
                break

            worry_level: int = self.operation(item, self.operand)

            if self.boring_division == 1:
                worry_level %= self.mod
            worry_level //= self.boring_division

            if worry_level % self.test == 0:
                items.append([worry_level, self.test_success])
            else:
                items.append([worry_level, self.test_fail])
            self.inspection_count += 1
        return items

    def __set_operation(self, desc: str):
        operator: str = desc[0]
        operand: str = desc[2:]

        if operator == "+":
            self.operation = self.__add
            self.operand = int(operand)
        elif operator == "-":
            self.operation = self.__sub
            self.operand = int(operand)
        elif operator == "*":
            if operand == "old":
                self.operation = self.__pow
                self.operand = 2
            else:
                self.operation = self.__mul
                self.operand = int(operand)

    @staticmethod
    def __add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def __sub(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def __mul(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def __pow(a: int, b: int) -> int:
        return a**b

    pass


def monkey_in_the_middle(rounds: int, boring_division: int):
    monkeys: list[Monkey] = []

    with open("11/input.txt", "r", encoding="utf-8") as f:
        while True:
            line = f.readline()

            if line == "":
                break

            if line.startswith("Monkey"):
                monkey = Monkey()
                for _ in range(5):
                    monkey.set_description(f.readline().strip())

                monkeys.append(monkey)

    mod = 1
    for monkey in monkeys:
        mod *= monkey.test
    Monkey.mod = mod
    Monkey.boring_division = boring_division

    for _ in range(rounds):
        for monkey in monkeys:
            items = monkey.inspect()

            for item in items:
                monkeys[item[1]].append(item[0])

    inspection_counts: list[int] = []
    for monkey in monkeys:
        inspection_counts.append(monkey.inspection_count)

    inspection_counts.sort(reverse=True)

    return inspection_counts[0] * inspection_counts[1]


def main():
    print(f"Part One: {monkey_in_the_middle(20, 3)}")
    print(f"Part Two: {monkey_in_the_middle(10000, 1)}")


if __name__ == "__main__":
    main()
