SCORES = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}


SCORES_2 = {"A": [4, 8, 3], "B": [1, 5, 9], "C": [7, 2, 6]}


def main():
    score_1 = 0
    score_2 = 0
    with open("02/input.txt", "r", encoding="utf-8") as f:
        while True:
            data = f.readline().rstrip()

            if not data:
                break

            score_1 += SCORES[data]

            strategy = data[2]

            lose_win = SCORES_2[data[0]].copy()
            lose_win.sort()

            if strategy == "X":
                score_2 += lose_win[0]
            elif strategy == "Y":
                score_2 += lose_win[1]
            elif strategy == "Z":
                score_2 += lose_win[2]

    print(f"Part one: Score = {score_1}")
    print(f"Part two: Score = {score_2}")


if __name__ == "__main__":
    main()
