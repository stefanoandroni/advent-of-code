
import re


INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    # S: (seeds) list of seeds
    # M: (mappings) list of mappings; M[i] is a set of mapping items
    # (source_range_start, destination_range_start, range) for i-mapping
    # (i=0 -> seed-to-soil, i=1 -> soil-to-fertilizer, ...)
    S, M = parse_input_file()

    # P: (paths) list of paths; P[i] is a list that represents the path
    # for i-seed; P[i][0] is the seed, P[i][-1] is the location
    P = get_paths(S, M) 

    # Part 1
    print(min(path[-1] for path in P))


def get_paths(seeds, mappings):
    paths = []
    for seed in seeds:
        path = [seed]
        for mapping_group in mappings:
            # Find mapping destination
            current_map_source = path[-1]
            current_map_dest = None
            for mapping in mapping_group:
                s, d, r = mapping # s: source_range_start; d: destination_range_start; r: range
                if s <= current_map_source <= s + r - 1:
                    current_map_dest = d + abs(current_map_source - s)
                    break # NOTE: bad
            path.append(current_map_dest or current_map_source) # current_map_dest if current_map_dest else current_map_source) 
        paths.append(path)
    return paths

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