
from itertools import combinations


INPUT_FILE_PATH = 'data/test-input.txt'

GALAXY_SYMBOL = '#'
EMPTY_SPACE_SYMBOL = '.'

EXPANSION_RATE = 2 # 1_000_000 for Part 2

def main():
    I = parse_input_file() # I: (image) matrix

    G = get_galaxies(I) # G: list of galaxies; G[i] = (x, y) where (x, y) are the coordinates for i-galaxy

    EG = get_expanded_galaxies(G) # EG: list of expanded galaxies; G[i] = (x, y) where (x, y) are the coordinates for i-galaxy

    galaxies_pairs = list(combinations(G, 2))

    sum = 0
    for g1, g2 in galaxies_pairs:
        sum += get_shortest_path_length(g1 ,g2)
    
    # Part 1 / Part 2
    print(sum)

def get_galaxies(matrix):
    galaxies = set()
    for y, line in enumerate(matrix):
        for x, symbol in enumerate(line):
            if symbol == GALAXY_SYMBOL:
                galaxies.add((x, y))
    return galaxies


def get_expanded_galaxies(galaxies):
    return
    

def get_shortest_path_length(galaxy1, galaxy2):
    x1, y1 = galaxy1
    x2, y2 = galaxy2

    return abs(x2 - x1) + abs(y2 - y1)

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    lines = file.split('\n')

    # Image
    image = [list(word) for word in lines]

    return image

if __name__ == "__main__":
    main()
