
INPUT_FILE_PATH = '../data/test-input.txt'

# COORDINATES: adjacent delta coordinates
COORDINATES = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)] 

def main():
    # L: square matrix's dimension (LxL)
    # N: (numbers) list of (number, (x,y)) where (x,y) are the coordinates of of the leftmost digit of the number
    # A: (asterisks) list of (x,y) where (x,y) are the coordinates of an asterisk
    L, N, A = parse_input_file() 

    # CG: (candidate gears) dictionary where the key represents the coordinates (x,y) of an asterisk, and the value is a list of adjacent numbers to the asterisk
    CG = get_candidate_gears(L, N, A)

    # VG: (valid gears) 
    VG = get_valid_gears(CG)

    # Part 2
    print(sum(value.pop() * value.pop() for value in VG.values()))

def get_valid_gears(candidate_gears):
    return {key: value for key, value in candidate_gears.items() if len(value) == 2}

def get_candidate_gears(L, N, A):
    CG = {}

    for number in N:
        n, coord = number
        adjacent_asterisks_coord = get_ajdacent_asterisks(number, A)
        for adjacent_asterisk_coord in adjacent_asterisks_coord:
            CG.setdefault(adjacent_asterisk_coord, set()).add(n) # TODO: n not unique identifier for numbers (use coord)
    return CG


def get_ajdacent_asterisks(number, A):
    n, coord  = number
    xn, yn = coord
    out = []
    for xs, ys in A:
        for xc, yc in COORDINATES:
            xsc = xs + xc
            ysc = ys + yc
            for i in range(len(str(n))):
                #if (is_within_matrix((x,y)):) # TODO: Check if in matrix limits
                if (xsc, ysc) == (xn + i, yn): 
                    out.append((xs, ys))
    return out

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    
    L = len(lines)
    A = []
    N = []

    # NOTE: bad coding
    # TODO: improve
    for y, line in enumerate(lines):
        x = 0
        while x < L:
            val = line[x]
            if (is_asterisk(val)):
                A.append((x, y))
                x += 1
            elif (is_digit(val)):
                number = ""
                coord = (x, y)
                while x < L and is_digit(line[x]):
                    number += line[x]
                    x += 1
                N.append((int(number), coord))
            else:
                x += 1
    return L, N, A

def is_period(val):
    return val == '.'

def is_digit(val):
    return str(val).isdigit()

def is_asterisk(val):
    return val == '*'

if __name__ == "__main__":
    main()