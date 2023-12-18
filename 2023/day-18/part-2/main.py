
import re


INPUT_FILE_PATH = '../data/test-input.txt'

HEX_TO_DIR = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U'
}

DIRS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def main():
    DP = parse_input_file() # DP: (dig plan) list of (dir, steps) tuples 

    # vertices: list of (r,c) vertices of polygon
    # n_edge_cells: number of cells along the border of polygon
    vertices, n_edge_cells = simulate_path(DP) 

    # Pick's theorem 
    #   i = A - b / 2 + 1
    #       i: the number of integer points interior to the polygon     [?]
    #       A: polygon's area                                           [with Shoelace theorem]
    #       b: number of integer points on its boundary                 [n_edge_cells]
    A = int(get_shoelace_area(vertices))
    b = n_edge_cells
    interior_cells_length = A - (b // 2) + 1
    
    # Part 2
    print(interior_cells_length + n_edge_cells)


def simulate_path(dig_plan):

    current_vertex = (0, 0) 
    n_edge_cells = 0
    vertices = []
    
    while dig_plan:
        dir, steps = dig_plan.pop(0)
        
        rd, cd = DIRS[dir] # rd: row direction, cd: column direction

        # Update current_vertex (with next vertex)
        (cr, cc) = current_vertex
        current_vertex = (cr + rd * steps, cc + cd * steps)

        # Update n_edge_cells
        n_edge_cells += steps

        vertices.append((current_vertex[0], current_vertex[1]))

    return vertices, n_edge_cells


def get_shoelace_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    regex = re.compile('([RLUD])\s(\d+) \(#(\w{6})\)')
    matches = re.findall(regex, file)

    dig_plan = []

    for match in matches:
        dir, steps = parse_hex(match[2])
        dig_plan.append((dir, steps))

    return dig_plan


def parse_hex(s):
    steps = int(s[:-1], 16)
    dir = HEX_TO_DIR[int(s[-1], 16)]
    return dir, steps


if __name__ == "__main__":
    main()
