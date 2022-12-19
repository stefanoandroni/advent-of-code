import re

# Assumptions
# > the monkey's id matches the index of its location in the file

INPUT_FILE_PATH = 'data/input.txt'

ROUNDS = 20

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()

    monkeys = parse_file(file)

    monkeys_inspect_item_count = [0 for _ in range(len(monkeys))]

    for round in range(ROUNDS):
        for monkey in monkeys:
            for item in monkey.items.copy():
                # Get new worry level (Operation on item) 
                worry_level = get_new_worry_level(item, monkey.operation)
                # Update worry level
                worry_level //= 3
                # Test to select the receiving monkey
                receiving_monkey = monkey.if_true if worry_level % monkey.divisor == 0 else monkey.if_false
                # Throw object at monkey 'receiving_monkey'
                monkey.items.remove(item)
                monkeys[receiving_monkey].items.append(worry_level)

                monkeys_inspect_item_count[monkey.id] += 1

        # print()
        # print("ROUND ", round + 1, " -"*20)
        # print("Monkey 0:", monkeys[0].items)
        # print("Monkey 1:", monkeys[1].items)
        # print("Monkey 2:", monkeys[2].items)
        # print("Monkey 3:", monkeys[3].items)

    print(get_monkey_business_level(monkeys_inspect_item_count)) # <Part 1>

def get_monkey_business_level(count_list):
    max1 = max(count_list)
    count_list.remove(max1)
    max2 = max(count_list)
    return max1 * max2

def get_new_worry_level(item, operation):
    old = item
    new = eval(operation)
    return new

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