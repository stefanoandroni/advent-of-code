
import re

INPUT_FILE_PATH = '../data/input.txt'

ROOT_NODE_END = 'A'
DEST_NODE_END = 'Z'

LEFT = 'L'
RIGHT = 'R'


def main():
    global I, N
    # I: (instructions) list of instructions, I[i]∈{R,L}
    # N: (nodes) dict of key=node value=(left_child_node, right_child_node)
    I, N = parse_input_file() 
    
    current_nodes = get_root_nodes()

    steps = 0
    while(not all(current_node.endswith(DEST_NODE_END) for current_node in current_nodes)):
        steps += 1

        next_move = I.pop(0)
        I.append(next_move)

        current_nodes = [get_next_node(current_node, next_move) for current_node in current_nodes]

    # Part 2
    print(steps)

def get_root_nodes():
    return [node for node in N.keys() if node.endswith(ROOT_NODE_END)]


def get_next_node(current_node, next_move):
    index = 0 if next_move == LEFT else 1
    return N[current_node][index]


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        first_line = f.readline()
        file = f.read()

    regex = re.compile('[LR]+')
    match = re.match(regex, first_line)
    instructions = list(match[0])

    regex = re.compile('(\w{3})\s=\s\((\w{3}), (\w{3})\)')
    matches = re.findall(regex, file)

    nodes = {}
    for match in matches:
        nodes[match[0]] = (match[1], match[2])
        
    return instructions, nodes


if __name__ == "__main__":
    main()