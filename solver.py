# heuristics
# backtracking

from pprint import pprint

def read_puzzle_file():
    with open("puzzles") as file:
        content = file.read().splitlines()
        return content

def convert_puzzle(string):
    puzzle = []
    for i in range(9):
        row = string[i*9 : i*9+9]
        row = list(row)
        row = list(map(int, row))
        puzzle.append(row)
    return puzzle


def check_pos(puzzle, x, y, n):
    row = puzzle[y]
    column = [row[x] for row in puzzle]
    i = x // 3
    j = y // 3
    print(puzzle[j*3 : j*3+3])



if __name__ == "__main__":
    import os
    correct_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(correct_dir)

    puzzles = read_puzzle_file()

    puzzle = convert_puzzle(puzzles[10])

    pprint(puzzle)
    check_pos(puzzle, 2, 6, None)
