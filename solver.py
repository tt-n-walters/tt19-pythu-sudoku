# heuristics
# backtracking

def read_puzzle_file():
    with open("puzzles") as file:
        content = file.read().splitlines()
        return content