'''
    IN PROGRESS
'''
INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    global settled_bricks

    B = parse_input_file() # B: (bricks) ordered by

    settled_bricks = set()

    while B:
       
        brick = B.pop(0)

        can_move = True
        while can_move:
            can_move, brick = move_one_step_down(brick)
        settled_bricks.append(brick)
            
    print(brick)

    # save upper z value of brick

def move_one_step_down(brick):
    (x, y, z), (dx, dy, dz) = brick
    
    if (z == 1):
        settled_bricks.add(((x, y, z), (dx, dy, dz)))
        return False, brick
    
    for ((xb, yb, zb), (dbx, dby, dbz)) in settled_bricks:
        M

    

    

def get_cubes(start, direction):
    x, y, z = start
    dx, dy, dz = direction

    if dx == 0 and dy == 0 and dz == 0:
        # No change in any direction
        return [start]
    
    # Identify the non-zero component
    if dx != 0:
        tuples = [(x + i, y, z) for i in range(dx + 1)]
    elif dy != 0:
        tuples = [(x, y + i, z) for i in range(dy + 1)]
    elif dz != 0:
        tuples = [(x, y, z + i) for i in range(dz + 1)]

    return tuples


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    bricks = []
    for line in file.splitlines():
        coords1, coords2 = line.split('~')
        x1, y1, z1 = map(int, coords1.split(','))
        x2, y2, z2 = map(int, coords2.split(','))
        bricks.append(((x1, y1, z1), (x2 - x1, y2 - y1, z2 - z1)))
    # ASSERTION: z1 <= z2 for each brick in bricks

    # Sort asc by z1
    bricks = sorted(bricks, key=lambda brick: brick[0][2])

    return bricks



if __name__ == "__main__":
    main()
