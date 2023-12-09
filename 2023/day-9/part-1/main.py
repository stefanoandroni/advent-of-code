
import re

INPUT_FILE_PATH = '../data/input.txt'


def main():
    H = parse_input_file() # H: H[i] = history list for i-value

    sum = 0
    for h in H:
        sum += predict_value(h)
    
    # Part 1
    print(sum)

def predict_value(h):
    # Base Case
    if all(x == 0 for x in h):
        return 0
    
    h_diff = [h[i + 1] - h[i] for i in range(len(h) - 1)]
    
    return h[-1] + predict_value(h_diff) 
    

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    return [[int(x) for x in line.split()] for line in file.split('\n')] 

if __name__ == "__main__":
    main()