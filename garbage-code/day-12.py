def get_shortest_path(current_pos, target_pos, matrix):
    return get_shortest_path_recursive(current_pos, target_pos, matrix, 0)

def get_shortest_path_recursive(current_pos, target_pos, matrix, steps):
    rc, cc = current_pos
    rt, ct = target_pos
    
    if rc == rt and cc == ct: 
        return steps
    
    min = -1
    for dir_r, dir_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_r = rc + dir_r
        new_c = cc + dir_c
        new_dest = (new_r, new_c)

        if is_valid_dest(new_dest, current_pos, matrix): # TODO adjuste
            new_path = get_shortest_path_recursive(new_dest, target_pos, matrix, steps + 1)
            if new_path < min:
                min = new_path

    possible_directions = set()
    for dir in {Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT}:
        if is_valid_dest(move(current_pos, dir), current_pos, matrix):
            possible_directions.add(dir)
    
         
def get_shortest_pathS(current_pos, target_pos, matrix, path):
    if current_pos[0] == target_pos[0] and current_pos[1] == target_pos[1]: 
        return path
    print("IN")
    possible_path_list = []
    # UP
    dest_pos = move(current_pos, Directions.UP)
    print("dest_pos", dest_pos)
    if is_valid_dest(dest_pos, current_pos, matrix, path):
        new_path = get_shortest_path(dest_pos, target_pos, matrix, path.copy().append(dest_pos))
        if new_path:
            possible_path_list.append(new_path)

    # DOWN
    print(current_pos)
    dest_pos = move(current_pos, Directions.DOWN)
    print("dest_pos", dest_pos)
    if is_valid_dest(dest_pos, current_pos, matrix, path):
        new_path = get_shortest_path(dest_pos, target_pos, matrix, path.copy().append(dest_pos))
        if new_path:
            possible_path_list.append(new_path)

    # LEFT
    dest_pos = move(current_pos, Directions.LEFT)
    if is_valid_dest(dest_pos, current_pos, matrix, path):
        new_path = get_shortest_path(dest_pos, target_pos, matrix, path.copy().append(dest_pos))
        if new_path:
            possible_path_list.append(new_path)

    # RIGHT
    dest_pos = move(current_pos, Directions.RIGHT)
    if is_valid_dest(dest_pos, current_pos, matrix, path):
        new_path = get_shortest_path(dest_pos, target_pos, matrix, path.copy().append(dest_pos))
        if new_path:
            possible_path_list.append(new_path)
    
    if len(possible_path_list) > 0:
        return (
            min (
                [path for path in possible_path_list if path is not None]
            )
        )
    
    print(possible_path_list)
    return None

def is_valid_dest(dest_pos, current_pos, matrix, path):
    L = len(matrix)
    if dest_pos in path:
        return False
    if dest_pos[0] in {-1, L} or dest_pos[1] in {-1, L}:
        return False
    if ord(matrix[dest_pos[0]][dest_pos[1]]) > ord(matrix[current_pos[0]][current_pos[1]]) + 1:
        return False

    return True

def move(pos, dir):
    match dir:
        case Directions.UP:
            pos[0] = pos[0]-1
        case Directions.DOWN:
            pos[0] = pos[0]+1
        case Directions.LEFT:
            pos[1] = pos[1]-1
        case Directions.RIGHT:
            pos[1] = pos[1]+1
    return pos

def get_matrix_from_file(file):
    matrix = []

    f = file.read().strip()
    lines = f.split('\n')
    for r, line in enumerate(lines):
        row = []
        for c, a in enumerate(line):
            if a == "S":
                current_pos = (r,c)
                a = 'a'
            if a == "E":
                target_pos = (r,c)
                a = 'z'
            row.append(ord(a)-ord('a'))
        matrix.append(row)
    return matrix, current_pos, target_pos

class Directions:
    UP = 'u'
    DOWN = 'd'
    LEFT = 'l'
    RIGHT = 'r'