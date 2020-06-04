# heuristics
# backtracking

def read_puzzle_file():
    with open("puzzles") as file:
        content = file.read().splitlines()
        return content

def convert_puzzle(string):
    puzzle = []
    for i in range(9):
        row = string[i*9 : i*10]
        puzzle.append(row)
    print(puzzle)