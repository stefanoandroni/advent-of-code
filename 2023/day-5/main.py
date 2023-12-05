
import re


INPUT_FILE_PATH = 'data/test-input.txt'

def main():
    # S: (seeds) list of seeds
    # M: (mappings) list of mappings; M[i] is a set of mapping items (source_range_start, destination_range_start, range) for i-mapping
    # (i=0 -> seed-to-soil, i=1 -> soil-to-fertilizer, ...)
    S, M = parse_input_file()

    # P: (paths) list of paths; P[i] is a list that represents the path for i-seed; P[i][0] is the seed, P[i][-1] is the location
    P = get_paths(S, M) 


    # ? = the lowest location number


def get_paths(S, M):
    pass

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        first_line = f.readline()
        file = f.read()
    
    # Seeds
    regex = re.compile('seeds:((?:\s\d+)+)')
    matches = re.match(regex, first_line)
    seeds = [int(x) for x in matches.group(1).split()]

    # Mappings
    mappings = []
    map_groups = file.split('\n\n')
    regex = re.compile('(\d+)\s+(\d+)\s+(\d+)')

    for map_group in map_groups:
        mg = set() # mg: map group
        matches = re.findall(regex, map_group)

        for match in matches:
            mg.add((int(match[1]), int(match[0]), int(match[2]))) # (source_range_start, destination_range_start, range)

        mappings.append(mg)
    
    return seeds, mappings


if __name__ == "__main__":
    main()