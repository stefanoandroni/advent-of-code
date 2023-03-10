# Approach: keep in memory during execution each number paired to its position in the array (list of tuples (num, index))

INPUT_FILE_PATH = '../data/test-input.txt'

X_C = 1_000
Y_C = 2_000
Z_C = 3_000

KEY = 811_589_153
TIMES = 10

def main():
    global L

    L = [(x * KEY, i) for i, x in enumerate(parse_file(INPUT_FILE_PATH))] # L: list of tuple (num, index)
    R = mixing(L) # R: resulting mixed list of tuple (num, index)
    C = get_coordinates(R) # C: list of 3 int (3 coordinates)

    print(sum(C)) # <Part 2>

def mixing(L):
    M = L.copy()

    for _ in range(TIMES):
        for i in range(len(M)):
            # Pop tuple from list (find the corresponding index and pop it)
            index = L.index(M[i])
            L.pop(index)
            # Insert tuple in list (updated_num, index)
            L.insert((index + M[i][0]) % len(L), M[i])

    return L

def get_coordinates(L):

    def get_coordinate(positions):
        for index, x in enumerate(L):
            if x[0] == 0: # item 0 found
                return L[(index + positions) % len(L)][0]
        
    x = get_coordinate(X_C)
    y = get_coordinate(Y_C)
    z = get_coordinate(Z_C)

    return [x, y, z]

def parse_file(path):
    with open(path, 'r') as f:
        file = f.read().strip()
    L = [int(x) for x in file.split('\n')]
    return L

if __name__ == "__main__":
    main()