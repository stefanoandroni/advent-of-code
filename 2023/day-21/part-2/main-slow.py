
INPUT_FILE_PATH = '../data/input.txt'


STEPS = 26501365

DIRS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def main():
    global R, L
    # R: (rocks) - set of rocks (r, c)
    # G: (garden plots) - set of garden plots (r, c) 
    # S: (starting position) - (r, c)
    # L: (length) - map side length (squared map)
    R, G, S, L = parse_input_file() 
    
    # NOTE: R << S -> use only R and L

    # - - - - - - - - - INPUT ANALYSES  - - - - - - - - - 
    # - (0, c) = '.' for any c
    # - (L-1, c) = '.' for any c
    # - (rs, c) = '.' for any c
    # - (r, cs) = '.' for any r
    # - (rs, cs) is in the center of the grid


    # - - - - - - - - END INPUT ANALYSES  - - - - - - - - 

    current_positions = set()
    current_positions.add(S)

    for _ in range(STEPS):
        new_positions = set()
        while current_positions:
            r, c = current_positions.pop()
            for dr, dc in DIRS:
                if is_garden_plot(r + dr, c + dc):
                    new_positions.add((r + dr, c + dc))
        current_positions = new_positions

    # Part 2
    print(len(current_positions))


def is_in_matrix(row, col):
    if row < 0 or col < 0 or row >= L or col >= L:
        return False
    return True    


def is_garden_plot(row, col):
    row = row % L
    col = col % L

    if (row, col) in R:
        return False

    return True


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    lines = file.splitlines()

    class Symbol:
        ROCK = "#"
        GARDEN_PLOT = "."
        START = "S"

    rocks = set()
    garden_plots = set()
    start = None
    length = len(lines)

    for row, line in enumerate(lines):
        for col, value in enumerate(line):
            cell = (row, col)
            match value:
                case Symbol.ROCK:
                    rocks.add(cell)
                case Symbol.GARDEN_PLOT:
                    garden_plots.add(cell)
                case Symbol.START:
                    start = cell
                    garden_plots.add(cell)

    return rocks, garden_plots, start, length


if __name__ == "__main__":
    main()
