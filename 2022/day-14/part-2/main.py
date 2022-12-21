INPUT_FILE_PATH = '../data/input.txt'

START_POINT = (0, 500)

def main():
    global S # fixed sand
    global R # rock points set
    global O
    global floor_depth

    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()
    
    P = get_paths(file) # path list
    R = get_rock_points(P) 

    max_rock_depth = max([x for x, y in R])
    floor_depth = max_rock_depth + 2

    O = R.copy()

    S = set() 
    stop = False
    while not stop:
        unit, stop = produce_unit_of_sand()
        S.add(unit)
        O.add(unit)
        # print_matrix(R, S)
    
    print(len(S)) # <Part 2>


def produce_unit_of_sand():
    c = START_POINT # current point
    
    fixed = False
    while not fixed:
        x, y = c
        # O = S.union(R) # occupied points (sand + rock) # !!slow
        
        if x + 1 == floor_depth:
            fixed = True
        else:
            x = x + 1
            if (x, y) not in O:           # down one step
                c = (x, y)
            elif (x, y - 1) not in O:     # one step down and to the left
                c = (x, y - 1)
            elif (x, y + 1) not in O:     # one step down and to the right
                c = (x, y + 1)
            else:                         # comes to rest
                fixed = True                

    if c == START_POINT: # a unit of sand comes to rest at START_POINT
        return c, True    
    return c, False

def get_rock_points(paths):
    R = set()
    for path in paths:
        i = 0
        w = 2 # window
        while (i + w - 1 < len(path)):
            start = sx, sy = path[i] # start point
            end = ex, ey = path[i+1] # end point
            delta = dx, dy = (ex-sx, ey-sy)
            
            p = (sx, sy)
            R.add(p)
            while p != end:
                px, py = p
                if dx != 0:
                    px = px + 1 if dx > 0 else px - 1
                else:
                    py = py + 1 if dy > 0 else py - 1
                p = (px, py)
                R.add(p)

            i += 1
    return R

def get_paths(file):
    lines = file.split('\n')
    P = []
    for line in lines:
        C = [(int(x.split(',')[1]), int(x.split(',')[0])) for x in line.split(' -> ')] 
        P.append(C) 
    return P

def print_matrix(R, S):
    h = floor_depth
    D = [y for x,y in R] + [y for x,y in S]
    w_max = max(D)
    w_min = min(D)
    w = w_max - w_min

    m = []
    for r in range(h):
        row = ''
        for c in range(w):
            if (r, c + w_min) in R:
                row += "#"
            elif (r, c + w_min) in S:
                row += "o"
            elif (r, c + w_min) == START_POINT:
                row += "s"
            else:
                row += "."
        m.append(row)

    print(*m, sep='\n')


if __name__ == "__main__":
    main()