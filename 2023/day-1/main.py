import re

INPUT_FILE_PATH = 'data/input.txt'


def main():
    lines = parse_input_file()

    caliration_values = []
    for line in lines:
        match = re.match(r'^[a-zA-Z]*(\d).*?(\d?)[a-zA-Z]*$', line)
        if(not match):
              raise Exception("RE does not match")
        first_number = match.group(1)
        last_number = match.group(2) or match.group(1) # match.group(2) if match.group(2) else match.grop(1)
        # print(first_number, last_number, first_number+last_number)
        caliration_values.append(int(first_number + last_number))
    
    # Part 1
    print(sum(caliration_values))


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    return lines

if __name__ == "__main__":
    main()