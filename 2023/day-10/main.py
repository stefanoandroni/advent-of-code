
INPUT_FILE_PATH = 'data/input.txt'

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
    global M, visited_cells
    # S: (start) coordinates (x,y) of starting cell
    # M: (matrix) where M[x][y] ∈ {S,.,NS,EW,NE,NW,SW,SE}
    S, M = parse_input_file() 
    visited_cells = []

    xs, ys = S
    cell1, cell2 = get_starting_cells(xs, ys)

    visited_cells.append(S)
    visited_cells.append(cell1)
    visited_cells.append(cell2)

    path_length = 1
    while cell1 != cell2:
        cell1 = get_next(cell1)
        visited_cells.append(cell1)

        cell2 = get_next(cell2)
        visited_cells.append(cell2)

        path_length += 1

    # Part 1
    print(path_length)
    

def get_next(cell):
    x, y = cell
    coords = get_coords_from_dirs(M[y][x])
    candidate_cells = [(x + xc, y + yc) for xc, yc in coords if (x + xc, y + yc) not in visited_cells]
    return candidate_cells[0] if len(candidate_cells) > 0 else visited_cells[-1] # else: path2 ends up in cell1 (cell1 = visited_cells[-1])


def get_coords_from_dirs(dirs):
    return [DIR_TO_COORDS[dir] for dir in dirs]

def get_starting_cells(xs, ys):
    starting_points = set()
    for xd, yd in DIR_TO_COORDS.values():
        xds, yds = xs + xd, ys + yd
        for x, y  in get_coords_from_dirs(M[yds][xds]):
            if (xds+x, yds+y) == (xs, ys):
                starting_points.add((xds, yds))
    return starting_points


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

if __name__ == "__main__":
    main()