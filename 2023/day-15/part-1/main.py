
INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    steps = parse_input_file()

    sum = 0 
    for step in steps:
        current_value = 0
        for c in step:
            current_value += ord(c)
            current_value *= 17
            current_value %= 256
        sum += current_value
    
    # Part 1
    print(sum)


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    steps = file.split(',')

    return steps


if __name__ == "__main__":
    main()
