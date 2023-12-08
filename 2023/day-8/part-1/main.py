
import re

INPUT_FILE_PATH = '../data/input.txt'

ROOT_NODE = 'AAA'
DEST_NODE = 'ZZZ'

LEFT = 'L'
RIGHT = 'R'


def main():
    global I, N
    I, N = parse_input_file() 
    
    current_node = ROOT_NODE
    steps = 0
    while(current_node != DEST_NODE):
        steps += 1
        current_node = get_next_node(current_node)

    # Part 1
    print(steps)


def get_next_node(current_node):
    next_move = I.pop(0)
    I.append(next_move)

    index = 0 if next_move == LEFT else 1

    return N[current_node][index]


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        first_line = f.readline()
        file = f.read()

    regex = re.compile('[LR]+')
    match = re.match(regex, first_line)
    instructions = list(match[0])

    regex = re.compile('([a-zA-Z]{3})\s=\s\(([a-zA-Z]{3}), ([a-zA-Z]{3})\)')
    matches = re.findall(regex, file)

    nodes = {}
    for match in matches:
        nodes[match[0]] = (match[1], match[2])
        
    return instructions, nodes


if __name__ == "__main__":
    main()