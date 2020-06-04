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

def print_puzzle(puzzle):
    output = "-" * 21 + "\n"
    for row in puzzle:
        output += "| "
        for n in row:
            if n == 0:
                output += " "
            else:
                output += str(n)
            output += " "
        output += "|\n"
    output += "-" * 21
    print(output)

def check_pos(puzzle, x, y, n):
    row = puzzle[y]
    column = [row[x] for row in puzzle]

    i = (x // 3) * 3
    j = (y // 3) * 3
    section = [n for row in puzzle[j : j+3] for n in row[i : i+3]]
    
    return not n in row and not n in column and not n in section
    return not n in row + column + section
    return not n in set([row, column, section])


def solve(puzzle):
    print_puzzle(puzzle)
    for j in range(9):
        for i in range(9):
            n = puzzle[j][i]
            if n == 0:
                for z in range(1, 10):
                    if check_pos(puzzle, i, j, z):
                        puzzle[j][i] = z
                        solve(puzzle)
                        # Here is where the backtracking has happened
                        puzzle[j][i] = 0
                # Decide to backtrack
                return None
    print("Yay we did it!")
    print_puzzle(puzzle)



if __name__ == "__main__":
    import os
    correct_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(correct_dir)

    puzzles = read_puzzle_file()

    puzzle = convert_puzzle(puzzles[10])

    solve(puzzle)
