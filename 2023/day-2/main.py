import re

# [R, G, B]

INPUT_FILE_PATH = 'data/test-input.txt'
RGB_CONSTRAINT = [12, 13, 14]

def main():
    G = parse_input_file() # G[i] = [r,g,b] array that contains max r,g,b vals for (i+1)-game
    
    # Part 1
    out = sum(i + 1 for i, g in enumerate(G) if is_possible(g))
    print(out)

    # Part 2
    out = sum(g[0]*g[1]*g[2] for g in G)
    print(out)


def is_possible(game) -> bool: 
    for i in range(3): 
        if game[i] > RGB_CONSTRAINT[i]:
            return False 
    return True


# NOTE: bad implementation
# TODO: parsing with regex
def parse_input_file():
    G = []

    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    regex = 'Game (\d+): (.*)'
    games = re.findall(regex, file)
    for i, game in enumerate(games):
        G.append([0, 0, 0])
        # game_id = match[0] # N: game number == line number in file
        for info in game[1].split(';'):
            for subset in info.split(','):
                n, color = subset.strip().split()
                n = int(n)
                match color:
                    case 'red':
                        if (n > G[i][0]):
                            G[i][0] = n
                    case 'green':
                        if (n > G[i][1]):
                            G[i][1] = n
                    case 'blue':
                        if (n > G[i][2]):
                            G[i][2] = n
    return G

if __name__ == "__main__":
    main()