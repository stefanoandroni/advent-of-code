
INPUT_FILE_PATH = '../data/test-input.txt'

CYCLES = 1000
DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def main():
    global H, W, RR, CR
    # H: platform height
    # W: platform width
    # RR: (rounded rocks) a list of (x, y) coordinates representing the positions of each rounded rock
    # CR: (cube rocks) a set of (x, y) coordinates representing the positions of each cube rock
    H, W, RR, CR = parse_input_file()

    for i in range(CYCLES):
        print(i)          
        for dir in DIRS:
            round_to_dir(dir)

    total_load = 0
    for rr in RR:
        total_load += get_load(rr)

    # Part 2
    print(total_load)


def get_load(rr):
    x, y  = rr
    return H - y


def round_to_dir(dir):
    '''
        TODO: change (bad performance) -> use 2d matrix
    '''
    xd, yd = dir

    def get_next_pos(coords):
        x, y = coords
        if (x + xd, y + yd) in CR:
            return (x, y)
        if y + yd < 0 or y + yd >= H or x + xd < 0 or x + xd >= W:
            return (x, y)
        if (x + xd, y + yd) in RR:
            return (x, y)
        return (x + xd, y + yd)

    can_move = [] # set of indexs of rounded rocks that can move
    if (dir == DIRS[0]):
        can_move = sorted(RR, key=lambda x: x[1])
    elif (dir == DIRS[1]):
        can_move = sorted(RR, key=lambda x: x[0])
    elif (dir == DIRS[2]):
        can_move = sorted(RR, key=lambda x: x[1], reverse=True)
    elif (dir == DIRS[3]):
        can_move = sorted(RR, key=lambda x: x[0], reverse=True)

    can_move = [RR.index(x) for x in can_move]

    while len(can_move) > 0:
        to_remove = set()
        for i in can_move:
            next_pos = get_next_pos(RR[i])
            if next_pos == RR[i]:
                to_remove.add(i)
            RR[i] = next_pos
        can_move = [x for x in can_move if x not in to_remove]


def parse_input_file():
    ROUNDED_ROCK_SYMBOL = 'O'
    CUBE_ROCK_SYMBOL = '#'

    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    rounded_rocks = []
    cube_rocks = set()

    lines = file.split('\n')
    for y, line in enumerate(lines):
        for x, symb in enumerate(list(line)):
            if symb == ROUNDED_ROCK_SYMBOL:
                rounded_rocks.append((x, y))
            elif symb == CUBE_ROCK_SYMBOL:
                cube_rocks.add((x, y))

    return len(lines), len(lines[0]), rounded_rocks, cube_rocks


if __name__ == "__main__":
    main()