# TODO: SLOW!

INPUT_FILE_PATH = '../data/test-input.txt'

ROUND = 10

def sum_tuple(tuple_1, tuple_2):
    return tuple(map(lambda i, j: i + j, tuple_1, tuple_2))

N = (0, -1)
S = (0, 1)
W = (-1, 0)
E = (1, 0)

NE = sum_tuple(N, E)
NW = sum_tuple(N, W)
SE = sum_tuple(S, E)
SW = sum_tuple(S, W)

ORT_DIR = {N, S, E, W}
DIA_DIR = {NE, NW, SE, SW}

DIR  = ORT_DIR | DIA_DIR

def main():
    global EL, D
    EL = parse_file(INPUT_FILE_PATH)
    
    # print_matrix(EL)

    D = [N, S, W, E]

    moves = True
    i = 0
    while moves:
        # point -> represents an elf  (point in 2d space -> (x, y) tuple)
        EM = set()  # EM: list of elves who have to move 
        REL = set() # REL: list of elves for the current round
        NP = set() # NP: list of point pairs (position), (new position proposed) 
        moves = 0

        # Populate the EM list
        for elf in EL:
            if has_adjacent(elf):
                EM.add(elf)
            else:
                REL.add(elf)

        # Populate the NP list
        for elf in EM:
            elf, new_elf = move(elf)
            if new_elf:
                NP.add((elf, new_elf))
            else:
                REL.add(elf)
        
        # Populate the REL list (update the pos of only elves who have proposed different locations)
        for elf, new_elf in NP:
            if is_only(new_elf, NP):
                moves += 1
                REL.add(new_elf)
            else:
                REL.add(elf)

        if moves == 0: # REL == EL:
            moves = False       
        EL = REL

        # print_matrix(EL)
        
        next_dir()
        i += 1

    print(i) # <Part 2>

def next_dir():
    d = D.pop(0)
    D.append(d)

def is_only(item, np):
    np_ls = [new_elf for elf, new_elf in np] 
    if np_ls.count(item) > 1:
        return False
    return True
    
def move(elf):
    for dir in D:
        if is_good(elf, dir):
            return elf, sum_tuple(elf,dir)
    return elf, None

def is_good(p, dir):
    elf_pos = EL

    if dir == N:
        return (sum_tuple(p, N) not in elf_pos) and (sum_tuple(p, NE) not in elf_pos) and (sum_tuple(p, NW) not in elf_pos) 
    if dir == S:
        return (sum_tuple(p, S) not in elf_pos) and (sum_tuple(p, SE) not in elf_pos) and (sum_tuple(p, SW) not in elf_pos) 
    if dir == E:
        return (sum_tuple(p, E) not in elf_pos) and (sum_tuple(p, NE) not in elf_pos) and (sum_tuple(p, SE) not in elf_pos) 
    if dir == W:
        return (sum_tuple(p, W) not in elf_pos) and (sum_tuple(p, NW) not in elf_pos) and (sum_tuple(p, SW) not in elf_pos) 

def has_adjacent(elf):
    for dir in DIR:
        if (sum_tuple(dir, elf)) in [e for e in EL]:
            return True
    return False

def parse_file(path):
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')
        EL = set()
        for y, line in enumerate(lines):
            for x, symbol in enumerate(line):
                if symbol == '#':
                    EL.add(((x, y)))
        return EL

def get_normalized_points(M):
    min_x, min_y = max_x, max_y = M[0]
    for x,y in M:
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    offset_x = abs(min_x) if min_x < 0 else -min_x
    offset_y = abs(min_y) if min_y < 0 else -min_y

    M = [(x + offset_x, y + offset_y) for x, y in M]

    for x,y in M:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    return M, max_x, max_y

def print_matrix(M): # TODO: bad function
    M, max_x, max_y = get_normalized_points(M)

    i = 0
    for y in range(max_y + 1):
        row = ""
        for x in range(max_x +1):
            if (x, y) in M:
                i+=1
                row += '#'
            else:
                row += '.'
        print(row)
    print(i)
    print()

def count_empty_tiles(M):
    M, max_x, max_y = get_normalized_points(M)

    i = 0
    for y in range(max_y + 1):
        for x in range(max_x +1):
            if (x, y) not in M:
                i+=1
    return i    

if __name__ == "__main__":
    main()