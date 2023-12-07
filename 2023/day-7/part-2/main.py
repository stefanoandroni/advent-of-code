
import re

INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    parse_input_file()

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

if __name__ == "__main__":
    main()