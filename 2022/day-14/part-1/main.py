INPUT_FILE_PATH = '../data/test-input.txt'

START_POINT = (0, 500)

def main():
    global S
    global R
    global max_rock_depth

    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()
    
    P = get_paths(file) # path list
    R = get_rock_points(P) # rock points set
    max_rock_depth = max([x for x, y in R])
    
    S = set() # fixed sand
    abyss = False
    while not abyss:
        unit = produce_unit_of_sand()
        if unit:
            S.add(unit)
        else:
            abyss = True
    
    print(len(S)) # <Part 1>

def produce_unit_of_sand():
    c = START_POINT # current point
    
    fixed = False
    while not fixed:
        x, y = c
        O = S.union(R) # occupied points (sand + rock)

        if ((x + 1), y) not in O:           # down one step
            c = ((x + 1), y)
        elif ((x + 1), y - 1) not in O:     # one step down and to the left
            c = ((x + 1), y - 1)
        elif ((x + 1), y + 1) not in O:     # one step down and to the right
            c = ((x + 1), y + 1)
        else:                               # comes to rest
            fixed = True                

        if c[0] >= max_rock_depth:          # falling forever
            return None 
    return c

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

if __name__ == "__main__":
    main()