
from collections import deque, defaultdict


INPUT_FILE_PATH = '../data/test-input.txt'

DIRS = {(0, 1), (0, -1), (-1, 0), (1, 0)}

# SYMBOLS
PATH_SYMB = "."
FOREST_SYMB = "#"


def main():
    global M, S, D
    # M: matrix map
    # S: (r, c) of source tile
    # D: (r, c) of destination tile
    M, S, D = parse_input_file() 

    '''
    GRAPH
        G = (V, E)
        V = split nodes (tiles that offer alternative paths)
        E = v1 x v2 -> weight (weight represents the length of the longest path from v1 to v2)
        - direct graph
    STEPS
        (1) Get graph 
        (2) Find maximum weight path
    '''

    # (1) Get graph
    graph = defaultdict(lambda: defaultdict(int))

    # state = (current_tile:tuple, previous_node:tuple, distance_from_previous_node:int, visited_tiles:set)
    s0 = (S, S, 0, {S})

    queue = deque()
    queue.append(s0)

    # TODO: OPT
    while queue:
        current_tile, previous_node, distance_from_previous_node, visited_tiles = queue.pop()
        r, c = current_tile

        # Get next tiles
        next_tiles = {tile for tile in get_adjacent_path_cells(r, c) if tile not in visited_tiles}

        # Update graph dict if current tile is a graph node (a split node) or destination node
        if len(next_tiles) > 1 or current_tile == D:
            # print(previous_node, "to", current_tile, "in", distance_from_previous_node)
            # Update Graph
            graph[previous_node][current_tile] = max(graph[previous_node][current_tile], distance_from_previous_node)

            # Update State
            distance_from_previous_node = 0
            previous_node = current_tile

        # Append new states to queue
        for tile in next_tiles:
            queue.append((tile, previous_node, distance_from_previous_node + 1, visited_tiles | {tile}))

    # VISUALIZATION (https://graphonline.ru/en/create_graph_by_edge_list)
    # for source_node, dests in graph.items():
    #     for dest_node, weight in dests.items():
    #         print(str(source_node) + "-(" + str(weight) + ")>" + str(dest_node))

    
    # (2) Find maximum weight path
    print(max_weight_path(graph, S, D))


def max_weight_path(graph, root_node, specific_node):
    
    def dfs(node, visited):
        if node == specific_node:
            return 0

        visited.add(node)
        max_path_weight = float('-inf')

        if node in graph:
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    path_weight = dfs(neighbor, visited)
                    if path_weight != float('-inf'):
                        max_path_weight = max(max_path_weight, path_weight + weight)

        visited.remove(node)
        return max_path_weight

    return dfs(root_node, set())


def get_adjacent_path_cells(r, c):
    adjacent_cells = set()

    for r_dir, c_dir in DIRS:
        r_new, c_new = r + r_dir, c + c_dir
        if r_new >= 0 and r_new < len(M) and c_new >= 0 and c_new < len(M[0]):
            if M[r_new][c_new] != FOREST_SYMB:
                adjacent_cells.add((r_new, c_new))
    
    return adjacent_cells


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
        
    map = [list(line) for line in file.split('\n')]

    src = (0, map[0].index(PATH_SYMB))
    dest = (len(map) - 1, map[len(map) - 1].index(PATH_SYMB))

    return map, src, dest            


if __name__ == "__main__":
    main()
