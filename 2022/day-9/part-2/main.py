from math import sqrt

# TODO: work with vector!

INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        global tail_pos_list
        tail_pos_list = []

        moves = get_moves_from_file(f)
        
        starting_pos = [0,0]
        head_pos = starting_pos.copy()
        tail_pos = [starting_pos.copy() for _ in range(9)]

        for move in moves:
            head_pos, tail_pos = make_move(head_pos, tail_pos, move) 
            # print_matrix(head_pos, tail_pos)

        tail_pos_set = {tuple(x) for x in tail_pos_list}
        # print_visited_matrix(tail_pos_set)
        print(len(tail_pos_set)) # <Part 2>

def make_move(head_pos, tail_pos, move):
    dir = move[0] # direction
    steps = move[1] # steps

    for i in range(steps):
        head_pos, tail_pos = make_one_step_move(head_pos, tail_pos, dir)
        tail_pos_list.append(tail_pos[len(tail_pos)-1]) # (not optimal) added to each step (even when it doesn't change)  
    return head_pos, tail_pos

def make_one_step_move(head_pos, tail_pos, dir):
    match dir:
        case Directions.UP:
            head_pos[0] -= 1
        case Directions.DOWN:
            head_pos[0] += 1
        case Directions.LEFT:
            head_pos[1] -= 1
        case Directions.RIGHT:
            head_pos[1] += 1

    # TODO refactor
    if not is_adjacent(head_pos, tail_pos[0]):
        tail_pos[0] = update_tail_pos(head_pos, tail_pos[0])

        # TODO (?) is the while loop useful? or it would suffice to simply move each Tail to the position of the next Tail in the list
        i = 0
        while i + 1 < len(tail_pos) and not is_adjacent(tail_pos[i], tail_pos[i+1]):
            tail_pos[i+1] = update_tail_pos(tail_pos[i], tail_pos[i+1])
            i += 1

    return head_pos, tail_pos

def update_tail_pos(pos_1, pos_2): #pos_2 -> pos to update
    x1, y1 = pos_1
    x2, y2 = pos_2

    delta_y = y2 - y1
    if delta_y != 0:
        if delta_y > 0:
            y2 -= 1
        else: # delta_y < 0
            y2 += 1
    
    delta_x = x2 - x1
    if delta_x != 0:
        if delta_x > 0:
            x2 -= 1
        else: # delta_x < 0
            x2 += 1

    return [x2, y2]

def is_adjacent(pos1, pos2): # bad function
    x1, y1 = pos1
    x2, y2 = pos2
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance == 1 or distance == 0 or distance == sqrt((1 - 0) ** 2 + (1 - 0) ** 2) 

def get_moves_from_file(file):
    f = file.read().strip()
    return [[x.split(" ")[0], int(x.split(" ")[1])] for x in f.split('\n')]

class Directions:
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'

def print_matrix(head_pos, tail_pos):
    # harcoded matrix
    # works with 'input-test-2.txt' 
    matrix = [ ["." for _ in range(26)] for _ in range(21)]

    # start_pos = [len(matrix) - 1, 0]
    start_pos = [15,11] 

    # axis translation
    head_pos = [head_pos[0] + start_pos[0], head_pos[1] + start_pos[1]]
    tail_pos = [[tail[0] + start_pos[0], tail[1] + start_pos[1]] for tail in tail_pos]

    matrix[start_pos[0]][start_pos[1]] = "s"

    for i, item in reversed(list(enumerate(tail_pos))):
        matrix[item[0]][item[1]] = str(i+1)

    matrix[head_pos[0]][head_pos[1]] = "H"
    
    # print
    print("-" * 30)
    for line in matrix:
        print("".join(line))

def print_visited_matrix(visited_pos_set):
    # harcoded matrix
    # works with 'input-test-2.txt' 
    matrix = [ ["." for _ in range(26)] for _ in range(21)]

    # start_pos = [len(matrix) - 1, 0]
    start_pos = [15,11] 

    for pos in visited_pos_set:
        matrix[pos[0] + start_pos[0]][pos[1] + start_pos[1]] = "#"
    
    matrix[start_pos[0]][start_pos[1]] = "s"

    # print
    print("_" * 30)
    for line in matrix:
        print("".join(line))

if __name__ == "__main__":
    main()