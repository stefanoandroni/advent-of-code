# not optimized algorithms (use tree)

INPUT_FILE_PATH = 'data/test-input.txt'

TOTAL_SPACE = 70_000_000
UPDATE_SIZE = 30_000_000

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().strip().split('\n')

    current_path = []
    files = []
    paths = set()

    for line in lines:
        words = line.strip().split()
        if words[0] == '$': # is command
            if words[1] == 'ls':
                continue
            elif words[1] == 'cd': 
                if words[2] == '..': # back
                    current_path.pop()
                elif words[2] == '/': # up (root)
                    current_path.append('root')
                    paths.add("/".join(current_path))
                else:
                    current_path.append(words[2]) # up
                    paths.add("/".join(current_path))
        else: # dir or file
            if words[0] != 'dir': # is a file
                file = {}
                file['path'] = "/".join(current_path) 
                file['name'] = words[1]
                file['size'] = int(words[0])
                files.append(file)
            # if is a dir -> folders that are not accessed (cd command), are not considered

    # files: contains all discovered files
    # print(*files, sep = "\n")
    # paths: contains all traversed paths (distinct)
    # print(*paths, sep = "\n")

    # get the sum of the file sizes in each path (which are directly contained)
    total_file_size_sum_per_path = [{'path': path, 'files-size': sum([file['size'] for file in files if file['path']==path])} for path in paths]
    # print(*total_file_size_sum_per_path, sep = "\n")

    # get total size for each distinct path (files which are directly and indirectly contained)
    total_size_per_path = [{'path': path['path'], 'total-size': sum([p['files-size'] for p in total_file_size_sum_per_path if p['path'].startswith(path['path'])])} for path in total_file_size_sum_per_path]
    # print(*total_size_per_path, sep = "\n")

    # Part 1 --------------------------------------------------------------------------------------------------------------------
    
    # find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes
    path_total_size_at_most_10000 = [path for path in total_size_per_path if path['total-size'] <= 100_000]
    # print(*path_total_size_at_most_10000, sep = "\n")

    print(sum([path['total-size'] for path in path_total_size_at_most_10000])) # <Part 1>

    # Part 2 --------------------------------------------------------------------------------------------------------------------
    
    used_space = next((item['total-size'] for item in total_size_per_path if item['path'] == 'root'), None)
    # print(used_space) 
    
    free_space = TOTAL_SPACE - used_space
    # print(free_space)

    space_to_free = UPDATE_SIZE - free_space
    # print(space_to_free)

    # get dirs whit total-size >= space_to_free
    candidate_dirs = [path for path in total_size_per_path if path['total-size'] >= space_to_free]

    # sort candidate dirs by size and get first
    candidate_dir = sorted(candidate_dirs, key=lambda x: x['total-size'])[0]
    
    print(candidate_dir['total-size']) # <Part 2>

if __name__ == "__main__":
    main()