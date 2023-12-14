
INPUT_FILE_PATH = 'data/input.txt'


def main():
    global H,RR, CR
    # H: platform height
    # RR: (rounded rocks) a list of (x, y) coordinates representing the positions of each rounded rock
    # CR: (cube rocks) a set of (x, y) coordinates representing the positions of each cube rock
    H, RR, CR = parse_input_file()

    round_to_north()

    total_load = 0
    for rr in RR:
        total_load += get_load(rr)

    # Part 1
    print(total_load)


def get_load(rr):
    x, y  = rr
    return H - y


def round_to_north():

    def get_next_pos(coords):
        x, y = coords
        if (x, y - 1) in CR:
            return (x, y)
        if y - 1 < 0:
            return (x, y)
        if (x, y - 1) in RR:
            return (x, y)
        return (x, y - 1)

    can_move = set(list(range(len(RR)))) # set of indexs of rounded rocks that can move

    while len(can_move) > 0:
        to_remove = set()
        for i in can_move:
            nex_pos = get_next_pos(RR[i])
            if nex_pos == RR[i]:
                to_remove.add(i)
            RR[i] = nex_pos
        can_move -= to_remove


def parse_input_file():
    ROUNDED_ROCK_SYMBOL = 'O'
    CUBE_ROCK_SYMBOL = '#'

    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    rounded_rocks = [] # NOTE: order is important
    cube_rocks = set()

    lines = file.split('\n')
    for y, line in enumerate(lines):
        for x, symb in enumerate(list(line)):
            if symb == ROUNDED_ROCK_SYMBOL:
                rounded_rocks.append((x, y))
            elif symb == CUBE_ROCK_SYMBOL:
                cube_rocks.add((x, y))

    return len(lines),rounded_rocks, cube_rocks


if __name__ == "__main__":
    main()