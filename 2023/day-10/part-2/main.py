
import math


INPUT_FILE_PATH = '../data/test-input-2-1.txt'

DIR_TO_COORDS = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
} 

SYMBOL_TO_DIRS = {
    '|': 'NS',
    '-': 'EW',
    'L': 'NE',
    'J': 'NW',
    '7': 'SW',
    'F': 'SE',
}

START = 'S'
GROUND = '.'


def main():
    global M, boundary_cells
    # S: (start) coordinates (x,y) of starting cell
    # M: (matrix) where M[y][x] ∈ {S,.,NS,EW,NE,NW,SW,SE}
    S, M = parse_input_file() 
    boundary_cells = []

    # Get boundary_cells
    xs, ys = S
    cell1, cell2 = get_starting_cells(xs, ys)

    current_cell = cell1 # or cell2

    boundary_cells.append(S)

    path_length = 1 # S -> cell1
    
    while current_cell != None:
        boundary_cells.append(current_cell)
        current_cell = get_next_cell(current_cell)
        path_length += 1

    # Part 2
    # Pick's theorem 
    # i = A - b / 2 + 1 where i is the number of integer points interior to the polygon
    # A: with Shoelace theorem
    # b: len(boundary_cells)
    print(int(get_shoelace_area(boundary_cells) - len(boundary_cells) / 2 + 1))


def get_next_cell(current_cell):
    x, y = current_cell
    coords = get_coords_from_dirs(M[y][x])
    next_cell = [(x + xc, y + yc) for xc, yc in coords if (x + xc, y + yc) not in boundary_cells]
    # assert: 0 <= len(candidate_cells) <= 1 
    return next_cell[0] if len(next_cell) > 0 else None # else: next cell is S


def get_coords_from_dirs(dirs):
    return [DIR_TO_COORDS[dir] for dir in dirs]


def get_starting_cells(xs, ys):
    starting_cells = set()
    for xd, yd in DIR_TO_COORDS.values():
        xds, yds = xs + xd, ys + yd
        if M[yds][xds] in SYMBOL_TO_DIRS.values():
            for x, y  in get_coords_from_dirs(M[yds][xds]):
                if (xds+x, yds+y) == (xs, ys):
                    starting_cells.add((xds, yds))
    # assert: len(starting_cells) == 2 
    return starting_cells


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    # matrix = [list(line) for line in file.split('\n')]
    start = None

    matrix = []
    lines = file.split('\n')
    for y, line in enumerate(lines):
        l = []
        for x, symbol in enumerate(line):
            if symbol == START:
                start = (x, y)
            l.append(SYMBOL_TO_DIRS[symbol] if symbol in SYMBOL_TO_DIRS else symbol)
        matrix.append(l)

    return start, matrix


def get_shoelace_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area


if __name__ == "__main__":
    main()