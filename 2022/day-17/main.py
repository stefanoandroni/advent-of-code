INPUT_FILE_PATH_ROCK = 'data/rocks.txt'
INPUT_FILE_PATH_JET = 'data/jet-pattern.txt'

STOP = 2022

LEFT_LIMIT = 0
RIGTH_LIMIT = 6
BOTTOM_LIMIT = 0

ROCK_SIMBOL = '#'
LEFT_SYBMOL = '<'
RIGTH_SYMBOL = '>'

def main():
    global J, R, S # J: jet pattern # R: rocks # S: stopped rocks

    S = set() 

    # Parse files
    R = parse_rock_file(INPUT_FILE_PATH_ROCK)
    J = parse_jet_file(INPUT_FILE_PATH_JET)

    c = 0
    while c <= 2022:
        r = get_rock()
        drop(r)


    # Rock: move to start (y= H + 3, x = 2) # no overflow control
    #       move sx # overflow control
    #       move rg # overflow control
    #       move down # overflow control
    # overflow-> return True o False?

def drop(rock):
    pass

def get_rock(): # infinite queue with list
    r = R.pop(0)
    R.append(r)
    return r

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

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y)

    def __sub__(self, point):
        return self + -point

class Rock:
    def __init__(self, points):
        self.points = points

    def __repr__(self):
        return ("[" + ",".join(set(str(p) for p in self.points )) + "]")


if __name__ == "__main__":
    main()