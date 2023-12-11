
from itertools import combinations


INPUT_FILE_PATH = 'data/test-input.txt'

GALAXY_SYMBOL = '#'
EMPTY_SPACE_SYMBOL = '.'

EXPANSION_RATE = 2 # 1_000_000 for Part 2


def main():
    I = parse_input_file() # I: (image) matrix

    I = expand_galaxy(I)

    G = get_galaxies(I) # G: list of galaxies; G[i] = (x, y) where (x, y) are the coordinates for i-galaxy

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


def expand_galaxy(matrix):
    # TODO: bad impl
    new_matrix = []

    tmp_row = []
    for row in matrix:
        if (all(element == EMPTY_SPACE_SYMBOL for element in row)):
            for i in range(EXPANSION_RATE - 1):
                tmp_row.append(row)
        tmp_row.append(row)

    for col in range(len(tmp_row[0])):
        column_elements = [tmp_row[row][col] for row in range(len(tmp_row))]
        if (all(element == EMPTY_SPACE_SYMBOL for element in column_elements)):
            for i in range(EXPANSION_RATE - 1):
                new_matrix.append(column_elements)
        new_matrix.append(column_elements)

    # Transpose matrix
    new_matrix = [[row[col] for row in new_matrix] for col in range(len(new_matrix[0]))]
    return new_matrix


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
