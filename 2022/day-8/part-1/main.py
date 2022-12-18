# not optimized (bad implementation) (TODO - recursive - if vis_matrix[r][c]=True and matrix[r][c]<current_val: return True)

INPUT_FILE_PATH = '../data/input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        matrix = get_matrix_from_file(f) # data matrix
        # print(*matrix, sep = "\n") 
        l = len(matrix)

        vis_matrix = [[False for _ in range(l)] for _ in range(l)] # visibility matrix (False by default)
        # print(*vis_matrix, sep = "\n") 

        for r in range(l):
            for c in range(l):
                vis_matrix[r][c] = check_visibility(r, c, matrix)
        # print(*vis_matrix, sep = "\n") 

        visible_count = count_true_in_matrix(vis_matrix)
        print(visible_count) # <Part 1>

def check_visibility(r, c, matrix):
    l = len(matrix)
    if r in {0, l-1} or c in {0, l-1}:
        return True
    
    return (
        check_direction_visibility(r, c, Directions.LEFT, matrix[r][c], matrix) or 
        check_direction_visibility(r, c, Directions.RIGHT, matrix[r][c], matrix) or
        check_direction_visibility(r, c, Directions.UP, matrix[r][c], matrix) or
        check_direction_visibility(r, c, Directions.DOWN, matrix[r][c], matrix)
        )

def check_direction_visibility(r, c, dir, val, matrix):
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
        if matrix[r][c] < val:
            return check_direction_visibility(r, c, dir, val, matrix)
        return False
    else:
        return True # visibility has reached the edge

def count_true_in_matrix(matrix):
    l = len(matrix) # square matrix -> l x l
    count = 0
    for row in range(l):
        for col in range(l):
            if matrix[row][col]:
                count += 1
    return count

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