
import re


INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    # S: (seeds) list of seeds range; each seed range is a tuple (start, end)
    # M: (mappings) list of mappings; M[i] is a set of mapping items
    # (destination_range_start, source_range_start, range) for i-mapping
    # (i=0 -> seed-to-soil, i=1 -> soil-to-fertilizer, ...)
    S, M = parse_input_file()

    for mappings in M:
        new_s = []
        while len(S) > 0:
            start, end = S.pop()
            is_new_s_up = False 
            for drs, srs, r in mappings: # drs: destination range start; srs: source range start; r: range
                new_start = max(start, srs)
                new_end = min(end, srs + r)
                if new_end > new_start:
                    new_s.append((new_start - srs + drs, new_end - srs + drs))
                    if new_start > start:
                        S.append((start, new_start))
                    if end > new_end:
                        S.append((new_end, end))
                    is_new_s_up = True
                    break
            if not is_new_s_up:
                new_s.append((start, end))
        S = new_s

    # Part 2
    print(min(S)[0])

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        first_line = f.readline()
        file = f.read()
    
    # Seeds
    regex = re.compile('seeds:((?:\s\d+)+)')
    matches = re.match(regex, first_line)
    seeds = [int(x) for x in matches.group(1).split()]
    seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    
    # Mappings
    mappings = []
    map_groups = file.split('\n\n')
    regex = re.compile('(\d+)\s+(\d+)\s+(\d+)')

    for map_group in map_groups:
        mg = set() # mg: map group
        matches = re.findall(regex, map_group)

        for match in matches:
            mg.add((int(match[0]), int(match[1]), int(match[2]))) # (source_range_start, destination_range_start, range)

        mappings.append(mg)
    
    return seeds, mappings


if __name__ == "__main__":
    main()