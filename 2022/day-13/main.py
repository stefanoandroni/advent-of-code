import ast
from functools import cmp_to_key

INPUT_FILE_PATH = 'data/test-input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()
    
    # Part 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    pairs = file.split('\n\n')
    S = []
    for index, pair in enumerate(pairs):
        p1, p2 = [ast.literal_eval(p) for p in pair.split('\n')]
        if compare(p1, p2) in {-1, 0}:
            S.append(index + 1)

    # print(S)
    print(sum(S)) # <Part 1>
    
    # Part 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    pairs = [ast.literal_eval(p) for p in file.replace('\n\n', '\n').split('\n')]
    pairs.append([[2]])
    pairs.append([[6]])

    pairs = sorted(pairs, key = cmp_to_key(lambda p1, p2: compare(p1, p2)))
    # print(*pairs, sep='\n')
   
    d_p1 = pairs.index([[2]]) + 1
    d_p2 = pairs.index([[6]]) + 1
    d_key = d_p1 * d_p2
    print(d_key) # <Part 2>

def compare(left, rigth):
    # both values are integers
    if isinstance(left, int) and isinstance(rigth, int):
        if left < rigth: 
            return -1
        elif left > rigth:
            return 1
        return 0
    # both values are lists
    if isinstance(left, list) and isinstance(rigth, list):
        i = 0
        while i < len(left) and i < len(rigth):
            c = compare(left[i], rigth[i])
            if c == -1:
                return -1
            if c == 1:
                return 1
            i += 1
        if len(left) < len(rigth):
            return -1
        if len(left) > len(rigth):
            return 1
        return 0
    # exactly one value is an integer
    if isinstance(left, int) and isinstance(rigth, list):
        return compare([left], rigth)
    # exactly one value is an integer
    if isinstance(left, list) and isinstance(rigth, int):
        return compare(left, [rigth])

if __name__ == "__main__":
    main()