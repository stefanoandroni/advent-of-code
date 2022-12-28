from copy import deepcopy

INPUT_FILE_PATH_ROCK = '../data/rocks.txt'
INPUT_FILE_PATH_JET = '../data/jet-pattern.txt'

STOP= 2022

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
    global J, R, S, H # J: jet pattern # R: rocks # S: stopped rocks # H: max y index height # M: {x: left/rigth, y: down}
    
    H = -1
    S = set() 

    # Parse files
    R = parse_rock_file(INPUT_FILE_PATH_ROCK)
    J = parse_jet_file(INPUT_FILE_PATH_JET)

    # Simulate
    simulate(STOP) # <Part 1>
    # simulate(STOP_PART_2) # <Part 2> slow

def simulate(stop_num):
    global M
    
    i = 0
    while i < stop_num:
        M = [X_MOVE_SYMBOL, y_MOVE_SYMBOL] 
        drop_rock()
        # print_matrix(S)
        i += 1

    update_H()
    print(H+1) 

def drop_rock():
    update_H()
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

def get_move(): # infinite queue with list
    m = M.pop(0)
    M.append(m)
    return m

def get_rock(): # infinite queue with list
    r = R.pop(0)
    R.append(r)
    return deepcopy(r)

def get_jet(): # infinite queue with list
    j = J.pop(0)
    J.append(j)
    return j

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

def update_H():
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