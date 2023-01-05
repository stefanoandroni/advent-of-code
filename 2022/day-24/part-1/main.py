from collections import deque
from math import lcm

INPUT_FILE_PATH = 'data/test-input.txt'

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)] # dirs:{up, down, left, rigth, none}
dirs_symb = ['^', 'v', '<', '>']

def main():
    global BS, max_x, max_y, period, s
    # B: blizzards states -> ((x,y), d) [d: index of dir]
    # s: start pos -> (x, y)
    # e: end pos -> (x, y)
    # period: maximum number of different combinations (states)
    B, s, e, period, max_x, max_y = parse_file(INPUT_FILE_PATH) 

    BS = get_states(B, period) #BS: all possible combinations/states for B (set of ((x,y), dir)) -> B[t] = blizards positions at time t
    # CG = get_clear_ground()  # CG: clear grounds -> CG[t] = clear grounds positions at time t # TODO: more efficient using this? # CG of << # of S

    t = get_best_time(s, e) 
    print(t) # <Part 2>

# iterative BFS
def get_best_time(sp, ep): # sp: start position, ep: end position
    queue = deque() # entry -> ((current_pos), minutes) where current_pos = (x, y)
    V = set() # V: visited states

    m = 0
    queue.append((sp, m)) 

    while queue:
        cp, m = item = queue.popleft()

        if item in V:
            continue
        V.add(item)

        if cp == ep:
            return m

        for d in dirs:
            new_pos = sum_tuple(cp, d)

            if (not new_pos in {sp, ep}) and not in_borders(new_pos):
                continue

            if new_pos in [x for x, _ in BS[(m + 1) % period]]: 
                continue
            
            queue.append((new_pos, m + 1))

def in_borders(pos):
    x, y = pos
    return (0 < x < max_x and 0 < y < max_y)

def sum_tuple(tuple_1, tuple_2):
    return tuple(map(lambda i, j: i + j, tuple_1, tuple_2))

def get_states(B, period):
    S = [None] * period

    S[0] = B
    for t in range(1, period):
        NB = set() # NB: new blizard
        for b in B:
            (x, y), d = b
            dx, dy = dirs[d]
            new_x, new_y = get_consistent_pos(x + dx, y + dy) # return in matrix limits pos
            NB.add(((new_x, new_y), d))
        S[t] = NB
        B = NB
    return S

def get_consistent_pos(x, y):
    if not in_borders((x, y)): # I'm on border
        if x == 0:
            return (max_x - 1, y)
        if x == max_x:
            return (1, y)
        if y == 0:
            return (x, max_y - 1)
        if y == max_y:
            return (x, 1)
    return (x, y)

def parse_file(path):
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()

    lines = file.split('\n')

    B = set()
    max_x = 0
    max_y = 0

    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            match symbol:
                case '>' | '<' | 'v' | '^':
                    B.add(((x,y), dirs_symb.index(symbol)))
                case '.' if y == 0:
                    s = (x, y)
                case '.' if y == len(lines) - 1:
                    e = (x, y)

    period = lcm(len(lines) - 2, len(lines[0]) - 2)

    return B, s, e, period, max_x, max_y

# def get_clear_ground(): # optimization: CG calculated in the same cycle as S
#     CG = [None] * period
#     for t in range(0, period):
#         CG[t] = set([x for x in A if x not in [k for k, j in S[t]]])
#     return CG

if __name__ == "__main__":
    main()