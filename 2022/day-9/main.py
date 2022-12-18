from math import sqrt

# TODO: work with vector!

INPUT_FILE_PATH = 'data/input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        global tail_pos_list
        tail_pos_list = []

        moves = get_moves_from_file(f)
        # print(moves)
        
        starting_pos = [0,0]
        head_pos = starting_pos.copy()
        tail_pos = starting_pos.copy()

        for move in moves:
            head_pos, tail_pos = make_move(head_pos, tail_pos, move) 

        tail_pos_set = {tuple(x) for x in tail_pos_list}
        print(len(tail_pos_set)) # <Part 1>

def make_move(head_pos, tail_pos, move):
    dir = move[0]
    steps = move[1]

    for i in range(steps):
        head_pos, tail_pos = make_one_step_move(head_pos, tail_pos, dir)
        tail_pos_list.append(tail_pos)  

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

    if not is_adjacent(head_pos, tail_pos): # update tail_pos
        tail_pos = update_tail_pos(head_pos, tail_pos)

    return head_pos, tail_pos

def update_tail_pos(head_pos, tail_pos):
    x1, y1 = head_pos
    x2, y2 = tail_pos

    y_dif = y2 - y1
    if y_dif != 0:
        if y_dif > 0:
            y2 -= 1
        else: # y_dif < 0
            y2 += 1
    
    x_dif = x2 - x1
    if x_dif != 0:
        if x_dif > 0:
            x2 -= 1
        else: # x_dif < 0
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

if __name__ == "__main__":
    main()