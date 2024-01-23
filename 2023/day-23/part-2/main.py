
from collections import deque


INPUT_FILE_PATH = '../data/test-input.txt'

# SYMBOLS
PATH_SYMB = "."
FOREST_SYMB = "#"
SLOPE_UP_SYMB = "^"
SLOPE_DOWN_SYMB = "v"
SLOPE_LEFT_SYMB = "<"
SLOPE_RIGHT_SYMB = ">"

DIRS = {
    SLOPE_RIGHT_SYMB: (0, 1), 
    SLOPE_LEFT_SYMB: (0, -1), 
    SLOPE_UP_SYMB: (-1, 0),
    SLOPE_DOWN_SYMB: (1, 0)
}


def main():
    global M, S, D
    # M: matrix map
    # S: (r, c) of source tile
    # D: (r, c) of destination tile
    M, S, D = parse_input_file() 

    # dist_map: max distance from source map
    dist_map =  [[0 for _ in range(len(M[0]))] for _ in range(len(M))] #[[None if element == '#' else 0 for element in row] for row in M]

    # state = (current_tile:tuple, distance_from_source:int, visited_tiles:set)
    s0 = (S, 0, set())

    queue = deque()
    queue.append(s0)

    while queue:
        current_tile, distance_from_source, visited_tiles = queue.pop()
        r, c = current_tile
        
        # Update dist_map
        if dist_map[r][c] < distance_from_source + 1:
           dist_map[r][c] = distance_from_source
        #else:
        #   continue
        
        # Get next tiles
        next_tiles = get_next_tiles(current_tile, visited_tiles)

        # Append new states to queue
        for tile in next_tiles:
            queue.append((tile, distance_from_source + 1, visited_tiles | {tile}))

    # Part 2
    print(dist_map[D[0]][D[1]])


def get_next_tiles(current_tile, visited_tiles):
    r, c = current_tile
    next_tiles = set()

    for r_dir, c_dir in DIRS.values():
        r_new, c_new = r + r_dir, c + c_dir
        if r_new >= 0 and r_new < len(M) and c_new >= 0 and c_new < len(M[0]):
            if M[r_new][c_new] != FOREST_SYMB:
                next_tiles.add((r_new, c_new))
    
    return {tile for tile in next_tiles if tile not in visited_tiles}


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
        
    map = [list(line) for line in file.split('\n')]

    src = (0, map[0].index(PATH_SYMB))
    dest = (len(map) - 1, map[len(map) - 1].index(PATH_SYMB))

    return map, src, dest            


if __name__ == "__main__":
    main()
