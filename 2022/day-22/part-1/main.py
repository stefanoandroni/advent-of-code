import re
from collections import deque

INPUT_FILE_PATH = '../data/test-input.txt'

R = 'R'
L = 'L'

def main():
    global M
    M, PM, PT, P = parse_file(INPUT_FILE_PATH) # M: matrix map, PT: path turn, PM: path move, P: starting position

    # Starting settings
    p = P # p: starting position
    d = Direction(Direction.RIGHT) # d: starting direction

    while PM:
        # 1) Pop
        pm = PM.popleft()
        if PT:
            pt = PT.popleft()
        else: # (?) strange case (with test-input.txt)
            break

        # 2) Move
        p = move(p, pm, d)
        # 3) Rotate
        d.rotate(pt)

    # print(p)
    print(get_password(p, d)) # <Part 1>

def get_password(p, d):
    r, c = p
    return 1000 * (r + 1) + 4 * (c + 1) + to_number(d)

def move(pos, tiles_number, direction):
    i = 0
    mi = direction.get_dir() # mi: move increase [x, y] in {[1,0], [-1,0], [0,1], [0,-1]}

    while i < tiles_number:
        new_pos = get_consistent_position([pos[0] + mi[0], pos[1] + mi[1]]) # return in matrix limit pos
        
        while M[new_pos[0]][new_pos[1]] == " ":
            new_pos = get_consistent_position([new_pos[0] + mi[0], new_pos[1] + mi[1]])
        
        if M[new_pos[0]][new_pos[1]] == "#":
            break
        
        pos = new_pos
        
        i += 1   

    return pos

def get_consistent_position(position):
    r, c = position
    if r > len(M) - 1:
        r = 0
    elif r < 0:
        r = len(M) - 1
    elif c > len(M[0]) - 1:
        c = 0
    elif c < 0:
        c = len(M[0]) - 1
    return [r, c]

def to_number(dir):
    d = dir.direction
    match d:
        case Direction.UP:
            return 3
        case Direction.LEFT:
            return 2
        case Direction.DOWN:
            return 1
        case Direction.RIGHT:
            return 0

class Direction:
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    
    def __init__(self, direction):
        self.direction = direction
    
    def rotate_left(self):
        self.direction = (self.direction - 1) % 4
    
    def rotate_right(self):
        self.direction = (self.direction + 1) % 4

    def rotate(self, s):
        if s == R:
            self.rotate_right()
        if s == L:
            self.rotate_left()

    def get_dir(self):
        if self.direction == Direction.UP:
            return [1, 0]
        if self.direction == Direction.DOWN:
            return [-1, 0]
        if self.direction == Direction.LEFT:
            return [0, -1]
        if self.direction == Direction.RIGHT:
            return [0, 1]

def parse_file(path):
    with open(path, 'r') as f:
        m, p = f.read().split('\n\n')
    lines = m.split('\n')
    
    # 1) Map
    r_len = max([len(x) for x in lines])
    M = []

    f = False
    for r, line in enumerate(lines):
        R = []
        for c in range(r_len):
            if c > len(line) - 1:
                R.append(" ")
            else:
                R.append(line[c])
                if not f and line[c] == '.':
                    s = c
                    f = True
        M.append(R)

    # 2) Path Turn and Path Move
    split_list = re.findall(r'\d+|\D+', p)
    PM = deque()
    PT = deque()

    for x in split_list:
        if x.isdigit():
            PM.append(int(x))
        else:
            PT.append(x)

    return M, PM, PT, [0, s]

def print_map(map):
    for line in map:
        print("".join(line))

if __name__ == "__main__":
    main()