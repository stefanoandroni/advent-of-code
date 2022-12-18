INPUT_FILE_PATH = '../data/input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        matrix = get_matrix_from_file(f) # data matrix
        # print(*matrix, sep = "\n") 
        l = len(matrix)

        scenic_score_matrix = [[None for _ in range(l)] for _ in range(l)] # scenic score matrix
        # print(*scenic_score_matrix, sep = "\n") 

        for r in range(l):
            for c in range(l):
                scenic_score_matrix[r][c] = get_score(r, c, matrix)
        # print(*scenic_score_matrix, sep = "\n") 

        max_scenic_score = get_max_in_matrix(scenic_score_matrix) # (can be calculated during matrix construction)
        print(max_scenic_score) # <Part 2>

def get_score(r, c, matrix):
    l = len(matrix)
    if r in {0, l-1} or c in {0, l-1}:
        return 0
    
    # score_direction -> viewing_distance
    return (
        get_direction_score(r, c, Directions.LEFT, matrix[r][c], matrix, 0) *
        get_direction_score(r, c, Directions.RIGHT, matrix[r][c], matrix, 0) *
        get_direction_score(r, c, Directions.UP, matrix[r][c], matrix, 0) *
        get_direction_score(r, c, Directions.DOWN, matrix[r][c], matrix, 0)
        )

def get_direction_score(r, c, dir, val, matrix, score):
    l = len(matrix)
    match dir:
        case Directions.UP:
            r = r-1
        case Directions.DOWN:
            r = r+1
        case Directions.LEFT:
            c = c-1
        case Directions.RIGHT:
            c = c+1

    if 0 <= r < l and 0 <= c < l:
        score += 1
        if matrix[r][c] < val:
            return get_direction_score(r, c, dir, val, matrix, score)
        else:
            return score # CB 2
    return score # CB 1

def get_max_in_matrix(matrix):
    l = len(matrix) # square matrix -> l x l
    max_val = 0
    for row in matrix:
        for val in row:
            if val > max_val:
                max_val = val
    return max_val

def get_matrix_from_file(file):
    f = file.read().strip()
    matrix = []
    lines = f.split('\n')
    for line in lines:
        matrix.append([eval(x) for x in list(line)])
    return matrix

class Directions:
    UP = 'u'
    DOWN = 'd'
    LEFT = 'l'
    RIGHT = 'r'

if __name__ == "__main__":
    main()