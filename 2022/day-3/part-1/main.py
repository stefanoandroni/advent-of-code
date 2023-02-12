INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = [x for x in f.read().split("\n")]
    
    half_splitted_list = [half_split_str(x) for x in lines]
    # checkHalfSplittedList(lines, half_splitted_list)
    common_item_list = [get_one_common_char(x[0], x[1]) for x in half_splitted_list]
    priority_common_item_list = [get_priority(x) for x in common_item_list]
    
    # print(get_priority("A"))
    # print(get_priority("Z"))
    # print(get_priority("a"))
    # print(get_priority("z"))

    print(sum(priority_common_item_list)) # <Part 1>

def get_priority(char):
    # a .. z from 1 to 26
    # A .. z from 27 to 52
    if char.isupper():
        return ord(char) - ord("A") + 27
    elif char.islower():
        return ord(char) - ord ("a") + 1

def half_split_str(str):
    return [str[:len(str)//2], str[len(str)//2:]]

def get_one_common_char(str1, str2):
    return list(set(str1)&set(str2))[0]

def checkHalfSplittedList(str_list, half_splitted_list):
    if len(str_list) != len(half_splitted_list):
        raise Exception("Differtent lists length")
    
    for x in range(len(str_list)):
        if str_list[x] != half_splitted_list[x][0] + half_splitted_list[x][1]:
            raise Exception("Differtent str")
    
if __name__ == "__main__":
    main()