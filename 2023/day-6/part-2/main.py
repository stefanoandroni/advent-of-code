
import re

INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    T, D = parse_input_file() # T: total time, D: distance record

    # Part 2
    print(get_number_of_winning_ways(T, D))

def get_number_of_winning_ways(total_time, distance_record):

    # PROBLEM
    # d = t (total_time - t)
    # 0 <= t <= total_time
    # d >= distance_record
    # t, d ∈ N

    solutions = []
    
    # TODO: optimization (constraint on t | d > distance_record)
    for t in range(total_time + 1):
        d = t * (total_time - t)
        if d > distance_record:
            solutions.append((d, t))

    return len(solutions)

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    lines = file.split('\n')

    # Time
    regex = re.compile('Time:\s+((?:(?:\d+)\s*)+)')
    matches = re.match(regex, lines[0])
    time = int("".join(matches.group(1).split()))

    # Distance
    regex = re.compile('Distance:\s+((?:(?:\d+)\s*)+)')
    matches = re.match(regex, lines[1])
    distance = int("".join(matches.group(1).split()))

    return time, distance

if __name__ == "__main__":
    main()