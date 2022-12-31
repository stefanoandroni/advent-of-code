INPUT_FILE_PATH = '../data/input.txt'

KEY = 811_589_153
TIMES = 10

X_C = 1_000
Y_C = 2_000
Z_C = 3_000

def main():
    global L

    L = [(x * KEY, i) for i, x in enumerate(parse_file(INPUT_FILE_PATH))] # L: list of tuple (num, index)
    
    R = mixing(L) # R: resulting mixed list of tuple (num, index)

    C = get_coordinates(R) # C list of 3 int (3 coordinates)

    print(sum(C)) # <Part 2>

def mixing(L):
    M = L.copy()

    for _ in range(TIMES):
        for i in range(len(M)):
            # Pop tuple from list
            index = L.index(M[i])
            L.pop(index)
            # Insert in list tuple (updated_num, index)
            L.insert((index + M[i][0]) % len(L), M[i])

    return L

def get_coordinates(L):

    def get_coordinate(positions):
        for index, x in enumerate(L):
            if x[0] == 0:
                zero_pos_index = index
                break
        return L[(zero_pos_index + positions) % len(L)][0]

    x = get_coordinate(X_C)
    y = get_coordinate(Y_C)
    z = get_coordinate(Z_C)

    return [x, y, z]

def parse_file(path):
    L = []
    with open(INPUT_FILE_PATH, 'r') as f:
        L = [int(x) for x in f.read().strip().split('\n')]
    return L

if __name__ == "__main__":
    main()