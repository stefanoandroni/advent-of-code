
import re


INPUT_FILE_PATH = '../data/test-input.txt'

START_WF = 'in'

ACCEPT = 'A'
REJECT = 'R'

GREATER = ">"
LESS = "<"

'''
    IDEA:
        Rule1;                      true_range_r1
        !Rule1 & Rule2              false_range_r1 ∩ true_range_r2
        !Rule1 & !Rule2 & Rule3     false_range_r1 ∩ false_range_r2 ∩ true_range_r3
        ....
'''

def main():
    global WF
    _, WF = parse_input_file()

    rages_dict_0 = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }

    # Part 2
    print(get_accepted_comb_number(rages_dict_0, START_WF))


def calculate_ranges_product(ranges):
    product = 1
    for start, end in ranges.values():
        product *= end - start + 1
    return product


def get_accepted_comb_number(ranges, wf_name):
    # BASE CASE (1)
    if wf_name == REJECT:
        return 0
    # BASE CASE (2)
    if wf_name == ACCEPT: 
        return calculate_ranges_product(ranges)

    rules, default = WF[wf_name] # rules: list of rules; default: default workflow name

    total = 0
    is_condition_impossible = False
    for var, symb, num, target in rules:
        start, end = ranges[var]
        # Calculate the range for the true and false condition
        if symb == LESS:
            rule_true_range = (start, num-1)
            rule_false_range = (num, end)
        else: # symb == GREATER:
            rule_true_range = (num + 1, end)
            rule_false_range = (start, num)
        
        if rule_true_range[0] <= rule_true_range[1]:
            ranges_copy = dict(ranges)
            ranges_copy[var] = rule_true_range
            total += get_accepted_comb_number(ranges_copy, target)

        if rule_false_range[0] <= rule_false_range[1]:
            ranges = dict(ranges)
            ranges[var] = rule_false_range
        else:
            # Impossible Condition 
            is_condition_impossible = True
            break

    if not is_condition_impossible:
        total += get_accepted_comb_number(ranges, default)
    
    return total


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    wf_file, parts_file = file.split('\n\n')    

    # Parts parsing    
    parts = set()
    regex = re.compile('{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    for line in parts_file.split('\n'):
        match = re.fullmatch(regex, line)
        parts.add(tuple(map(int, match.groups())))
    
    # Workflow parsing 
    # NOTE: bad parsing TODO: regex
    workflows = dict()
    # regex = re.compile('([a-zA-Z]+){(?:(?:([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+),)+)([a-zA-Z]+)}')
    rule_regex = re.compile('([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)')
    # rule_regex = re.compile('([a-zA-Z]+[<>]\d+):([a-zA-Z]+)')
    for line in wf_file.split('\n'):
        # Name
        index_of_curly= line.index('{')
        name = line[:index_of_curly]
        # Default rule
        rest_line = line[index_of_curly + 1:len(line)-1]
        default = rest_line.split(',')[-1]
        # Rules
        rules = []
        matches = re.findall(rule_regex, rest_line)
        for match in matches:
            rules.append((match[0], match[1], int(match[2]), match[3]))
            # print(match[0], match[1], match[2], match[3])
        workflows[name] = (rules, default)

    return parts, workflows


if __name__ == "__main__":
    main()