
INPUT_FILE_PATH = '../data/test-input.txt'

# COORDINATES: adjacent delta coordinates
COORDINATES = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)] 

def main():
    # L: square matrix's dimension (LxL)
    # N: (numbers) list of (number, (x,y)) where (x,y) are the coordinates of of the leftmost digit of the number
    # S: (symbols) list of (x,y) where (x,y) are the coordinates of a symbol
    L, N, S = parse_input_file() 

    NAS = get_numbers_adjacent_to_symbol(N, S, L)

    # Part 1
    print(sum(NAS))

def get_numbers_adjacent_to_symbol(N, S):
    out = []
    for number in N:
        if is_adjacent_to_symbol(number, S):
            n, _ = number
            out.append(n)
    return out

def is_adjacent_to_symbol(number, S):
    n, coord  = number
    xn, yn = coord

    for xs, ys in S:
        for xc, yc in COORDINATES:
            xsc = xs + xc
            ysc = ys + yc
            for i in range(len(str(n))):
                #if (is_within_matrix((x,y)):) # TODO: Check if in matrix limits
                if (xsc, ysc) == (xn + i, yn): 
                    return True
    return False

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    
    L = len(lines)
    S = []
    N = []

    # NOTE: bad coding
    # TODO: improve
    for y, line in enumerate(lines):
        x = 0
        while x < L:
            val = line[x]
            if (is_symbol(val)):
                S.append((x, y))
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
    return L, N, S

def is_period(val):
    return val == '.'

def is_digit(val):
    return str(val).isdigit()

def is_symbol(val):
    return not(is_digit(val) or is_period(val))

if __name__ == "__main__":
    main()