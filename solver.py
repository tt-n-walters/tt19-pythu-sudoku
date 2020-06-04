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
        puzzle.append(row)
    print(puzzle)


import os
correct_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(correct_dir)

puzzles = read_puzzle_file()
convert_puzzle(puzzles[10])
