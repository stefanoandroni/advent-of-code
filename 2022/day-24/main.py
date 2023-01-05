from collections import deque
from math import lcm

INPUT_FILE_PATH = 'data/input.txt'

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)] # dirs:{up, down, left, rigth}
dirs_symb = ['^', 'v', '<', '>']

def main():
    global A, L, S, CG, max_x, max_y, period, s
    A, B, W, s, e, period, max_x, max_y = parse_file(INPUT_FILE_PATH) # A: all grounds within the borders (x,y) # B: blizzards ((x,y), d) [d: index of dir], W: walls, s: start, e: end, period: maximum number of different combinations (states)

    L = get_L(W, s, e) # L: W + s + e

    S = get_states(B, period) #S: all possible combinations/states for B (set of ((x,y), t)) -> B[t] = blizards positions at time t
    # for p, s in enumerate(S):
    #     print("p:", p, " S:", s)
    #     print(len(s))
    
    CG = get_clear_ground()  # CG: clear grounds -> CG[t] = clear grounds positions at time t
    # for p, cg in enumerate(CG):
    #      print("p:", p, " CG:", cg)
    #      print(len(cg))

    t = get_best_time(s, e) 
    print(t)


def get_best_time(sp, ep): # current_pos, target_pos, minutes
    queue = deque()

    V = set() # V: visited
    m = 0
    queue.append((sp, m))

    while queue:
        cp, m = item = queue.popleft()
        # print(cp, m)

        if item in V:
            continue
        V.add(item)

        if cp == ep:
            return m

        for d in dirs:
            #print(d)
            new_x, new_y = new_pos = sum_tuple(cp, d)

            if (not new_pos in [sp, ep]) and not (1 <= new_x <= max_x - 1 and 1 <= new_y <= max_y - 1):
                continue

            if new_pos in [x for x, y in S[(m + 1) % period]]: 
                continue
            
            queue.append((new_pos, m + 1))

        #queue = remove_duplicates(queue) # use visited set and check
            # print(pos)

    # print(cp, ep, m)
    # if cp == ep:
    #     return m

    # p = m % period # period time
    
    # m += 1

    # poss_pos = set()
    # for d in dirs + [(0,0)]:
    #     x, y = pos = sum_tuple(cp, d)
    #     # if pos == ep:
    #     #     print("OO")
    #     #     return get_best_time(pos, ep, m + 1)
    #     if pos in S[p]:
    #         continue
    #     if x <= 0 or x >= max_x or y <= 0 or y >= max_y:
    #         continue
    #     return get_best_time(pos, ep, m + 1)
    
# [sum_tuple(cp, x) for x in dirs if sum_tuple(cp, x) not in S[p]]
#     print(p, poss_pos)

def remove_duplicates(d):
    result = deque()

    for element in d:
        if element not in result:
            result.append(element)

    return result

def sum_tuple(tuple_1, tuple_2):
    return tuple(map(lambda i, j: i + j, tuple_1, tuple_2))

def get_clear_ground(): # optimization: CG calculated in the same cycle as S
    CG = [None] * period
    for t in range(0, period):
        CG[t] = set([x for x in A if x not in [k for k, j in S[t]]])
    return CG

def get_states(B, period):
    S = [None] * period

    S[0] = B
    for t in range(1, period):
        NB = set() # NB: new blizard
        for b in B:
            (x, y), d = b
            dx, dy = dirs[d]
            new_x, new_y = get_consistent_pos(x + dx, y + dy) # return in matrix limit pos
            NB.add(((new_x, new_y), d))
        S[t] = NB
        B = NB
    return S

def get_const_pos(x, y):
    if (x, y) in L: # Son sul bordo
        if x <= 0:
            return (max_x - 1, y)
        if x >= max_x:
            return (1, y)
        if y <= 0:
            return (x, max_y - 1)
        if y >= max_y:
            return (x, 1)
    return x,y

def get_consistent_pos(x, y):
    if (x, y) in L: # Son sul bordo
        if x == 0:
            return (max_x - 1, y)
        if x == max_x:
            return (1, y)
        if y == 0:
            return (x, max_y - 1)
        if y == max_y:
            return (x, 1)
    return (x, y)

def get_L(W, s, e):
    L = W.copy()
    L.update([s, e])
    return L

def parse_file(path):
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()
    lines = file.split('\n')
    W = set()
    B = set()
    A = set()

    max_x = 0
    max_y = 0
    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            match symbol:
                case '#':
                    W.add((x, y))
                case '>' | '<' | 'v' | '^':
                    B.add(((x,y), dirs_symb.index(symbol)))
                    A.add((x, y))
                case '.' if y == 0:
                    s = (x, y)
                case '.' if y == len(lines) - 1:
                    e = (x, y)
                case _:
                    A.add((x, y))

    period = lcm(len(lines) - 2, len(lines[0]) - 2)

    return A, B, W, s, e, period, max_x, max_y

if __name__ == "__main__":
    main()

# import time

# if __name__ == "__main__":
#     start_time = time.time()
#     main()
#     print("--- %s seconds ---" % (time.time() - start_time))