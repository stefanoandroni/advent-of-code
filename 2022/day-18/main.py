from collections import deque
from pprint import pprint

#  Q? Count the number of sides of each cube that are not immediately connected to another cube.
INPUT_FILE_PATH = 'data/test-input.txt'

# Lamda function te get all cube's sides
sides = lambda x, y, z: {(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)}

def main():
    
    # Parse file
    C = parse_cubes(INPUT_FILE_PATH)

    # Part 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # S = []
    # for c in C:
    #     for s in sides(*c):
    #         if s not in C:
    #             S.append(s)

    free_sides = [s for c in C for s in sides(*c) if s not in C]
    print(len(free_sides)) # <Part 1>
    
    # Part 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    global L, N, S

    # 1) N: normalized cubes points
    x_max, y_max, z_max  = get_max_coordinates(C.copy())
    x_min, y_min, z_min = get_min_coordinates(C.copy())

    N = set()
    for (x, y, z) in C:
        N.add((x -x_min+1, y-y_min+1, z-z_min+1))

    # 2) S: search space -> all points (normalized cubes points max and min per axis + 1 unit border for axis)
    x_max, y_max, z_max  = get_max_coordinates(N.copy())
    x_min, y_min, z_min = get_min_coordinates(N.copy())

    S = set()
    for x in range(0, x_max + 2):
        for y in range(0, y_max + 2):
            for z in range(0, z_max + 2):
                S.add((x, y, z))

    # 3) L: axis' limit on S - > S ranges with extremes included per axis
    x_max, y_max, z_max  = get_max_coordinates(S.copy())
    x_min, y_min, z_min = get_min_coordinates(S.copy())

    L = {'x': [x_min, x_max], 'y': [y_min, y_max], 'z': [z_min, z_max]}

    # 4) Calulcate # of faces of external surface
    n = calculate_external_surface()
    print(n) # <Part 2>
    
def calculate_external_surface():

    def is_in_search_space(point):
        x, y, z = point
        if x < L['x'][0] or x > L['x'][1]:
            return False
        if y < L['y'][0] or y > L['y'][1]:
            return False
        if z < L['z'][0] or z > L['z'][1]:
            return False
        return True

    queue = deque()
    V = set() # visited points
    count = 0

    s = (0, 0, 0) # starting point
    queue.append(s)

    while queue:
        point = queue.popleft()
        if point not in V:
            V.add(point)

            for p in sides(*point):
                if is_in_search_space(p):
                    if p in N:
                        count += 1
                    else:
                        queue.append(p)

    return count

def get_max_coordinates(C):
    x_max, y_max, z_max = C.pop()
    
    for c in C:
        x, y, z = c
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
        if z > z_max:
            z_max = z

    return x_max, y_max, z_max

def get_min_coordinates(C):
    x_min, y_min, z_min = C.pop()

    for c in C:
        x, y, z = c
        if x < x_min:
            x_min = x
        if y < y_min:
            y_min = y
        if z < z_min:
            z_min = z

    return x_min, y_min, z_min

def parse_cubes(path):
    # Return: set of tuples of type (x1, x2, x3) with integer xi, i in {1, 2, 3}
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')
    
    S = set()
    for line in lines:
        x, y, z = line.split(',')
        S.add((int(x),int(y),int(z)))
        
    return S

if __name__ == "__main__":
    main()