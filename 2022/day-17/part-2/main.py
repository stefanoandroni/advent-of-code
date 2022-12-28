from math import lcm
from copy import deepcopy

INPUT_FILE_PATH_ROCK = '../data/rocks.txt'
INPUT_FILE_PATH_JET = '../data/jet-pattern.txt'

STOP = 1_000_000_000_000

LEFT_LIMIT = 0
RIGTH_LIMIT = 6
BOTTOM_LIMIT = 0

X_MOVE_SYMBOL = 'x'
y_MOVE_SYMBOL = 'y'

NO_ROCK_SYMBOL = '.'
ROCK_SIMBOL = '#'
LEFT_SYBMOL = '<'
RIGTH_SYMBOL = '>'


def main():
    simulate(STOP) 

def simulate(stop_num):
    global heights

    # state = (current_jet_index, current_shape_index, normalized heights for x = 0..6)
   
    # Find the first state already encountered  - - - - - - - - - - - - - - - - 
    reset()

    i = 0
    while i < stop_num:
        drop_rock()
        state = (JIndex, RIndex, ",".join([str(x) for x in heights]))
        if state in STATES:
            target_state = state
            break
        STATES.append(state)
        i += 1

    last_state = STATES[-1]

    # Find the width and height gain of the cycle   - - - - - - - - - - - - - -
    reset()

    L = []
    
    found_cycle_start = False
    i = 0
    while i < stop_num:
        prev_H = H + 1 # if H > 0 else 0
        drop_rock()
        state = (JIndex, RIndex, ",".join([str(x) for x in heights]))
        if not(found_cycle_start):
            if state == target_state:
                first_cycle_start_index = i
                found_cycle_start = True
        else:
            L.append(H + 1 - prev_H)
            if state == target_state:
                break               
        i += 1

    cycle_H_gain = sum(L) # Cycle H gained
    cycle_width = len(L)  # Cycle width


    # Calculate the total height    - - - - - - - - - - - - - - - - - - - - - -
    total_height = 0

    # Drop the blocks until the first cycle starts
    reset()
    i = 0
    while i < first_cycle_start_index:
        drop_rock()
        h = H
        i += 1
    
    total_height += h

    # Calculate total height for full cycles
    n = (STOP - (first_cycle_start_index)) // cycle_width
    r = (STOP - (first_cycle_start_index)) % cycle_width
    
    total_height += n * cycle_H_gain

    # Calculate the height for the remaining blocks starting from the last state of the cycle
    reset_from_state(last_state) # last state of cycle
    
    i = 0
    while i < r:
        drop_rock()
        h = H
        i += 1

    _, _, heights = last_state
    starting_h = max([int(x) for x in heights.split(",")])

    total_height += h - starting_h + 1

    print(total_height) # <Part 2>


# FIRST APPROACH (not worked for me)    \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
# Idea -->  c,d,e,a,b,c,d,e,a,b,c,d,e,a,b,c,d,e,a,b
#           final part of the cycle + N*cycle + early part of the cycle
#           with cycle = a,b,c,d,e

#     for i in range(len(L) - 1, len(L) - first_cycle_start_index - 1, -1):
#         total_height += L[i]

#     n = (STOP - (first_cycle_start_index)) // cycle_width
#     r = (STOP - (first_cycle_start_index)) % cycle_width
    
#     total_height += n * cycle_H_gain

#     for i in range(0, r):
#         total_height += L[i]

#     print(total_height)
# \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 

def drop_rock():
    global M
    M = [X_MOVE_SYMBOL, y_MOVE_SYMBOL]
    r = get_rock().put_in_start_pos()

    stop = False
    while not stop:
        m = get_move()
        if m == X_MOVE_SYMBOL: # X MOVE
            j = get_jet()
            r = r.move_to(j)
        else: # Y MOVE
            r, stop = r.move_down() 
      
    S.update(r.points)
    update_H(r.points)
    udateNormalizedHeights(r.points)
    
def get_move(): # infinite queue with list
    m = M.pop(0)
    M.append(m)
    return m

def get_rock(): # infinite queue with list
    global RIndex
    RIndex += 1
    if RIndex >= len(R):
        RIndex -= len(R)
    r = R.pop(0)
    R.append(r)
    return deepcopy(r)

def get_jet(): # infinite queue with list
    global JIndex
    JIndex += 1
    if JIndex >= len(J):
        JIndex -= len(J)
    j = J.pop(0)
    J.append(j)
    return j

