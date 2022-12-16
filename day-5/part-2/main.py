import re

INPUT_FILE_PATH = '../input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        stacks_body, moves_body = f.read().split("\n\n")
        
        stacks_list = create_stacks(stacks_body)
        # print(stacks_list)

        moves_list = create_moves(moves_body)
        # print(moves_list)

        stacks_movies_applied_list = apply_moves(stacks_list, moves_list)
        # print(stacks_movies_applied_list)
        
        top_items = get_top_items_string(stacks_movies_applied_list)
        print(top_items) # Part 2

def get_top_items_string(stacks_list):
    top_items_string = ""
    for stack in stacks_list:
        top_items_string += stack[-1]
    return top_items_string

def apply_move(stacks_list, move): # only method changed from part-1
    popped_items = []
    for i in range(move['move']):
        popped_item = stacks_list[move['from'] - 1].pop()
        popped_items.append(popped_item)
    popped_items.reverse()
    stacks_list[move['to'] - 1].extend(popped_items)
    return stacks_list

def apply_moves(stacks_list, moves_list):
    for move in moves_list:
        moves_list = apply_move(stacks_list, move)
    return stacks_list

def create_moves(moves_body):
    list = []
    for line in moves_body.split("\n"):
        line_without_spaces = line.replace(" ", "")
        tmp_list = re.split("move|from|to", line_without_spaces)
        tmp_list.pop(0)

        obj = {}
        obj['move'] = int(tmp_list[0])
        obj['from'] = int(tmp_list[1])
        obj['to'] = int(tmp_list[2])
        list.append(obj)

    return list

def create_stacks(stacks_body):
    stacks_body_list = stacks_body.split("\n")
    stacks_body_list.reverse()

    first_row = stacks_body_list.pop(0)
    n_stacks = len(first_row.split())

    stacks_list = [[] for i in range(n_stacks)]        
    for line in stacks_body_list:
        stacks_index = 0
        for i in range(1, len(line), 4):
            if line[i] != " ":
                stacks_list[stacks_index].append(line[i])
            stacks_index += 1
    return stacks_list

if __name__ == "__main__":
    main()