INPUT_FILE_PATH = 'data/input.txt'

X_C  = 1_000
Y_C  = 2_000
Z_C  = 3_000


def main():
    global N
    L = parse_file(INPUT_FILE_PATH) # L )
    N = len(L)
    R = mixing(L)

def mixing(L):

    def get_list_index(index):
        div = index // N
        r = index % N
        return r + div

    M = L.copy() # M: mixed list
    I = [x for x in range(len(L))] # I[k] = index of k-element of L list in M list

    for i in range(len(I)):
        
        # 1) Get and move number from list
        index = I[i]
        n = M.pop(index)
        new_index = get_list_index(index + n)
        
        if new_index == 0:
            new_index = N - 1

        M.insert(new_index, n)
    
        # 2) Update support array I
        if new_index > index:
                for j in range(0, len(I)):
                    if I[j] in range(index + 1, new_index + 1):
                        I[j] -= 1
        else:
                for j in range(0, len(I)):
                    if I[j] in range(new_index, index):
                        I[j] += 1
        I[i] = new_index

    C = get_coordinates(M)
    print(sum(C)) # <Part 1>

def get_coordinates(M):

    def get_coordinate(positions):
        zero_pos_index = M.index(0)
        tmp1 = positions - (len(M) - zero_pos_index - 1)
        r = tmp1 % len(M)
        return M[r - 1]

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