
from heapq import heappush, heappop

INPUT_FILE_PATH = '../data/test-input.txt'

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def main():
    global M, L
    M, L = parse_input_file() # M: square matrix; L: square matrix side length

    S = (0, 0) # S: source cell
    D = (L - 1, L - 1) # D: destination cell

    s0_r, s0_c = S

    # Initial states
    # state => (heat_loss, (r, c), ((r_dir, c_dir), n_dir))
    s1 = (M[s0_r][s0_c + 1], (s0_r, s0_c + 1), ((0, 1), 1))
    s2 = (M[s0_r + 1][s0_c], (s0_r + 1, s0_c), ((1, 0), 1))

    visited = set()

    queue = []
    heappush(queue, s1)
    heappush(queue, s2)

    while queue:
        (heat_loss, (r, c), ((r_dir, c_dir), n_dir)) = s = heappop(queue)

        # Destination cell
        if (r, c) == D:
            # Part 1
            print(heat_loss)
            break

        # Visited state
        if ((r, c), ((r_dir, c_dir), n_dir)) in visited:
            continue

        visited.add(((r, c), ((r_dir, c_dir), n_dir)))

        # (1) Same dir
        if n_dir < 3:
            nr = r + r_dir
            nc = c + c_dir
            if in_matrix_limit(nr, nc):
                heappush(queue, (heat_loss + M[nr][nc], (nr, nc), ((r_dir, c_dir), n_dir + 1)))
             
        # (2) Left and Right dirs
        for nr_dir, nc_dir in DIRS:
            if (nr_dir, nc_dir) != (r_dir, c_dir) and (nr_dir, nc_dir) != (-r_dir, -c_dir):
                nr = r + nr_dir
                nc = c + nc_dir
                if in_matrix_limit(nr, nc):
                    heappush(queue, (heat_loss + M[nr][nc], (nr, nc), ((nr_dir, nc_dir), 1)))


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
