
from collections import OrderedDict
import re


INPUT_FILE_PATH = '../data/test-input.txt'

REGEX = re.compile("([a-zA-Z]+)([=,-])(\d*)") #


def main():
    steps = parse_input_file()

    # 1) Populate a data structure representing the boxes
    boxes = [OrderedDict() for _ in range(256)] # list of boxes; each box is an OrderedDict (key = label, value = focal length)

    for step in steps:
        # Parsing step
        label, operation, focal_length = parse_step(step)
        # Get correct box for that step
        box = hash_algorithm(label)
        # Operation
        if operation == '-':
            if label in boxes[box]:
                boxes[box].pop(label)
        else: # operation == '='
            boxes[box][label] = focal_length

    # 2) Caclualate the total focusing power
    focusing_power = 0
    for i, box in enumerate(boxes):
        for index, (label, focal_length) in enumerate(box.items()):
            focusing_power += (1 + i) * (index + 1) * focal_length

    # Part 2
    print(focusing_power)


def hash_algorithm(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def parse_step(step):
    match = re.fullmatch(REGEX, step)

    label = match.group(1)
    operation = match.group(2)
    focal_length = match.group(3)

    return label, operation, int(focal_length) if focal_length else focal_length


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    steps = file.split(',')

    return steps


if __name__ == "__main__":
    main()
