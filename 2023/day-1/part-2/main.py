import regex as re

INPUT_FILE_PATH = '../data/test-input-2.txt'
DIGIT_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
RE = '\d|' + '|'.join(DIGIT_WORDS)

def main():
    lines = parse_input_file()
    calibration_values = [get_calibration_value(line) for line in lines]
    
    # Part 2
    print(sum(calibration_values))

def get_calibration_value(line):
    def get_digit_from_digit_or_word_digit(target):
        # returns (index + 1) if target in DIGIT_WORDS, else returns target
        return str(DIGIT_WORDS.index(target) + 1) if target in DIGIT_WORDS else target
    
    matches = re.findall(RE, line, overlapped=True)
    first_digit = matches[0]
    last_digit = matches[-1]

    first_digit = get_digit_from_digit_or_word_digit(first_digit)
    last_digit = get_digit_from_digit_or_word_digit(last_digit)
    
    return int(first_digit + last_digit)

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    return lines

if __name__ == "__main__":
    main()