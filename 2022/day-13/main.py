# pair of packet
# \n
# pair of packet

import ast

# You need to identify how many pairs of packets are in the right order.
INPUT_FILE_PATH = 'data/test-input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()
    pairs = file.split('\n\n')

    right_order_pairs = []
    for index, pair in enumerate(pairs):
        print(index + 1, "---------------------------------------------------------------------------------")
        if is_in_right_order(pair):
            right_order_pairs.append(index + 1)

    print(right_order_pairs)
    print(sum(right_order_pairs)) # <Part 1>

def is_in_right_order(pair):
    pair_1, pair_2 = [ ast.literal_eval(p) for p in pair.split('\n')]
    return is_in_right_order_recursive(pair_1, pair_2)

def is_in_right_order_recursive(pair_1, pair_2):
    left = None
    rigth = None
    print("*****************")
    print("ENTER - pair1, pair2", pair_1, pair_2)
    
    if pair_1 is None and pair_2 is None:
        return True

    # is not None
    if pair_1 is not None:
        if isinstance(pair_1, list):
            if len(pair_1) > 0:
                left = pair_1.pop(0)
            else:
                pair_1 = None
                left = None
        else:
            left = pair_1
            pair_1 = None
    else: # pair_1 is None, pair_2 is not None
        return True
    
    if pair_2 is not None:
        if isinstance(pair_2, list):
            if len(pair_2) > 0:
                rigth = pair_2.pop(0)
            else:
                pair_2 = None
                rigth = None
        else:
            rigth = pair_2
            pair_2 = None
    else: # pair_2 is None, pair_1 is not None
        return False

    print("l", left, "r", rigth)

    if isinstance(left, int) and isinstance(rigth, int): # Both values are integers
        print("Both values are integers")
        if left < rigth: 
            return True
        if left > rigth:
            return False
        return is_in_right_order_recursive(pair_1, pair_2)

    elif isinstance(left, list) and isinstance(rigth, list): # Both values are lists
        print("Both values are lists")
        return all(
            [
                is_in_right_order_recursive(
                    left[x] if x < len(left) else None, rigth[x] if x < len(rigth) else None
                ) for x in range(max(len(left), len(rigth)))
            ]
        ) and is_in_right_order_recursive(pair_1, pair_2) # TODO: keep checking even after a False return in the list (?)
    
    else: # exactly one value is an integer (safe condition (?))
        print("Mixed types")
        if isinstance(left, int):
            pair_2 = rigth
            return is_in_right_order_recursive([left], pair_2)
        else:
            pair_1 = left
            return is_in_right_order_recursive(pair_1, [rigth])
    
if __name__ == "__main__":
    main()