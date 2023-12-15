
from collections import OrderedDict
import re


INPUT_FILE_PATH = '../data/test-input.txt'

REGEX = re.compile("([a-zA-Z]+)([=,-])(\d*)")


def main():
    steps = parse_input_file()

    BOXES = [OrderedDict() for _ in range(256)] # (key = label, value = focal length)

    for step in steps:
        label, operation, focal_length = parse_step(step)
        # Get correct box for that step
        box = hash_algorithm(label)
        # Operation
        if operation == '-':
            if label in BOXES[box]:
                BOXES[box].pop(label)
        else: # operation == '='
            BOXES[box][label] = focal_length

    focusing_power = 0
    for i, box in enumerate(BOXES):
        for index, (label, focal_length) in enumerate(box.items()):
            focusing_power += (1 + i) * (index + 1) * int(focal_length)

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

    return label, operation, focal_length


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    steps = file.split(',')

    return steps


if __name__ == "__main__":
    main()
