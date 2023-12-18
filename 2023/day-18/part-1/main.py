
import re


INPUT_FILE_PATH = '../data/test-input.txt'

DIRS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def main():
    DP = parse_input_file() # DP: (dig plan) list of (dir, steps, color) tuples 

    # vertices: list of (r,c) vertices of polygon
    # edge_cells: list of ((r, c), color) cells along the border of polygon
    vertices, edge_cells = get_edge_cells(DP) 

    # Pick's theorem 
    #   i = A - b / 2 + 1
    #       i: the number of integer points interior to the polygon     [?]
    #       A: polygon's area                                           [with Shoelace theorem]
    #       b: number of integer points on its boundary                 [len(boundary_cells)]
    A = get_shoelace_area(vertices)
    b = len(edge_cells)
    interior_cells_length = int(A - b / 2 + 1)
    
    # Part 1
    print(interior_cells_length + len(edge_cells))
    

def get_edge_cells(dig_plan):

    current_cell = ((0, 0), None) 
    edge_cells = set()
    vertices = []
    
    while dig_plan:
        dir, steps, color = dig_plan.pop(0)
        rd, cd = DIRS[dir] # rd: row direction, cd: column direction
        for _ in range(steps):
            ((cr, cc), _) = current_cell # cr: current cell row, cc: current cell column
            current_cell = ((cr + rd, cc + cd), color)
            edge_cells.add(current_cell)
        vertices.append((current_cell[0][0], current_cell[0][1]))

    return vertices, edge_cells


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
        dig_plan.append((match[0], int(match[1]), match[2]))

    return dig_plan


if __name__ == "__main__":
    main()
