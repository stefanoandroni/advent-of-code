
INPUT_FILE_PATH = '../input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        str_list = [x for x in f.read().split("\n")]       

        group_list = [[str_list[i], str_list[i+1], str_list[i+2]] for i in range(len(str_list))[::3]]
        group_badge_list = [get_common_item(group[0], group[1], group[2]) for group in group_list]
        
        priority_common_group_list = [get_priority(x) for x in group_badge_list]

        print(sum(priority_common_group_list)) # Part 2

def get_common_item(str1, str2, str3):
    str1_set = set(str1)
    str2_set = set(str2)
    str3_set = set(str3)
    common_items = str1_set.intersection(str2_set, str3_set)
    if len(common_items) == 1:
        return list(common_items)[0]
    raise Exception("More than 1 common item")

def get_priority(char):
    if char.isupper():
        return ord(char) - ord("A") + 27
    elif char.islower():
        return ord(char) - ord ("a") + 1
    
if __name__ == "__main__":
    main()