def reset():
    global J, R, S, H # J: jet pattern # R: rocks # S: stopped rocks # H: max y index height
    global STATES, JIndex, RIndex, heights
    
    # Parse files
    R = parse_rock_file(INPUT_FILE_PATH_ROCK)
    J = parse_jet_file(INPUT_FILE_PATH_JET)

    H = -1
    S = set()
    get_H() 
    
    l = RIGTH_LIMIT - LEFT_LIMIT 
    heights = [0 for _ in range(l + 1)]

    JIndex = -1
    RIndex = -1

    STATES = []

def reset_from_state(state):
    global J, R, S, H # J: jet pattern # R: rocks # S: stopped rocks # H: max y index height
    global STATES, JIndex, RIndex, heights
    
    # Parse files
    R = parse_rock_file(INPUT_FILE_PATH_ROCK)
    J = parse_jet_file(INPUT_FILE_PATH_JET)

    j, r, hs = state
    
    S = set() 
    for index, h in enumerate(hs.split(",")):
        S.add(Point(index, int(h)))

    H = -1
    get_H()
    
    l = RIGTH_LIMIT - LEFT_LIMIT 
    heights = [int(x) for x in hs.split(",")]

    JIndex = -1
    RIndex = -1

    for _ in range(0, j+1):
        get_jet()

    for _ in range(0, r+1):
        get_rock()

    STATES = [] 

def udateNormalizedHeights(new_points):
    global heights

    l = RIGTH_LIMIT - LEFT_LIMIT 

    for i in range(l + 1):
        for p in new_points:
            if p.x == i:
                if p.y > heights[i]: heights[i] = p.y 
    
    # Normalize 
    m = min(heights)
    for i in range(len(heights)):
        heights[i] -= m

def parse_jet_file(path):
    J = []

    with open(path, 'r') as f:
        row = f.read().strip()

    for dir in row:
        J.append(dir)
    return J    

def parse_rock_file(path):
    R = []

    def parse_rock(rock):
        s = set()
        
        lines = rock.split('\n')
        h = len(lines)
        w = len(lines[0])

        y = h - 1
        for line in lines:
            x = 0
            for c in line:
                if c == ROCK_SIMBOL:
                    s.add(Point(x, y))
                x += 1
            y -= 1
        return s

    with open(path, 'r') as f:
        rocks = f.read().strip().split('\n\n')

    for r in rocks:
        rock = Rock(parse_rock(r))
        R.append(rock)    

    return R

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __key(self):
        return (self.x, self.y)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__key() == other.__key()
        return NotImplemented

    def move_to_start_pos(self):
        self.x = self.x + 2
        self.y = self.y + (H + 1) + 3

    def move_to(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        return self
    
    def move_down(self):
        self.y -= 1
        return self

class Rock:
    def __init__(self, points):
        self.points = points

    def __repr__(self):
        return ("[" + ",".join(set(str(p) for p in self.points )) + "]")

    def put_in_start_pos(self):
        for point in self.points:
            point.move_to_start_pos()
        return self

    def move_to(self, dir):
        delta_x = 1
        if dir == LEFT_SYBMOL:
            delta_x = -1

        points = self.points

        new_points = set()
        for point in points:
            new_points.add(deepcopy(point).move_to(delta_x, 0))

        is_valid = is_valid_x_move(new_points)
        if is_valid: 
            self.points = new_points
        else:
            self.points = points
        return self
    
    def move_down(self):
        points = self.points

        new_points = set()
        for point in points:
            new_points.add(deepcopy(point).move_down())

        is_valid = is_valid_y_move(new_points)
        if is_valid: 
            self.points = new_points
        else:
            self.points = points
        return self, not is_valid

def is_valid_x_move(points):
    for point in points:
        x = point.x
        y = point.y 
        if point in S: # stopped rock 
            return False
        if x < LEFT_LIMIT or x > RIGTH_LIMIT: # walls
            return False
    return True

def is_valid_y_move(points):
    for point in points:
        x = point.x
        y = point.y 
        if point in S: # stopped rock
            return False
        if x < LEFT_LIMIT or x > RIGTH_LIMIT: # walls # TODO: remove if statement
            return False
        if y < 0:
            return False
    return True

def update_H(s):
    # assigns H the highest y-value among the points in S
    global H
    for p in s:
        y = p.y
        if y > H:
            H = y

def get_H():
    # assigns H the highest y-value among the points in S
    global H
    for p in S:
        y = p.y
        if y > H:
            H = y

def print_matrix(s):  
    y_max = 0
    for p in s:
        y = p.y
        if y > y_max:
            y_max = y
    yh = max(y_max, H+3)

    m = []
    for h in range(yh, -1, -1):
        row = ""
        for r in range(RIGTH_LIMIT + 1):
            # print((r,h))
            if Point(r,h) in s:
                row += ROCK_SIMBOL
            else:
                row += NO_ROCK_SYMBOL
        m.append(row)
    print(*m, sep='\n')
    print()

if __name__ == "__main__":
    main()