
from collections import deque


INPUT_FILE_PATH = 'data/input.txt'


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

DIR_TO_COORD = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0)
}

def main():
    global L, visited_states
    matrix = parse_input_file() # matrix[y][x] ∈ {.,|,-,/,\}
    L = len(matrix)

    visited_tiles = set() # set of visited tiles (x, y)
    visited_states = set() # set of visited states ((x, y), dir)

    s0 = ((0, 0), RIGHT) # initial state

    queue = deque()
    queue.append(s0)

    while queue:
        s = queue.popleft()

        if (not is_valid(s)):
            continue

        (x, y), dir = s
        visited_states.add(s)
        visited_tiles.add((x, y))

        symbol = matrix[y][x]

        # NOTE: bad
        match symbol:
            case '.':
                queue.append(next_state(s, dir))
            case '\\':
                match dir:
                    case 'down':
                        queue.append(next_state(s, RIGHT))
                    case 'up':
                        queue.append(next_state(s, LEFT))
                    case 'left':
                        queue.append(next_state(s, UP))
                    case 'right':
                        queue.append(next_state(s, DOWN))
            case '/':
                match dir:
                    case 'down':
                        queue.append(next_state(s, LEFT))
                    case 'up':
                        queue.append(next_state(s, RIGHT))
                    case 'left':
                        queue.append(next_state(s, DOWN))
                    case 'right':
                        queue.append(next_state(s, UP))
            case '-':
                match dir:
                    case 'left' | 'right':
                        queue.append(next_state(s, dir))
                    case 'up' | 'down':
                        queue.append(next_state(s, RIGHT))
                        queue.append(next_state(s, LEFT))
            case '|':
                match dir:
                    case 'up' | 'down':
                        queue.append(next_state(s, dir))
                    case 'left' | 'right':
                        queue.append(next_state(s, UP))
                        queue.append(next_state(s, DOWN))

    # Part 1
    print(len(visited_tiles))


def next_state(current_state, dir):
    (x, y), _ = current_state
    xd, yd = DIR_TO_COORD[dir]
    return ((x + xd, y + yd), dir)


def is_valid(state): 
    '''
        returns True iff (x,y) in matrix limit && state not in visited_states
    '''
    (x, y), _ = state
    if x < 0 or y < 0 or x >= L or y >= L:
        return False
    if state in visited_states:
        return False
    return True


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    matrix = []
    for y, line in enumerate(file.split('\n')):
        matrix_y = []
        for symbol in list(line):
            matrix_y.append(symbol)  
        matrix.append(matrix_y)
    
    return matrix


if __name__ == "__main__":
    main()