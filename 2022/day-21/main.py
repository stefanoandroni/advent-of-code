# TODO: code refactoring

from collections import deque
import re

INPUT_FILE_PATH = 'data/input.txt'

ROOT_ID = 'root'

def main():
    global N, NI
    N, root, NI = parse_file(INPUT_FILE_PATH) # N: list of nodes obj (nodes of the graph) # root: node root obj # NI: useful for getting the position of the node object in list N from the name (BAD!)
    root_value = get_value(root)
    print(root_value) # <Part 1>

def get_value(node):
    return calculate_number_dfs(node)

def calculate_number_dfs(node):
    
    # CB
    if node.number:
         return node.number

    # Very bad implementation
    match node.operation:
        case '+': 
            return calculate_number_dfs(N[NI.index(node.childs[0])]) + calculate_number_dfs(N[NI.index(node.childs[1])])
        case '-': 
            return calculate_number_dfs(N[NI.index(node.childs[0])]) - calculate_number_dfs(N[NI.index(node.childs[1])])
        case '*':
            return calculate_number_dfs(N[NI.index(node.childs[0])]) * calculate_number_dfs(N[NI.index(node.childs[1])])
        case '/':
            return calculate_number_dfs(N[NI.index(node.childs[0])]) / calculate_number_dfs(N[NI.index(node.childs[1])])

def parse_file(path):
    N = []
    NI = []

    with open(path, 'r') as f:
        file = f.read().strip()

    lines = file.split('\n')

    for line in lines:
        node = Node(line)
        if node.id == ROOT_ID:
            root = node
        N.append(node)
        NI.append(node.id)
        
    return N, root, NI

class Node():

    def __init__(self, textual):
        id = operation = number = None
        id, other = [x.strip() for x in textual.split(":")]
        childs = []
        if other.isnumeric():
            number = int(other)
        else:
            operation = other.split(" ")[1]
            childs = re.split('[\W,]+', other)
        self.id = id
        self.number = number
        self.operation = operation
        self.childs = childs

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return self.__repr__()
    
    def get_childs(self):
        C = set()
        for node in N:
            if node.id in self.childs:
                C.add(node)
        return C
    
    def is_solved(self):
        if self.number:
            return True
        return False 

if __name__ == "__main__":
    main()