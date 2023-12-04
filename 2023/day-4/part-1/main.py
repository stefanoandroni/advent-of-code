
import re


INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    # SC: (scratchcards) list of scratchcards. Each scrachcard is 2-items tuple.
    # The first item is the set of winnig numbers and the second one is the set 
    # of numbers you have. [({winning_numbers}, {numbers_you_have}), ..]
    SC = parse_input_file() 

    # TP: total points; wn: winning numbers; n: numbers you have
    TP = sum(get_points(len(wn.intersection(n))) for (wn, n) in SC) 
    # Part 1
    print(TP)

def get_points(matches: int) -> int:
    return int(2 ** (matches - 1))

def parse_input_file():

    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    regex = 'Card\s+\d+:\s+((?:\d+\s+)+)\|\s+((?:\d+\s+)+)'
    matches = re.findall(regex, file)

    SC = []
    for match in matches:
        wn = set(int(x) for x in match[0].split()) # wn: winning numbers
        n = set(int(x) for x in match[1].split()) # n: numbers you have
        SC.append((wn, n))

    return SC
    
if __name__ == "__main__":
    main()