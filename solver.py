# heuristics
# backtracking

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
    print(puzzle)


if __name__ == "__main__":
    import os
    correct_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(correct_dir)

    puzzles = read_puzzle_file()
    convert_puzzle(puzzles[10])
