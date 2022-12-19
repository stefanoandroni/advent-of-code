import re

INPUT_FILE_PATH = 'data/test-input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()

    monkeys = parse_file(file)

    for monkey in monkeys:
        for item in monkey.items:
            # Operation on worry level # TODO make function
            old = item
            new = eval(monkey.operation)
            worry_level = new
            # Divide worry level
            worry_level //= 3
            # Test to select the receiving monkey
            receiving_monkey = monkey.if_true if worry_level % monkey.divisor == 0 else monkey.if_false
            
            # HERE!
            # remove item from current
            # append item from receiving


def parse_file(file): # bad function
    monkeys = file.split('\n\n')
    monkey_obj_list = []
    for monkey in monkeys:
        lines = [ line.strip() for line in monkey.split('\n')]
        # First line
        line = lines.pop(0)
        match = re.search(r'Monkey (\d+):', line)
        id = int(match.group(1))
        # Second line
        line = lines.pop(0)
        matches = re.findall(r'\d+', line)
        starting_items = [int(x) for x in matches]
        # Third line
        line = lines.pop(0)
        match = re.search(r"^Operation: new = (.*)", line)
        operation = match.group(1)
        # Fourth line
        line = lines.pop(0)
        match = re.search(r'Test: divisible by (\d+)', line)
        test = int(match.group(1))
        # Fifth line
        line = lines.pop(0)
        match = re.search(r'If true: throw to monkey (\d+)', line)
        if_true = int(match.group(1))
        # Sixth line
        line = lines.pop(0)
        match = re.search(r'If false: throw to monkey (\d+)', line)
        if_false = int(match.group(1))

        monkey_obj_list.append(Monkey(id, starting_items, operation, test, if_true, if_false))
    
    return monkey_obj_list

class Monkey():
    def __init__(self, id, items, operation, divisor, if_true, if_false) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.if_true = if_true
        self.if_false = if_false

if __name__ == "__main__":
    main()