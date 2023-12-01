import re

INPUT_FILE_PATH = '../data/test-input-1.txt'
RE = '\d'

def main():
    lines = parse_input_file()
    calibration_values = [get_calibration_value(line) for line in lines]
    
    # Part 1
    print(sum(calibration_values))

def get_calibration_value(string):
    matches = re.findall(RE, string)
    first_digit = matches[0]
    last_digit = matches[-1]
    return int(first_digit + last_digit)

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    return lines

if __name__ == "__main__":
    main()