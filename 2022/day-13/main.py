import ast

INPUT_FILE_PATH = 'data/input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()
    pairs = file.split('\n\n')

    S = []

    for index, pair in enumerate(pairs):
        p1, p2 = [ast.literal_eval(p) for p in pair.split('\n')]
        if not compare(p1, p2) == False:
            S.append(index + 1)

    # print(S)
    print(sum(S)) # <Part 1>

def compare(left, rigth):

    # both values are integers
    if isinstance(left, int) and isinstance(rigth, int):
        if left < rigth: 
            return True
        elif left > rigth:
            return False
        return None

    # both values are lists
    if isinstance(left, list) and isinstance(rigth, list):
        i = 0

        while i < len(left) and i < len(rigth):
            c = compare(left[i], rigth[i])
            if c == True:
                return True
            if c == False:
                return False
            i += 1

        if len(left) < len(rigth):
            return True
        if len(left) > len(rigth):
            return False
        return None

    # exactly one value is an integer
    if isinstance(left, int) and isinstance(rigth, list):
        return compare([left], rigth)

    if isinstance(left, list) and isinstance(rigth, int):
        return compare(left, [rigth])

if __name__ == "__main__":
    main()