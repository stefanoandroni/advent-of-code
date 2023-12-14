
INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    # P: (patterns) list of pattern; each pattern is a list of rows;
    # each rows is a list of symbols ∈ {., #} 
    P = parse_input_file() 

    sum = 0
    for pattern in P:
        sum += get_score(pattern)

    # Part 2
    print(sum)


def get_score(p):
    hr_reflection_line_index = get_hr_reflection_line_index(p)

    if hr_reflection_line_index is None:
        vr_reflection_line_index = get_vr_reflection_line_index(p)
        return vr_reflection_line_index + 1

    return (hr_reflection_line_index + 1) * 100


def get_hr_reflection_line_index(pattern):

    hr_reflection_line_index = None
    for index in range(len(pattern) - 1):
        if is_hr_reflection_line(index, index + 1, pattern, True):
            hr_reflection_line_index = index
            break # bad
    
    return hr_reflection_line_index


def get_vr_reflection_line_index(pattern):
    
    vr_reflection_line_index = None
    for index in range(len(pattern[0]) - 1):
        if is_vr_reflection_line(index, index + 1, pattern, True):
            vr_reflection_line_index = index
            break # bad
    
    return vr_reflection_line_index


def is_vr_reflection_line(i1, i2, p, is_smudge_available) -> bool:
    if i1 < 0:
        if is_smudge_available:
            return False # no repairs (exactly 1 repair required)
        else:
            return True
    if i2 > len(p[0]) - 1:
        if is_smudge_available:
            return False # no repairs (exactly 1 repair required)
        else:
            return True
    col1 = [row[i1] for row in p]
    col2 = [row[i2] for row in p]
    diff_number = get_number_of_different_items(col1, col2)

    if diff_number > 1:
        return False
    elif diff_number == 1:
        if is_smudge_available:
            return is_vr_reflection_line(i1 - 1, i2 + 1, p, False)
        else:
            return False
    return is_vr_reflection_line(i1 - 1, i2 + 1, p, is_smudge_available)


def is_hr_reflection_line(i1, i2, p, is_smudge_available) -> bool:
    if i1 < 0:
        if is_smudge_available:
            return False # no repairs (exactly 1 repair required)
        else:
            return True
    if i2 > len(p) - 1:
        if is_smudge_available:
            return False # no repairs (exactly 1 repair required)
        else:
            return True
    
    diff_number = get_number_of_different_items(p[i1], p[i2])
    
    if diff_number > 1:
        return False
    elif diff_number == 1:
        if is_smudge_available:
            return is_hr_reflection_line(i1 - 1, i2 + 1, p, False)
        else:
            return False
    return is_hr_reflection_line(i1 - 1, i2 + 1, p, is_smudge_available)


def get_number_of_different_items(list1, list2):
    return sum(1 for a, b in zip(list1, list2) if a != b)


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    blocks = file.split('\n\n')
    patterns = [[list(line) for line in block.split('\n')] for block in blocks]
    
    return patterns


if __name__ == "__main__":
    main()