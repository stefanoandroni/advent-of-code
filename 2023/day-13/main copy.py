
INPUT_FILE_PATH = 'data/test-input.txt'

def main():
    # P: (patterns) list of pattern; each pattern is a list of rows;
    # each rows is a list of symbols ∈ {., #} 
    P = parse_input_file() 

    # find consecutive rows equals (candidate hr reflection line)
    # find consecutive cols equals (candidate vr reflection line)

    p = P[0]
    # Find candidate lines as hr reflection lines (consecutive equal rows)
    hr_candidate_reflection_lines_indexs = get_hr_candidate_reflection_lines(p)

def get_hr_candidate_reflection_lines(matrix):
    indexs = set()
    

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    blocks = file.split('\n\n')

    patterns = [[list(line) for line in block.split('\n')] for block in blocks]
    
    return patterns

if __name__ == "__main__":
    main()