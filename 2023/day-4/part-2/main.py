
import re


INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    # SC: (scratchcards) list of scratchcards. Each scrachcard is a 2-items
    # tuple. The first item represents the number of instances of the card.
    # The second itema is a 2-items tuple. The first item is the set of 
    # winnig numbers and the second one is the set of numbers you have.
    # [(number_of_cards, ({winning_numbers}, {numbers_you_have})), ..]
    SC = parse_input_file() 

    # SN: scratchcards number; sc: scratch card; num: number of instances;
    # wn: winning numbers; n: numbers you have
    SN = 0
    for i, sc in enumerate(SC):
        num, (wn, n) = sc
        SN += num
        points = len(wn.intersection(n))
        
        # SC[i + 1 : i + points + 1] = [(a + num, (b, c)) for a, (b, c) in SC[i + 1 : i + points + 1]]
        for i in range(i + 1, i + points + 1):
            a, (b,c) = SC[i];
            SC[i] = (a + num, (b, c))

    # Part 2
    print(SN)

def parse_input_file():

    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    regex = 'Card\s+\d+:\s+((?:\d+\s+)+)\|\s+((?:\d+\s+)+)'
    matches = re.findall(regex, file)

    SC = []
    for match in matches:
        wn = set(int(x) for x in match[0].split()) # wn: winning numbers
        n = set(int(x) for x in match[1].split()) # n: numbers you have
        SC.append((1, (wn, n)))

    return SC
    
if __name__ == "__main__":
    main()