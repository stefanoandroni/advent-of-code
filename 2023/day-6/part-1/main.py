
import math
import re

from sympy import Eq, solve, symbols

INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    D = parse_input_file() # D: (data) list of tuples (total_time, distance_record)

    prod = 1
    for total_time, distance_record in D:
        prod *= get_number_of_winning_ways(total_time, distance_record)
    # Part 1
    print(prod)

def get_number_of_winning_ways(total_time, distance_record):

    # PROBLEM
    # d = t (total_time - t)
    # 0 <= t <= total_time
    # d > distance_record
    # t, d ∈ N

    # graph (time=7, distance=9): https://imgbb.com/YTnY9vy


    '''
    # Sol1 - - - - - - - - - - 
    solutions = []
    
    # TODO: optimization (constraint on t | d > distance_record)
    for t in range(total_time + 1):
        d = t * (total_time - t)
        if d > distance_record:
            solutions.append((d, t))

    return len(solutions)
    '''
    
    # Sol2 - - - - - - - - - -
    solutions = []
    
    # intersection between 'd = distance_record' and 'd = t (total_time - t)'
    # distance_record = t (total_time - t)
    t = symbols('t')
    equation = Eq(distance_record, t * (total_time - t))
    solutions = solve(equation, t)

    t1 = float(solutions[0])
    t2 = float(solutions[1])

    t1 = math.floor(t1)
    t2 = math.floor(t2) if not t2.is_integer() else math.floor(t2) - 1

    return t2 - t1
    

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    lines = file.split('\n')

    # Time
    regex = re.compile('Time:\s+((?:(?:\d+)\s*)+)')
    matches = re.match(regex, lines[0])
    times = list(map(int, matches.group(1).split()))

    # Distance
    regex = re.compile('Distance:\s+((?:(?:\d+)\s*)+)')
    matches = re.match(regex, lines[1])
    distances = list(map(int, matches.group(1).split()))

    # Merge times and distances in data
    data = []
    for i, _ in enumerate(times):
        data.append((times[i], distances[i]))
    
    return data

if __name__ == "__main__":
    main()