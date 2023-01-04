
from math import lcm

INPUT_FILE_PATH = 'data/test-input.txt'

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)] # dirs:{up, down, left, rigth}
dirs_symb = ['^', 'v', '<', '>']

def main():
    B, W, s, e, period = parse_file(INPUT_FILE_PATH) # B: blizzards, W: walls, s: start, e: end, period: maximum number of different combinations (states)

    # Populate S with all possible states
    S = []
    S[0] = B
    for i in range(1, period):
        pass
        # HERE move all B and add as state i

def parse_file(path):
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()
    lines = file.split('\n')
    W = set()
    B = set()

    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):
            match symbol:
                case '#':
                    W.add((x, y))
                case '>' | '<' | 'v' | '^':
                    B.add(((x,y), dirs_symb.index(symbol)))
                case '.' if y == 0:
                    s = (x, y)
                case '.' if y == len(lines) - 1:
                    e = (x, y)

    period = lcm(len(lines) - 2, len(lines[0]) - 2)

    return B, W, s, e, period

if __name__ == "__main__":
    main()

# import time

# if __name__ == "__main__":
#     start_time = time.time()
#     main()
#     print("--- %s seconds ---" % (time.time() - start_time))