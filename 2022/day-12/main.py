# heightmap of the surrounding area
# a: lowest elevation ... z: highest elevation
# S: current position
# E: best_signal position

# from S to E in few steps as possible
# one step: UP, DOWN, LEFT, RIGTH but elevation(destination_square) <= elevation(current_square) + 1

from collections import deque

INPUT_FILE_PATH = 'data/input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        global matrix

        matrix, starting_node, target_node = get_matrix_from_file(f)
        # print(*matrix, sep='\n')
        # print("starting_pos", starting_pos)
        # print("target_pos", target_pos)

        edges = get_edges(matrix)
        # print(edges)

        min_distance = get_shortest_path_length(starting_node, target_node, edges, 1)
        print(min_distance) # <Part 1>

        min_distance = get_shortest_path_length(starting_node, target_node, edges, 2)
        print(min_distance) # <Part 2>

def get_shortest_path_length(starting_node, target_node, edges, part):
    # (with BFS)
    visited_set = set()
    Q = deque()
    
    if part == 1:
        Q.append((starting_node, 0))
    else:
        for edge_from, edge_to in edges:
            r, c = edge_from
            if matrix[r][c] == ord('a') - ord('a'):
                Q.append((edge_from, 0))
        
    while Q:
        current_node, distance = Q.popleft()
        if current_node not in visited_set:
            visited_set.add(current_node)
            if current_node == target_node:
                return distance
            [Q.append((edge_to, distance + 1)) for edge_from, edge_to in edges if edge_from == current_node]

def get_edges(matrix):
    # Create Direct Graph (Edges list representation)
    edges = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            current_node = (r, c)
            for dir_r, dir_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dest_r = r + dir_r
                dest_c = c + dir_c
                dest_node = (dest_r, dest_c)
                if (is_valid_edge(current_node, dest_node)):
                    edges.add((current_node, dest_node))

    return edges

def is_valid_edge(current_node, dest_node):
    dest_r, dest_c = dest_node
    current_r, current_c = current_node
    if 0 <= dest_r < len(matrix) and 0 <= dest_c < len(matrix[0]):
        if matrix[dest_r][dest_c] <= matrix[current_r][current_c] + 1:
            return True
    return False

def get_matrix_from_file(file):
    matrix = []

    f = file.read().strip()
    lines = f.split('\n')
    for r, line in enumerate(lines):
        row = []
        for c, a in enumerate(line):
            if a == "S":
                current_pos = (r,c)
                a = 'a'
            if a == "E":
                target_pos = (r,c)
                a = 'z'
            row.append(ord(a) - ord('a'))
        matrix.append(row)
    return matrix, current_pos, target_pos

if __name__ == "__main__":
    main()