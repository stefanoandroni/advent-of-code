#  Q? Count the number of sides of each cube that are not immediately connected to another cube.
INPUT_FILE_PATH = 'data/input.txt'

def main():
    # Parse file
    C = parse_cubes(INPUT_FILE_PATH)
    # Lamda function te get all cube's sides
    sides = lambda x, y, z: {(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)}

    # Part 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # S = []
    # for c in C:
    #     for s in sides(*c):
    #         if s not in C:
    #             S.append(s)

    free_sides = [s for c in C for s in sides(*c) if s not in C]
    print(len(free_sides)) # <Part 1>

    # Part 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




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