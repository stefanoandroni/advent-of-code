
from itertools import combinations


INPUT_FILE_PATH = 'data/test-input.txt'

GALAXY_SYMBOL = '#'
EMPTY_SPACE_SYMBOL = '.'

EXPANSION_RATE = 1_000_000 # 2 for Part 1


def main():
    I = parse_input_file() # I: (image) matrix

    G = get_galaxies(I) # G: set of galaxies; a galaxy is a (x, y) tuple where x and y are the coordinates for i-galaxy

    EG = get_expanded_galaxies(I, G) # EG: set of expanded galaxies

    galaxies_pairs = list(combinations(EG, 2))

    sum = 0
    for g1, g2 in galaxies_pairs:
        sum += get_shortest_path_length(g1 ,g2)
    
    # Part 1 / Part 2 (Changing EXPANSION_RATE value)
    print(sum)


def get_galaxies(matrix):
    galaxies = set()
    for y, line in enumerate(matrix):
        for x, symbol in enumerate(line):
            if symbol == GALAXY_SYMBOL:
                galaxies.add((x, y))
    return galaxies


def get_expanded_galaxies(matrix, galaxies):
    # Empty rows indexs
    empty_rows_indexs = [i for i, row in enumerate(matrix) if all(element == EMPTY_SPACE_SYMBOL for element in row)] 
    
    # Empty cols indexs
    empty_cols_indexs = []
    for col in range(len(matrix[0])):
        column_elements = [matrix[row][col] for row in range(len(matrix))]
        if all(element == EMPTY_SPACE_SYMBOL for element in column_elements):
            empty_cols_indexs.append(col)
    
    extended_galaxies = set()

    for galaxy in galaxies:
        x, y = galaxy

        nx = len([index for index in empty_cols_indexs if index < x])
        x += (EXPANSION_RATE - 1) * nx

        ny = len([index for index in empty_rows_indexs if index < y])
        y += (EXPANSION_RATE - 1) * ny

        extended_galaxies.add((x, y))

    return extended_galaxies


def get_shortest_path_length(galaxy1, galaxy2):
    x1, y1 = galaxy1
    x2, y2 = galaxy2
    # Manhattan distance
    return abs(x2 - x1) + abs(y2 - y1)


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    lines = file.split('\n')
    image = [list(word) for word in lines]

    return image


if __name__ == "__main__":
    main()
