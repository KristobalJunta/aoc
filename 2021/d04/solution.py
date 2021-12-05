import fileinput
from pprint import pprint


def get_input():
    data = [s.strip() for s in fileinput.input()]
    return data


def parse_input(data):
    calls = data[0].split(",")
    boards = [[s.split() for s in data[i : i + 5]] for i in range(2, len(data), 6)]
    return boards, calls


def count_score(board, call):
    board_score = sum(int(x) for row in board for x in row if x != "x")
    return board_score * int(call)


def get_winning_scores(boards, calls):
    won = []
    scores = {}

    for call in calls:
        for idx, board in enumerate(boards):
            if idx in won:
                continue

            for i in range(5):
                for j in range(5):
                    if board[i][j] == call:
                        board[i][j] = "x"

            if any(  # any row is x
                [
                    all([x == 'x' for x in row])
                    for row in board
                ]
            ) or any(  # any column is x
                [
                    all([row[i] == 'x' for row in board])
                    for i in range(5)
                ]
            ):
                won.append(idx)
                scores[idx] = count_score(board, call)

    return won, scores


def part1(data):
    boards, calls = parse_input(data)
    won, scores = get_winning_scores(boards, calls)
    return scores[won[0]]

def part2(data):
    boards, calls = parse_input(data)
    won, scores = get_winning_scores(boards, calls)
    return scores[won[-1]]


if __name__ == "__main__":
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
