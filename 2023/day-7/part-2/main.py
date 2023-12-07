
import re

INPUT_FILE_PATH = '../data/test-input.txt'

CARDS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
ALPHABET = [chr(ord('A') + i) for i in range(len(CARDS))]

def main():
    # B: (bids) dict of key=hand, value=bid
    # H: (hands) list of hands
    B, H = parse_input_file() 

    # OH: (ordered hands) list of ordered hands
    OH = sorted(H, key=hand_strength, reverse=True)

    result = 0
    for i, oh in enumerate(OH):
        result += (i + 1) * B[oh]
    # Part 2
    print(result)

def hand_strength(hand):
    '''
        The strength is represented by a 6-character string. The first character
        represents the hand type ('A' for 'five of a kind', 'B' for 'four of a kind', ..).
        The remaining 5 characters represent the hand values ('A' for 'A', 'B' for 'K', 'C' for 'J', ..)
    '''
    strength = get_hand_strength(hand)
    return strength

def get_hand_strength(hand):
    return get_type_strength(hand) + get_values_strength(hand)

def get_values_strength(hand):
    strength = ""
    for c in hand:
        strength += ALPHABET[CARDS.index(c)]
    return strength

def get_type_strength(hand):
    joker_count, char_count = get_characters_count_desc(hand)
    
    char_count_0 = char_count[0] if len(char_count) > 0 else 0
    char_count_1 = char_count[1] if len(char_count) > 1 else 0

    if char_count_0 + joker_count == 5: # Five of a kind -> 'A'
        return ALPHABET[0]
    if char_count_0 + joker_count == 4: # Four of a  kind -> 'B'
        return ALPHABET[1]
    if char_count_0 + joker_count == 3:
        if char_count_1 == 2:
            return ALPHABET[2] # Full house -> 'C'
        else:
            return ALPHABET[3] # Three of a kind -> 'D'
    if char_count_0 + joker_count == 2:
        if char_count_1 == 2:
            return ALPHABET[4] # Two pair -> 'E'
        else:
            return ALPHABET[5] # One pair -> 'F'
    return ALPHABET[6] # High card -> 'G'

def get_characters_count_desc(input_string):
    '''
    Ex:
        input_string = "T55J5"
        return = 1, [3, 1] cause 3x'5', 1x'T' and 1x'J'
    '''
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    if 'J' in char_count:
        j_count = char_count['J']
        char_count.pop('J')
    else:
        j_count = 0

    return j_count, sorted(char_count.values(), reverse=True)

def parse_input_file():
    bids = {}
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    lines = file.split('\n')
    for line in lines:
        hand, bid = line.split()
        bids[hand] = int(bid)
    
    hands = list(bids.keys())
    
    return  bids, hands

if __name__ == "__main__":
    main()