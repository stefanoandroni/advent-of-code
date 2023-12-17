
from collections import deque

# NOTE: (BFS) bad sol (TODO: use a priority queue!!), bad coding

INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    global M, L
    M, L = parse_input_file() 

    rs, cs = source = (0, 0)
    rd, cd = dest = (L - 1, L - 1)

    s1 = ((rs, cs + 1), ((0, 1), 1), M[rs][cs + 1], ((rs, cs + 1),))
    s2 = ((rs + 1, cs), ((1, 0), 1), M[rs + 1][cs], ((rs + 1, cs),))

    queue = deque()
    queue.append(s1)
    queue.append(s2)

    cache = dict()

    min_val = None
    while queue:
        ((r, c), ((dir_r, dir_c), n_dir), heat_loss, visited) = s = queue.popleft()

        # Optimizations
        if (r, c, dir_r, dir_c) in cache:
            if  min(filter(lambda x: x is not None, cache[(r, c, dir_r, dir_c)][0:n_dir]), default=float('inf')) < heat_loss:
                continue
            else:
                cache[(r, c, dir_r, dir_c)][n_dir - 1] = heat_loss
        else:
            cache[(r, c, dir_r, dir_c)] = [None, None, None]
            cache[(r, c, dir_r, dir_c)][n_dir - 1] = heat_loss
        
        # Update min_val
        if r == rd and c == cd:
            if not min_val:
                min_val = heat_loss
            elif heat_loss < min_val:
                min_val = heat_loss

        # Get next states
        next_states = get_next_states(s)
        for state in next_states:
            queue.append(state)
    # Part 1
    print(min_val)


def get_next_states(state):
    next_states = set()
    ((r, c), ((dir_r, dir_c), n_dir), heat_loss, visited) = state

    # Same dir
    if n_dir < 3 and in_matrix_limit(r + dir_r, c + dir_c) and (r + dir_r, c + dir_c) not in visited:
        next_states.add(((r + dir_r, c + dir_c), ((dir_r, dir_c), n_dir + 1), heat_loss + M[r + dir_r][c + dir_c], visited + ((r + dir_r, c + dir_c),)))
    # Left/Right
    if dir_r == 0:
        if in_matrix_limit(r + 1, c) and (r + 1, c) not in visited:
            next_states.add(((r + 1, c), ((1, 0), 1), heat_loss + M[r + 1][c], visited + ((r + 1, c),)))
        if in_matrix_limit(r - 1, c) and (r - 1, c) not in visited:
            next_states.add(((r - 1, c), ((-1, 0), 1), heat_loss + M[r - 1][c], visited + ((r - 1, c),)))
    else: # dir_c == 0
        if in_matrix_limit(r, c + 1) and (r, c + 1) not in visited:
            next_states.add(((r, c + 1), ((0, 1), 1), heat_loss + M[r][c + 1], visited + ((r, c + 1),)))
        if in_matrix_limit(r, c - 1) and (r, c - 1) not in visited:
            next_states.add(((r, c - 1), ((0, -1), 1), heat_loss + M[r][c - 1], visited + ((r, c - 1),)))
    return next_states


def in_matrix_limit(r, c):
    if r < 0 or r >= L or c < 0 or c >= L:
        return False
    return True


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    matrix = []
    for row in file.split('\n'):
        matrix.append([int(x) for x in list(row)])
    return matrix, len(matrix) 


if __name__ == "__main__":
    main()
